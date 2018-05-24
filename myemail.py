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
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
def SendEmail(strFrom,strTo,strSubject,strBody,strTextType,strAttachFileContent=None,strAttachFileName=None):
    import sendgrid
    from sendgrid.helpers.mail import *
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    try:
        if not(strAttachFileName == None) and (strAttachFileContent == None):
            data = {
                "personalizations": [
                    {
                        "to": [
                            {
                                "email": strTo
                            }
                        ],
                        "subject": strSubject
                    }
                ],
                "from": {
                    "email": strFrom
                },
                "content": [
                    {
                        "type": strTextType,
                        "value": strBody
                    }
                ],
                "attachments": [
                    {
                        "content": strAttachFileContent,
                        "filename": strAttachFileName,
                    }
                ]
            }
        else:
            data = {
                "personalizations": [
                    {
                        "to": [
                            {
                                "email": strTo
                            }
                        ],
                        "subject": strSubject
                    }
                ],
                "from": {
                    "email": strFrom
                },
                "content": [
                    {
                        "type": strTextType,
                        "value": strBody
                    }
                ]
            }

        thisresponse = sg.client.mail.send.post(request_body=data)
        if (thisresponse.status_code >= 200) and (thisresponse.status_code <= 400):
            return True
        else:
            logging.info("Failure sending email")
            return False
    except:
        return False

