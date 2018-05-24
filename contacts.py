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




class Notes(ndb.Expando):
    strContactID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()

    strSubject = ndb.StringProperty()
    strNotes = ndb.StringProperty()
    strDateTaken = ndb.DateProperty()
    strTimeTaken = ndb.TimeProperty()

    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strContactID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strChurchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSubject(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSubject = strinput
                return True
            else:
                return False

        except:
            return False
    def writeNotes(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strNotes = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateTaken(self,strinput):
        try:

            if isinstance(strinput,datetime.date):
                self.strDateTaken = strinput
                return True
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

class Contacts(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strContactID = ndb.StringProperty()

    strTitle = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strFax = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebsite = ndb.StringProperty()

    strDateCreated = ndb.DateProperty()


    def CreateContactID(self):
        import string,random
        try:
            strContactID = ""
            for i in range(13):
                strContactID +=  random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strContactID
        except:
            return None

    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strContactID = strinput
                return True
            else:
                return False
        except:
            return False


    def writeTitle(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strTitle = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMemberID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strMemberID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strChurchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchBranchID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strChurchBranchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNames(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strNames = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurname(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSurname = strinput
                return True
            else:
                return False

        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strTel = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFax(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strFax = strinput
                return True
            else:
                return False

        except:
            return False
    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False
    def writeWebsite(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strWebsite = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateCreated(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateCreated = strinput
                return True
            else:
                return False
        except:
            return False


    def sendEmailToContact(self,strMessage,strSubject):
        pass

    def sendSMSToContact(self,strMessage):
        pass

    def sendFax(self):
        pass

class PostalAddress(ndb.Expando):
    strContactID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strBox = ndb.StringProperty()
    strCityTown = ndb.StringProperty()
    strProvince = ndb.StringProperty()
    strCountry = ndb.StringProperty()
    strPostalCode = ndb.StringProperty()


    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)

            if not(strinput == None):
                self.strContactID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchID(self,strinput):
        try:

            strinput = str(strinput)
            if not(strinput == None):
                self.strChurchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBox(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strBox = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCityTown(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCityTown = strinput
                return True
            else:
                return False
        except:
            return False
    def writeProvince(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strProvince = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCountry(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCountry = strinput
                return True
            else:
                return False
        except:
            return False
    def writePostalCode(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strPostalCode = strinput
                return True
            else:
                return False
        except:
            return False

class PhysicalAddress(ndb.Expando):
    strContactID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()

    strStandNumber = ndb.StringProperty()
    strStreetName = ndb.StringProperty()
    strCityTown = ndb.StringProperty()
    strProvince = ndb.StringProperty()
    strCountry = ndb.StringProperty()
    strPostalCode = ndb.StringProperty()


    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strContactID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeChurchID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strChurchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStandNumber(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strStandNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStreetName(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strStreetName = strinput
                return True
            else:
                return False

        except:
            return False
    def writeCityTown(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCityTown = strinput
                return True
            else:
                return False
        except:
            return False
    def writeProvince(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strProvince =  strinput
                return True
            else:
                return False
        except:
            return False
    def writeCountry(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCountry = strinput
                return True
            else:
                return False
        except:
            return False
    def writePostalCode(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strPostalCode = strinput
                return True
            else:
                return False
        except:
            return False

class SMSOutBox(ndb.Expando):
    strContactID = ndb.StringProperty()
    strMessageID = ndb.StringProperty()
    strMessage = ndb.StringProperty()
    strIsSent = ndb.BooleanProperty(default=False)
    strDateSent = ndb.DateProperty()
    strTimeSent = ndb.TimeProperty()

    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strContactID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMessageID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strMessageID = strinput
                return True
            else:
                return False

        except:
            return False

    def writeMessage(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strMessage = strinput
                return True
            else:
                return False
        except:
            return False

    def writeIsSent(self,strinput):
        try:
            if strinput in [True,False]:
                self.strIsSent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateSent(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateSent = strinput
                return True
            else:
                return False

        except:
            return False

    def writeTimeSent(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeSent = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateMessageID(self,strinput):
        import random,string
        try:
            strMessageID = ""
            for i in range(13):
                strMessageID += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strMessageID
        except:
            return None

class SMSInBox(ndb.Expando):
    strContactID = ndb.StringProperty()
    strMessageID = ndb.StringProperty()
    strResponse = ndb.StringProperty()
    strDateReceived = ndb.DateProperty()
    strTimeReceived = ndb.TimeProperty()


    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strContactID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMessageID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strMessageID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeResponse(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strResponse = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateReceived(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateReceived = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeReceived(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeReceived = strinput
                return True
            else:
                return False

        except:
            return False

class EmailOutBox(ndb.Expando):
    strContactID = ndb.StringProperty()
    strSubject = ndb.StringProperty()
    strMessage = ndb.StringProperty()
    strIsSent = ndb.BooleanProperty(default=False)
    strDateSent = ndb.DateProperty()
    strTimeSent = ndb.TimeProperty()
    strMessageID = ndb.StringProperty()
    strFromEmail = ndb.StringProperty()

    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)

            if not(strinput == None):
                self.strContactID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSubject(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSubject = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMessage(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strMessage = strinput
                return True
            else:
                return False
        except:
            return False

    def writeIsSent(self,strinput):
        try:
            if isinstance(strinput,bool):
                self.strIsSent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateSent(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateSent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeSent(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeSent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMessageID(self,strinput):
        try:
            if isinstance(strinput,str):
                self.strMessageID = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateMessageID(self):
        import random,string
        try:
            strMessageID = ""
            for i in range(13):
                strMessageID += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strMessageID
        except:
            return None

    def sendEmail(self):
        try:
            findRequest = Contacts.query(Contacts.strContactID == self.strContactID)
            thisContactList = findRequest.fetch()

            if len(thisContactList) > 0:
                thisContact = thisContactList[0]
            else:
                thisContact = Contacts()
                return False


            self.strFromEmail =  str(self.strContactID) + "@church-admins.appspotmail.com"


            message = mail.EmailMessage()
            message.sender = self.strFromEmail
            message.to = thisContact.strEmail
            message.subject = self.strSubject
            message.body = self.strMessage
            message.send()

            return True
        except:
            return False



class EmailInBox(ndb.Expando):
    strContactID = ndb.StringProperty()
    strSubject = ndb.StringProperty()
    strResponse = ndb.StringProperty()
    strDateReceived = ndb.DateProperty()
    strTimeReceived = ndb.TimeProperty()
    strMessageID = ndb.StringProperty()


    def writeContactID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strContactID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSubject(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSubject = strinput
                return True
            else:
                return False
        except:
            return False


    def writeResponse(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strResponse = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateReceived(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateReceived = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeReceived(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeReceived = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMessageID(self,strinput):
        try:
            if isinstance(strinput,str):
                self.strMessageID = strinput
                return True
            else:
                return False
        except:
            return False



class ContactsHandler(webapp2.RequestHandler):


    def get(self):
        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        if Guser:

            findRequests = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequests.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()


            findRequests = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequests.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                findRequests = Contacts.query(Contacts.strChurchID == thisChurchMember.strChurchID)
                thisContactsList = findRequests.fetch()

                template = template_env.get_template("templates/contacts/contacts.html")
                context = {'thisContactsList':thisContactsList}
                self.response.write(template.render(context))

            else:
                template = template_env.get_template('templates/subRestricted.html')
                context = {'thisChurchMember':thisChurchMember}
                self.response.write(template.render(context))
    def post(self):
        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        if Guser:

            findRequests = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequests.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()


            findRequests = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequests.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                vstrChoice = self.request.get('vstrChoice')

                if vstrChoice == "0":
                    vstrNames = self.request.get('vstrNames')
                    vstrSurname = self.request.get('vstrSurname')
                    vstrCell = self.request.get('vstrCell')
                    vstrTel = self.request.get('vstrTel')
                    vstrFax = self.request.get('vstrFax')
                    vstrEmail = self.request.get('vstrEmail')
                    vstrWebsite = self.request.get('vstrWebsite')
                    vstrDateCreated = self.request.get('vstrDateCreated')
                    vstrTitle= self.request.get('vstrTitle')

                    findRequests = Contacts.query(Contacts.strCell == vstrCell,Contacts.strChurchID == thisChurchMember.strChurchID,Contacts.strChurchBranchID == thisChurchMember.strChurchBranchID)
                    thisContactList = findRequests.fetch()

                    if len(thisContactList) > 0:
                        thisContact = thisContactList[0]
                    else:
                        thisContact = Contacts()
                        thisContact.writeContactID(strinput=thisContact.CreateContactID())

                    thisContact.writeChurchID(strinput=thisChurchMember.strChurchID)
                    thisContact.writeChurchBranchID(strinput=thisChurchMember.strChurchBranchID)
                    thisContact.writeNames(strinput=vstrNames)
                    thisContact.writeSurname(strinput=vstrSurname)
                    thisContact.writeCell(strinput=vstrCell)
                    thisContact.writeTel(strinput=vstrTel)
                    thisContact.writeFax(strinput=vstrFax)
                    thisContact.writeEmail(strinput=vstrEmail)
                    thisContact.writeWebsite(strinput=vstrWebsite)
                    thisContact.writeDateCreated(strinput=vstrDateCreated)
                    thisContact.writeTitle(strinput=vstrTitle)
                    thisContact.put()
                    self.response.write("Contact successfully uploaded")

            else:
                template = template_env.get_template('templates/subRestricted.html')
                context = {'thisChurchMember':thisChurchMember}
                self.response.write(template.render(context))


class ThisContactHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        if Guser:

            findRequests = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequests.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()


            findRequests = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequests.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                URL = self.request.url
                URLlist = URL.split("/")
                vstrCell = URLlist[len(URLlist) - 1]

                findRequest = Contacts.query(Contacts.strCell == vstrCell,Contacts.strChurchID == thisChurchMember.strChurchID)
                thisContactList = findRequest.fetch()

                if len(thisContactList) > 0:
                    thisContact = thisContactList[0]
                else:
                    thisContact = Contacts()

                template   = template_env.get_template('templates/contacts/thisContact.html')
                context = {'thisContact':thisContact}
                self.response.write(template.render(context))

    def post(self):

        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        if Guser:

            findRequests = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequests.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()


            findRequests = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequests.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                vstrChoice  = self.request.get('vstrChoice')

                if vstrChoice == "0":
                    vstrCell = self.request.get('vstrCell')

                    findRequests = Contacts.query(Contacts.strCell == vstrCell,Contacts.strChurchID == thisChurchMember.strChurchID)
                    thisContactList = findRequests.fetch()

                    if len(thisContactList) > 0:
                        thisContact = thisContactList[0]
                    else:
                        thisContact = Contacts()


                    findRequests = Notes.query(Notes.strContactID == thisContact.strContactID)
                    thisNotesList = findRequests.fetch()

                    findRequests = PostalAddress.query(PostalAddress.strContactID == thisContact.strContactID)
                    thisPostalAddressList = findRequests.fetch()

                    if len(thisPostalAddressList) > 0:
                        thisPostalAddress = thisPostalAddressList[0]
                    else:
                        thisPostalAddress = PostalAddress()
                        thisPostalAddress.writeContactID(strinput=thisContact.strContactID)
                        thisPostalAddress.writeChurchID(strinput=thisContact.strChurchID)
                        thisPostalAddress.put()


                    findRequests = PhysicalAddress.query(PhysicalAddress.strContactID == thisContact.strContactID)
                    thisPhysicalAddressList = findRequests.fetch()

                    if len(thisPhysicalAddressList) > 0:
                        thisPhysicalAddress = thisPhysicalAddressList[0]
                    else:
                        thisPhysicalAddress = PhysicalAddress()
                        thisPhysicalAddress.writeContactID(strinput=thisContact.strContactID)
                        thisPhysicalAddress.writeChurchID(strinput=thisContact.strChurchID)
                        thisPhysicalAddress.put()

                    template = template_env.get_template('templates/contacts/sub/manage.html')
                    context = {'thisContact':thisContact,'thisNotesList':thisNotesList,'thisPostalAddress':thisPostalAddress,'thisPhysicalAddress':thisPhysicalAddress}
                    self.response.write(template.render(context))

                elif vstrChoice == "1":

                    vstrContactID = self.request.get('vstrContactID')
                    vstrPostalCode = self.request.get('vstrPostalCode')
                    vstrCountry = self.request.get('vstrCountry')
                    vstrProvince = self.request.get('vstrProvince')
                    vstrCityTown = self.request.get('vstrCityTown')
                    vstrBox = self.request.get('vstrBox')


                    findRequests = PostalAddress.query(PostalAddress.strContactID == vstrContactID)
                    thisPostalAddressList = findRequests.fetch()


                    if len(thisPostalAddressList) > 0:
                        thisPostalAddress = thisPostalAddressList[0]
                    else:
                        thisPostalAddress = PostalAddress()

                    thisPostalAddress.writeChurchID(strinput=thisChurchMember.strChurchID)
                    thisPostalAddress.writeContactID(strinput=vstrContactID)
                    thisPostalAddress.writeBox(strinput=vstrBox)
                    thisPostalAddress.writeCityTown(strinput=vstrCityTown)
                    thisPostalAddress.writeProvince(strinput=vstrProvince)
                    thisPostalAddress.writeCountry(strinput=vstrCountry)
                    thisPostalAddress.writePostalCode(strinput=vstrPostalCode)
                    thisPostalAddress.put()

                    self.response.write("Postal Address updated successfully")

                elif vstrChoice == "2":
                    vstrSubject = self.request.get('vstrSubject')
                    vstrNotes = self.request.get('vstrNotes')
                    vstrContactID = self.request.get('vstrContactID')

                    findRequests = Notes.query(Notes.strContactID == vstrContactID,Notes.strSubject == vstrSubject,Notes.strNotes == vstrNotes)
                    thisNotesList = findRequests.fetch()

                    if len(thisNotesList) > 0:
                        thisNote = thisNotesList[0]
                    else:
                        thisNote = Notes()

                    thisNote.writeContactID(strinput=vstrContactID)
                    thisNote.writeChurchID(strinput=thisChurchMember.strChurchID)
                    thisDate = datetime.datetime.now()
                    thisDate  = thisDate.date()
                    thisNote.writeDateTaken(strinput=thisDate)
                    thisTime = datetime.datetime.now()
                    thisTime  = thisTime.time()
                    thisTime = datetime.time(hour=thisTime.hour,minute=thisTime.minute,second=thisTime.second)
                    thisNote.writeTimeTaken(strinput=thisTime)
                    thisNote.writeSubject(strinput=vstrSubject)
                    thisNote.writeNotes(strinput=vstrNotes)
                    thisNote.put()

                    self.response.write("Note successfully uploaded")

                elif vstrChoice == "3":
                    vstrContactID = self.request.get('vstrContactID')
                    vstrStandNumber = self.request.get('vstrStandNumber')
                    vstrStreetName = self.request.get('vstrStreetName')
                    vstrPhyCityTown = self.request.get('vstrPhyCityTown')
                    vstrPhyProvince = self.request.get('vstrPhyProvince')
                    vstrPhyCountry = self.request.get('vstrPhyCountry')
                    vstrPhyPostalCode = self.request.get('vstrPhyPostalCode')

                    findRequests = PhysicalAddress.query(PhysicalAddress.strContactID == vstrContactID)
                    thisPhysicalAddressList = findRequests.fetch()

                    if len(thisPhysicalAddressList) > 0:
                        thisPhysicalAddress = thisPhysicalAddressList[0]
                    else:
                        thisPhysicalAddress = PhysicalAddress()

                    thisPhysicalAddress.writeContactID(strinput=vstrContactID)
                    thisPhysicalAddress.writeChurchID(strinput=thisChurchMember.strChurchID)
                    thisPhysicalAddress.writeStandNumber(strinput=vstrStandNumber)
                    thisPhysicalAddress.writeStreetName(strinput=vstrStreetName)
                    thisPhysicalAddress.writeCityTown(strinput=vstrPhyCityTown)
                    thisPhysicalAddress.writeProvince(strinput=vstrPhyProvince)
                    thisPhysicalAddress.writeCountry(strinput=vstrPhyCountry)
                    thisPhysicalAddress.writePostalCode(strinput=vstrPhyPostalCode)

                    thisPhysicalAddress.put()

                    self.response.write("Physical Address successfully updated")

                elif vstrChoice == "4":
                    vstrCell = self.request.get('vstrCell')

                    findRequests = Contacts.query(Contacts.strChurchID == thisChurchMember.strChurchID,Contacts.strCell == vstrCell)
                    thisContactList = findRequests.fetch()

                    if len(thisContactList) > 0:
                        thisContact = thisContactList[0]
                    else:
                        thisContact = Contacts()

                    findRequests = SMSInBox.query(SMSInBox.strContactID == thisContact.strContactID)
                    thisInBoxMessagesList = findRequests.fetch()

                    findRequests = SMSOutBox.query(SMSOutBox.strContactID == thisContact.strContactID)
                    thisSMSOutBoxList = findRequests.fetch()

                    template = template_env.get_template('templates/contacts/sub/sms.html')
                    context = {'thisInBoxMessagesList':thisInBoxMessagesList,'thisSMSOutBoxList':thisSMSOutBoxList,
                               'thisContact':thisContact}
                    self.response.write(template.render(context))

                elif vstrChoice == "5":
                    from mysms import SMSAccount,SMSPortalVodacom,SMSPortalBudget,DeliveryReport
                    vstrMessage = self.request.get('vstrMessage')
                    vstrContactID = self.request.get('vstrContactID')
                    vstrCell = self.request.get('vstrCell')

                    findRequest = SMSAccount.query(SMSAccount.strChurchID == thisChurchMember.strChurchID)
                    thisSMSAccountList = findRequest.fetch()
                    if len(thisSMSAccountList) > 0:
                        thisSMSAccount = thisSMSAccountList[0]
                    else:
                        thisSMSAccount = SMSAccount()


                    if thisSMSAccount.strUsePortal == "Vodacom":

                        findRequest = SMSPortalVodacom.query()
                        thisPortalList = findRequest.fetch()

                        if len(thisPortalList) > 0:
                            thisPortal = thisPortalList[0]
                        else:
                            thisPortal = SMSPortalVodacom()

                        i = 0

                        message = mail.EmailMessage()
                        message.sender = thisPortal.strSenderAddress
                        message.to = thisPortal.strEmailAddress
                        message.subject = vstrCell
                        message.body = vstrMessage
                        message.send()
                        thisPortal.strAvailableCredit = thisPortal.strAvailableCredit - 1

                        thisDeliveryReport = DeliveryReport()
                        thisDeliveryReport.writeGroupID(vstrContactID)
                        thisDeliveryReport.writeCell(vstrCell)
                        thisDeliveryReport.writeDelivered(strinput=True)
                        thisDate = datetime.datetime.now()
                        strThisDate = thisDate.date()
                        strThisTime = thisDate.time()
                        strThisTime = datetime.time(hour=strThisTime.hour, minute=strThisTime.minute,second=strThisTime.second)
                        thisDeliveryReport.writeDate(strinput=strThisDate)
                        thisDeliveryReport.writeTime(strinput=strThisTime)
                        thisDeliveryReport.writeMessageID(strinput=vstrMessage)
                        thisDeliveryReport.put()
                        thisPortal.put()

                        thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - 1
                        thisSMSAccount.put()


                        thisOutBox = SMSOutBox()
                        thisOutBox.writeMessage(strinput=vstrMessage)
                        thisOutBox.writeContactID(strinput=vstrContactID)
                        thisOutBox.writeMessageID(strinput=thisOutBox.CreateMessageID())
                        thisOutBox.writeDateSent(strinput=strThisDate)
                        thisOutBox.writeTimeSent(strinput=strThisTime)
                        thisOutBox.put()

                        self.response.write("SMS Successfully sent")

                elif vstrChoice == "6":
                    vstrCell = self.request.get('vstrCell')

                    findRequest = Contacts.query(Contacts.strCell == vstrCell)
                    thisContactList = findRequest.fetch()

                    if len(thisContactList) > 0:
                        thisContact = thisContactList[0]
                    else:
                        thisContact = Contacts()


                    findRequest = EmailInBox.query(EmailInBox.strContactID == thisContact.strContactID)
                    thisEmailInboxList = findRequest.fetch()

                    findRequest = EmailOutBox.query(EmailOutBox.strContactID == thisContact.strContactID)
                    thisEmailOutBoxList = findRequest.fetch()

                    template = template_env.get_template('templates/contacts/sub/email.html')
                    context = {'vstrCell':vstrCell,'thisEmailInboxList':thisEmailInboxList,'thisEmailOutBoxList':thisEmailOutBoxList}
                    self.response.write(template.render(context))

                elif vstrChoice == "7":

                    vstrCell = self.request.get('vstrCell')
                    vstrSubject = self.request.get('vstrSubject')
                    vstrMessage = self.request.get('vstrMessage')



                    findRequest = Contacts.query(Contacts.strCell == vstrCell)
                    thisContactList = findRequest.fetch()

                    if len(thisContactList) > 0:
                        thisContact = thisContactList[0]
                    else:
                        thisContact = Contacts()

                    findRequest = EmailOutBox.query(EmailOutBox.strSubject == vstrSubject,EmailOutBox.strMessage == vstrMessage)
                    thisEmailOutBoxList = findRequest.fetch()

                    if len(thisEmailOutBoxList) > 0:
                        thisEmailOutBox = thisEmailOutBoxList[0]
                    else:
                        thisEmailOutBox = EmailOutBox()

                    thisEmailOutBox.writeContactID(strinput=thisContact.strContactID)
                    thisEmailOutBox.writeMessageID(strinput=thisEmailOutBox.CreateMessageID())
                    thisEmailOutBox.writeMessage(strinput=vstrMessage)
                    thisDate = datetime.datetime.now()
                    thisDate = thisDate.date()
                    thisTime = datetime.datetime.now()
                    thisTime = datetime.time(hour=thisTime.hour,minute=thisTime.minute,second=thisTime.second)
                    if thisEmailOutBox.sendEmail():
                        thisEmailOutBox.writeIsSent(strinput=True)
                        thisEmailOutBox.writeTimeSent(strinput=thisTime)
                        thisEmailOutBox.writeDateSent(strinput=thisDate)

                        thisEmailOutBox.put()
                        self.response.write("Successfully sent an Email")
                    else:
                        self.response.write("Error Sending Email")








app = webapp2.WSGIApplication([
    ('/admin/contacts', ContactsHandler),
    ('/admin/contacts/.*', ThisContactHandler)
], debug=True)
