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


import os
import webapp2
import jinja2
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import urlfetch
import urllib,urllib2
from church import ChurchMember
from userRights import UserRights
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
import logging
#from twilio.rest import Client
from xml.etree import ElementTree

#client = Client(account,token)

class Groups(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strGroupID = ndb.StringProperty()
    strGroupName = ndb.StringProperty()
    strGroupDescription = ndb.StringProperty()
    strTotalNumbers = ndb.IntegerProperty(default=0)


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
    def writeGroupID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strGroupID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeGroupName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strGroupName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeGroupDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strGroupDescription = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateGroupID(self):
        import random,string
        try:
            strGroupID = "SMS"
            for i in range(36):
                strGroupID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strGroupID
        except:
            return None

    def writeTotalNumbers(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalNumbers = int(strinput)
                return True
            else:
                return False
        except:
            return False

class SMSContacts(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strCellNumber = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strGroupID = ndb.StringProperty()

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
    def writeGroupID(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.strGroupID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCellNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCellNumber = strinput
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

class Messages(ndb.Expando):
    strGroupID = ndb.StringProperty()
    strMessageID = ndb.StringProperty()
    strMessage = ndb.StringProperty()
    strSubmitted = ndb.BooleanProperty(default=False)
    strDateSubmitted = ndb.DateProperty()
    strTimeSubmitted = ndb.TimeProperty()
    strDateCreated = ndb.DateProperty(auto_now_add=True)
    strTimeCreated = ndb.TimeProperty(auto_now_add=True)


    def writeGroupID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strGroupID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMessageID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMessageID = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateMessageID(self):
        import string,random
        try:
            strMessageID = "MESS"

            for i in range(36):
                strMessageID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strMessageID
        except:
            return None

    def writeMessage(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMessage = strinput
                return True
            else:
                return False

        except:
            return False

    def writeSubmitted(self,strinput):
        try:
            if strinput in [True,False]:
                self.strSubmitted = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateSubmitted(self,strinput):
        try:
            if strinput is not None:
                self.strDateSubmitted = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeSubmitted(self,strinput):
        try:
            if strinput is not None:
                self.strTimeSubmitted = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeCreated(self,strinput):
        try:
            if strinput != None:
                self.strTimeCreated = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateCreated(self,strinput):
        try:
            if strinput != None:
                self.strDateCreated = strinput
                return True
            else:
                return False
        except:
            return False

class MessageSchedule(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strMessageID = ndb.StringProperty()
    strStartDate = ndb.DateProperty()
    strStartTime = ndb.TimeProperty()
    strEndDate = ndb.DateProperty()
    strEndTime = ndb.TimeProperty()
    strStatus = ndb.StringProperty(default="Scheduled") # Running , Completed
    strNotifyOnStart = ndb.BooleanProperty(default=True)
    strNotifyonEnd = ndb.BooleanProperty(default=True)

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
    def writeMessageID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMessageID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStartDate(self,strinput):
        try:
            if strinput != None:
                self.strStartDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStartTime(self,strinput):
        try:
            if strinput != None:
                self.strStartTime = strinput
                return True
            else:
                return False

        except:
            return False

    def writeEndTime(self,strinput):
        try:
            if strinput != None:
                self.strEndTime = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEndDate(self,strinput):
        try:
            if strinput != None:
                self.strEndDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStatus(self,strinput):
        try:
            strinput = str(strinput)

            if strinput in ['Scheduled','Running','Completed']:
                self.strStatus = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNotifyOnStart(self,strinput):
        try:
            if strinput in [True,False]:
                self.strNotifyOnStart = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNotifyonEnd(self,strinput):
        try:
            if strinput in [True,False]:
                self.strNotifyonEnd = strinput
                return True
            else:
                return False
        except:
            return False

class DeliveryReport(ndb.Expando):
    strMessageID = ndb.StringProperty()
    strGroupID = ndb.StringProperty()
    strCell = ndb.StringProperty()

    strResponse = ndb.StringProperty()
    strRef = ndb.StringProperty()
    strDelivered = ndb.BooleanProperty(default=False)
    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()
    strDateResponse = ndb.DateProperty()
    strTimeResponse = ndb.TimeProperty()
    strResponseReceived = ndb.BooleanProperty(default=False)


    def writeDateResponse(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateResponse = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeResponse(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeResponse = strinput
                return True
            else:
                return False
        except:
            return False
    def writeResponseReceived(self,strinput):
        try:
            if strinput in [True,False]:
                self.strResponseReceived = strinput
                return True
            else:
                return False
        except:
            return False

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


    def writeRef(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRef = strinput
                return True
            else:
                return False
        except:
            return False


    def writeMessageID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMessageID = strinput
                return True
            else:
                return False

        except:
            return False

    def writeGroupID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strGroupID = strinput
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

    def writeDelivered(self,strinput):
        try:
            if strinput in [True,False]:
                self.strDelivered = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDate(self,strinput):
        try:
            if strinput != None:
                self.strDate = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTime(self,strinput):
        try:
            if strinput != None:
                self.strTime = strinput
                return True
            else:
                return False
        except:
            return False

class SMSAccount(ndb.Expando):
    strChurchID = ndb.StringProperty()
    strCreditAmount = ndb.FloatProperty(default=0)
    strCostPerSMS = ndb.FloatProperty(default=50)
    strTotalSMS = ndb.IntegerProperty(default=10)
    strDateCredited = ndb.DateProperty()
    strTimeCredited = ndb.TimeProperty()
    strUsePortal = ndb.StringProperty(default="Budget") # Budget, Vodacom, ClickSend, Twilio

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
    def writeCreditAmount(self,strinput):
        try:
            if isinstance(strinput,float) or isinstance(strinput,int):
                self.strCreditAmount = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCostPerSMS(self,strinput):
        try:
            if isinstance(strinput,float) or isinstance(strinput,int):
                self.strCostPerSMS = strinput
                return True
            else:
                return False
        except:
            return False
    def CalculateTotalSMS(self):
        try:
            strTotalSMS = (self.strCreditAmount * 100)//self.strCostPerSMS
            return strTotalSMS
        except:
            return None
    def writeTotalSMS(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalSMS = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeDateCredited(self,strinput):
        try:

            if strinput != None:
                self.strDateCredited = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeCredited(self,strinput):
        try:
            if strinput != None:
                self.strTimeCredited = strinput
                return True
            else:
                return False
        except:
            return False
    def writeUsePortal(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUsePortal = strinput
                return True
            else:
                return False
        except:
            return False
    def AddTotalSMS(self,strinput):
        try:
            strinput = str(strinput)

            if strinput.isdigit():
                self.strTotalSMS += int(strinput)
                return True
            else:
                return False
        except:
            return False

class SMSPortalVodacom(ndb.Expando):
    """
        When using the CSV file format send the file as an attachment
    """
    strSenderAddress = ndb.StringProperty(default='sendsms@church-admins.appspotmail.com')
    strEmailAddress = ndb.StringProperty(default='mobjustice_sms@smsgw1.gsm.co.za')
    strCSVEmail = ndb.StringProperty(default="mobjustice@smsgw1.gsm.co.za")
    strSMSSizeLimit = ndb.IntegerProperty(default=600)
    strAvailableCredit = ndb.IntegerProperty(default=67)
    strBuyRate = ndb.IntegerProperty(default=32)
    strSellRate = ndb.IntegerProperty(default=50)
    strProfit = ndb.ComputedProperty(lambda self: self.strSellRate - self.strBuyRate)
    strPortalAddress = ndb.StringProperty(default="https://vodacommessaging.co.za")
    strSystemCredit = ndb.IntegerProperty(default=0)
    strPortalLogin = ndb.StringProperty(default=os.environ.get('PORTAL_VODACOM_USER'))
    strPortalPassword = ndb.StringProperty(default=os.environ.get('PORTAL_VODACOM_PASSWORD'))

    def writeSenderAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSenderAddress = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCSVEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCSVEmail = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEmailAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmailAddress = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSMSSixeLimit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 160):
                self.strSMSSizeLimit = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeAvailableCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 0):
                self.strAvailableCredit = int(strinput)
                return True
            else:
                return False

        except:
            return False
    def writeSellRate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= self.strBuyRate):
                self.strSellRate = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeBuyRate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 0):
                self.strBuyRate = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeSystemCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 0):
                self.strSystemCredit = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writePortaLogin(self,strinput):
        try:
            strinput = str(strinput)
            if (strinput == None):
                self.strPortalLogin = strinput
                return True
            else:
                return False
        except:
            return False
    def writePassword(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPortalPassword = strinput
                return True
            else:
                return False
        except:
            return False
    def writePortalAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPortalAddress = strinput
                return True
            else:
                return False
        except:
            return False
    def SendMessages(self,strCellNumberList,strMessage):
        Guser = users.get_current_user()
        try:
            strSubject = ""
            strInvalid = False
            if isinstance(strCellNumberList,list):
                for strCell in strCellNumberList:
                    if strSubject == "":
                        strSubject = strCell
                    else:
                        strSubject = strSubject + " " + strCell

            elif "," in strCellNumberList:
                strCellNumberList = strCellNumberList.split(",")
                for strCell in strCellNumberList:
                    if strSubject == "":
                        strSubject = strCell
                    else:
                        strSubject = strSubject + " " + strCell
            else:
                strInvalid = True

            if not(strInvalid):

                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                findRequest = SMSAccount.query(SMSAccount.strChurchID == thisChurchMember.strChurchID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                else:
                    thisSMSAccount = SMSAccount()
                    thisSMSAccount.writeChurchID(strinput=thisChurchMember.strChurchID)
                    thisSMSAccount.put()

                if thisSMSAccount.strTotalSMS >= len(strCellNumberList):

                    message = mail.EmailMessage()
                    message.sender = self.strSenderAddress
                    message.to = self.strEmailAddress
                    message.subject = strSubject
                    message.body = strMessage
                    thisSMSAccount.writeTotalSMS(strinput=str(thisSMSAccount.strTotalSMS - len(strCellNumberList)))
                    thisSMSAccount.put()
                    try:
                        self.writeAvailableCredit(strinput=str(self.strAvailableCredit - len(strCellNumberList)))
                        self.put()
                    except:
                        pass
                    message.send()
                    return True
                else:
                    return False
            else:
                return False


        except:
            return False

    def CronSendMessages(self,strCellNumberList,strMessage,strAccountID):
        try:

            strSubject = ""
            strInvalid = False
            if isinstance(strCellNumberList,list):
                for strCell in strCellNumberList:
                    if strSubject == "":
                        strSubject = strCell
                    else:
                        strSubject = strSubject + " " + strCell

            elif "," in strCellNumberList:
                strCellNumberList = strCellNumberList.split(",")
                for strCell in strCellNumberList:
                    if strSubject == "":
                        strSubject = strCell
                    else:
                        strSubject = strSubject + " " + strCell
            else:
                strInvalid = True

            if not(strInvalid):

                findRequest = SMSAccount.query(SMSAccount.strChurchID == strAccountID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                else:
                    thisSMSAccount = SMSAccount()
                    thisSMSAccount.writeChurchID(strinput=strAccountID)
                    thisSMSAccount.put()


                if thisSMSAccount.strTotalSMS >= len(strCellNumberList):
                    message = mail.EmailMessage()

                    message.sender = self.strSenderAddress

                    message.to = self.strEmailAddress
                    message.subject = strSubject
                    message.body = strMessage
                    thisSMSAccount.writeTotalSMS(strinput=str(thisSMSAccount.strTotalSMS - len(strCellNumberList)))
                    thisSMSAccount.put()
                    self.writeAvailableCredit(strinput=str(self.strAvailableCredit - len(strCellNumberList)))
                    self.put()
                    message.send()
                    return True
                else:
                    logging.info("This False")
                    return False
            else:
                logging.info("This Falesity")
                return False

        except:
            logging.info("Bad Exception")
            return False

class SMSPortalBudget(ndb.Expando):
    """
            Send Example
            e.g https://www.budgetmessaging.com/sendsms.ashx?user=john&password=4567&cell=1234567890&msg=test&ref=9999&senddate=DD/MM/YYYY
            Status Example
            e.g  https://www.budgetmessaging.com/smsstatus.ashx?user=john&password=4567&ref=9999&startdate=DD/MM/YYYY&enddate=DD/MM/YYYY

            Replies :
            Query by date range
            https://www.budgetmessaging.com/smsreply.ashx?user=john&password=4567&startdate=DD/MM/YYYY&enddate=DD/MM/YYYY
            Query by message

            Parameters:
            User (eg. john)
            Password
            ref (a unique string that can identify the message)

            e.g  https://www.budgetmessaging.com/smsreply.ashx?
            user=john&password=4567&ref=9999

            Query credits available on your account

            https://www.budgetmessaging.com/credits.ashx

            Parameters

            User (eg. john)
            Password

            e.g  https://www.budgetmessaging.com/credits.ashx?user=john&password=4567

            Return Resultset

            This api will return the number of credits available

    API Documentation
    HTTP posts are used by programmers to intergrate their existing applications into Budget Messaging.


    Send an SMS

    https://www.budgetmessaging.com/sendsms.ashx

    Parameters

    User (eg. john)
    Password
    cell (Cell number to which to send the message)
    msg (message)
    ref (a unique string that can identify the message)
    - This field is optional. If there is no user input, system will generate a 'ref' parameter
    senddate (e.g DD/MM/YYYY)
    - This field is optional. If there is no user input, system will set 'senddate' as today's date

    e.g https://www.budgetmessaging.com/sendsms.ashx?user=john&password=4567&cell=1234567890&msg=test&ref=9999&senddate=DD/MM/YYYY


    Query the status of an SMS

    https://www.budgetmessaging.com/smsstatus.ashx

    Parameters

    User (eg. john)
    Password
    ref (a unique string that can identify the message) - If querying by ref, use the following format REF_cellNum
    startdate (e.g DD/MM/YYYY)
    enddate (e.g DD/MM/YYYY)

    e.g  https://www.budgetmessaging.com/smsstatus.ashx?user=john&password=4567&ref=9999&startdate=DD/MM/YYYY&enddate=DD/MM/YYYY

    Return Resultset:

    This api will return the status of the messages.


    Content Types supported: text/html, text/xml, application/json


    Replies

    https://www.budgetmessaging.com/smsreply.ashx

    Query by date range

    Parameters:

    User (eg. john)
    Password
    startdate (e.g DD/MM/YYYY)
    enddate (e.g DD/MM/YYYY)

    e.g  https://www.budgetmessaging.com/smsreply.ashx?
    user=john&password=4567&startdate=DD/MM/YYYY&enddate=DD/MM/YYYY

    Query by message

    Parameters:

    User (eg. john)
    Password
    ref (a unique string that can identify the message)

    e.g  https://www.budgetmessaging.com/smsreply.ashx?
    user=john&password=4567&ref=9999


    Query credits available on your account

    https://www.budgetmessaging.com/credits.ashx

    Parameters

    User (eg. john)
    Password

    e.g  https://www.budgetmessaging.com/credits.ashx?user=john&password=4567

    Return Resultset

    This api will return the number of credits available


"""
    strSendHTTPS = ndb.StringProperty(default="https://www.budgetmessaging.com/sendsms.ashx")
    strStatusHTTPS = ndb.StringProperty(default="https://www.budgetmessaging.com/smsstatus.ashx")
    strRepliesHTTPS = ndb.StringProperty(default="https://www.budgetmessaging.com/smsreply.ashx")
    strCreditsHTTPS = ndb.StringProperty(default="https://www.budgetmessaging.com/credits.ashx")
    strLoginName = ndb.StringProperty(default=os.environ.get('PORTAL_BUDGET_USER'))
    strPassword = ndb.StringProperty(default=os.environ.get('PORTAL_BUDGET_PASSWORD'))
    strPortalAddress = ndb.StringProperty(default="https://www.budgetmessaging.com")

    strSMSSizeLimit = ndb.IntegerProperty(default=150)
    strAvailableCredit = ndb.IntegerProperty(default=0)
    strSellRate = ndb.IntegerProperty(default=50)
    strBuyRate = ndb.IntegerProperty(default=17)
    strProfit = ndb.ComputedProperty(lambda self: self.strSellRate - self.strBuyRate)
    strSystemCredit = ndb.IntegerProperty(default=0)


    def writeSystemCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 0):
                self.strSystemCredit = int(strinput)
                return  True
            else:
                return False
        except:
            return False
    def writeBuyRate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 0):
                self.strBuyRate = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeSendHTTPS(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSendHTTPS = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStatusHTTPS(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strStatusHTTPS = strinput
                return True
            else:
                return False

        except:
            return False
    def writeRepliesHTTPS(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRepliesHTTPS = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCreditHTTPS(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCreditsHTTPS = strinput
                return True
            else:
                return False
        except:
            return False
    def writeLoginName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strLoginName = strinput
                return True
            else:
                return False
        except:
            return False
    def writePassword(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPassword = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSMSSizeLimit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strSMSSizeLimit = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeAvailableCredit(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strAvailableCredit = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeSellRate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strSellRate = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writePortalAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPortalAddress = strinput
                return True
            else:
                return False

        except:
            return False
    def SendMessage(self,strMessage,strMessageID,strCell):
        """

        :param strMessage:
        :param strMessageID: Message ID Will replace the system own ID Field
        :param strCell:
        :return:
        """
        try:

            strMessage = strMessage + " Optout:Reply STOP"
            form_data = 'user=' + self.strLoginName + '&password=' + self.strPassword + '&cell=' + strCell + '&msg=' + strMessage + '&ref=' + strMessageID
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.strSendHTTPS,payload=form_data,method=urlfetch.POST,headers=headers,validate_certificate=True)
            if result.status_code == 200:
                strResult = result.content
                strResult = strResult.replace("ACCEPTED"," ")
                strResult = strResult.strip()
                return strResult
            else:
                return None
        except urlfetch.Error:
            return None

    def SendCronMessage(self,strMessage,strCell):
        try:
            strMessage = strMessage + " Optout:Reply STOP"
            form_data = 'user=' + self.strLoginName + '&password=' + self.strPassword + '&cell=' + strCell + '&msg=' + strMessage
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.strSendHTTPS,payload=form_data,method=urlfetch.POST,headers=headers,validate_certificate=True)

            if result.status_code == 200:
                strResult = result.content
                strResult = strResult.replace("ACCEPTED"," ")
                strResult = strResult.strip()
                return strResult
            else:
                return None
        except urlfetch.Error:
            return None

    def CheckMessageStatus(self,strRef,strCell):
        try:
            if "ACCEPTED" in strRef:
                strRef = strRef.replace("ACCEPTED","")

            strRef = strRef.strip()
            logging.info(strRef)
            form_data = 'user=' + self.strLoginName + '&password=' + self.strPassword + '&ref=' + strRef+"_"+strCell
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.strStatusHTTPS, payload=form_data, method=urlfetch.POST, headers=headers,validate_certificate=True)

            if result.status_code == 200:
                return result.content
            else:
                return None

        except urlfetch.Error:
            return None


    def CheckMessageStatusByDateRange(self,strMessageID,strStartDate,strEndDate):
        """
        format of StartDate = DD/MM/YYYY
        format of EndDate = DD/MM/YYYY
        :param strMessageID:
        :param strStartDate:
        :param strEndDate:
        :return:
        """
        try:
            form_data = '&user=' + self.strLoginName + '&password=' + self.strPassword + '&ref=' + strMessageID + '&startdate=' + strStartDate + '&enddate=' + strEndDate
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.strStatusHTTPS, payload=form_data, method=urlfetch.POST, headers=headers,validate_certificate=True)
            return result.content
        except urlfetch.Error:
            return None


    def CheckMessageReplies(self,strStartDate,strEndDate):
        try:
            form_data = '&user=' + self.strLoginName + '&password=' + self.strPassword + '&startdate=' + strStartDate + '&enddate=' + strEndDate
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.strRepliesHTTPS, payload=form_data, method=urlfetch.POST, headers=headers,
                                    validate_certificate=True)

            if result.status_code == 200:
                xStatusMessage = ElementTree.fromstring(result.content)
                return xStatusMessage
            else:
                return None

        except urlfetch.Error:
            return None

    def CheckSpecificReply(self,strRef):
        try:
            if "ACCEPTED" in strRef:
                strRef = strRef.replace("ACCEPTED","")
            strRef = strRef.strip()

            logging.info(strRef)
            form_data = 'user=' + self.strLoginName + '&password=' + self.strPassword + '&ref=' + strRef
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.strRepliesHTTPS, payload=form_data, method=urlfetch.POST, headers=headers,
                                    validate_certificate=True)

            if result.status_code == 200:
                xStatusMessage = ElementTree.fromstring(result.content)
                strStatusMessage = xStatusMessage.findtext(".//message")
                if not(strStatusMessage == None):
                    return strStatusMessage
                else:
                    return None
            else:
                return None

        except urlfetch.Error:
            logging.exception('Caught exception fetching ' + self.strRepliesHTTPS)


    def CheckCredits(self):
        try:
            form_data = '&user=' + self.strLoginName + '&password=' + self.strPassword
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.strCreditsHTTPS, payload=form_data, method=urlfetch.POST, headers=headers,
                                    validate_certificate=True)

            logging.info(result.content)
            return result.content

        except urlfetch.Error:
            return None

class mySMSHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightList = findRequest.fetch()
            if len(thisUserRightList) > 0:
                thisUserRight = thisUserRightList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisAdminList = findRequest.fetch()
                if len(thisAdminList) > 0:
                    thisAdmin = thisAdminList[0]
                else:
                    thisAdmin = ChurchMember()

                findRequest = Groups.query(Groups.strChurchID == thisAdmin.strChurchID)
                thisGroupsList = findRequest.fetch()

                template = template_env.get_template('templates/sms/sms.html')
                context = {}
                self.response.write(template.render(context))

class SMSGroupHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "1":
                findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
                thisUserRightList = findRequest.fetch()
                if len(thisUserRightList) > 0:
                    thisUserRight = thisUserRightList[0]
                else:
                    thisUserRight = UserRights()

                if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisAdminList = findRequest.fetch()
                    if len(thisAdminList) > 0:
                        thisAdmin = thisAdminList[0]
                    else:
                        thisAdmin = ChurchMember()

                    findRequest = Groups.query(Groups.strChurchID == thisAdmin.strChurchID)
                    thisGroupsList = findRequest.fetch()

                    template = template_env.get_template('templates/sms/creategroups.html')
                    context = {'thisGroupsList':thisGroupsList}
                    self.response.write(template.render(context))

            elif vstrChoice == "2":
                vstrGroupName = self.request.get('vstrGroupName')
                vstrGroupDescription = self.request.get('vstrGroupDescription')

                findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
                thisUserRightsList = findRequest.fetch()
                if len(thisUserRightsList) > 0:
                    thisUserRight = thisUserRightsList[0]
                else:
                    thisUserRight = UserRights()

                if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisAdminList = findRequest.fetch()

                    if len(thisAdminList) > 0:
                        thisAdmin = thisAdminList[0]
                    else:
                        thisAdmin = ChurchMember()

                    findRequest = Groups.query(Groups.strGroupName == vstrGroupName, Groups.strChurchID == thisAdmin.strChurchID)
                    thisGroupList = findRequest.fetch()

                    if len(thisGroupList) > 0:
                        thisGroup = thisGroupList[0]
                    else:
                        thisGroup = Groups()

                    thisGroup.writeChurchID(strinput=thisAdmin.strChurchID)
                    thisGroup.writeChurchBranchID(strinput=thisAdmin.strChurchBranchID)
                    thisGroup.writeGroupName(strinput=vstrGroupName)
                    thisGroup.writeGroupDescription(strinput=vstrGroupDescription)
                    thisGroup.writeMemberID(strinput=Guser.user_id())
                    thisGroup.writeGroupID(strinput=thisGroup.CreateGroupID())
                    thisGroup.put()

                    self.response.write('Group Successfully created ')


            elif vstrChoice == "3":
                pass

            elif vstrChoice == "4":
                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                findRequest = UserRights.query(UserRights.strMemberID == thisChurchMember.strMemberID)
                thisUserRightList = findRequest.fetch()

                if len(thisUserRightList) > 0:
                    thisUserRight = thisUserRightList[0]
                else:
                    thisUserRight = UserRights()

                if thisUserRight.strAdminUser:
                    findRequest = SMSAccount.query(SMSAccount.strChurchID == thisChurchMember.strChurchID)
                    thisSMSAccountList = findRequest.fetch()

                    if len(thisSMSAccountList) > 0:
                        thisSMSAccount = thisSMSAccountList[0]
                    else:
                        thisSMSAccount = SMSAccount()
                        thisSMSAccount.writeChurchID(strinput=thisChurchMember.strChurchID)
                        thisSMSAccount.put()

                    findRequest = SMSPortalVodacom.query()
                    thisVodacomPortalList = findRequest.fetch()

                    if len(thisVodacomPortalList) > 0:
                        thisVodacomPortal = thisVodacomPortalList[0]

                    else:
                        thisVodacomPortal = SMSPortalVodacom()

                    findRequest = SMSPortalBudget.query()
                    thisBudgetPortalList = findRequest.fetch()

                    if len(thisBudgetPortalList) > 0:
                        thisBudgetPortal = thisBudgetPortalList[0]
                    else:
                        thisBudgetPortal = SMSPortalBudget()




                    template = template_env.get_template('templates/sms/groups/account.html')
                    context = {'thisSMSAccount':thisSMSAccount,'thisVodacomPortal':thisVodacomPortal,'thisBudgetPortal':thisBudgetPortal}
                    self.response.write(template.render(context))


            elif vstrChoice == "5":

                template = template_env.get_template('templates/sms/groups/reports.html')
                context = {}
                self.response.write(template.render(context))

class GroupManagerHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            URL = self.request.url
            URLlist = URL.split("/")
            strGroupID = URLlist[len(URLlist) - 1]


            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisAdminList = findRequest.fetch()
                if len(thisAdminList) > 0:
                    thisAdmin = thisAdminList[0]
                else:
                    thisAdmin = ChurchMember()

                findRequest = Groups.query(Groups.strChurchID == thisAdmin.strChurchID,Groups.strGroupID == strGroupID)
                thisGroupList = findRequest.fetch()

                if len(thisGroupList) > 0:
                    thisGroup = thisGroupList[0]
                else:
                    thisGroup = Groups()

                template = template_env.get_template('templates/sms/thisGroup.html')
                context = {'thisGroup':thisGroup}
                self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:

            vstrChoice = self.request.get('vstrChoice')
            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisAdminList = findRequest.fetch()

            if len(thisAdminList) > 0:
                thisAdmin = thisAdminList[0]
            else:
                thisAdmin = ChurchMember()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:

                if vstrChoice == "0":
                    vstrGroupID = self.request.get('vstrGroupID')

                    findRequest = SMSContacts.query(SMSContacts.strGroupID == vstrGroupID)
                    thisContactList = findRequest.fetch()

                    template = template_env.get_template('templates/sms/groups/upcontacts.html')
                    context = {'thisContactList':thisContactList,'vstrGroupID':vstrGroupID}
                    self.response.write(template.render(context))

                elif vstrChoice == "1":

                    vstrNames = self.request.get('vstrNames')
                    vstrSurname = self.request.get('vstrSurname')
                    vstrCellNumber = self.request.get('vstrCellNumber')

                    URL = self.request.url
                    URLlist = URL.split("/")
                    vstrGroupID = URLlist[len(URLlist) - 1]



                    findRequest = SMSContacts.query(SMSContacts.strGroupID == vstrGroupID,SMSContacts.strCellNumber == vstrCellNumber)
                    thisContactList = findRequest.fetch()

                    if len(thisContactList) > 0:
                        thisContact = thisContactList[0]
                    else:
                        thisContact = SMSContacts()

                    findRequest = ChurchMember.query(ChurchMember.strCell == vstrCellNumber)
                    thisChurchMemberList = findRequest.fetch()
                    if len(thisChurchMemberList) > 0:
                        thisChurchMember = thisChurchMemberList[0]
                    else:
                        thisChurchMember = ChurchMember()

                    thisContact.writeGroupID(strinput=vstrGroupID)
                    thisContact.writeMemberID(strinput=thisChurchMember.strMemberID)
                    thisContact.writeNames(strinput=vstrNames)
                    thisContact.writeSurname(strinput=vstrSurname)
                    thisContact.writeCellNumber(strinput=vstrCellNumber)

                    thisContact.put()

                    findRequest = Groups.query(Groups.strGroupID == vstrGroupID,Groups.strChurchID == thisChurchMember.strChurchID)
                    thisGroupList = findRequest.fetch()

                    if len(thisGroupList) > 0:
                        thisGroup = thisGroupList[0]
                    else:
                        thisGroup = Groups()

                    thisGroup.writeTotalNumbers(strinput=str(thisGroup.strTotalNumbers + 1))
                    thisGroup.put()

                    self.response.write("Contact Successfully uploaded")

                elif vstrChoice == "2":
                    vstrGroupID = self.request.get('vstrGroupID')

                    findRequest = Messages.query(Messages.strGroupID == vstrGroupID)
                    thisMessagesList = findRequest.fetch()

                    template = template_env.get_template('templates/sms/groups/createmessage.html')
                    context = {'thisMessagesList':thisMessagesList,'vstrGroupID':vstrGroupID}
                    self.response.write(template.render(context))

                elif vstrChoice == "3":
                    vstrGroupID = self.request.get('vstrGroupID')
                    vstrMessage = self.request.get('vstrMessage')

                    thisMessage = Messages()
                    thisMessage.writeGroupID(strinput=vstrGroupID)
                    thisMessage.writeMessageID(strinput=thisMessage.CreateMessageID())
                    thisMessage.writeMessage(strinput=vstrMessage)
                    thisDate = datetime.datetime.now()
                    thisDate = thisDate.date()

                    thisTime = datetime.datetime.now()
                    thisTime = thisTime.time()
                    thisTime = datetime.time(hour=thisTime.hour,minute=thisTime.minute,second=thisTime.second)
                    thisMessage.writeDateCreated(strinput=thisDate)
                    thisMessage.writeTimeCreated(strinput=thisTime)


                    thisMessage.put()
                    self.response.write("Message Uploaded successfully")

                elif vstrChoice == "4":
                    vstrMemberID = self.request.get('vstrMemberID')
                    vstrGroupList = self.request.get('vstrGroupList')

                    if len(vstrGroupList) > 0:
                        vstrGroupList = vstrGroupList.split(",")
                    else:
                        vstrGroupList = []

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == vstrMemberID)
                    thisChurchMemberList = findRequest.fetch()

                    if len(thisChurchMemberList) > 0:
                        thisChurchMember = thisChurchMemberList[0]
                    else:
                        thisChurchMember = ChurchMember()

                    strAssigned = False
                    for strGroupID in vstrGroupList:
                        thisSMSContacts = SMSContacts()


                        thisSMSContacts.writeMemberID(strinput=thisChurchMember.strMemberID)
                        thisSMSContacts.writeNames(strinput=thisChurchMember.strMemberNames)
                        thisSMSContacts.writeSurname(strinput=thisChurchMember.strMemberSurname)
                        thisSMSContacts.writeCellNumber(strinput=thisChurchMember.strCell)
                        thisSMSContacts.writeGroupID(strinput=strGroupID)

                        thisSMSContacts.put()
                        findRequest = Groups.query(Groups.strGroupID == strGroupID)
                        thisGroupsList = findRequest.fetch()
                        if len(thisGroupsList) > 0:
                            thisGroup = thisGroupsList[0]
                        else:
                            thisGroup = Groups()

                        thisGroup.writeTotalNumbers(strinput=str(thisGroup.strTotalNumbers + 1))
                        thisGroup.put()
                        strAssigned = True

                    if not(strAssigned):
                        self.response.write("Church Member not assigned into Groups")
                    else:
                        self.response.write("Church Member Subscribed to selected SMS Groups")

                elif vstrChoice == "5":
                    vstrGroupID = self.request.get('vstrGroupID')

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisChurchMemberList = findRequest.fetch()

                    if len(thisChurchMemberList) > 0:
                        thisChurchMember = thisChurchMemberList[0]
                    else:
                        thisChurchMember = ChurchMember()

                    findRequest = UserRights.query(UserRights.strMemberID == thisChurchMember.strMemberID)
                    thisUserRightsList = findRequest.fetch()

                    if len(thisUserRightsList) > 0:
                        thisUserRight = thisUserRightsList[0]
                    else:
                        thisUserRight = UserRights()

                    if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                        findRequest = Groups.query(Groups.strGroupID == vstrGroupID,Groups.strChurchID == thisChurchMember.strChurchID)
                        thisGroupList = findRequest.fetch()

                        if len(thisGroupList) > 0:
                            thisGroup = thisGroupList[0]
                        else:
                            thisGroup = Groups()

                        findRequest = SMSContacts.query(SMSContacts.strGroupID == thisGroup.strGroupID)
                        thisSMSContactsList = findRequest.fetch()

                        template = template_env.get_template('templates/sms/groups/editGroup.html')
                        context = {'thisGroup':thisGroup,'thisSMSContactsList':thisSMSContactsList}
                        self.response.write(template.render(context))


                elif vstrChoice == "6":
                    vstrGroupID = self.request.get('vstrGroupID')
                    vstrGroupName = self.request.get('vstrGroupName')
                    vstrGroupDescription = self.request.get('vstrGroupDescription')

                    findRequest = Groups.query(Groups.strGroupID == vstrGroupID)
                    thisGroupList = findRequest.fetch()

                    if len(thisGroupList) > 0:
                        thisGroup = thisGroupList[0]
                    else:
                        thisGroup = Groups()

                    thisGroup.writeGroupName(strinput=vstrGroupName)
                    thisGroup.writeGroupDescription(strinput=vstrGroupDescription)
                    thisGroup.put()

                    self.response.write("SMS Group Successfully updated")



                elif vstrChoice == "7":
                    vstrGroupID = self.request.get('vstrGroupID')

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisChurchMemberList = findRequest.fetch()

                    if len(thisChurchMemberList) > 0:
                        thisChurchMember = thisChurchMemberList[0]
                    else:
                        thisChurchMember = ChurchMember()

                    findRequest = UserRights.query(UserRights.strMemberID == thisChurchMember.strMemberID)
                    thisUserRightsList = findRequest.fetch()

                    if len(thisUserRightsList) > 0:
                        thisUserRight = thisUserRightsList[0]
                    else:
                        thisUserRight = UserRights()

                    if thisUserRight.strAdminUser:
                        findRequest = Groups.query(Groups.strGroupID == vstrGroupID,Groups.strChurchID == thisChurchMember.strChurchID)
                        thisGroupList = findRequest.fetch()

                        if len(thisGroupList) > 0:
                            thisGroup = thisGroupList[0]
                        else:
                            thisGroup = Groups()

                        template = template_env.get_template('templates/sms/groups/deleteGroup.html')
                        context = {'thisGroup':thisGroup}
                        self.response.write(template.render(context))


                elif vstrChoice == "8":
                    vstrGroupID = self.request.get('vstrGroupID')

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisChurchMemberList = findRequest.fetch()

                    if len(thisChurchMemberList) > 0:
                        thisChurchMember = thisChurchMemberList[0]
                    else:
                        thisChurchMember = ChurchMember()

                    findRequest = UserRights.query(UserRights.strMemberID == thisChurchMember.strMemberID)
                    thisUserRightsList = findRequest.fetch()

                    if len(thisUserRightsList) > 0:
                        thisUserRight = thisUserRightsList[0]
                    else:
                        thisUserRight = UserRights()

                    if thisUserRight.strAdminUser:
                        findRequest = Groups.query(Groups.strGroupID == vstrGroupID,Groups.strChurchID == thisChurchMember.strChurchID)
                        thisGroupList = findRequest.fetch()

                        for thisGroup in thisGroupList:
                            thisGroup.key.delete()

                        findRequest = SMSContacts.query(SMSContacts.strGroupID == vstrGroupID)
                        thisContactList = findRequest.fetch()

                        for thisContact in thisContactList:
                            thisContact.key.delete()

                        self.response.write("SMS Group Successfully Deleted")
                        #TODO- Try redirecting the user from the page by using a timed javascript redirector

                elif vstrChoice == "9":
                    vstrGroupID = self.request.get('vstrGroupID')
                    vstrContacts = self.request.get('vstrContacts')
                    logging.info(vstrContacts)

                    vstrContactList = vstrContacts.split("|")

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisChurchMemberList = findRequest.fetch()

                    if len(thisChurchMemberList) > 0:
                        thisChurchMember = thisChurchMemberList[0]
                    else:
                        thisChurchMember = ChurchMember()

                    findRequest = UserRights.query(UserRights.strMemberID == thisChurchMember.strMemberID)
                    thisUserRightList = findRequest.fetch()

                    if len(thisUserRightList) > 0:
                        thisUserRight = thisUserRightList[0]
                    else:
                        thisUserRight = UserRights()

                    if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                        for vstrContact in vstrContactList :
                            if len(vstrContact) > 10:
                                try:
                                    vstrConList = vstrContact.split(",")
                                    vstrCell = vstrConList[0]
                                    vstrFirstname = vstrConList[1]
                                    vstrSurname = vstrConList[2]
                                    findRequest = SMSContacts.query(SMSContacts.strCellNumber == vstrCell)
                                    thisContactList = findRequest.fetch()

                                    if len(thisContactList) > 0:
                                        thisContact = thisContactList[0]
                                    else:
                                        thisContact = SMSContacts()
                                    findRequest = ChurchMember.query(ChurchMember.strChurchID == thisChurchMember.strChurchID,ChurchMember.strCell == vstrCell)
                                    thisContactDataList = findRequest.fetch()
                                    if len(thisContactDataList) > 0:
                                        thisConData = thisContactDataList[0]
                                    else:
                                        thisConData = ChurchMember()

                                    thisContact.writeCellNumber(strinput=vstrCell)
                                    thisContact.writeGroupID(strinput=vstrGroupID)
                                    thisContact.writeNames(strinput=vstrFirstname)
                                    thisContact.writeSurname(strinput=vstrSurname)
                                    thisContact.writeMemberID(strinput=thisConData.strMemberID)
                                    thisContact.put()

                                    findRequest = Groups.query(Groups.strChurchID == thisChurchMember.strChurchID,Groups.strGroupID == vstrGroupID)
                                    thisGroupList = findRequest.fetch()

                                    if len(thisGroupList) > 0:
                                        thisGroup = thisGroupList[0]
                                        thisGroup.writeTotalNumbers(strinput=str(thisGroup.strTotalNumbers + 1))
                                        thisGroup.put()
                                except:
                                    pass

                        self.response.write("Successfully Loaded all Bulk Contacts")
                    else:
                        self.response.write("Unable to load bulk contacts as you are not allowed to perform this operation")

                elif vstrChoice == "10":
                    vstrGroupID = self.request.get('vstrGroupID')

                    findRequest = DeliveryReport.query(DeliveryReport.strGroupID == vstrGroupID)
                    thisDeliveryReportList = findRequest.fetch()

                    template  =template_env.get_template('templates/sms/groups/groupreports.html')
                    context = {'thisDeliveryReportList':thisDeliveryReportList}
                    self.response.write(template.render(context))


                elif vstrChoice == "11":
                    vstrGroupID = self.request.get('vstrGroupID')
                    vstrRemoveCell = self.request.get('vstrRemoveCell')

                    findRequest = SMSContacts.query(SMSContacts.strGroupID == vstrGroupID,SMSContacts.strCellNumber == vstrRemoveCell)
                    thisSMSContactsList = findRequest.fetch()

                    for thisContact in thisSMSContactsList:
                        thisContact.key.delete()
                    self.response.write("Successfully delete contact")

class thisSMSManagerHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = self.request.url
            URLlist = URL.split("/")
            vstrMessageID = URLlist[len(URLlist) - 1]

            findRequest = Messages.query(Messages.strMessageID == vstrMessageID)
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


            template = template_env.get_template('templates/sms/groups/thisMessage.html')
            context = {'thisMessage':thisMessage,'thisGroup':thisGroup}
            self.response.write(template.render(context))


    def post(self):
        Guser = users.get_current_user()
        from myemail import SendEmail
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrMessageID = self.request.get('vstrMessageID')
                vstrGroupID = self.request.get('vstrGroupID')

                findRequest = Messages.query(Messages.strMessageID == vstrMessageID,Messages.strGroupID == vstrGroupID)
                thisMessageList = findRequest.fetch()

                if len(thisMessageList) > 0:
                    thisMessage = thisMessageList[0]
                else:
                    thisMessage  = Messages()

                template = template_env.get_template('templates/sms/groups/message/editsms.html')
                context = {'thisMessage':thisMessage,'vstrMessageID':vstrMessageID,'vstrGroupID':vstrGroupID}
                self.response.write(template.render(context))

            elif vstrChoice == "1":
                vstrGroupID = self.request.get('vstrGroupID')
                vstrMessageID = self.request.get('vstrMessageID')
                vstrMessage = self.request.get('vstrMessage')

                findRequest = Messages.query(Messages.strMessageID == vstrMessageID,Messages.strGroupID == vstrGroupID)
                thisMessageList = findRequest.fetch()

                if len(thisMessageList) > 0:
                    thisMessage = thisMessageList[0]
                else:
                    thisMessage  = Messages()

                thisMessage.writeMessage(strinput=vstrMessage)
                thisMessage.put()
                self.response.write("Successfully updated Message")

            elif vstrChoice == "2":
                vstrGroupID = self.request.get('vstrGroupID')
                vstrMessageID = self.request.get('vstrMessageID')

                findRequest = MessageSchedule.query(MessageSchedule.strMessageID == vstrMessageID)
                thisMessageScheduleList = findRequest.fetch()

                if len(thisMessageScheduleList) > 0:
                    thisMessageSchedule = thisMessageScheduleList[0]
                else:
                    thisMessageSchedule = MessageSchedule()



                template = template_env.get_template('templates/sms/groups/message/schedule.html')
                context = {'thisMessageSchedule':thisMessageSchedule,'vstrGroupID':vstrGroupID,'vstrMessageID':vstrMessageID}
                self.response.write(template.render(context))

            elif vstrChoice == "3":
                vstrGroupID = self.request.get('vstrGroupID')
                vstrMessageID = self.request.get('vstrMessageID')
                vstrScheduleTime = self.request.get('vstrScheduleTime')
                vstrNotifyOnStart = self.request.get('vstrNotifyOnStart')
                vstrNotifyOnEnd = self.request.get('vstrNotifyOnEnd')


                findRequest = MessageSchedule.query(MessageSchedule.strMessageID == vstrMessageID)
                thisMessageScheduleList = findRequest.fetch()

                if len(thisMessageScheduleList) > 0:
                    thisMessageSchedule = thisMessageScheduleList[0]
                else:
                    thisMessageSchedule = MessageSchedule()
                try:
                    logging.info("THIS IS WHAT I AM GETTING : " + vstrScheduleTime)
                    vstrScheduleTime = vstrScheduleTime.split("-")
                    vstrBeginDateTime = vstrScheduleTime[0]
                    vstrEndDateTime = vstrScheduleTime[1]

                    vstrBeginDateTime = vstrBeginDateTime.strip()
                    vstrEndDateTime = vstrEndDateTime.strip()

                    vstrBeginDateTimeList = vstrBeginDateTime.split(" ")
                    vstrEndDateTimeList = vstrEndDateTime.split(" ")

                    vstrBeginDate = vstrBeginDateTimeList[0]
                    vstrBeginTime = vstrBeginDateTimeList[1]

                    vstrEndDate = vstrEndDateTimeList[0]
                    vstrEndTime = vstrEndDateTimeList[1]

                    vstrBeginDateList = vstrBeginDate.split("/")
                    vstrBeginTimeList = vstrBeginTime.split(":")

                    vstrBeginDay = vstrBeginDateList[1]
                    vstrBeginMonth = vstrBeginDateList[0]
                    vstrBeginYear = vstrBeginDateList[2]
                    vstrBeginHour = vstrBeginTimeList[0]
                    vstrBeginMinute = vstrBeginTimeList[1]
                    vstrBeginSecond = 0

                    vstrEndDateList = vstrEndDate.split("/")
                    vstrEndTimeList = vstrEndTime.split(":")

                    vstrEndDay = vstrEndDateList[1]
                    vstrEndMonth = vstrEndDateList[0]
                    vstrEndYear = vstrEndDateList[2]
                    vstrEndHour = vstrEndTimeList[0]
                    vstrEndMinute = vstrEndTimeList[1]
                    vstrEndSecond = 0

                    vstrBeginDate = datetime.date(year=int(vstrBeginYear),month=int(vstrBeginMonth),day=int(vstrBeginDay))
                    vstrBeginTime = datetime.time(hour=int(vstrBeginHour),minute=int(vstrBeginMinute),second=vstrBeginSecond)
                    vstrEndDate = datetime.date(year=int(vstrEndYear),month=int(vstrEndMonth),day=int(vstrEndDay))
                    vstrEndTime = datetime.time(hour=int(vstrEndHour),minute=int(vstrEndMinute),second=int(vstrEndSecond))
                except:
                    strToday = datetime.datetime.now()
                    strThisDate = strToday.date()
                    strThisTime = strToday.time()
                    vstrEndTime = strThisTime


                    strThisTime += datetime.timedelta(minutes=15)
                    vstrBeginDate = strThisDate
                    vstrBeginTime = strThisTime
                    vstrEndDate = strThisDate
                    vstrEndTime += datetime.timedelta(minutes=135)

                thisMessageSchedule.writeMessageID(strinput=vstrMessageID)
                thisMessageSchedule.writeStartDate(strinput=vstrBeginDate)
                thisMessageSchedule.writeStartTime(strinput=vstrBeginTime)
                thisMessageSchedule.writeEndDate(strinput=vstrEndDate)
                thisMessageSchedule.writeEndTime(strinput=vstrEndTime)
                if vstrNotifyOnStart == "Yes":
                    thisMessageSchedule.writeNotifyOnStart(strinput=True)
                else:
                    thisMessageSchedule.writeNotifyOnStart(strinput=False)

                if vstrNotifyOnEnd == "No":
                    thisMessageSchedule.writeNotifyonEnd(strinput=True)
                else:
                    thisMessageSchedule.writeNotifyonEnd(strinput=False)

                thisMessageSchedule.writeMemberID(strinput=Guser.user_id())

                thisMessageSchedule.put()

                self.response.write("Successfully created Schedule")
            elif vstrChoice == "4":
                vstrGroupID = self.request.get('vstrGroupID')
                vstrMessageID = self.request.get('vstrMessageID')

                findRequest = Messages.query(Messages.strMessageID == vstrMessageID,Messages.strGroupID == vstrGroupID)
                thisMessagesList = findRequest.fetch()
                if len(thisMessagesList) > 0:
                    thisMessage = thisMessagesList[0]
                else:
                    thisMessage = Messages()

                findRequest = Groups.query(Groups.strGroupID == vstrGroupID)
                thisGroupList = findRequest.fetch()

                if len(thisGroupList) > 0:
                    thisGroup = thisGroupList[0]
                else:
                    thisGroup = Groups()

                findRequest = SMSContacts.query(SMSContacts.strGroupID == vstrGroupID)
                thisSMSContactsList = findRequest.fetch()

                findRequest = SMSAccount.query(SMSAccount.strChurchID == thisGroup.strChurchID)
                thisSMSAccountList = findRequest.fetch()
                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                else:
                    thisSMSAccount = SMSAccount()
                    thisSMSAccount.writeChurchID(strinput=thisGroup.strChurchID)
                    thisSMSAccount.put()
                    findRequest = SMSAccount.query(SMSAccount.strChurchID == thisGroup.strChurchID)
                    SMSAccountList = findRequest.fetch()

                    if len(SMSAccountList) > 0:
                        thisSMSAccount = SMSAccountList[0]


                template = template_env.get_template('templates/sms/groups/message/sendSMS.html')
                context = {'thisMessage':thisMessage,'thisGroup':thisGroup,'thisSMSContactsList':thisSMSContactsList,'thisSMSAccount':thisSMSAccount}
                self.response.write(template.render(context))

            elif vstrChoice == "5":
                vstrGroupID = self.request.get('vstrGroupID')
                vstrMessageID = self.request.get('vstrMessageID')


                findRequest = Messages.query(Messages.strMessageID == vstrMessageID,Messages.strGroupID == vstrGroupID)
                thisMessagesList = findRequest.fetch()
                if len(thisMessagesList) > 0:
                    thisMessage = thisMessagesList[0]
                else:
                    thisMessage = Messages()

                findRequest = Groups.query(Groups.strGroupID == vstrGroupID)
                thisGroupList = findRequest.fetch()

                if len(thisGroupList) > 0:
                    thisGroup = thisGroupList[0]
                else:
                    thisGroup = Groups()


                findRequest = SMSContacts.query(SMSContacts.strGroupID == vstrGroupID)
                thisSMSContactsList = findRequest.fetch()

                findRequest = SMSAccount.query(SMSAccount.strChurchID == thisGroup.strChurchID)
                thisSMSAccountList = findRequest.fetch()
                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]
                else:
                    thisSMSAccount = SMSAccount()
                    thisSMSAccount.writeChurchID(strinput=thisGroup.strChurchID)
                    thisSMSAccount.put()
                    findRequest = SMSAccount.query(SMSAccount.strChurchID == thisGroup.strChurchID)
                    SMSAccountList = findRequest.fetch()

                    if len(SMSAccountList) > 0:
                        thisSMSAccount = SMSAccountList[0]


                if thisSMSAccount.strUsePortal == "Vodacom":

                    findRequest = SMSPortalVodacom.query()
                    thisPortalList = findRequest.fetch()

                    if len(thisPortalList) > 0:
                        thisPortal = thisPortalList[0]
                    else:
                        thisPortal = SMSPortalVodacom()

                    i = 0
                    self.response.write("""
                    <div class="box box-body with-border">
                        <div class="box box-body with-border">
                            <h3 class="box-title">Messages Sent Through Blue IT Marketing Voda Portal</h3>
                        </div>

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
                    while (thisSMSAccount.strTotalSMS > 0) and (i < len(thisSMSContactsList)):
                        thisContact = thisSMSContactsList[i]
                        if SendEmail(strFrom=thisPortal.strSenderAddress,strTo=thisPortal.strEmailAddress,strSubject=thisContact.strCellNumber,strBody=thisMessage.strMessage,strTextType='text/plain'):
                            self.response.write("""
                            <tr> <td> """ + thisContact.strNames + """</td><td> """ + thisContact.strSurname + """</td><td>""" +  thisContact.strCellNumber + """</td><td> <span class="label label-success">Sent</span> </td></tr>""")
                            i = i + 1
                            thisPortal.strAvailableCredit = thisPortal.strAvailableCredit - 1
                            thisDeliveryReport = DeliveryReport()
                            thisDeliveryReport.writeGroupID(thisGroup.strGroupID)
                            thisDeliveryReport.writeCell(thisContact.strCellNumber)
                            thisDeliveryReport.writeDelivered(strinput=True)
                            thisDate = datetime.datetime.now()
                            strThisDate = thisDate.date()
                            strThisTime = thisDate.time()
                            strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,second=strThisTime.second)
                            thisDeliveryReport.writeDate(strinput=strThisDate)
                            thisDeliveryReport.writeTime(strinput=strThisTime)
                            thisDeliveryReport.writeMessageID(strinput=thisMessage.strMessageID)
                            thisDeliveryReport.put()
                        else:
                            self.response.write("""
                            <tr> <td> """ + thisContact.strNames + """</td><td> """ + thisContact.strSurname + """</td><td>""" +  thisContact.strCellNumber + """</td><td> <span class="label label-danger">Not Sent</span> </td></tr>""")

                    self.response.write("""</tbody><tfoot><tr>
                            <tr>
                                <td>Names</td>
                                <td>Surname</td>
                                <td>Cell</td>
                                <td>Status</td>
                            </tr>
                            </tfoot>
                            </table>

                            </div>
                    """)
                    thisPortal.put()
                    i = i + 1
                    thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - (i)
                    thisSMSAccount.put()
                    thisMessage.writeSubmitted(strinput=True)

                    thisDate = datetime.datetime.now()
                    strThisDate = thisDate.date()
                    strThisTime = thisDate.time()
                    strThisTime = datetime.time(hour=strThisTime.hour,minute=strThisTime.minute,second=strThisTime.second)
                    thisMessage.writeDateSubmitted(strinput=strThisDate)
                    thisMessage.writeTimeSubmitted(strinput=strThisTime)
                    thisMessage.put()

                elif thisSMSAccount.strUsePortal == "Budget":
                    findRequest = SMSPortalBudget.query()
                    thisBudgetPortalList = findRequest.fetch()

                    if len(thisBudgetPortalList) > 0:
                        thisBudgetPortal = thisBudgetPortalList[0]
                    else:
                        thisBudgetPortal = SMSPortalBudget()

                    i = 0
                    self.response.write("""
                    <div class="box box-body with-border">


                        <div class="box box-header with-border">
                            <h3 class="box-title">Messages will be sent with Blue IT Marketing Budget Portal</h3>
                        </div>

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
                    while (thisSMSAccount.strTotalSMS > 0) and (i < len(thisSMSContactsList)):
                        thisContact = thisSMSContactsList[i]
                        thisDate = datetime.datetime.now()
                        thisDate = thisDate.date()
                        strThisDate = str(thisDate.day) + "/" + str(thisDate.month) + "/" + str(thisDate.year)
                        result = thisBudgetPortal.SendCronMessage(strMessage=thisMessage.strMessage,strCell=thisContact.strCellNumber)
                        if result == None:
                            isSent = False
                            self.response.write("""<tr> <td> """ + thisContact.strNames + """</td><td> """ + thisContact.strSurname + """</td><td>""" + thisContact.strCellNumber + """</td><td> <span class="label label-danger">Not Sent</span> </td></tr>""")

                        else:
                            isSent = True
                            logging.info("THIS IS THE RETURNED RESULT : " + str(result.content))
                            self.response.write("""<tr> <td> """ + thisContact.strNames + """</td><td> """ + thisContact.strSurname + """</td><td>""" + thisContact.strCellNumber + """</td><td> <span class="label label-success">Sent</span> </td></tr>""")

                        if isSent:
                            i = i + 1
                            thisBudgetPortal.strAvailableCredit = thisBudgetPortal.strAvailableCredit - 1
                            thisDeliveryReport = DeliveryReport()
                            thisDeliveryReport.writeGroupID(thisGroup.strGroupID)
                            thisDeliveryReport.writeCell(thisContact.strCellNumber)
                            thisDeliveryReport.writeDelivered(strinput=True)
                            thisDate = datetime.datetime.now()
                            strThisDate = thisDate.date()
                            strThisTime = thisDate.time()
                            strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,
                                                        second=strThisTime.second)
                            thisDeliveryReport.writeDate(strinput=strThisDate)
                            thisDeliveryReport.writeTime(strinput=strThisTime)
                            thisDeliveryReport.writeMessageID(strinput=thisMessage.strMessageID)
                            thisDeliveryReport.writeRef(result)
                            thisDeliveryReport.put()
                        else:
                            i = i + 1
                            #thisBudgetPortal.strAvailableCredit = thisBudgetPortal.strAvailableCredit - 1
                            thisDeliveryReport = DeliveryReport()
                            thisDeliveryReport.writeGroupID(thisGroup.strGroupID)
                            thisDeliveryReport.writeCell(thisContact.strCellNumber)
                            thisDeliveryReport.writeDelivered(strinput=False)
                            thisDate = datetime.datetime.now()
                            strThisDate = thisDate.date()
                            strThisTime = thisDate.time()
                            strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,
                                                        second=strThisTime.second)
                            thisDeliveryReport.writeDate(strinput=strThisDate)
                            thisDeliveryReport.writeTime(strinput=strThisTime)
                            thisDeliveryReport.writeMessageID(strinput=thisMessage.strMessageID)
                            thisDeliveryReport.put()


                    self.response.write("""</tbody><tfoot><tr>
                            <tr>
                                <td>Names</td>
                                <td>Surname</td>
                                <td>Cell</td>
                                <td>Status</td>
                            </tr>
                            </tfoot>
                            </table>
                          </div>
                    """)
                    thisBudgetPortal.put()
                    i = i + 1
                    thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - (i)
                    thisSMSAccount.put()
                    thisMessage.writeSubmitted(strinput=True)

                    thisDate = datetime.datetime.now()
                    strThisDate = thisDate.date()
                    strThisTime = thisDate.time()
                    strThisTime = datetime.time(hour=strThisTime.hour,minute=strThisTime.minute,second=strThisTime.second)
                    thisMessage.writeDateSubmitted(strinput=strThisDate)
                    thisMessage.writeTimeSubmitted(strinput=strThisTime)
                    thisMessage.put()


app = webapp2.WSGIApplication([
    ('/admin/mysms', mySMSHandler),
    ('/admin/sms/groups', SMSGroupHandler),
    ('/sms/groupman/.*', GroupManagerHandler),
    ('/sms/manage/.*', thisSMSManagerHandler)



], debug=True)
