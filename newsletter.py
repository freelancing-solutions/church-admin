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


class ContactList(ndb.Expando):
    strListID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()

    def writeListID(self,strinput):
        try:
            if strinput != None:
                self.strListID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeChurchID(self,strinput):
        try:
            if strinput != None:
                self.strChurchID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeNames(self,strinput):
        try:
            if strinput != None:
                self.strNames = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSurname(self,strinput):
        try:
            if strinput != None:
                self.strSurname = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCell(self,strinput):
        try:
            if strinput != None:
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False

    def writeEmail(self,strinput):
        try:
            if strinput != None:
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False

class Letters(ndb.Expando):

    strMemberID = ndb.StringProperty()
    strPenName = ndb.StringProperty()

    strLetterIndex = ndb.IntegerProperty(default=0)
    strListID = ndb.StringProperty() #strNewsLetterID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strArticleID = ndb.StringProperty()

    strLetterHeading = ndb.StringProperty()
    strLetterBody = ndb.StringProperty()
    strHostedLink = ndb.StringProperty()
    strSent = ndb.BooleanProperty(default=False)
    strDateSent = ndb.DateProperty()

    strDateCreated = ndb.DateProperty()
    strTimeCreated = ndb.TimeProperty()

    strPublished = ndb.BooleanProperty(default=False)
    strDatePublished = ndb.DateProperty()
    strTimePublished = ndb.TimeProperty()


    def AdvanceIndex(self,strinput):
        from church import ChurchMember

        try:
            Guser = users.get_current_user()

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = Letters.query(Letters.strChurchID == thisChurchMember.strChurchID,Letters.strListID == strinput)
            thisLetterList = findRequest.fetch()

            return len(thisLetterList)
        except:
            return None

    def writeIndex(self,strinput):
        try:
            if strinput != None:
                self.strLetterIndex = strinput
                return True
            else:
                return False
        except:
            return False

    def writeListID(self,strinput):
        try:
            if strinput != None:
                self.strListID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeChurchID(self,strinput):
        try:
            if strinput != None:
                self.strChurchID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeLetterHeading(self,strinput):
        try:
            if strinput != None:
                self.strLetterHeading = strinput
                return True
            else:
                return False
        except:
            return False

    def writeLetterBody(self,strinput):
        try:
            if strinput != None:
                self.strLetterBody = strinput
                return True
            else:
                return False
        except:
            return False

    def writeHostedLink(self,strinput):
        try:
            if strinput != None:
                self.strHostedLink = strinput
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
    def writePenName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPenName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeArticlesID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strArticleID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateArticleID(self):
        import random,string
        try:
            strArticleID = ""
            for i in range(256):
                strArticleID +=  random.SystemRandom().choice(string.ascii_lowercase + string.digits)
            return strArticleID
        except:
            return None

    def CreateHostedLink(self):
        import random,string
        try:
            strHostedLink = ""
            for i in range(32):
                strHostedLink +=  random.SystemRandom().choice(string.ascii_lowercase + string.digits)
            return strHostedLink
        except:
            return None
    def writeDateCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeCreated = strinput
                return True
            else:
                return False
        except:
            return False
    def writePublished(self,strinput):
        try:
            if strinput in [True,False]:
                self.strPublished = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDatePublished(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDatePublished = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimePublished(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimePublished = strinput
                return True
            else:
                return False
        except:
            return False

class MailingList (ndb.Expando):
    strSenderAddress = ndb.StringProperty(default="newsletter@church-admins.appspotmail.com")

    strListID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()

    strListName = ndb.StringProperty()
    strListDescription = ndb.StringProperty()

    strStartSendingDate = ndb.DateProperty()
    strStartSendingTime = ndb.TimeProperty()



    def CreateListID(self):
        import string,random
        try:
            strListID = ""
            for i in range(128):
                strListID += random.SystemRandom().choice(string.ascii_lowercase + string.digits)
            return strListID
        except:
            return None
    def writeListID(self,strinput):
        try:

            if isinstance(strinput,str):
                self.strListID = strinput
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
    def writeListName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strListName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeListDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strListDescription = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStartSendingDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strStartSendingDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStartSendingTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strStartSendingTime = strinput
                return True
            else:
                return False
        except:
            return False




class NewslettersHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from church import ChurchMember
        if Guser:

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()


            findRequest = MailingList.query(MailingList.strChurchID == thisChurchMember.strChurchID)
            thisMailingList = findRequest.fetch()


            template = template_env.get_template('templates/newsletter/newsletter.html')
            context = {'thisMailingList':thisMailingList}
            self.response.write(template.render(context))



    def post(self):
        Guser = users.get_current_user()
        from church import ChurchMember
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrListName = self.request.get('vstrListName')
                vstrListDescription = self.request.get('vstrListDescription')
                vstrStartSendingDate = self.request.get('vstrStartSendingDate')
                DateList = vstrStartSendingDate.split("-")
                strYear = int(DateList[0])
                strMonth = int(DateList[1])
                strDay = int(DateList[2])

                vstrDate = datetime.date(year=strYear,month=strMonth,day=strDay)


                vstrStartSendingTime = self.request.get('vstrStartSendingTime')
                TimeList = vstrStartSendingTime.split(":")
                strHour = int(TimeList[0])
                strMinute = int(TimeList[1])
                vstrTime = datetime.time(hour=strHour,minute=strMinute,second=0)



                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                findRequest = MailingList.query(MailingList.strChurchID == thisChurchMember.strChurchID,MailingList.strListName == vstrListName,MailingList.strListDescription == vstrListDescription)
                thisMailingList = findRequest.fetch()

                if len(thisMailingList) > 0:
                    thisMailing = thisMailingList[0]
                else:
                    thisMailing = MailingList()
                    thisMailing.writeListID(strinput=thisMailing.CreateListID())

                thisMailing.writeChurchID(strinput=thisChurchMember.strChurchID)
                thisMailing.writeListName(strinput=vstrListName)
                thisMailing.writeListDescription(strinput=vstrListDescription)
                thisMailing.writeStartSendingDate(strinput=vstrDate)
                thisMailing.writeStartSendingTime(strinput=vstrTime)
                thisMailing.put()
                self.response.write("Mailing List successfully update")


class ThisNewsLetterHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        if Guser:
            URL = self.request.url

            vstrURLlist = URL.split("/")
            vstrListID = vstrURLlist[len(vstrURLlist) - 1]

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightList = findRequest.fetch()

            if len(thisUserRightList) > 0:
                thisUserRight = thisUserRightList[0]
            else:
                thisUserRight = UserRights()

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            if thisUserRight.strSuperUser or thisUserRight.strAdminUser:
                findRequest = MailingList.query(MailingList.strListID == vstrListID,MailingList.strChurchID == thisChurchMember.strChurchID)
                thisMailingList = findRequest.fetch()

                if len(thisMailingList) > 0:
                    thisNewsLetter = thisMailingList[0]
                else:
                    thisNewsLetter = MailingList()

                template = template_env.get_template('templates/newsletter/thisNewsletter.html')
                context = {'thisNewsLetter':thisNewsLetter}
                self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightList = findRequest.fetch()

            if len(thisUserRightList) > 0:
                thisUserRight = thisUserRightList[0]
            else:
                thisUserRight = UserRights()

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            vstrDateTime = datetime.datetime.now()
            strDate = vstrDateTime.date()
            strTime = datetime.time(hour=vstrDateTime.hour,minute=vstrDateTime.minute,second=vstrDateTime.second)

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                if vstrChoice == "0":
                    vstrListID = self.request.get('vstrListID')

                    findRequest = Letters.query(Letters.strListID == vstrListID)
                    thisLettersList = findRequest.fetch()

                    template = template_env.get_template('templates/newsletter/sub/letters.html')
                    context = {'thisLettersList':thisLettersList,'vstrListID':vstrListID}
                    self.response.write(template.render(context))

                elif vstrChoice == "1":
                    vstrLetterHeading = self.request.get('vstrLetterHeading')
                    vstrLetterBody = self.request.get('vstrLetterBody')
                    vstrListID = self.request.get('vstrListID')

                    findRequest = Letters.query(Letters.strLetterHeading == vstrLetterHeading)
                    thisLettersList = findRequest.fetch()

                    if len(thisLettersList) > 0:
                        thisLetter = thisLettersList[0]
                    else:
                        thisLetter = Letters()
                        thisLetter.writeArticlesID(strinput=thisLetter.CreateArticleID())
                        thisLetter.writeIndex(strinput=thisLetter.AdvanceIndex(strinput=vstrListID))
                        thisLetter.writeHostedLink(strinput=thisLetter.CreateHostedLink())
                        thisLetter.writeDateCreated(strinput=strDate)
                        thisLetter.writeTimeCreated(strinput=strTime)
                        thisLetter.writeMemberID(strinput=Guser.user_id())

                    thisLetter.writeChurchID(strinput=thisChurchMember.strChurchID)
                    thisLetter.writeLetterHeading(strinput=vstrLetterHeading)
                    thisLetter.writeLetterBody(strinput=vstrLetterBody)
                    thisLetter.writeListID(strinput=vstrListID)

                    thisLetter.put()

                    self.response.write("Article successfully updated")

                elif vstrChoice == "2":
                    vstrListID = self.request.get('vstrListID')

                    findRequest = ContactList.query(ContactList.strListID == vstrListID)
                    thisContactList = findRequest.fetch()

                    template = template_env.get_template('templates/newsletter/sub/contact.html')
                    context = {'thisContactList':thisContactList,'vstrListID':vstrListID}
                    self.response.write(template.render(context))

                elif vstrChoice == "3":
                    vstrListID = self.request.get('vstrListID')
                    vstrContacts = self.request.get('vstrContacts')

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisChurchMemberList = findRequest.fetch()

                    if len(thisChurchMemberList) > 0:
                        thisChurchMember = thisChurchMemberList[0]
                    else:
                        thisChurchMember = ChurchMember()

                    strContactList = vstrContacts.split("|")

                    for thisContact in strContactList:
                        thisContactList = thisContact.split(",")
                        if len(thisContactList) == 4:
                            findRequest = ContactList.query(ContactList.strListID == vstrListID,ContactList.strEmail == thisContactList[1])
                            strthisContactList = findRequest.fetch()

                            if len(strthisContactList) > 0:
                                strContact = strthisContactList[0]
                            else:
                                strContact = ContactList()

                            strContact.writeListID(strinput=vstrListID)
                            strContact.writeCell(strinput=thisContactList[0])
                            strContact.writeEmail(strinput=thisContactList[1])
                            strContact.writeNames(strinput=thisContactList[2])
                            strContact.writeSurname(strinput=thisContactList[3])
                            strContact.writeChurchID(strinput=thisChurchMember.strChurchID)
                            strContact.put()
                    self.response.write("Contact list updated successfully")

                elif vstrChoice == "4":
                    vstrListID = self.request.get('vstrListID')
                    vstrNames = self.request.get('vstrNames')
                    vstrSurname = self.request.get('vstrSurname')
                    vstrCellNumber = self.request.get('vstrCellNumber')
                    vstrEmail = self.request.get('vstrEmail')

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisChurchMemberList = findRequest.fetch()

                    if len(thisChurchMemberList) > 0:
                        thisChurchMember = thisChurchMemberList[0]
                    else:
                        thisChurchMember = ChurchMember()

                    findRequest = ContactList.query(ContactList.strListID == vstrListID,ContactList.strEmail == vstrEmail)
                    thisContactList = findRequest.fetch()

                    if len(thisContactList) > 0:
                        thisContact = thisContactList[0]
                    else:
                        thisContact = ContactList()

                    thisContact.writeChurchID(strinput=thisChurchMember.strChurchID)
                    thisContact.writeListID(strinput=vstrListID)
                    thisContact.writeNames(strinput=vstrNames)
                    thisContact.writeSurname(strinput=vstrSurname)
                    thisContact.writeCell(strinput=vstrCellNumber)
                    thisContact.writeEmail(strinput=vstrEmail)
                    thisContact.put()

                    self.response.write("Successfully uploaded contact")

                elif vstrChoice == "5":
                    vstrListID = self.request.get('vstrListID')
                    vstrListID = vstrListID.strip()
                    vstrRemoveEmail = self.request.get('vstrRemoveEmail')
                    vstrRemoveEmail = vstrRemoveEmail.strip()

                    findRequest = ContactList.query(ContactList.strEmail == vstrRemoveEmail,ContactList.strListID == vstrListID)
                    thisContactList = findRequest.fetch()

                    contactRemoved = False
                    for thisContact in thisContactList:
                        thisContact.key.delete()
                        contactRemoved = True


                    if contactRemoved:
                        self.response.write("Successfully removed email")
                    else:
                        self.response.write("Contact not removed  :  " + vstrRemoveEmail)

                elif vstrChoice == "6":
                    vstrListID = self.request.get('vstrListID')
                    vstrListID = vstrListID.strip()

                    findRequest = MailingList.query(MailingList.strListID == vstrListID)
                    thisMailingList = findRequest.fetch()

                    template = template_env.get_template('templates/newsletter/sub/schedule.html')
                    context = {'thisMailingList':thisMailingList,'vstrListID':vstrListID}
                    self.response.write(template.render(context))

                elif vstrChoice == "7":
                    vstrListID = self.request.get('vstrListID')
                    vstrDate = self.request.get('vstrDate')
                    strDateList = vstrDate.split("/")
                    strMonth = strDateList[0]
                    strDay = strDateList[1]
                    strYear = strDateList[2]
                    vstrTime = self.request.get('vstrTime')
                    if "AM" in vstrTime:
                        vstrTime = vstrTime.replace("AM","")
                        vstrTime = vstrTime.strip()
                        strTimeList = vstrTime.split(":")
                        strHour = strTimeList[0]
                        strMinute = strTimeList[1]
                    elif "PM" in vstrTime:
                        vstrTime = vstrTime.replace("PM","")
                        vstrTime = vstrTime.strip()
                        strTimeList = vstrTime.split(":")
                        strHour = strTimeList[0]
                        strHour = int(strHour)
                        strHour += 12
                        strMinute = strTimeList[1]
                    else:
                        vstrTime = vstrTime.strip()
                        strTimeList = vstrTime.split(":")
                        strHour = strTimeList[0]
                        strMinute = strTimeList[1]

                    vstrThisDate = datetime.date(year=int(strYear),month=int(strMonth),day=int(strDay))
                    vstrTime = datetime.time(hour=int(strHour),minute=int(strMinute))

                    findRequest = MailingList.query(MailingList.strListID == vstrListID)
                    thisMailingList = findRequest.fetch()

                    if len(thisMailingList) > 0:
                        thisMailing = thisMailingList[0]
                        thisMailing.writeStartSendingDate(strinput=vstrThisDate)
                        thisMailing.writeStartSendingTime(strinput=vstrTime)
                        thisMailing.put()
                        self.response.write("Successfully updated Scheduled date and time")
                    else:
                        self.response.write("Error updating scheduled date and time")

class ThisHostedHandler(webapp2.RequestHandler):
    def get(self):
        URL = self.request.url
        URLlist = URL.split("/")
        strHostedURL = URLlist[len(URLlist) - 1]

        findRequest = Letters.query(Letters.strHostedLink == strHostedURL)
        thisLetterList = findRequest.fetch()


        if len(thisLetterList) > 0:
            thisArticle = thisLetterList[0]
        else:
            thisArticle = Letters()

        findRequest = Letters.query(Letters.strLetterHeading != None)
        thisLettersList = findRequest.fetch(limit=35)


        template = template_env.get_template('templates/newsletter/hosted/newsletter.html')
        context = {'thisArticle':thisArticle,'thisLettersList':thisLettersList}
        self.response.write(template.render(context))

class ThisArticleEditorHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = self.request.url
            strURLList = URL.split("/")
            strArticleID = strURLList[len(strURLList) - 1]


            findRequest = Letters.query(Letters.strArticleID == strArticleID)
            thisArticlesList = findRequest.fetch()

            if len(thisArticlesList) > 0:
                thisArticle = thisArticlesList[0]
            else:
                thisArticle = Letters()


            template = template_env.get_template('templates/newsletter/editor/edit.html')
            context = {'thisArticle':thisArticle}
            self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrListID = self.request.get('vstrListID')

                findRequest = Letters.query(Letters.strListID == vstrListID)
                thisArticlesList = findRequest.fetch()

                template = template_env.get_template('templates/newsletter/editor/articlelist.html')
                context = {'thisArticlesList':thisArticlesList}
                self.response.write(template.render(context))

            elif vstrChoice == "1":
                vstrArticleHeading = self.request.get('vstrArticleHeading')
                vstrURL = self.request.get('vstrURL')
                vstrArticleEditor = self.request.get('vstrArticleEditor')
                vstrListID = self.request.get('vstrListID')
                vstrArticleID = self.request.get('vstrArticleID')

                findRequest = Letters.query(Letters.strArticleID == vstrArticleID)
                thisLettersList = findRequest.fetch()

                if len(thisLettersList) > 0:
                    thisArticle = thisLettersList[0]

                    thisArticle.writeArticlesID(strinput=vstrArticleID)
                    thisArticle.writeLetterBody(strinput=vstrArticleEditor)
                    #TODO- check to see if URL is not already taken if yes then try and differentiate
                    thisArticle.writeHostedLink(strinput=vstrURL)

                    thisArticle.writeLetterHeading(strinput=vstrArticleHeading)
                    thisArticle.put()
                    self.response.write("Succesfully updated your article")
                else:
                    self.response.write("Error saving article")

            elif vstrChoice == "2":
                vstrArticleID = self.request.get('vstrArticleID')

                findRequest = Letters.query(Letters.strArticleID == vstrArticleID)
                thisArticleList = findRequest.fetch()
                isDel = False
                for thisArticle in thisArticleList:
                    thisArticle.key.delete()
                    isDel = True

                if isDel:
                    self.response.write("Successfully deleted Article")
                else:
                    self.response.write("Article Already deleted")


            elif vstrChoice == "3":
                vstrArticleHeading = self.request.get('vstrArticleHeading')
                vstrURL = self.request.get('vstrURL')
                vstrArticleEditor = self.request.get('vstrArticleEditor')
                vstrListID = self.request.get('vstrListID')
                vstrArticleID = self.request.get('vstrArticleID')

                findRequest = Letters.query(Letters.strArticleID == vstrArticleID)
                thisLettersList = findRequest.fetch()

                if len(thisLettersList) > 0:
                    thisArticle = thisLettersList[0]
                else:
                    thisArticle = Letters()

                vstrThisDate = datetime.datetime.now()
                strThisDate = datetime.date(year=vstrThisDate.year,month=vstrThisDate.month,day=vstrThisDate.day)
                strThisTime = datetime.time(hour=vstrThisDate.hour,minute=vstrThisDate.minute,second=vstrThisDate.second)




                thisArticle.writeLetterBody(strinput=vstrArticleEditor)
                thisArticle.writeLetterHeading(strinput=vstrArticleHeading)
                thisArticle.writeHostedLink(strinput=vstrURL)
                if thisArticle.writePublished(strinput=True):
                    thisArticle.writeDatePublished(strinput=strThisDate)
                    thisArticle.writeTimePublished(strinput=strThisTime)
                    thisArticle.put()
                    self.response.write("Article Published Successfully")
                else:
                    self.response.write("Error Publishing Article")







class ThisHostedArticlesHandler(webapp2.RequestHandler):
    def get(self):
        """
            a list of all open newsletters hosted in church admin
        :return:
        """
        pass














app = webapp2.WSGIApplication([
    ('/admin/newsletters', NewslettersHandler),
    ('/admin/newsletters/.*', ThisNewsLetterHandler),
    ('/newsletters/hosted', ThisHostedArticlesHandler),
    ('/newsletters/hosted/.*', ThisHostedHandler),
    ('/newsletters/editor/.*', ThisArticleEditorHandler)

], debug=True)