class MyEmailSettings(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strEmailAddress = ndb.StringProperty()
    strName = ndb.StringProperty()
    strSignature = ndb.StringProperty()
    strDateCreated = ndb.DateProperty(auto_now_add=True)
    strTimeCreated = ndb.TimeProperty(auto_now_add=True)

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

    def writeName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strName = strinput
                return True
            else:
                return False

        except:
            return False

    def writeSignature(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSignature = strinput
                return True
            else:
                return False
        except:
            return False

class MyEmail(ndb.Expando):
    """
        Thread ID allows send response emails to be saved in a single thread
    """
    strMemberID = ndb.StringProperty()
    strThreadID = ndb.StringProperty()
    strEmailID = ndb.StringProperty() # Unique ID for every email
    strToAddress = ndb.StringProperty()
    strToName = ndb.StringProperty()
    strSubject = ndb.StringProperty()
    strBodyText = ndb.StringProperty()
    strBodyHTML = ndb.StringProperty()

    strYearSent = ndb.StringProperty()
    strMonthSent = ndb.StringProperty()
    strDaySent = ndb.StringProperty()
    strTimeSent = ndb.TimeProperty()

    strYearCreated = ndb.StringProperty()
    strMonthCreated = ndb.StringProperty()
    strDayCreated = ndb.StringProperty()
    strTimeCreated = ndb.TimeProperty()

    strStatus = ndb.StringProperty(default="Draft") # Sent,  Trash

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
    def writeThreadID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strThreadID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateEmailID(self):
        try:
            strTemp = "EMAIL"
            findRequest = MyEmail.query()
            thisMyEmailList = findRequest.fetch()
            strID = str(len(thisMyEmailList))
            strEmailID = strTemp + strID
            return strEmailID
        except:
            return None
    def writeEmailID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmailID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeToAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strToAddress = strinput
                return True
            else:
                return False
        except:
            return False
    def writeToName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strToName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSubject(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSubject = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBodyText(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBodyText = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBodyHTML(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBodyHTML = strinput
                return True
            else:
                return False
        except:
            return False
    def writeYearSent(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 2100) and (int(strinput) >= 2016):
                self.strYearSent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonthSent(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 12) and (int(strinput) >= 1):
                self.strMonthSent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDaySent(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 31) and (int(strinput) >= 1):
                self.strDaySent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeCreated(self,strinput):
        try:
            if strinput is not None:
                self.strTimeCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeSent(self,strinput):
        try:

            if strinput is not None:
                self.strTimeSent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonthCreated(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 12) and (int(strinput) >= 1):
                self.strMonthCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writeYearCreated(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 2100) and (int(strinput) >= 2016):
                self.strYearCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDayCreated(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 31):
                self.strDayCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def changeState(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ['Draft','Sent','Trash']:
                self.strStatus = strinput
                return True
            else:
                return False
        except:
            return False

class MyInbox(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strThreadID = ndb.StringProperty()
    strFromAddress = ndb.StringProperty()
    strFromName = ndb.StringProperty()
    strSubject = ndb.StringProperty()
    strBodyText = ndb.StringProperty()
    strBodyHTML = ndb.StringProperty()
    strIsText = ndb.StringProperty(default="No") # YES

    strYearReceived = ndb.StringProperty()
    strMonthReceived = ndb.StringProperty()
    strDayReceived = ndb.StringProperty()

    strTimeReceived = ndb.TimeProperty()

    strStatus = ndb.StringProperty(default="Inbox") # Trash, Junk

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
    def writeThreadID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strThreadID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFromAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFromAddress = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFromName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFromName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSubject(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSubject = strinput
                return True
            else:
                return False

        except:
            return False
    def writeBodyText(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBodyText = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBodyHTML(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBodyHTML = strinput
                return True
            else:
                return False
        except:
            return False
    def writeYearReceived(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 2100) and (int(strinput) >= 2016):
                self.strYearReceived = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonthReceived(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 12) and  (int(strinput) >= 1):
                self.strMonthReceived = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDayReceived(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 31):
                self.strDayReceived = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeReceived(self,strinput):
        try:
            if strinput is not None:
                self.strTimeReceived = strinput
                return True
            else:
                return False
        except:
            return False


    def changeState(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ['Inbox','Trash']:
                self.strStatus = strinput
                return True
            else:
                return False
        except:
            return False

class myEmailHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = MyEmailSettings.query(MyEmailSettings.strMemberID == Guser.user_id())
            thisEmailSettingsList = findRequest.fetch()
            if len(thisEmailSettingsList) > 0:
                thisEmailSettings = thisEmailSettingsList[0]
            else:
                thisEmailSettings = MyEmailSettings()


            templates = template_env.get_template("templates/myemail/myemail.html")
            context = {'thisEmailSettings':thisEmailSettings}
            self.response.write(templates.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrEmailAddress = self.request.get('vstrEmailAddress')
                vstrName = self.request.get('vstrName')
                vstrSignature = self.request.get('vstrSignature')

                findRequest = MyEmailSettings.query(MyEmailSettings.strMemberID == Guser.user_id())
                thisEmailSettingsList = findRequest.fetch()
                if len(thisEmailSettingsList) > 0:
                    thisEmailSetting = thisEmailSettingsList[0]
                else:
                    thisEmailSetting = MyEmailSettings()

                thisEmailSetting.writeMemberID(strinput=Guser.user_id())
                thisEmailSetting.writeEmailAddress(strinput=vstrEmailAddress)
                thisEmailSetting.writeName(strinput=vstrName)
                thisEmailSetting.writeSignature(strinput=vstrSignature)
                thisEmailSetting.put()
                self.response.write("Email Settings Successfully Saved")

            elif vstrChoice == "1":
                findRequest = MyInbox.query(MyInbox.strMemberID == Guser.user_id(),MyInbox.strStatus == "Inbox")
                thisInboxList = findRequest.fetch()

                template = template_env.get_template('templates/myemail/email/inbox.html')
                context = {'thisInboxList':thisInboxList}
                self.response.write(template.render(context))

            elif vstrChoice == "2":
                findRequest = MyEmail.query(MyEmail.strMemberID == Guser.user_id(),MyEmail.strStatus == "Sent")
                thisSentEmailsList = findRequest.fetch()

                template = template_env.get_template('templates/myemail/email/sent.html')
                context = {'thisSentEmailsList':thisSentEmailsList}
                self.response.write(template.render(context))

            elif vstrChoice == "3":
                findRequest = MyEmail.query(MyEmail.strMemberID == Guser.user_id(), MyEmail.strStatus == "Draft")
                thisEmailDraftsList = findRequest.fetch()

                template = template_env.get_template('templates/myemail/email/drafts.html')
                context = {'thisEmailDraftsList':thisEmailDraftsList}
                self.response.write(template.render(context))

            elif vstrChoice == "4":
                findRequest = MyEmailSettings.query(MyEmailSettings.strMemberID == Guser.user_id())
                thisEmailSettingsList = findRequest.fetch()

                if len(thisEmailSettingsList) > 0:
                    thisEmailSetting = thisEmailSettingsList[0]

                    template = template_env.get_template('templates/myemail/email/compose.html')
                    context = {'thisEmailSetting':thisEmailSetting}
                    self.response.write(template.render(context))
                else:
                    self.response.write("Please setup your email first")
            elif vstrChoice == "5":
                vstrToEmail = self.request.get('vstrToEmail')
                vstrSubject = self.request.get('vstrSubject')
                vstrEmailText = self.request.get('vstrEmailText')

                thisDraft = MyEmail()
                thisDraft.writeMemberID(strinput=Guser.user_id())
                thisDraft.writeSubject(strinput=vstrSubject)
                thisDraft.writeBodyHTML(strinput=vstrEmailText)
                thisDraft.writeToAddress(strinput=vstrToEmail)
                thisDate = datetime.datetime.now()
                thisDate = thisDate.date()
                thisYear = thisDate.year
                thisMonth = thisDate.month
                thisDay = thisDate.day
                thisDraft.writeYearCreated(strinput=str(thisYear))
                thisDraft.writeMonthCreated(strinput=str(thisMonth))
                thisDraft.writeDayCreated(strinput=str(thisDay))
                thisDraft.changeState(strinput="Draft")
                thisTime = datetime.datetime.now()
                thisTime = thisTime.time()

                thisTime = datetime.time(hour=thisTime.hour,minute=thisTime.minute,second=thisTime.second)
                thisDraft.writeTimeCreated(strinput=thisTime)
                thisDraft.put()

                self.response.write("Email Successfully saved as draft")

            elif vstrChoice == "6":
                vstrToEmail = self.request.get('vstrToEmail')
                vstrSubject = self.request.get('vstrSubject')
                vstrEmailText = self.request.get('vstrEmailText')

                thisSent = MyEmail()
                thisSent.writeMemberID(strinput=Guser.user_id())
                thisSent.writeSubject(strinput=vstrSubject)
                thisSent.writeBodyHTML(strinput=vstrEmailText)
                thisSent.writeToAddress(strinput=vstrToEmail)
                thisDate = datetime.datetime.now()
                thisDate = thisDate.date()
                thisYear = thisDate.year
                thisMonth = thisDate.month
                thisDay = thisDate.day
                thisSent.writeYearCreated(strinput=str(thisYear))
                thisSent.writeMonthCreated(strinput=str(thisMonth))
                thisSent.writeDayCreated(strinput=str(thisDay))
                thisSent.changeState(strinput="Sent")
                thisTime = datetime.datetime.now()
                thisTime = thisTime.time()

                thisTime = datetime.time(hour=thisTime.hour,minute=thisTime.minute,second=thisTime.second)
                thisSent.writeTimeCreated(strinput=thisTime)

                findRequest = MyEmailSettings.query(MyEmailSettings.strMemberID == Guser.user_id())
                thisEmailSettingsList = findRequest.fetch()

                if len(thisEmailSettingsList) > 0:
                    thisEmailSetting = thisEmailSettingsList[0]

                    thisEmailSetting.strEmailAddress = thisEmailSetting.strEmailAddress + "@church-admins.appspotmail.com"
                    try:
                        message = mail.EmailMessage()
                        message.sender = thisEmailSetting.strEmailAddress
                        message.to = thisSent.strToAddress
                        message.subject = thisSent.strSubject
                        message.body = thisSent.strBodyHTML
                        message.send()
                        Now = datetime.datetime.now()
                        thisYear  = Now.year
                        thisMonth = Now.month
                        thisDay = Now.day
                        thisTime = datetime.time(hour=Now.hour,minute=Now.minute,second=Now.second)

                        thisSent.writeYearSent(strinput=str(thisYear))
                        thisSent.writeMonthSent(strinput=str(thisMonth))
                        thisSent.writeDaySent(strinput=str(thisDay))
                        thisSent.writeTimeSent(strinput=thisTime)



                        thisSent.put()
                        self.response.write("Message Successfully sent")
                    except:
                        self.response.write("Error Sending Message")
                else:
                    self.response.write("Please setup your email address before sending email")


class  IncomingMailhandler(InboundMailHandler):
    def receive(self, mail_message):
        """
            find out how to detect the sending email address
        :param mail_message:
        :return:
        """
        try:
            thisIncoming = MyInbox()

            bodies_list = mail_message.bodies('text/plain')

            for content_type, body in bodies_list:
                decode_text = body.decode()

            thisIncoming.writeBodyHTML(strinput=decode_text)
            thisIncoming.writeSubject(strinput=mail_message.subject)
            thisIncoming.writeFromAddress(strinput=mail_message.sender)
            Now = datetime.datetime.now()
            thisYear = Now.year
            thisMonth = Now.month
            thisDay = Now.day

            thisTime = datetime.time(hour=Now.hour,minute=Now.minute,second=Now.second)

            thisIncoming.writeYearReceived(strinput=str(thisYear))
            thisIncoming.writeMonthReceived(strinput=str(thisMonth))
            thisIncoming.writeDayReceived(strinput=str(thisDay))
            thisIncoming.writeTimeReceived(strinput=thisTime)
            thisIncoming.changeState(strinput="Inbox")
            thisIncoming.put()


        except:
            pass



app = webapp2.WSGIApplication([
    ('/admin/myemail', myEmailHandler),
    ('/_ah/mail/.+', IncomingMailhandler)

], debug=True)
