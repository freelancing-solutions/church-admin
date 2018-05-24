

import os
from google.appengine.api import urlfetch
import webapp2
import jinja2
from google.appengine.ext import ndb
import logging
import datetime





template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
strDefaultWhiteList = ["https://church-admins.appspot.com","https://www.church-admins.appspot.com",
                       "https://sa-loans.appspot.com","https://www.sa-loans.appspot.com",
                       "https://ab-loan.appspot.com","https://www.ab-loan.appspot.com",
                       "https://pro-finance.appspot.com", "https://www.pro-finance.appspot.com",
                       "https://midey-finance.appspot.com", "https://www.midey-finance.appspot.com",
                       "https://client-trace.appspot.com", "https://www.client-trace.appspot.com",
                       "https://choosen-loan.appspot.com", "https://www.choosen-loan.appspot.com",
                       "https://manage-hotels.appspot.com", "https://www.manage-hotels.appspot.com",
                       "https://p2ptraders-app.appspot.com", "https://www.p2ptraders-app.appspot.com",
                       "https://rinde-cashloan.appspot.com", "https://www.rinde-cashloan.appspot.com",
                       "https://sa-sms.appspot.com", "https://sa-sms.appspot.com",
                       "https://sa-fax.appspot.com", "https://sa-fax.appspot.com",
                       "https://justice-ndou.appspot.com","https://www.justice-ndou.appspot.com",
                       "https://freelancing-solutions.appspot.com", "https://freelancing-solutions.appspot.com",
                       "https://easy-hosting.appspot.com", "https://easy-hosting.appspot.com",
                       "https://cloud-job.appspot.com", "https://cloud-job.appspot.com"]


#TODO- consider allowing blue it marketing to also work as a partner list information exchange platform database
#TODO- this will allow blue it marketing to sell access to the API


class WhiteList(ndb.Expando):
    strURL = ndb.StringProperty()

    def writeURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strURL = strinput
                return True
            else:
                return False
        except:
            return False


class ErrorMessages(ndb.Expando):

    strLangCode = ndb.StringProperty()

    strOrganizationID = ndb.StringProperty() #TODO Allow organization to select Language, then use the translate API to translate all the interfaces and html documents

    strMessReportNotFound = ndb.StringProperty(default="Report not found")
    strMessAccountNotVerified = ndb.StringProperty(default="Account not verified")
    strMessAccountNotValid = ndb.StringProperty(default="Account not valid")
    strMessWebsiteNotAuthorized = ndb.StringProperty(default="Website not authorized for use with API")
    strMessAuthenticationError = ndb.StringProperty(default="Authentication error")
    strMessErrorSendingMessage = ndb.StringProperty(default="Error sending message")
    strMessInsufficientCredit = ndb.StringProperty(default="Insufficient credit")

class Const(ndb.Expando):
    strNoDataCode = ndb.StringProperty(default="X0001")
    strDataSplitter = ndb.StringProperty(default="-")
    strAPIGroupID = ndb.StringProperty(default="APIGROUP")

