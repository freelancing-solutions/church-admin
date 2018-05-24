import os

import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


from church import ChurchMember, Churches
from userRights import UserRights

class Products(ndb.Expando):
    strProductName = ndb.StringProperty(default="Basic Admin")
    strProductTag = ndb.StringProperty(default="BasicAdminApp")
    strProductDescription = ndb.StringProperty(default="Basic Administration App, users can perform all common administrative tasks of a church")
    strProductCost = ndb.IntegerProperty(default=6000)

    def setAdminPlusSMS(self):
        try:
            self.strProductName = "Basic Admin plus SMS Notifications App"
            self.strProductTag = "AdminPlusSMS"
            self.strProductDescription = "Basic Admin plus SMS Notifications App, Allowing users to perform all common administrative tasks of a church plus an SMS Enabled Notification Module allowing for timely notifications of all church events plus meetings"
            self.strProductCost = 8000
            return True
        except:
            return False

    def setAdminSMSEmail(self):
        try:
            self.strProductName = "Basic Admin plus SMS and Email Notifications App"
            self.strProductTag = "AdminPlusSMSEmail"
            self.strProductDescription = "Basic Admin plus SMS and Email Notifications App, Allowing users to perform all common administrative tasks of a church plus an SMS and Email Enabled Notification Module allowing for timely notifications of all church events plus meetings"
            self.strProductCost = 9500
            return True
        except:
            return False


    def GenerateProductDataStore(self):
        try:

            findRequest = Products.query(Products.strProductTag == "BasicAdminApp")
            lenThisProductsList = findRequest.fetch()

            if len(lenThisProductsList) > 0:
                pass
            else:
                thisProducts = Products()
                thisProducts.put()

            findRequest = Products.query(Products.strProductTag == "AdminPlusSMS")
            listThisProductsList = findRequest.fetch()
            if len(listThisProductsList) > 0:
                pass
            else:
                thisProducts = Products()
                thisProducts.setAdminPlusSMS()
                thisProducts.put()

            findRequest = Products.query(Products.strProductTag == "AdminPlusSMSEmail")
            listThisProductsList = findRequest.fetch()

            if len(listThisProductsList) > 0:
                pass
            else:
                thisProducts = Products()
                thisProducts.setAdminSMSEmail()
                thisProducts.put()

            return True
        except:
            return False


