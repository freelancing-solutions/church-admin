
import os
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class ContactMessages(ndb.Expando):
    strMessageReference = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strSubject = ndb.StringProperty()
    strMessage = ndb.StringProperty()
    strMessageExcerpt = ndb.StringProperty()

    strDateSubmitted = ndb.DateProperty(auto_now_add=True)
    strTimeSubmitted = ndb.TimeProperty(auto_now_add=True)

    strResponseSent = ndb.BooleanProperty(default=False)

    def readDateSubmitted(self):
        try:
            strTemp = str(self.strDateSubmitted)
            strTemp = strTemp.strip()

            return strTemp
        except:
            return None
    def readTimeSubmitted(self):
        try:
            strTemp = str(self.strTimeSubmitted)
            strTemp = strTemp.strip()

            return strTemp
        except:
            return None
    def readResposeSent(self):
        try:
            return self.strResponseSent
        except:
            return False
    def writeResponseSent(self,strinput):
        try:
            if strinput == True:
                self.strResponseSent = True
                return True
            else:
                self.strResponseSent = False
                return True
        except:
            return False
    def readNames(self):
        try:
            strTemp = str(self.strNames)
            strTemp = strTemp.strip()

            if not(strTemp == None):
                return strTemp
            else:
                return None
        except:
            return None
    def writeNames(self,strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.strip()

            if strinput != None:
                self.strNames = strinput
                return True
            else:
                return False
        except:
            return False
    def readEmail(self):
        try:
            strTemp = str(self.strEmail)
            strTemp = strTemp.strip()

            if not(strTemp == None):
                return strTemp
            else:
                return None
        except:
            return None
    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.strip()

            if strinput != None:
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False
    def readCell(self):
        try:
            strTemp = str(self.strCell)
            strTemp = strTemp.strip()

            if not(strTemp == None):
                return strTemp
            else:
                return None
        except:
            None
    def writeCell(self,strinput):
        try:

            strinput = str(strinput)
            strinput = strinput.strip()

            if strinput != None:
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False
    def readSubject(self):
        try:
            strTemp = str(self.strSubject)
            strTemp = strTemp.strip()

            if not(strTemp == None):
                return strTemp
            else:
                return None

        except:
            return None
    def writeSubject(self,strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.strip()

            if strinput != None:
                self.strSubject = strinput
                return True
            else:
                return False
        except:
            return False
    def readMessage(self):
        try:
            strTemp = str(self.strMessage)
            strTemp = strTemp.strip()

            if not(strTemp == None):
                return strTemp
            else:
                return None

        except:
            return None
    def writeMessage(self,strinput):
        try:
            strinput = str(strinput)
            strinput = strinput.strip()

            if strinput != None:
                self.strMessage = strinput
                MessageLen = len(self.strMessage)

                if MessageLen > 16:
                    self.strMessageExcerpt = self.strMessage[0:16]
                else:
                    self.strMessageExcerpt = self.strMessage

                return True
            else:
                return False
        except:
            return False
    def sendResponse(self):
        try:
            sender_address = ('support@church-admins.appspot.com')
            mail.send_mail(sender_address, self.strEmail, self.strSubject, self.strMessage)
            return True
        except:
            return False

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            template = template_env.get_template('templates/contact/contact.html')
            context = {}
            self.response.write(template.render(context))


    def post(self):
        try:
            Guser = users.get_current_user()
            if Guser:
                strnames = self.request.get('vstrNames')
                strEmail = self.request.get('vstrEmail')
                strcell = self.request.get('vstrCell')
                strsubject = self.request.get('vstrSubject')
                strmessage = self.request.get('vstrMessage')

                ContactMessage = ContactMessages()
                ContactMessage.strMessageReference = str(Guser.user_id())
                ContactMessage.writeNames(strinput=strnames)
                ContactMessage.writeEmail(strinput=strEmail)
                ContactMessage.writeCell(strinput=strcell)
                ContactMessage.writeSubject(strinput=strsubject)
                ContactMessage.writeMessage(strinput=strmessage)

                ContactMessage.put()
                self.response.write("""
                Contact Message Submitted Successfully One of our Representatives will get back to you as soon as possible
                """)
            else:
                self.response.write("""
                                Please Login to Send Messages, [*]
                                """)


        except:
            self.response.write("""
            Error unable to send contact message
            """)


class readContactHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = self.request.url
            URLlist = URL.split("/")
            strReference = URLlist[len(URLlist) - 1]

            findRequest = ContactMessages.query(ContactMessages.strMessageReference == strReference)
            thisContactMessagesList = findRequest.fetch()

            if len(thisContactMessagesList) > 0:
                thisContactMessage = thisContactMessagesList[0]
            else:
                thisContactMessage = ContactMessages()

            template = template_env.get_template('templates/contact/readContact.html')
            context = {'thisContactMessage':thisContactMessage}
            self.response.write(template.render(context))





app = webapp2.WSGIApplication([
    ('/contact', ContactHandler),
    ('/contact/read/.*', readContactHandler)

], debug=True)