class PartnerSites(Const):
    """
        Return data format for contacts
        name-surname-cell-email
    """
    strSiteName = ndb.StringProperty(default="Church Admin")
    strServiceName = ndb.StringProperty(default="Contacts")
    strSiteID = ndb.StringProperty()
    strURL = ndb.StringProperty(default="https://church-admins.appspot.com/endpoints/contacts-get")
    strAPIKey = ndb.StringProperty(default=os.environ.get('BIM_INTERNAL_API'))
    strAPISecret = ndb.StringProperty(default=os.environ.get('BIM_INTERNAL_SECRET'))

    def writeSiteID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSiteID = strinput
                return True
            else:
                return False

        except:
            return False
    def CreateSiteID(self):
        import random,string
        try:
            strSiteID = ""
            for i in range(256):
                strSiteID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strSiteID
        except:
            return None
    def writeURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strURL = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAPIKey(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAPIKey = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateAPIKey(self):
        import random,string
        try:
            strAPIKey = ""
            for i in range(512):
                strAPIKey += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strAPIKey
        except:
            return None
    def CreateAPISecret(self):
        import random,string
        try:
            strSecretCode = ""
            for i in range(512):
                strSecretCode += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strSecretCode
        except:
            return None
    def writeAPISecret(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAPISecret = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSiteName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSiteName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeServiceName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strServiceName = strinput
                return True
            else:
                return False
        except:
            return False

    def FetchMessage(self):
        """
            call the partner site through its API and fetch contact information
            if there comes a need to add more information on the contact another API and API call can be built
        :return:
        """
        pass

    def FetchContact(self,index):
        """
        Please implement a matching protocol on church admin

        :return:
        """
        try:
            form_data = "&api=" + self.strAPIKey + "&secret=" + self.strAPISecret + "&index=" + str(index)
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.strURL,payload=form_data,method=urlfetch.POST,headers=headers,validate_certificate=True)
            if (result.status_code >= 200) and (result.status_code < 400):
                return result.content
            else:
                return self.strNoDataCode
        except urlfetch.Error:
            return self.strNoDataCode

    def FetchContactsJSONList(self,index):
        """

        :param index: total contacts to return
        :return:
        """
        try:
            form_data = "&api=" + self.strAPIKey + "&secret=" + self.strAPISecret + "&index=" + str(index)
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(url=self.strURL, payload=form_data, method=urlfetch.POST, headers=headers,
                                    validate_certificate=True)
            if (result.status_code >= 200) and (result.status_code < 400):
                return result.content
            else:
                return self.strNoDataCode
        except urlfetch.Error:
            return self.strNoDataCode


#TODO- Consider implementing PartnerSites on internal consumer services API


class EndPoints(Const):

    strOrganizationID = ndb.StringProperty() #Used only for external API that uses internal resources example message sending API
    strServiceName = ndb.StringProperty(default="Contacts")
    strPointID = ndb.StringProperty()
    strPointURL = ndb.StringProperty()
    #TODO- Organizations must be given their own contacts end point key and secret, and also their websites included
    #TODO- in the white list
    strAPIKey = ndb.StringProperty()
    strAPISecret = ndb.StringProperty()

    def writeOrganizationID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOrganizationID = strinput
                return True
            else:
                return False
        except:
            return False

    def writePointID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPointID = strinput
                return True
            else:
                return False
        except:
            return False

    def writePointURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPointURL = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAPiKey(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAPIKey = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAPISecret(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAPISecret = strinput
                return True
            else:
                return False
        except:
            return False

    def CreatePointID(self):
        import random,string
        try:
            strPointID = ""
            for i in range(256):
                self.strPointID += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strPointID
        except:
            return None

    def CreateAPIKey(self):
        import random,string
        try:
            strAPIKey = ""
            for i in range(256):
                strAPIKey += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strAPIKey
        except:
            return None

    def CreateAPISecret(self):
        import random,string
        try:
            strAPISecret = ""
            for i in range(256):
                strAPISecret += random.SystemRandom().choice(string.digits + string.ascii_uppercase)
            return strAPISecret
        except:
            return None

class RoutesHandler(webapp2.RequestHandler):


    def get(self):
        pass

    def post(self):
        """
                '/endpoints/contacts-get'
                '/endpoints/contact-add'
                '/endpoints/contact-exist'
        :return:
        """

        URL = self.request.url
        strURLlist = URL.split("/")
        strFunction = strURLlist[4]
        #TODO-turn all Handlers into local functions
        logging.info("this is the function : " + strFunction)

        strAPI = self.request.get('api')
        strSecret = self.request.get('secret')
        try:
            if os.environ["REMOTE_ADDR"] != None:
                strOriginURL = os.environ["REMOTE_ADDR"]
            else:
                strOriginURL = self.request.remote_addr
        except:
            strOriginURL = self.request.remote_addr


def RetrieveContactList():

    from contacts import Contacts

    findQuery = Contacts.query().order(+Contacts.strDateCreated)
    thisContactList = findQuery.fetch()
    return thisContactList




class EpRouterHandler(webapp2.RequestHandler):
    def get(self):
        pass

    def post(self):
        """
                '/endpoints/contacts-get'
                '/endpoints/contact-add'
                '/endpoints/contact-exist'

                Sharing information accross apps ever app must have this endpoint and also other apps can call it from tasks jobs

        :return:
        """

        strAPI = self.request.get('api')
        strSecret = self.request.get('secret')
        URL = self.request.url
        strURLList = URL.split("/")
        strFunction = strURLList[4]
        try:
            if os.environ["REMOTE_ADDR"] != None:
                strOriginURL = os.environ["REMOTE_ADDR"]
            else:
                strOriginURL = self.request.remote_addr
        except:
            strOriginURL = self.request.remote_addr

        if strOriginURL in strDefaultWhiteList:
            if (strAPI == str(os.environ.get('BIM_INTERNAL_API'))) and (strSecret == str(os.environ.get('BIM_INTERNAL_SECRET'))):

                if strFunction == "contacts-get":
                    strIndex = self.request.get("index")
                    thisContactList = RetrieveContactList()
                    self.response.headers["Content-Type"] = "application/json"
                    template  = template_env.get_template('templates/epdataexchange/contacts-list.json')
                    context = {"thisContactList":thisContactList}
                    self.response.write(template.render(context))



app = webapp2.WSGIApplication([
    ('/endpoints/.*', RoutesHandler),
    ('/epinternal/.*', EpRouterHandler)
    #TODO- Create Advertising Endpoints and also Surveys End Points---Refine this idea its prooving to be difficult
], debug=True)