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
from google.appengine.ext import ndb
from google.appengine.api import users
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
from church import ChurchMember, Churches
from userRights import UserRights
from contact import ContactMessages
from accounts import Accounts

class BlueITMarketingAdminStaff(ndb.Expando):
    strStaffID = ndb.StringProperty(default="111111111111111111111110000222232")
    strReference = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strPosition = ndb.StringProperty(default="Admin") # Technical, Marketing, Consultant
    strSendNotices = ndb.BooleanProperty(default=True)



class AppRequests(ndb.Expando):
    strReference = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strIDNumber = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strRequestAccepted = ndb.BooleanProperty(default=False)
    strPaymentReceived = ndb.BooleanProperty(default=False)
    strDateRequestSent = ndb.DateProperty(auto_now_add=True)
    strProduct = ndb.StringProperty(default="BasicAdminApp") # AdminPlusSMS , AdminPlusSMSEmail

    strNotificationSent = ndb.BooleanProperty(default=False)

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False
    def writeRequestAccepted(self,strinput):
        try:
            if strinput in [True,False]:
                self.strRequestAccepted  = strinput
                return True
            else:
                return False
        except:
            return False
    def writePaymentReceived(self,strinput):
        try:
            if strinput in [True,False]:
                self.strPaymentReceived = strinput
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
    def writeIDNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strIDNumber = strinput
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
    def writeProduct(self,strinput):
        try:
            strinput = str(strinput)

            if strinput == "BasicAdminApp":
                self.strProduct = strinput
                return True
            elif strinput == "AdminPlusSMS":
                self.strProduct = strinput
                return True
            elif strinput == "AdminPlusSMSEmail":
                self.strProduct = strinput
                return True
            else:
                return False
        except:
            return False

class Administrators(ndb.Expando):


    strAdminID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strDateAssigned = ndb.DateProperty(auto_now_add=True)
    strActive = ndb.BooleanProperty(default=False)

    def writeAdminID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAdminID = strinput
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
    def setActive(self,strinput):
        try:
            if strinput in [True,False]:
                self.strActive = strinput
                return True
            else:
                return False
        except:
            return False

class Dashboardhandler(webapp2.RequestHandler):
    def get(self):

        Guser = users.get_current_user()
        from accounts import Products
        if Guser:
            if users.is_current_user_admin():
                findRequest = AppRequests.query(AppRequests.strRequestAccepted == True)
                thisAppRequestList = findRequest.fetch()

                findRequest = ContactMessages.query(ContactMessages.strResponseSent == False)
                thisContactMessagesList = findRequest.fetch()

                findRequest = Administrators.query()
                thisAdminList = findRequest.fetch()

                findRequest = Products.query()
                thisProductsList = findRequest.fetch()

                template = template_env.get_template('templates/dashboard/dashboard.html')
                context = {'thisAdminList':thisAdminList,'thisAppRequestList':thisAppRequestList,
                           'thisContactMessagesList':thisContactMessagesList,'thisProductsList':thisProductsList}
                self.response.write(template.render(context))
            else:
                findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisUserRights = thisUserRightsList[0]
                else:
                    thisUserRights = UserRights()

                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                if thisUserRights.strAdminUser:
                    findRequest = Administrators.query(Administrators.strAdminID == Guser.user_id())
                    thisAdminList = findRequest.fetch()
                    if len(thisAdminList) > 0:
                        thisAdmin = thisAdminList[0]

                    else:
                        thisAdmin = Administrators()

                    template = template_env.get_template('templates/dashboard/adminUsers.html')
                    context = {'thisAdmin':thisAdmin,'thisChurchMember':thisChurchMember}
                    self.response.write(template.render(context))
                elif thisUserRights.strSuperUser:
                    template = template_env.get_template('templates/dashboard/superUsers.html')
                    context = {'thisChurchMember':thisChurchMember}
                    self.response.write(template.render(context))

                elif thisUserRights.strChurchMember:
                    template = template_env.get_template('templates/dashboard/churchMemberUser.html')
                    context = {'thisChurchMember':thisChurchMember}
                    self.response.write(template.render(context))
                else:
                    template = template_env.get_template('templates/dashboard/Visitor.html')
                    context = {'thisChurchMember':thisChurchMember}
                    self.response.write(template.render(context))

class AdminRequestsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = AppRequests.query(AppRequests.strRequestAccepted == False)
            thisAppRequestsList = findRequest.fetch()

            template = template_env.get_template('templates/dashboard/dashfiles/adminRequests.html')
            context = {'thisAppRequestsList': thisAppRequestsList}
            self.response.write(template.render(context))

class AdminsListHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Administrators.query()
            thisAdminsList = findRequest.fetch()

            template = template_env.get_template('templates/dashboard/dashfiles/admins.html')
            context = {'thisAdminsList':thisAdminsList}
            self.response.write(template.render(context))

class PaymentsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Accounts.query()
            thisAccountsList = findRequest.fetch()

            template = template_env.get_template('templates/dashboard/dashfiles/payments.html')
            context = {'thisAccountsList':thisAccountsList}
            self.response.write(template.render(context))

class ContactsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = ContactMessages.query(ContactMessages.strResponseSent == False)
            thisContactMessageList = findRequest.fetch()

            template = template_env.get_template('templates/dashboard/dashfiles/contact.html')
            context = {'thisContactMessageList':thisContactMessageList}
            self.response.write(template.render(context))

class ThisAdminHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = self.request.url
            URLlist = URL.split("/")
            vstrAdminReference = URLlist[len(URLlist) - 1]

            findRequest = Administrators.query(Administrators.strAdminID == vstrAdminReference)
            thisAdminList = findRequest.fetch()

            if len(thisAdminList) > 0:
                thisAdmin = thisAdminList[0]
            else:
                thisAdmin = Administrators()

            findRequest = ChurchMember.query(ChurchMember.strMemberID == vstrAdminReference)
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = Churches.query(Churches.strChurchID == thisChurchMember.strChurchID)
            thisChurchesList = findRequest.fetch()

            if len(thisChurchesList) > 0:
                thisChurch = thisChurchesList[0]
            else:
                thisChurch = Churches()


            template = template_env.get_template('templates/dashboard/dashfiles/thisAdmin.html')
            context = {'thisAdmin':thisAdmin,'thisChurchMember':thisChurchMember,'thisChurch':thisChurch}
            self.response.write(template.render(context))

class BulkSMSHandler(webapp2.RequestHandler):

    def get(self):
        from mysms import SMSPortalVodacom, SMSPortalBudget,SMSAccount
        Guser = users.get_current_user
        if users.is_current_user_admin:

            findRequests = SMSPortalVodacom.query()
            thisSMSPortalVodacomList = findRequests.fetch()

            if len(thisSMSPortalVodacomList) > 0:
                thisVodacomPortal = thisSMSPortalVodacomList[0]
            else:
                thisVodacomPortal = SMSPortalVodacom()

            findRequests = SMSPortalBudget.query()
            thisBudgetPortalList = findRequests.fetch()

            if len(thisBudgetPortalList) > 0:
                thisBudgetPortal = thisBudgetPortalList[0]
            else:
                thisBudgetPortal = SMSPortalBudget()

            findRequests = SMSAccount.query()
            thisSMSAccountList = findRequests.fetch()

            template = template_env.get_template('templates/dashboard/dashfiles/BulkSMS.html')
            context = {'thisBudgetPortal':thisBudgetPortal,'thisVodacomPortal':thisVodacomPortal,'thisSMSAccountList':thisSMSAccountList}
            self.response.write(template.render(context))


    def post(self):
        from mysms import SMSPortalVodacom, SMSPortalBudget,SMSAccount
        Guser = users.get_current_user
        if users.is_current_user_admin:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrSenderAddress = self.request.get('vstrSenderAddress')
                vstrEmailAddress = self.request.get('vstrEmailAddress')
                vstrCSVEmail = self.request.get('vstrCSVEmail')
                vstrSMSSizeLimit = self.request.get('vstrSMSSizeLimit')
                vstrBuyRate = self.request.get('vstrBuyRate')
                vstrSellRate = self.request.get('vstrSellRate')
                vstrAvailableCredit = self.request.get('vstrAvailableCredit')
                vstrPortalLogin = self.request.get('vstrPortalLogin')
                vstrPortalPassword = self.request.get('vstrPortalPassword')
                vstrPortalAddress = self.request.get('vstrPortalAddress')
                vstrSystemCredit = self.request.get('vstrSystemCredit')

                findRequest = SMSPortalVodacom.query()
                thisVodacomPortalList = findRequest.fetch()
                if len(thisVodacomPortalList) > 0:
                    thisVodacomPortal = thisVodacomPortalList[0]
                else:
                    thisVodacomPortal = SMSPortalVodacom()

                thisVodacomPortal.writeSystemCredit(strinput=vstrSystemCredit)
                thisVodacomPortal.writeCSVEmail(strinput=vstrCSVEmail)
                thisVodacomPortal.writeEmailAddress(strinput=vstrEmailAddress)
                thisVodacomPortal.writeSMSSixeLimit(strinput=vstrSMSSizeLimit)
                thisVodacomPortal.writeAvailableCredit(strinput=vstrAvailableCredit)
                thisVodacomPortal.writeSellRate(strinput=vstrSellRate)
                thisVodacomPortal.writePortalAddress(strinput=vstrPortalAddress)
                thisVodacomPortal.writeSenderAddress(strinput=vstrSenderAddress)
                thisVodacomPortal.writeBuyRate(strinput=vstrBuyRate)
                thisVodacomPortal.writePortaLogin(strinput=vstrPortalLogin)
                thisVodacomPortal.writePassword(strinput=vstrPortalPassword)

                thisVodacomPortal.put()

                self.response.write("Successfully updated vodacom SMS portal settings")
            elif vstrChoice == "1":
                vstrChurchID = self.request.get('vstrChurchID')
                vstrAdditionalCredit = self.request.get('vstrAdditionalCredit')

                findRequest = SMSAccount.query(SMSAccount.strChurchID == vstrChurchID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0 and (int(vstrAdditionalCredit) > 0):
                    thisSMSAccount = thisSMSAccountList[0]

                    thisSMSAccount.writeChurchID(strinput=vstrChurchID)
                    thisSMSAccount.AddTotalSMS(strinput=vstrAdditionalCredit)
                    thisSMSAccount.put()
                    self.response.write("Successfully added new credit amount please refresh your browser to see new values")
                else:
                    self.response.write("Error Crediting Account")



app = webapp2.WSGIApplication([
    ('/dashboard', Dashboardhandler),
    ('/dashboard/adminrequests', AdminRequestsHandler),
    ('/dashboard/adminslist', AdminsListHandler),
    ('/dashboard/payments', PaymentsHandler),
    ('/dashboard/contacts', ContactsHandler),
    ('/dashboard/thisadmins/.*', ThisAdminHandler),
    ('/dashboard/bulksms', BulkSMSHandler)

], debug=True)
