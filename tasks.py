#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users,mail
import logging
import math
import datetime
from datetime import timedelta
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class NewsLettersHandler(webapp2.RequestHandler):

    def get(self):
        from newsletter import MailingList, Letters, ContactList
        #TODO- Please make use of a third party emailing Service
        #TODO- Or Consider Sending Newsletter Links through SMS Messages so users can open it through the App

        NOW = datetime.datetime.now()
        thisTime = NOW.time()
        thisDate = NOW.date()

        findRequest = MailingList.query(MailingList.strStartSendingDate == thisDate,MailingList.strStartSendingTime <= thisTime)
        thisMailingList = findRequest.fetch()

        findRequest = Letters.query(Letters.strSent == False)
        thisLettersList = findRequest.fetch()

        ListIDList = []
        for thisLetter in thisLettersList:
            ListIDList.append(thisLetter.strListID)


        for thisMailing in thisMailingList:

            if thisMailing.strListID in ListIDList:
                for thisLetter in thisLettersList:
                    if thisLetter.strListID == thisMailing.strListID:
                        break

                findRequest = ContactList.query(ContactList.strListID == thisMailing.strListID)
                thisContactsList = findRequest.fetch()

                for thisContact in thisContactsList:

                    message = mail.EmailMessage()
                    message.sender = thisMailing.strSenderAddress
                    message.to = thisContact.strEmail
                    message.subject = "Church Admin Newsletters"
                    message.html = """
                    <h2>Church Admins Newsletters

                    you are receiving this message from church admin as you have been subscribed
                    to one of the newsletters hosted in our app.

                    to open your newsletter please click on the link below...<br>
                    """+ """<a href="/newsletters/hosted/"""+ thisLetter.strHostedLink+ """">""" + thisLetter.strHostedLink+"""</a>"""

                    message.send()

                thisLetter.strSent = True
                thisDate = datetime.datetime.now()
                thisLetter.strDateSent = thisDate.date()
                thisLetter.put()





class BirthDaysHandler(webapp2.RequestHandler):
    def get(self):
        from events import Birthdays
        from church import ChurchMember
        from mysms import SMSAccount


        findRequest = Birthdays.query()
        thisBirthDaysList = findRequest.fetch()

        thisDate = datetime.datetime.now()
        thisDate = thisDate.now()

        for thisBirthDay in thisBirthDaysList:
            if thisBirthDay.strAutoSend:
                findRequest = ChurchMember.query(ChurchMember.strChurchID == thisBirthDay.strChurchID)
                thisChurchMemberList = findRequest.fetch()

                for thisChurchMember in thisChurchMemberList:
                    if (thisChurchMember.strMonth == thisDate.month) and (thisChurchMember.strDay == thisDate.day) and (thisChurchMember.strCell <> None):
                        findRequest = SMSAccount.query(SMSAccount.strChurchID == thisChurchMember.strChurchID)
                        thisSMSAccountList = findRequest.fetch()

                        if len(thisSMSAccountList) > 0:
                            thisSMSAccount = thisSMSAccountList[0]
                            if (thisSMSAccount.strTotalSMS > 1):
                                if thisBirthDay.SendBirthdayWishes(strMessage=thisBirthDay.strBirthdayMessage,strCell=thisChurchMember.strCell,strPortal=thisSMSAccount.strUsePortal):
                                    if thisSMSAccount.strUsePortal == "Budget":
                                        thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - 1

                                    thisSMSAccount.put()
                                else:
                                    logging.info("Error sending birthday messages")
                            else:
                                pass
                                #TODO- Send a notification to the user indicating that their SMS Credits are insufficient and notifications can no loner be sent
                        else:
                            pass
                    else:
                        pass
            else:
                pass



