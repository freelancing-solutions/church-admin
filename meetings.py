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
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))



class Meeting(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strMeetingID = ndb.StringProperty()

    strDateMeetingSchedule = ndb.DateProperty()
    strTimeMeetingScheduled = ndb.TimeProperty()

    strMeetingDuration = ndb.IntegerProperty(default=60) # in Minutes

    strSubjectOfMeeting = ndb.StringProperty()
    strIntroduction = ndb.StringProperty()

    strMeetingVenue = ndb.StringProperty()

    strIsPrivate = ndb.BooleanProperty(default=False)

    strFacilitatorName = ndb.StringProperty()
    strFacilitatorSurname = ndb.StringProperty()
    strFacilitatorCell = ndb.StringProperty()
    strFacilitatoEmail = ndb.StringProperty()

    strTodaysNotificationSent = ndb.BooleanProperty(default=False)
    strUpcomingNotificationSent = ndb.BooleanProperty(default=False)



    def writeMemberID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMemberID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChurchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchBranchID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChurchBranchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMeetingID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMeetingID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateMeetingScheduled(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateMeetingSchedule = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeMeetingScheduled(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeMeetingScheduled = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSubjectOfMeeting(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSubjectOfMeeting = strinput
                return True
            else:
                return False
        except:
            return False
    def writeIntroduction(self,strinput):
        try:
            strinput =str(strinput)
            if strinput != None:
                self.strIntroduction = strinput
                return True
            else:
                return False
        except:
            return False
    def writeISPrivate(self,strinput):
        try:
            if strinput in [True,False]:
                self.strIsPrivate = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateMeetingID(self,strChurchID):
        import random,string
        try:
            strMeetingID = ""
            for i in range(13):
                strMeetingID +=  random.SystemRandom().choice(string.ascii_uppercase + string.digits)

            strMeetingID += strChurchID
            return strMeetingID
        except:
            return None
    def writeFacilitatorName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFacilitatorName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFacilitatorSurname(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFacilitatorSurname = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFacilitatorCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFacilitatorCell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFacilitatorEmail(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.strFacilitatoEmail = strinput
                return True
            else:
                return False
        except:
            return False




class Attendees(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strMeetingID = ndb.StringProperty()
    # Reference String for invitation message
    strRef = ndb.StringProperty()
    # Meeting invitation response
    strResponse = ndb.StringProperty()
    strResponseSent = ndb.BooleanProperty(default=False)


    strAttendeeID = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()

    strInvited = ndb.BooleanProperty(default=False)
    strAttended = ndb.BooleanProperty(default=False)

    def writeRef(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRef  = strinput
                return True
            else:
                return False
        except:
            return

    def writeResponse(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strResponse = strinput
                return True
            else:
                return False
        except:
            return False

    def writeResponseSent(self,strinput):
        try:
            if strinput in [True,False]:
                self.strResponseSent = strinput
                return True
            else:
                return False
        except:
            return False



    def writeAttendeeID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAttendeeID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNames(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNames = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurname(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurname = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False
    def writeInvited(self,strinput):
        try:
            if strinput in [True,False]:
                self.strInvited = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAttended(self,strinput):
        try:
            if strinput in [True,False]:
                self.strAttended = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateAttendeeID(self):
        import random,string
        try:
            strAttendeeID = ""
            for i in range(13):
                strAttendeeID += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return  strAttendeeID
        except:
            return None
    def writeMeetingID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMeetingID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMemberID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strMemberID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strChurchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchBranchID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strChurchBranchID = strinput
                return True
            else:
                return False
        except:
            return False

class Agenda(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strMeetingID = ndb.StringProperty()

    strAgendaTitle = ndb.StringProperty()
    strItemsID = ndb.StringProperty()

    def writeMemberID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMemberID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChurchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchBranchID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChurchBranchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMeetingID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMeetingID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeItemsID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strItemsID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateItemsID(self,strMeetingID):
        import random,string
        try:
            strItemsID = strMeetingID
            for i in range(6):
                strItemsID += random.SystemRandom().choice(string.ascii_uppercase + string.digits)

            return strItemsID
        except:
            return None
    def writeAgendaTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAgendaTitle = strinput
                return True
            else:
                return False
        except:
            return False

class AgendaItems(ndb.Expando):
    strItemsID = ndb.StringProperty()
    strItemName = ndb.StringProperty()
    strNotes = ndb.StringProperty()
    strFromTime = ndb.TimeProperty()
    strToTime = ndb.TimeProperty()

    def writeItemsID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strItemsID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeItemName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strItemName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNotes(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNotes = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFromTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strFromTime = strinput
                return True
            else:
                return False
        except:
            return False
    def writeToTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strToTime = strinput
                return True
            else:
                return False
        except:
            return False

class Minutes(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strMeetingID = ndb.StringProperty()

    strMinutesTitle = ndb.StringProperty()
    strMinutesID = ndb.StringProperty()
    strDateTaken = ndb.DateProperty()
    strTimeTaken = ndb.TimeProperty()


    def writeMinutesTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMinutesTitle = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateTaken(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateTaken = strinput
                return  True
            else:
                return False
        except:
            return False

    def writeTimeTaken(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeTaken = strinput
                return True
            else:
                return False
        except:
            return False


    def writeMemberID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMemberID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChurchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchBranchID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChurchBranchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMeetingID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMeetingID = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateMinutesID(self):
        import random,string
        try:
            strMinutesID = ""
            for i in range(120):
                strMinutesID += random.SystemRandom().choice(string.ascii_uppercase + string.digits)

            return strMinutesID
        except:
            return None

    def writeMinutesID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMinutesID = strinput
                return True
            else:
                return False
        except:
            return False


class MinutesItems(ndb.Expando):
    strMinutesID = ndb.StringProperty()

    strSpeaker = ndb.StringProperty()
    strSpeakerID = ndb.StringProperty()
    strAgenda = ndb.StringProperty()
    strAgendaID = ndb.StringProperty()

    strMinutes = ndb.StringProperty()
    strNotes = ndb.StringProperty()

    def writeSpeaker(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSpeaker = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSpeakerID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSpeakerID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAgendaItem(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAgenda = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAgendaID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAgendaID = strinput
                return True
            else:
                return False
        except:
            return False


    def writeMinutesID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMinutesID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMinutes(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMinutes = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNotes(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNotes = strinput
                return True
            else:
                return False
        except:
            return False


class MeetingsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        if Guser:

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRights = thisUserRightsList[0]
            else:
                thisUserRights = UserRights()

            if thisUserRights.strAdminUser or thisUserRights.strSuperUser:

                findRequest = Meeting.query(Meeting.strChurchID == thisChurchMember.strChurchID,Meeting.strIsPrivate == False)
                thisPublicMeetingList = findRequest.fetch()

                template = template_env.get_template('templates/meetings/meetinglist.html')
                context = {'thisPublicMeetingList':thisPublicMeetingList}
                self.response.write(template.render(context))
            else:
                template = template_env.get_template('templates/subRestricted.html')
                context = {'thisChurchMember':thisChurchMember}
                self.response.write(template.render(context))


    def post(self):
        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        if Guser:
            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRights = thisUserRightsList[0]
            else:
                thisUserRights = UserRights()

            if thisUserRights.strAdminUser or thisUserRights.strSuperUser:
                vstrChoice = self.request.get('vstrChoice')

                if vstrChoice == "0":
                    vstrMeetingSubject = self.request.get('vstrMeetingSubject')
                    vstrIntroduction = self.request.get('vstrIntroduction')
                    vstrDateSchedule = self.request.get('vstrDateSchedule')
                    vstrDateList = vstrDateSchedule.split("-")
                    vstrYear = vstrDateList[0]
                    vstrMonth = vstrDateList[1]
                    vstrDay = vstrDateList[2]
                    vstrDateSchedule = datetime.date(year=int(vstrYear),month=int(vstrMonth),day=int(vstrDay))

                    vstrTimeScheduled = self.request.get('vstrTimeScheduled')
                    vstrTimeList = vstrTimeScheduled.split(":")
                    vstrHour = vstrTimeList[0]
                    vstrMinute = vstrTimeList[1]
                    vstrTimeScheduled = datetime.time(hour=int(vstrHour),minute=int(vstrMinute))

                    findRequest = Meeting.query(Meeting.strChurchID == thisChurchMember.strChurchID,Meeting.strDateMeetingSchedule == vstrDateSchedule,Meeting.strTimeMeetingScheduled == vstrTimeScheduled)
                    thisMeetingList = findRequest.fetch()

                    if len(thisMeetingList) > 0:
                        thisMeeting = thisMeetingList[0]

                    else:
                        thisMeeting = Meeting()
                        thisMeeting.writeMeetingID(strinput=thisMeeting.CreateMeetingID(strChurchID=thisChurchMember.strChurchID))
                        thisMeeting.writeChurchID(strinput=thisChurchMember.strChurchID)
                        thisMeeting.writeChurchBranchID(strinput=thisChurchMember.strChurchBranchID)

                    thisMeeting.writeSubjectOfMeeting(strinput=vstrMeetingSubject)
                    thisMeeting.writeIntroduction(strinput=vstrIntroduction)
                    thisMeeting.writeDateMeetingScheduled(strinput=vstrDateSchedule)
                    thisMeeting.writeTimeMeetingScheduled(strinput=vstrTimeScheduled)
                    thisMeeting.put()
                    self.response.write("Successfully updated Meeting")

            else:

                template = template_env.get_template('templates/subRestricted.html')
                context = {'thisChurchMember':thisChurchMember}
                self.response.write(template.render(context))



class ThisMeetingHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        if Guser:

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:

                URL = self.request.url
                URLlist = URL.split("/")
                vstrMeetingID = URLlist[len(URLlist) - 1]

                findRequest = Meeting.query(Meeting.strChurchID == thisChurchMember.strChurchID,Meeting.strMeetingID == vstrMeetingID)
                thisMeetingList = findRequest.fetch()
                if len(thisMeetingList) > 0:
                    thisMeeting = thisMeetingList[0]
                else:
                    thisMeeting = Meeting()
                template = template_env.get_template('templates/meetings/thisMeeting.html')
                context = {'thisChurchMember':thisChurchMember,'thisMeeting':thisMeeting}
                self.response.write(template.render(context))

            else:
                template = template_env.get_template('templates/subRestricted.html')
                context = {'thisChurchMember':thisChurchMember}
                self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        from mysms import SMSAccount,SMSPortalVodacom, SMSPortalBudget,DeliveryReport
        if Guser:

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                vstrChoice = self.request.get('vstrChoice')

                if vstrChoice == "0":
                    vstrMeetingID = self.request.get('vstrMeetingID')

                    findRequest = Meeting.query(Meeting.strMeetingID == vstrMeetingID,Meeting.strChurchID == thisChurchMember.strChurchID)
                    thisMeetingList = findRequest.fetch()

                    if len(thisMeetingList) > 0:
                        thisMeeting = thisMeetingList[0]
                    else:
                        thisMeeting = Meeting()

                    template = template_env.get_template('templates/meetings/sub/details.html')
                    context = {'thisMeeting':thisMeeting}
                    self.response.write(template.render(context))

                elif vstrChoice == "1":
                    vstrMeetingID = self.request.get('vstrMeetingID')

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisChurchMemberList = findRequest.fetch()

                    if len(thisChurchMemberList) > 0:
                        thisChurchMember = thisChurchMemberList[0]
                    else:
                        thisChurchMember = ChurchMember()


                    findRequest = Attendees.query(Attendees.strMeetingID == vstrMeetingID)
                    thisAttendeesList = findRequest.fetch()

                    findRequest = SMSAccount.query(SMSAccount.strChurchID == thisChurchMember.strChurchID)
                    thisSMSAccountList = findRequest.fetch()

                    if len(thisSMSAccountList) > 0:
                        thisSMSAccount = thisSMSAccountList[0]
                    else:
                        thisSMSAccount = SMSAccount()

                    template = template_env.get_template('templates/meetings/sub/attendees.html')
                    context = {'thisAttendeesList':thisAttendeesList,'thisSMSAccount':thisSMSAccount,'vstrMeetingID':vstrMeetingID }
                    self.response.write(template.render(context))

                elif vstrChoice == "2":
                    vstrMeetingID = self.request.get('vstrMeetingID')
                    vstrInviteMessage = self.request.get('vstrInviteMessage')


                    findRequest = Attendees.query(Attendees.strMeetingID == vstrMeetingID)
                    thisAttendeesList = findRequest.fetch()

                    findRequest = SMSAccount.query(SMSAccount.strChurchID == thisChurchMember.strChurchID)
                    thisSMSAccountList = findRequest.fetch()

                    if len(thisSMSAccountList) > 0:
                        thisSMSAccount = thisSMSAccountList[0]
                    else:
                        thisSMSAccount = SMSAccount()

                    self.response.write("""
                    <table id="SentTable" class="table table-bordered table-striped">
                        <thead>
                            <tr>
                                <td>Names</td>
                                <td>Surname</td>
                                <td>Cell</td>
                                <td>Status</td>
                            </tr>
                        </thead>
                        <tbody>
                    """)

                    i = 0
                    for thisAttendee in thisAttendeesList:
                        if thisSMSAccount.strTotalSMS > 0:
                            if not(thisAttendee.strCell == None):
                                if thisSMSAccount.strUsePortal == "Vodacom":
                                    thisVodacomPortal = SMSPortalVodacom()
                                    thisSMSEmail = mail.EmailMessage()
                                    thisSMSEmail.sender = thisVodacomPortal.strSenderAddress
                                    thisSMSEmail.to = thisVodacomPortal.strEmailAddress
                                    thisSMSEmail.subject = thisAttendee.strCell
                                    thisSMSEmail.body = vstrInviteMessage
                                    thisSMSEmail.send()


                                    self.response.write("""
                                    <tr> <td> """ + thisAttendee.strNames + """</td><td> """ + thisAttendee.strSurname + """</td><td>""" + thisAttendee.strCell + """</td><td> <span class="label label-success">Sent</span> </td></tr>""")

                                    thisVodacomPortal.strAvailableCredit = thisVodacomPortal .strAvailableCredit - 1
                                    thisDeliveryReport = DeliveryReport()
                                    thisDeliveryReport.writeGroupID(vstrMeetingID)
                                    thisDeliveryReport.writeCell(thisAttendee.strCell)
                                    thisDeliveryReport.writeDelivered(strinput=True)
                                    thisDate = datetime.datetime.now()
                                    strThisDate = thisDate.date()
                                    strThisTime = thisDate.time()
                                    strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute, second=strThisTime.second)
                                    thisDeliveryReport.writeDate(strinput=strThisDate)
                                    thisDeliveryReport.writeTime(strinput=strThisTime)
                                    thisDeliveryReport.writeMessageID(strinput=vstrMeetingID)
                                    thisDeliveryReport.put()
                                    i += 1

                                elif thisSMSAccount.strUsePortal == "Budget":
                                    findRequest = SMSPortalBudget.query()
                                    thisPortalList = findRequest.fetch()

                                    if len(thisPortalList) > 0:
                                        thisPortal = thisPortalList[0]
                                    else:
                                        thisPortal = SMSPortalBudget()

                                    strRef = thisPortal.SendCronMessage(strCell=thisAttendee.strCell,strMessage=vstrInviteMessage)
                                    if not(strRef == None):
                                        thisDeliveryReport = DeliveryReport()
                                        thisDeliveryReport.writeGroupID(vstrMeetingID)
                                        thisDeliveryReport.writeCell(thisAttendee.strCell)
                                        thisDeliveryReport.writeDelivered(strinput=True)
                                        thisDate = datetime.datetime.now()
                                        strThisDate = thisDate.date()
                                        strThisTime = thisDate.time()
                                        strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,second=strThisTime.second)
                                        thisDeliveryReport.writeDate(strinput=strThisDate)
                                        thisDeliveryReport.writeTime(strinput=strThisTime)
                                        thisDeliveryReport.writeMessageID(strinput=vstrMeetingID)
                                        thisDeliveryReport.writeRef(strinput=strRef)
                                        thisDeliveryReport.put()
                                        i += 1

                    self.response.write("""</tbody><tfoot><tr>
                            <tr>
                                <td>Names</td>
                                <td>Surname</td>
                                <td>Cell</td>
                                <td>Status</td>
                            </tr>
                            </tfoot>
                            </table>
                    """)
                    try:
                        thisVodacomPortal.put()
                    except:
                        pass


                    thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - (i)
                    thisSMSAccount.put()

                elif vstrChoice == "3":


                    vstrMeetingID = self.request.get('vstrMeetingID')
                    vstrNames = self.request.get('vstrNames')
                    vstrSurname = self.request.get('vstrSurname')
                    vstrCell = self.request.get('vstrCell')
                    vstrEmail = self.request.get('vstrEmail')

                    findRequest = Attendees.query(Attendees.strCell == vstrCell,Attendees.strMeetingID == vstrMeetingID)
                    thisAttendeeList = findRequest.fetch()

                    if len(thisAttendeeList) > 0:
                        thisAttendee = thisAttendeeList[0]
                    else:
                        thisAttendee = Attendees()
                        findRequest = ChurchMember.query(ChurchMember.strCell == vstrCell)
                        thisChurchMemberList = findRequest.fetch()
                        if len(thisChurchMemberList) > 0:
                            thisMember = thisChurchMemberList[0]
                            thisAttendee.writeAttendeeID(strinput=thisMember.strMemberID)
                        else:
                            thisAttendee.writeAttendeeID(strinput=thisAttendee.CreateAttendeeID())
                    thisAttendee.writeMeetingID(strinput=vstrMeetingID)
                    thisAttendee.writeNames(strinput=vstrNames)
                    thisAttendee.writeSurname(strinput=vstrSurname)
                    thisAttendee.writeCell(strinput=vstrCell)
                    thisAttendee.writeEmail(strinput=vstrEmail)
                    thisAttendee.writeChurchID(strinput=thisChurchMember.strChurchID)
                    thisAttendee.writeChurchBranchID(strinput=thisChurchMember.strChurchBranchID)
                    thisAttendee.writeMemberID(strinput=thisChurchMember.strMemberID)
                    thisAttendee.put()
                    self.response.write("Successfully updated Attendee")

                elif vstrChoice == "4":
                    vstrMeetingID = self.request.get('vstrMeetingID')
                    vstrCell = self.request.get('vstrCell')

                    findRequest = Attendees.query(Attendees.strCell == vstrCell,Attendees.strMeetingID == vstrMeetingID)
                    thisAttendeeList = findRequest.fetch()

                    for thisAttendee in thisAttendeeList:
                        thisAttendee.key.delete()

                    self.response.write("Successfully removed Attendee")

                elif vstrChoice == "5":
                    vstrMeetingID = self.request.get('vstrMeetingID')

                    findRequest = Agenda.query(Agenda.strMeetingID == vstrMeetingID)
                    thisAgendaList = findRequest.fetch()

                    if len(thisAgendaList) > 0:
                        thisAgenda = thisAgendaList[0]
                    else:
                        thisAgenda = Agenda()
                        thisAgenda.writeItemsID(strinput=thisAgenda.CreateItemsID(strMeetingID=vstrMeetingID))
                        thisAgenda.writeMeetingID(strinput=vstrMeetingID)
                        thisAgenda.writeMemberID(strinput=thisChurchMember.strMemberID)
                        thisAgenda.writeChurchID(strinput=thisChurchMember.strChurchID)
                        thisAgenda.writeChurchBranchID(strinput=thisChurchMember.strChurchBranchID)
                        thisAgenda.put()

                    findRequest = AgendaItems.query(AgendaItems.strItemsID == thisAgenda.strItemsID)
                    thisAgendaItemsList = findRequest.fetch()



                    template = template_env.get_template('templates/meetings/sub/agenda.html')
                    context = {'thisAgendaItemsList':thisAgendaItemsList,'thisAgenda':thisAgenda}
                    self.response.write(template.render(context))

                elif vstrChoice == "6":
                    vstrMeetingID = self.request.get('vstrMeetingID')
                    vstrAgendaTitle = self.request.get('vstrAgendaTitle')

                    findRequest = Agenda.query(Agenda.strMeetingID == vstrMeetingID)
                    thisAgendaList = findRequest.fetch()

                    if len(thisAgendaList) > 0:
                        thisAgenda = thisAgendaList[0]
                    else:
                        thisAgenda = Agenda()

                    thisAgenda.writeAgendaTitle(strinput=vstrAgendaTitle)
                    thisAgenda.put()
                    self.response.write("Successfully updated Agenda Title")

                elif vstrChoice == "7":
                    vstrMeetingID = self.request.get('vstrMeetingID')
                    vstrItemName = self.request.get('vstrItemName')
                    vstrNotes = self.request.get('vstrNotes')
                    vstrFromTime = self.request.get('vstrFromTime')
                    FromTimeList = vstrFromTime.split(":")
                    vstrHour = FromTimeList[0]
                    vstrMin = FromTimeList[1]
                    vstrFromTime = datetime.time(hour=int(vstrHour),minute=int(vstrMin))
                    vstrToTime = self.request.get('vstrToTime')
                    ToTimeList = vstrToTime.split(":")
                    vstrHour = ToTimeList[0]
                    vstrMin = ToTimeList[1]
                    vstrToTime = datetime.time(hour=int(vstrHour),minute=int(vstrMin))

                    findRequest = Agenda.query(Agenda.strMeetingID == vstrMeetingID,Agenda.strChurchID == thisChurchMember.strChurchID)
                    thisAgendaList = findRequest.fetch()

                    if len(thisAgendaList) > 0:
                        thisAgenda = thisAgendaList[0]
                    else:
                        thisAgenda = Agenda()

                    findRequest = AgendaItems.query(AgendaItems.strItemsID == thisAgenda.strItemsID, AgendaItems.strFromTime == vstrFromTime,AgendaItems.strToTime == vstrToTime)
                    thisAgendaItemList = findRequest.fetch()

                    if len(thisAgendaItemList) > 0:
                        thisAgendaItem = thisAgendaItemList[0]
                    else:
                        thisAgendaItem = AgendaItems()

                    thisAgendaItem.writeItemsID(strinput=thisAgenda.strItemsID)
                    thisAgendaItem.writeItemName(strinput=vstrItemName)
                    thisAgendaItem.writeNotes(strinput=vstrNotes)
                    thisAgendaItem.writeFromTime(strinput=vstrFromTime)
                    thisAgendaItem.writeToTime(strinput=vstrToTime)
                    thisAgendaItem.put()

                    self.response.write("Successfully updated items agenda")

                elif vstrChoice == "8":
                    vstrMeetingID = self.request.get('vstrMeetingID')

                    findRequest = Meeting.query(Meeting.strMeetingID == vstrMeetingID,Meeting.strChurchID == thisChurchMember.strChurchID)
                    thisMeetingList = findRequest.fetch()

                    if len(thisMeetingList) > 0:
                        thisMeeting = thisMeetingList[0]
                    else:
                        thisMeeting = Meeting()


                    template = template_env.get_template('templates/meetings/sub/facilitator.html')
                    context = {'thisMeeting':thisMeeting}
                    self.response.write(template.render(context))

                elif vstrChoice == "9":
                    vstrMeetingID = self.request.get('vstrMeetingID')
                    vstrFacilitatorName = self.request.get('vstrFacilitatorName')
                    vstrFacilitatorSurname = self.request.get('vstrFacilitatorSurname')
                    vstrFacilitatorCell = self.request.get('vstrFacilitatorCell')
                    vstrFacilitatorEmail = self.request.get('vstrFacilitatorEmail')


                    findRequest = Meeting.query(Meeting.strMeetingID == vstrMeetingID, Meeting.strChurchID == thisChurchMember.strChurchID)
                    thisMeetingList = findRequest.fetch()

                    if len(thisMeetingList) > 0:
                        thisMeeting = thisMeetingList[0]
                    else:
                        thisMeeting = Meeting()

                    thisMeeting.writeFacilitatorName(strinput=vstrFacilitatorName)
                    thisMeeting.writeFacilitatorSurname(strinput=vstrFacilitatorSurname)
                    thisMeeting.writeFacilitatorCell(strinput=vstrFacilitatorCell)
                    thisMeeting.writeFacilitatorEmail(strinput=vstrFacilitatorEmail)
                    thisMeeting.put()

                    self.response.write("Successfully updated Meeting Facilitator")

                elif vstrChoice == "10":
                    vstrMeetingID = self.request.get('vstrMeetingID')
                    #TODO- create minutes class and launch it here

                    findRequest = Minutes.query(Minutes.strMeetingID == vstrMeetingID)
                    thisMinutesList = findRequest.fetch()
                    if len(thisMinutesList) > 0:
                        thisMinute = thisMinutesList[0]
                    else:
                        thisMinute = Minutes()

                    findRequest = MinutesItems.query(MinutesItems.strMinutesID == thisMinute.strMinutesID)
                    thisMinuteItemsList = findRequest.fetch()



                    template = template_env.get_template('templates/meetings/sub/minutes.html')
                    context = {'thisMinute':thisMinute, 'thisMinuteItemsList':thisMinuteItemsList}
                    self.response.write(template.render(context))

                elif vstrChoice == "11":
                    vstrMeetingID = self.request.get('vstrMeetingID')
                    vstrMinutesTitle = self.request.get('vstrMinutesTitle')
                    vstrDateTaken = self.request.get('vstrDateTaken')
                    vstrTimeTaken = self.request.get('vstrTimeTaken')
                    vstrDateTime = datetime.datetime.now()
                    vstrDateTakenList = vstrDateTaken.split("/")
                    if len(vstrDateTakenList) == 3:
                        strYear = vstrDateTakenList[2]
                        strMonth = vstrDateTakenList[0]
                        strDay = vstrDateTakenList[1]
                        strDate = datetime.date(year=int(strYear),month=int(strMonth),day=int(strDay))
                    else:

                        strDate =vstrDateTime.date()

                    vstrTimeTakenList = vstrTimeTaken.split(" ")
                    if len(vstrTimeTakenList) == 2:
                        strTimeTaken = vstrTimeTakenList[0]
                        strAMPM = vstrTimeTakenList[1]

                        strTimeTakeList = strTimeTaken.split(":")
                        strHour = int(strTimeTakeList[0])
                        if strAMPM == "PM":
                            strHour += 12
                        strMinute = int(strTimeTakeList[1])

                        strTime = datetime.time(hour=strHour,minute=strMinute,second=0)
                    else:
                        strTime = datetime.time(hour=vstrDateTime.hour,minute=vstrDateTime.minute,second=0)

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisAdminList = findRequest.fetch()

                    if len(thisAdminList) > 0:
                        thisAdmin = thisAdminList[0]
                    else:
                        thisAdmin = ChurchMember()

                    findRequest = Minutes.query(Minutes.strMeetingID == vstrMeetingID)
                    thisMinutesList = findRequest.fetch()

                    if len(thisMinutesList) > 0:
                        thisMinutes = thisMinutesList[0]
                    else:
                        thisMinutes = Minutes()
                        thisMinutes.writeMinutesID(strinput=thisMinutes.CreateMinutesID())

                    thisMinutes.writeMeetingID(strinput=vstrMeetingID)
                    thisMinutes.writeMemberID(strinput=Guser.user_id())

                    thisMinutes.writeMinutesTitle(strinput=vstrMinutesTitle)
                    thisMinutes.writeDateTaken(strinput=strDate)
                    thisMinutes.writeTimeTaken(strinput=strTime)
                    thisMinutes.writeChurchBranchID(strinput=thisAdmin.strChurchBranchID)
                    thisMinutes.writeChurchID(strinput=thisAdmin.strChurchID)
                    thisMinutes.put()
                    self.response.write("Minutes updated successfully")


                elif vstrChoice == "12":
                    vstrMeetingID = self.request.get('vstrMeetingID')

                    findRequest = Agenda.query(Agenda.strMeetingID == vstrMeetingID)
                    thisAgendaList = findRequest.fetch()
                    if len(thisAgendaList) > 0:
                        thisAgenda = thisAgendaList[0]

                        if thisAgenda.strItemsID == None:
                            thisAgendaItemsList = []
                        else:
                            findRequest = AgendaItems.query(AgendaItems.strItemsID == thisAgenda.strItemsID)
                            thisAgendaItemsList = findRequest.fetch()
                    else:
                        thisAgendaItemsList = []

                    self.response.headers['Content-Type'] = "text/plain"
                    template = template_env.get_template('templates/meetings/sub/agendalist.txt')
                    context = {'thisAgendaItemsList':thisAgendaItemsList}
                    self.response.write(template.render(context))

                elif vstrChoice == "13":
                    vstrMeetingID = self.request.get('vstrMeetingID')
                    vstrMinutesID = self.request.get('vstrMinutesID')
                    vstrSelectAgendaItem = self.request.get('vstrSelectAgendaItem')
                    vstrAgenda = self.request.get('vstrAgenda')
                    vstrAddMinutesTitle = self.request.get('vstrAddMinutesTitle')
                    vstrMinutes = self.request.get('vstrMinutes')
                    vstrNotes = self.request.get('vstrNotes')

                    findRequest = MinutesItems.query(MinutesItems.strMinutesID == vstrMinutesID,MinutesItems.strMinutes == vstrMinutes)
                    thisMinutesItemsList = findRequest.fetch()

                    if len(thisMinutesItemsList) > 0:
                        thisMinuteItem = thisMinutesItemsList[0]
                    else:
                        thisMinuteItem = MinutesItems()

                    thisMinuteItem.writeMinutesID(strinput=vstrMinutesID)
                    thisMinuteItem.writeAgendaItem(strinput=vstrAgenda)
                    thisMinuteItem.writeAgendaID(strinput=vstrSelectAgendaItem)
                    thisMinuteItem.writeMinutes(strinput=vstrMinutes)
                    thisMinuteItem.writeNotes(strinput=vstrNotes)
                    thisMinuteItem.put()
                    self.response.write("succesfully added minutes items")

            else:
                template = template_env.get_template('templates/subRestricted.html')
                context = {'thisChurchMember':thisChurchMember}
                self.response.write(template.render(context))


class ThisPrintMeetingHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChoice = self.request.get('vstrChoice')


            if vstrChoice == "0":
                vstrMeetingID = self.request.get('vstrMeetingID')

                findRequest = Meeting.query(Meeting.strMeetingID == vstrMeetingID)
                thisMeetingList = findRequest.fetch()

                if len(thisMeetingList) > 0:
                    thisMeeting = thisMeetingList[0]

                    template = template_env.get_template('templates/meetings/print/print.html')
                    context = {'thisMeeting':thisMeeting}
                    self.response.write(template.render(context))

class ThisPrintHandler(webapp2.RequestHandler):
    def get(self):

        URL = self.request.url
        strURLList = URL.split("/")
        strSection = strURLList[len(strURLList) - 2]
        strMeetingID = strURLList[len(strURLList) - 1]

        findRequest = Meeting.query(Meeting.strMeetingID == strMeetingID)
        thisMeetingList = findRequest.fetch()

        if len(thisMeetingList) > 0:
            thisMeeting = thisMeetingList[0]
        else:
            thisMeeting = Meeting()

        findRequest = Agenda.query(Agenda.strMeetingID == thisMeeting.strMeetingID)
        thisAgendaList = findRequest.fetch()
        if len(thisAgendaList) > 0:
            thisAgenda = thisAgendaList[0]
        else:
            thisAgenda = Agenda()

        findRequest = AgendaItems.query(AgendaItems.strItemsID == thisAgenda.strItemsID)
        thisAgendaItemsList = findRequest.fetch()

        findRequest = Minutes.query(Minutes.strMeetingID == thisMeeting.strMeetingID)
        thisMinutesList = findRequest.fetch()

        if len(thisMinutesList) > 0:
            thisMinute = thisMinutesList[0]
        else:
            thisMinute = Minutes()

        findRequest = MinutesItems.query(MinutesItems.strMinutesID == thisMinute.strMinutesID)
        thisMinutesItemsList = findRequest.fetch()


        findRequest = Attendees.query(Attendees.strMeetingID == thisMeeting.strMeetingID)
        thisAttendeesList = findRequest.fetch()

        if strSection == "complete":

            template = template_env.get_template('templates/meetings/print/complete.html')
            context = {'thisMeeting':thisMeeting,'thisAgenda':thisAgenda,'thisAgendaItemsList':thisAgendaItemsList,
                       'thisMinute':thisMinute,'thisMinutesItemsList':thisMinutesItemsList,'thisAttendeesList':thisAttendeesList}
            self.response.write(template.render(context))

        elif strSection == "agenda":
            template = template_env.get_template('templates/meetings/print/agenda.html')
            context = {'thisMeeting':thisMeeting,'thisAgenda':thisAgenda,'thisAgendaItemsList':thisAgendaItemsList,
                       'thisMinute':thisMinute,'thisMinutesItemsList':thisMinutesItemsList,'thisAttendeesList':thisAttendeesList}
            self.response.write(template.render(context))
        elif strSection == "attendees":
            template = template_env.get_template('templates/meetings/print/attendees.html')
            context = {'thisMeeting':thisMeeting,'thisAgenda':thisAgenda,'thisAgendaItemsList':thisAgendaItemsList,
                       'thisMinute':thisMinute,'thisMinutesItemsList':thisMinutesItemsList,'thisAttendeesList':thisAttendeesList}
            self.response.write(template.render(context))

        elif strSection == "minutes":
            template = template_env.get_template('templates/meetings/print/minutes.html')
            context = {'thisMeeting':thisMeeting,'thisAgenda':thisAgenda,'thisAgendaItemsList':thisAgendaItemsList,
                       'thisMinute':thisMinute,'thisMinutesItemsList':thisMinutesItemsList,'thisAttendeesList':thisAttendeesList}
            self.response.write(template.render(context))


#TODO- on the meetings module the Send Invites Must be removed,
#TODO- There should be a print out module for printind the details of the meeting and also
#TODO- there should be a p[lace to write all the meeting minutes

app = webapp2.WSGIApplication([
    ('/admin/meetings', MeetingsHandler),
    ('/admin/meetings/print', ThisPrintMeetingHandler),
    ('/admin/meetings/print/.*', ThisPrintHandler),
    ('/admin/meetings/.*', ThisMeetingHandler)

], debug=True)