class Accounts(ndb.Expando):
    strReference = ndb.StringProperty()
    strProductName = ndb.StringProperty()
    strProductTag = ndb.StringProperty()
    strProductDescription = ndb.StringProperty()
    strFixedProductCost = ndb.IntegerProperty(default=6000)
    strFixedPaymentReceived = ndb.IntegerProperty(default=0)
    strFixedBalance = ndb.IntegerProperty(default=6000)



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

    def setProductCost(self,strinput):
        try:
            strinput = str(strinput)

            if strinput.isdigit():
                self.strFixedProductCost = strinput
                return True
            else:
                return False
        except:
            return False

    def setPaymentReceived(self,strinput):
        try:
            strinput = str(strinput)

            if strinput.isdigit():
                self.strFixedPaymentReceived = self.strFixedPaymentReceived + int(strinput)
                self.strFixedBalance = self.strFixedProductCost - self.strFixedPaymentReceived
                return True
            else:
                return False
        except:
            return False

    def writeProductName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProductName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeProductTag(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProductTag = strinput
                return True
            else:
                return False
        except:
            return False


    def writeProductDescription(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.strProductDescription = strinput
                return True
            else:
                return False
        except:
            return False

class AccountsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from dashboard import AppRequests
        if Guser:
            findRequest = AppRequests.query(AppRequests.strReference == Guser.user_id())
            thisAppRequestsList = findRequest.fetch()

            if len(thisAppRequestsList) > 0:
                thisAppRequest = thisAppRequestsList[0]
            else:
                thisAppRequest = AppRequests()

            findRequest = Accounts.query(Accounts.strReference == Guser.user_id())
            thisAccountsList = findRequest.fetch()

            if len(thisAccountsList) > 0:
                thisAccount = thisAccountsList[0]
            else:
                thisAccount = Accounts()

            template = template_env.get_template('templates/account/account.html')
            context = {'thisAppRequest':thisAppRequest,'thisAccount':thisAccount}
            self.response.write(template.render(context))
        else:
            pass

    def post(self):
        Guser = users.get_current_user()
        from dashboard import AppRequests
        if Guser:
            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrIDNumber = self.request.get('vstrIDNumber')
            vstrCell = self.request.get('vstrCell')
            vstrEmail = self.request.get('vstrEmail')
            vstrSelectProduct = self.request.get('vstrSelectProduct')

            findRequest = AppRequests.query(AppRequests.strReference == Guser.user_id())
            thisAppRequestsList = findRequest.fetch()

            if len(thisAppRequestsList) > 0:
                thisAppRequest = thisAppRequestsList[0]
            else:
                thisAppRequest = AppRequests()

            thisAppRequest.writeReference(strinput=Guser.user_id())
            thisAppRequest.writeNames(strinput=vstrNames)
            thisAppRequest.writeSurname(strinput=vstrSurname)
            thisAppRequest.writeIDNumber(strinput=vstrIDNumber)
            thisAppRequest.writeCell(strinput=vstrCell)
            thisAppRequest.writeEmail(strinput=vstrEmail)
            thisAppRequest.writeProduct(strinput=vstrSelectProduct)
            thisAppRequest.writePaymentReceived(strinput=False)
            thisAppRequest.writeRequestAccepted(strinput=False)
            thisAppRequest.put()


            if vstrSelectProduct == "BasicAdminApp":

                findRequest = Products.query(Products.strProductTag == "BasicAdminApp")
                thisProductsList = findRequest.fetch()

                if len(thisProductsList) > 0:
                    thisProduct = thisProductsList[0]
                else:
                    thisProduct = Products()
                    thisProduct.put()


                thisAccount = Accounts()
                thisAccount.writeReference(strinput=Guser.user_id())
                thisAccount.writeProductName(strinput=thisProduct.strProductName)
                thisAccount.writeProductDescription(strinput=thisProduct.strProductDescription)
                thisAccount.setProductCost(strinput=str(thisProduct.strProductCost))
                thisAccount.setPaymentReceived(strinput=str(0))

                thisAccount.put()

            elif vstrSelectProduct == "AdminPlusSMS":

                findRequest = Products.query(Products.strProductTag == "AdminPlusSMS")
                thisProductsList = findRequest.fetch()

                if len(thisProductsList) > 0:
                    thisProduct = thisProductsList[0]
                else:
                    thisProduct = Products()
                    thisProduct.setAdminPlusSMS()
                    thisProduct.put()

                thisAccount = Accounts()
                thisAccount.writeReference(strinput=Guser.user_id())
                thisAccount.writeProductName(strinput=thisProduct.strProductName)
                thisAccount.writeProductDescription(strinput=thisProduct.strProductDescription)
                thisAccount.setProductCost(strinput=str(thisProduct.strProductCost))
                thisAccount.setPaymentReceived(strinput=str(0))

                thisAccount.put()

            elif vstrSelectProduct == "AdminPlusSMSEmail":

                findRequest = Products.query(Products.strProductTag == "AdminPlusSMSEmail")
                thisProductsList = findRequest.fetch()

                if len(thisProductsList) > 0:
                    thisProduct = thisProductsList[0]
                else:
                    thisProduct = Products()
                    thisProduct.setAdminSMSEmail()
                    thisProduct.put()

                thisAccount = Accounts()
                thisAccount.writeReference(strinput=Guser.user_id())
                thisAccount.writeProductName(strinput=thisProduct.strProductName)
                thisAccount.writeProductDescription(strinput=thisProduct.strProductDescription)
                thisAccount.setProductCost(strinput=str(thisProduct.strProductCost))
                thisAccount.setPaymentReceived(strinput=str(0))

                thisAccount.put()


            self.response.write("Church Account Created")

class UpdateAccountHandler(webapp2.RequestHandler):
    def post(self):
        Guser = users.get_current_user()
        from dashboard import AppRequests
        if Guser:
            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrIDNumber = self.request.get('vstrIDNumber')
            vstrCell = self.request.get('vstrCell')
            vstrEmail = self.request.get('vstrEmail')
            vstrSelectProduct = self.request.get('vstrSelectProduct')

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUsersRightsList = findRequest.fetch()

            if len(thisUsersRightsList) > 0:
                thisUserRight = thisUsersRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser:
                findRequest = AppRequests.query(AppRequests.strIDNumber == vstrIDNumber)
                thisAppRequestsList = findRequest.fetch()

                if len(thisAppRequestsList) > 0:
                    thisAppRequest = thisAppRequestsList[0]
                    thisAppRequest.writeNames(strinput=vstrNames)
                    thisAppRequest.writeSurname(strinput=vstrSurname)
                    thisAppRequest.writeIDNumber(strinput=vstrIDNumber)
                    thisAppRequest.writeCell(strinput=vstrCell)
                    thisAppRequest.writeEmail(strinput=vstrEmail)
                    thisAppRequest.put()
                    self.response.write("Successfully updated Account Information")
                else:
                    self.response.write("Unable to locate account information please try again later")
            else:
                self.response.write("you are not allowed to make changes to this account")




class thisRequestHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from dashboard import AppRequests
        if Guser:
            strURL = self.request.url
            URLlist = strURL.split("/")
            strReference = URLlist[len(URLlist) - 1]

            findRequest = AppRequests.query(AppRequests.strReference == strReference)
            thisAppRequestsList = findRequest.fetch()

            if len(thisAppRequestsList) > 0:
                thisAppRequest = thisAppRequestsList[0]
            else:
                thisAppRequest = AppRequests()

            template = template_env.get_template('templates/account/appRequests.html')
            context = {'thisAppRequest':thisAppRequest}
            self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        from dashboard import AppRequests, Administrators
        if Guser:
            vstrReference = self.request.get('vstrReference')
            vstrIDNumber = self.request.get('vstrIDNumber')

            findRequest = AppRequests.query(AppRequests.strIDNumber == vstrIDNumber)
            thisAppRequestsList = findRequest.fetch()

            if len(thisAppRequestsList) > 0:
                thisAppRequest = thisAppRequestsList[0]
            else:
                thisAppRequest = AppRequests()

            if thisAppRequest.strIDNumber == vstrIDNumber:
                thisAppRequest.writeRequestAccepted(strinput=True)
                findRequest = ChurchMember.query(ChurchMember.strMemberID == vstrReference)
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                thisChurchMember.writeMemberID(strinput=vstrReference)
                thisChurchMember.writeCell(strinput=thisAppRequest.strCell)
                thisChurchMember.writeMemberNames(strinput=thisAppRequest.strNames)
                thisChurchMember.writeMemberSurname(strinput=thisAppRequest.strSurname)
                thisChurchMember.writeMemberIDNumber(strinput=thisAppRequest.strIDNumber)
                thisChurchMember.writeEmail(strinput=thisAppRequest.strEmail)
                thisChurchMember.writeProfileClaimed(strinput=True)

                findRequest = Churches.query(Churches.strFounderMemberID == vstrReference)
                thisChurchesList = findRequest.fetch()

                if len(thisChurchesList) > 0:
                    thisNewChurch = thisChurchesList[0]
                else:
                    thisNewChurch = Churches()

                thisNewChurch.createChurchID(strinput=vstrReference)
                thisNewChurch.writeFounderMemberID(strinput=vstrReference)
                thisChurchMember.writeChurchID(strinput=thisNewChurch.strChurchID)

                findRequest = UserRights.query(UserRights.strMemberID  == vstrReference)
                thisUsersRightsList = findRequest.fetch()

                if len(thisUsersRightsList) > 0:
                    thisUsersRight = thisUsersRightsList[0]
                else:
                    thisUsersRight = UserRights()

                thisUsersRight.setAdminUser(strinput=True)
                thisUsersRight.setSuperUser(strinput=False)
                thisUsersRight.setChurchMember(strinput=False)
                thisUsersRight.writeMemberID(strinput=vstrReference)

                findRequest = Administrators.query(Administrators.strAdminID == thisUsersRight.strMemberID)
                thisAdminList = findRequest.fetch()

                if len(thisAdminList) > 0:
                    thisAdmin = thisAdminList[0]
                else:
                    thisAdmin = Administrators()

                thisAdmin.writeAdminID(strinput=thisUsersRight.strMemberID)
                thisAdmin.writeChurchID(strinput=thisNewChurch.strChurchID)

                thisAdmin.put()
                thisUsersRight.put()
                thisNewChurch.put()
                thisChurchMember.put()
                thisAppRequest.put()

                self.response.write("App Request Accepted")
            else:
                self.request.write("Error Data Mismatch")



class ProductsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Products.query()
            thisProductsList = findRequest.fetch()

            if len(thisProductsList) == 3:
                template = template_env.get_template('templates/account/products.html')
                context = {'thisProductsList':thisProductsList}
                self.response.write(template.render(context))
            else:
                thisProducts = Products()
                thisProducts.put()

                thisProducts = Products()
                thisProducts.setAdminPlusSMS()
                thisProducts.put()

                thisProducts = Products()
                thisProducts.setAdminSMSEmail()
                thisProducts.put()


                findRequest = Products.query()
                thisProductsList = findRequest.fetch()

                template = template_env.get_template('templates/account/products.html')
                context = {'thisProductsList':thisProductsList}
                self.response.write(template.render(context))


class ProfileInfoHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from dashboard import AppRequests
        if Guser:

            findRequest = AppRequests.query(AppRequests.strReference == Guser.user_id())
            thisAppRequestList = findRequest.fetch()
            if len(thisAppRequestList) > 0:
                thisAppRequest = thisAppRequestList[0]
            else:
                thisAppRequest = AppRequests()

            template = template_env.get_template('templates/account/profileinfo.html')
            context = {'thisAppRequest':thisAppRequest}
            self.response.write(template.render(context))







app = webapp2.WSGIApplication([
    ('/accounts', AccountsHandler),
    ('/accounts/update', UpdateAccountHandler),
    ('/accounts/proinfo', ProfileInfoHandler),
    ('/accounts/request/.*', thisRequestHandler),
    ('/accounts/products', ProductsHandler)


], debug=True)