class BulkSMSHandler(webapp2.RequestHandler):
    def get(self):
        from mysms import MessageSchedule, Messages, SMSContacts, Groups, SMSAccount, SMSPortalVodacom, DeliveryReport,SMSPortalBudget
        from church import ChurchMember
        Today = datetime.datetime.now()
        thisDate = Today.date()
        thisTime = Today.time()

        findRequest = MessageSchedule.query(MessageSchedule.strStatus == "Scheduled",
                                            MessageSchedule.strStartDate == thisDate,
                                            MessageSchedule.strStartTime >= thisTime)
        thisMessageScheduleList = findRequest.fetch()

        for thisSchedule in thisMessageScheduleList:
            findRequest = Messages.query(Messages.strMessageID == thisSchedule.strMessageID,
                                         Messages.strSubmitted == False)
            thisMessageList = findRequest.fetch()

            if len(thisMessageList) > 0:
                thisMessage = thisMessageList[0]
            else:
                thisMessage = Messages()

            findRequest = Groups.query(Groups.strGroupID == thisMessage.strGroupID)
            thisGroupList = findRequest.fetch()

            if len(thisGroupList) > 0:
                thisGroup = thisGroupList[0]
            else:
                thisGroup = Groups()

            findRequest = SMSAccount.query(SMSAccount.strChurchID == thisGroup.strChurchID)
            thisSMSAccountList = findRequest.fetch()

            if len(thisSMSAccountList) > 0:
                thisSMSAccount = thisSMSAccountList[0]
            else:
                thisSMSAccount = SMSAccount()
                thisSMSAccount.writeChurchID(strinput=thisGroup.strChurchID)
                thisSMSAccount.put()

            findRequest = SMSContacts.query(SMSContacts.strGroupID == thisMessage.strGroupID)
            thisContactsList = findRequest.fetch()

            ReceipientList = []
            for thisContact in thisContactsList:
                if thisContact.strCellNumber != None:
                    ReceipientList.append(thisContact.strCellNumber)

            if thisSchedule.strNotifyOnStart == True:
                findRequest = ChurchMember.query(ChurchMember.strMemberID == thisSchedule.strMemberID)
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                    if thisChurchMember.strCell in ReceipientList:
                        pass
                    else:
                        ReceipientList.append(thisChurchMember.strCell)

            if thisSMSAccount.strTotalSMS >= len(ReceipientList):
                if thisSMSAccount.strUsePortal == "Vodacom":
                    findRequest = SMSPortalVodacom.query()
                    thisVodaList = findRequest.fetch()

                    if len(thisVodaList) > 0:
                        thisVoda = thisVodaList[0]
                    else:
                        thisVoda = SMSPortalVodacom()
                        thisVoda.put()

                    if thisVoda.CronSendMessages(strCellNumberList=ReceipientList, strMessage=thisMessage.strMessage,
                                                 strAccountID=thisSMSAccount.strChurchID):
                        thisSchedule.writeStatus(strinput="Completed")
                        thisSchedule.put()
                        thisMessage.writeDateSubmitted(strinput=thisDate)
                        thisMessage.writeTimeSubmitted(strinput=thisTime)
                        thisMessage.writeSubmitted(strinput=True)
                        thisMessage.put()
                        for StrCell in ReceipientList:
                            #TODO- Investigate if Vodacom uses cell number for reference to obtain response
                            thisDeliveryReport = DeliveryReport()
                            thisDeliveryReport.writeMessageID(strinput=thisMessage.strMessageID)
                            thisDeliveryReport.writeGroupID(strinput=thisMessage.strGroupID)
                            thisDeliveryReport.writeCell(strinput=StrCell)
                            thisDeliveryReport.writeDate(strinput=thisDate)
                            thisDeliveryReport.writeTime(strinput=thisTime)
                            thisDeliveryReport.writeDelivered(strinput=True)
                            thisDeliveryReport.put()
                        logging.info("Bulk SMS Schedule executed")

                        # thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - len(ReceipientList)
                        # Vodacom Portal Subtracts its own Credits


                elif thisSMSAccount.strUsePortal == "Budget":
                    findRequest = SMSPortalBudget.query()
                    thisPortalList = findRequest.fetch()

                    if len(thisPortalList) > 0:
                        thisPortal = thisPortalList[0]
                    else:
                        thisPortal = SMSPortalBudget()

                    for thisCell in ReceipientList:
                        strRef = thisPortal.SendCronMessage(strMessage=thisMessage.strMessage,strCell=thisCell)
                        if not(strRef == None):
                            thisDeliveryReport = DeliveryReport()
                            thisDeliveryReport.writeMessageID(strinput=thisMessage.strMessageID)
                            thisDeliveryReport.writeGroupID(strinput=thisMessage.strGroupID)
                            thisDeliveryReport.writeCell(strinput=thisCell)
                            thisDeliveryReport.writeRef(strinput=strRef)
                            thisDeliveryReport.writeDate(strinput=thisDate)
                            thisDeliveryReport.writeTime(strinput=thisTime)
                            thisDeliveryReport.writeDelivered(strinput=True)
                            thisDeliveryReport.put()
                            thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - 1
                        else:
                            thisDeliveryReport = DeliveryReport()
                            thisDeliveryReport.writeMessageID(strinput=thisMessage.strMessageID)
                            thisDeliveryReport.writeGroupID(strinput=thisMessage.strGroupID)
                            thisDeliveryReport.writeCell(strinput=thisCell)
                            thisDeliveryReport.writeRef(strinput="")
                            thisDeliveryReport.writeDate(strinput=thisDate)
                            thisDeliveryReport.writeTime(strinput=thisTime)
                            thisDeliveryReport.writeDelivered(strinput=False)
                            thisDeliveryReport.put()


                    thisMessage.writeDateSubmitted(strinput=thisDate)
                    thisMessage.writeTimeSubmitted(strinput=thisTime)
                    thisMessage.writeSubmitted(strinput=True)
                    thisMessage.put()



                            #TODO- Include Budget Sending Capability to enable the Messages to be sent on schedule

                thisSMSAccount.put()

class BulkEmailHandler(webapp2.RequestHandler):

    def get(self):
        pass
    #TODO- Consider finishing this part


class MeetingsHandler(webapp2.RequestHandler):
    def get(self):
        from meetings import Meeting,Attendees
        from mysms import SMSAccount,SMSPortalVodacom,SMSPortalBudget

        thisDate = datetime.datetime.now()
        UpComingDate = thisDate - timedelta(days=1)
        findRequest = Meeting.query(Meeting.strDateMeetingSchedule == thisDate)
        thisTodaysMeetingList = findRequest.fetch()

        for thisMeeting in thisTodaysMeetingList:

            if thisMeeting.strTodaysNotificationSent == False:
                findRequest = SMSAccount.query(SMSAccount.strChurchID == thisMeeting.strChurchID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]

                    strMessage = "Meeting Reminder" + "%0A"
                    Subject = thisMeeting.strSubjectOfMeeting + "%0A"
                    Venue =  thisMeeting.strMeetingVenue + "%0A"
                    Facilitator = thisMeeting.strFacilitatorName + " " +   thisMeeting.strFacilitatorSurname + "%0A"
                    Cell =  thisMeeting.strFacilitatorCell + "%0A"
                    Time = thisMeeting.strTimeMeetingScheduled + "%0A"
                    ThanksMessage = " Thank You " +  "%0A" + "Church Admin Team"
                    strMessage = strMessage + Subject + Venue + Facilitator + Cell + Time + ThanksMessage

                    findRequest = Attendees.query(Attendees.strMeetingID == thisMeeting.strMeetingID)
                    thisAttendeesList = findRequest.fetch()

                    ReceipientList = []
                    for thisAttendee in thisAttendeesList:
                        if thisAttendee.strCell <> None:
                            ReceipientList.append(thisAttendee.strCell)

                    ReceipientList.append(thisMeeting.strFacilitatorCell)

                    if thisSMSAccount.strTotalSMS >= len(ReceipientList):

                        if thisSMSAccount.strUsePortal == "Vodacom":

                            findRequests = SMSPortalVodacom.query()
                            thisVodaPortalList = findRequests.fetch()

                            if len(thisVodaPortalList) > 0:
                                thisVoda = thisVodaPortalList()
                            else:
                                thisVoda = SMSPortalVodacom()
                                thisVoda.put()


                            if thisVoda.CronSendMessages(strCellNumberList=ReceipientList, strMessage=strMessage,strAccountID=thisSMSAccount.strChurchID):
                                logging.info("Meeting Reminder Messages successfully sent")
                            else:
                                logging.info("Failure sending Meeting Reminder messages")

                            # thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - len(ReceipientList)
                            # Vodacom Portal Subtracts its own credits

                        elif thisSMSAccount.strUsePortal == "Budget":
                            findRequest = SMSPortalBudget.query()
                            thisPortalList = findRequest.fetch()

                            if len(thisPortalList) > 0:
                                thisPortal = thisPortalList[0]
                            else:
                                thisPortal = SMSPortalBudget()

                            for thisCell in ReceipientList:
                                findRequest = Attendees.query(Attendees.strChurchID == thisSMSAccount.strChurchID,Attendees.strCell == thisCell)
                                thisAttendeeList = findRequest.fetch()

                                if len(thisAttendeeList) > 0:
                                    thisAttendee = thisAttendeeList[0]
                                else:
                                    thisAttendee = Attendees()

                                strRef = thisPortal.SendCronMessage(strMessage=strMessage,strCell=thisCell)
                                if not(strRef == None):
                                    thisAttendee.writeRef(strinput=strRef)
                                    thisAttendee.put()
                                    thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - 1

                        thisSMSAccount.put()


                thisMeeting.strTodaysNotificationSent = True
                thisMeeting.put()


        #TODO-Upcoming Meetings Reminder

        findRequest = Meeting.query(Meeting.strDateMeetingSchedule == UpComingDate)
        thisUpcomingMeetingsList = findRequest.fetch()

        for thisMeeting in thisUpcomingMeetingsList:

            if thisMeeting.strUpcomingNotificationSent == False:
                findRequest = SMSAccount.query(SMSAccount.strChurchID == thisMeeting.strChurchID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]

                    strMessage = "Upcoming Meeting Reminder" + "%0A"
                    Subject = thisMeeting.strSubjectOfMeeting + "%0A"
                    Venue =  thisMeeting.strMeetingVenue + "%0A"
                    Facilitator = thisMeeting.strFacilitatorName + " " +   thisMeeting.strFacilitatorSurname + "%0A"
                    Cell =  thisMeeting.strFacilitatorCell + "%0A"
                    Date = thisMeeting.strDateMeetingSchedule + "%0A"
                    Time = thisMeeting.strTimeMeetingScheduled + "%0A"
                    ThanksMessage = " Thank You " +  "%0A" + "Church Admin Team"
                    strMessage = strMessage + Subject + Venue + Facilitator + Cell + Date + Time + ThanksMessage

                    findRequest = Attendees.query(Attendees.strMeetingID == thisMeeting.strMeetingID)
                    thisAttendeesList = findRequest.fetch()

                    ReceipientList = []
                    for thisAttendee in thisAttendeesList:
                        if thisAttendee.strCell != None:
                            ReceipientList.append(thisAttendee.strCell)

                    ReceipientList.append(thisMeeting.strFacilitatorCell)

                    if thisSMSAccount.strUsePortal == "Vodacom":
                        findRequests = SMSPortalVodacom.query()
                        thisVodaPortalList = findRequests.fetch()

                        if len(thisVodaPortalList) > 0:
                            thisVoda = thisVodaPortalList()
                        else:
                            thisVoda = SMSPortalVodacom()
                            thisVoda.put()


                        if thisVoda.CronSendMessages(strCellNumberList=ReceipientList,strMessage=strMessage,strAccountID=thisSMSAccount.strChurchID):
                            logging.info("Upcoming Meeting Reminders Sent")
                        else:
                            logging.info("Upcoming Meeting Reminders Not Sent")
                            #TODO- Notify the user via SMS to buy more credits and his meeting notifications will no longer be sent

                    elif thisSMSAccount.strUsePortal == "Budget":
                        findRequest = SMSPortalBudget.query()
                        thisPortalList = findRequest.fetch()

                        if len(thisPortalList) > 0:
                            thisPortal = thisPortalList[0]
                        else:
                            thisPortal = SMSPortalBudget()

                        for thisCell in ReceipientList:
                            findRequest = Attendees.query(Attendees.strChurchID == thisSMSAccount.strChurchID,Attendees.strCell == thisCell)
                            thisAttendeeList = findRequest.fetch()

                            if len(thisAttendeeList) > 0:
                                thisAttendee = thisAttendeeList[0]
                            else:
                                thisAttendee = Attendees()

                            strRef = thisPortal.SendCronMessage(strMessage=strMessage,strCell=thisCell)
                            if not(strRef == None):
                                thisAttendee.writeRef(strinput=strRef)
                                thisAttendee.put()
                                thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - 1

                    thisSMSAccount.put()

                    thisMeeting.strUpcomingNotificationSent = True
                    thisMeeting.put()



class SystemStatusHandler(webapp2.RequestHandler):
    """
        In order for the system notification to work
        i have to create the staff data entry interface within church admin
        then i also have to include the System SMS Account Settings with its own allocation of SMSes
    """
    def get(self):

        from dashboard import AppRequests,BlueITMarketingAdminStaff
        from mysms import SMSAccount,SMSPortalVodacom,SMSPortalBudget

        findRequests = AppRequests.query(AppRequests.strRequestAccepted == False,AppRequests.strNotificationSent == False)
        thisAppRequestList = findRequests.fetch()

        findRequests = BlueITMarketingAdminStaff.query(BlueITMarketingAdminStaff.strPosition == "Admin",BlueITMarketingAdminStaff.strPosition == "Marketing")
        thisBlueStaffList = findRequests.fetch()

        strTotalRequests = len(thisAppRequestList)

        findRequests = SMSPortalVodacom.query()
        thisVodaPortalList = findRequests.fetch()

        if len(thisVodaPortalList) > 0:
            thisVoda = thisVodaPortalList[0]
        else:
            thisVoda = SMSPortalVodacom()


        findRequests = SMSPortalBudget.query()
        thisBudgetPortalList = findRequests.fetch()

        if len(thisBudgetPortalList) > 0:
            thisBudget = thisBudgetPortalList[0]
        else:
            thisBudget = SMSPortalBudget()

        strMessage = "Church Admin" + "%0A"
        strNotifications = "System Notifications" + "%0A"
        NewClients  ="New Clients : " + str(strTotalRequests) + "%0A"
        Vodacom_Credit ="Vodacom Credit : " + str(thisVoda.strAvailableCredit) + "%0A"
        Budget_Credit = "Budget Credit : " + str(thisBudget.CheckCredits())

        strMessage = strMessage + strNotifications + NewClients  + Vodacom_Credit + Budget_Credit




        thisAdminStaff = BlueITMarketingAdminStaff()
        findRequests = SMSAccount.query(SMSAccount.strChurchID == thisAdminStaff.strStaffID)
        thisSMSAccountList = findRequests.fetch()

        if len(thisSMSAccountList) > 0:
            thisSMSAccount = thisSMSAccountList[0]
        else:
            thisSMSAccount = SMSAccount()

        ReceipientList = []

        if len(thisBlueStaffList) > 0:
            for thisStaff in thisBlueStaffList:
                ReceipientList.append(thisStaff.strCell)

        if "0790471559" in ReceipientList:
            pass
        else:
            ReceipientList.append("0790471559")


        if thisSMSAccount.strUsePortal == "Vodacom":
            findRequests = SMSPortalVodacom.query()
            thisVodaPortalList = findRequests.fetch()

            if len(thisVodaPortalList) > 0:
                Voda = thisVodaPortalList[0]
            else:
                Voda = SMSPortalVodacom()
                Voda.put()

            if Voda.CronSendMessages(strCellNumberList=ReceipientList,strMessage=strMessage,strAccountID=thisAdminStaff.strStaffID):
                logging.info("Successfully sent system messages")
            else:
                logging.info("Error sending system messages")

        elif thisSMSAccount.strUsePortal == "Budget":

            for thisNumber in ReceipientList:
                thisBudget.SendCronMessage(strCell=thisNumber,strMessage=strMessage)
                thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - 1
            thisSMSAccount.put()



class BulkSMSResponsesHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            from mysms import Messages, SMSPortalBudget, DeliveryReport
            vstrThisDate = datetime.datetime.now()
            strThisDate = vstrThisDate.date()
            strThisTime = datetime.time(hour=vstrThisDate.hour, minute=vstrThisDate.minute, second=vstrThisDate.second)

            # TODO-This is a code fix
            findRequest = DeliveryReport.query()
            thisDeliveyReportsList = findRequest.fetch()

            for normalize in thisDeliveyReportsList:
                if normalize.strRef == None:
                    normalize.strRef = "11111"
                normalize.put()

            # TODO-Code Fix ended here

            findRequest = DeliveryReport.query(DeliveryReport.strDate <= strThisDate,
                                               DeliveryReport.strResponseReceived == False)
            thisDeliveryList = findRequest.fetch()

            thisPortal = SMSPortalBudget()
            for thisDelivery in thisDeliveryList:
                if not (thisDelivery.strRef == "11111"):
                    strResponse = thisPortal.CheckSpecificReply(strRef=thisDelivery.strRef)

                    if not (strResponse == None):
                        strResponse = strResponse.strip()
                        thisDelivery.writeResponse(strinput=strResponse)
                        thisDelivery.writeDateResponse(strinput=strThisDate)
                        thisDelivery.writeTimeResponse(strinput=strThisTime)
                        thisDelivery.writeResponseReceived(strinput=True)
                        thisDelivery.put()
                        # TODO-Note that in order for the response module to work successfully all the time the message id field must contain the reference of the message
                        # TODO- On Bulk SMS Message Module Responses can be loaded there for each bulk SMS Module
                    else:
                        pass

                else:
                    strResponse = "11111"
                    thisDelivery.writeResponse(strinput=strResponse)
                    thisDelivery.writeDateResponse(strinput=strThisDate)
                    thisDelivery.writeTimeResponse(strinput=strThisTime)
                    thisDelivery.writeResponseReceived(strinput=True)
                    thisDelivery.put()


class MeetingResponsesHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from meetings import Meeting,Attendees
        from mysms import SMSPortalBudget
        if Guser:
            vstrThisDate = datetime.datetime.now()
            strThisDate = vstrThisDate.date()
            strThisTime = datetime.time(hour=vstrThisDate.hour,minute=vstrThisDate.minute,second=vstrThisDate.second)

            findRequest = Meeting.query(Meeting.strDateMeetingSchedule == strThisDate,Meeting.strTodaysNotificationSent == True)
            thisMeetingList = findRequest.fetch()

            findRequest = SMSPortalBudget.query()
            thisPortalList = findRequest.fetch()

            if len(thisPortalList) > 0:
                thisPortal = thisPortalList
            else:
                thisPortal = SMSPortalBudget()

            for thisMeeting in thisMeetingList:
                findRequest = Attendees.query(Attendees.strMeetingID == thisMeeting.strMeetingID, Attendees.strResponseSent == False)
                thisAttendeeList = findRequest.fetch()

                for thisAttendee in thisAttendeeList:
                    strResponse = thisPortal.CheckSpecificReply(strRef=thisAttendee.strRef)
                    if not(strResponse == None):
                        thisAttendee = Attendees() #TODO-Remove this Line
                        thisAttendee.writeResponse(strinput=strResponse)
                        thisAttendee.writeResponseSent(strinput=True)
                        thisAttendee.put()


#TODO- Take Care to actually Display Meeting Response in Church Admin

#TODO- Very important revise the whole tasks module to work using present technologies and also to handle response for all the messages being sent

#TODO- Add Response Functionality for all messaging features of this App

#TODO- Please Add Event Notifications/ reminders and also finish up on events also consider intergrating

#TODO- Google Calendar for its own event notification

#TODO- Suppliers and Services Providers Messaging must be attached to their response tasks

app = webapp2.WSGIApplication([
    ('/tasks/newsletters', NewsLettersHandler),
    ('/tasks/birthdays', BirthDaysHandler),
    ('/tasks/bulksms', BulkSMSHandler),
    ('/tasks/bulkemail', BulkEmailHandler),
    ('/tasks/meetings', MeetingsHandler),
    ('/tasks/system', SystemStatusHandler),
    ('/tasks/bulksmsresponses', BulkSMSResponsesHandler),
    ('/tasks/meetingresponses', MeetingResponsesHandler),


], debug=True)