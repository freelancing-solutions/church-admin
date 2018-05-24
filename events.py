

__author__ = 'mashudu'
import os

import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
from church import MemberAddresses, ChurchMember
from userRights import UserRights
import datetime,logging

from datetime import timedelta
class EventTypes(ndb.Expando):
    strIndex = ndb.IntegerProperty(default=0)
    strEventType = ndb.StringProperty(default="Conference") # Night Prayer,
    strDescription = ndb.StringProperty()

    def writeEventType(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventType = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDescription = strinput
                return True
            else:
                return False
        except:
            return False

    def CreateIndex(self):
        import random,string
        strIndexID = ""
        for i in range(16):
            strIndexID += random.SystemRandom().choice(string.digits)

        return strIndexID

    def writeIndex(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strIndex = int(strinput)
                return True
            else:
                return False
        except:
            return False
class Event(ndb.Expando):
    strEventID = ndb.StringProperty()
    strCreatorID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strEventType = ndb.StringProperty(default="Conference")
    strEventName = ndb.StringProperty()
    strEventIntro = ndb.StringProperty()
    strDescription = ndb.StringProperty()

    strStartDate = ndb.DateProperty()
    strStartTime = ndb.TimeProperty()

    strEndDate = ndb.DateProperty()
    strEndTime = ndb.TimeProperty()

    strDateCreated = ndb.DateProperty(auto_now_add=True)
    strTimeCreated = ndb.TimeProperty() #TODO- Intergrate this with the rest of the app

    strSendEventNotification = ndb.BooleanProperty(default=False)

    strEventIsPrivate = ndb.BooleanProperty(default=False)

    strShares = ndb.IntegerProperty(default=0)
    strLikes = ndb.IntegerProperty(default=0)



    def writeDateCreated(self,strinput):
        try:

            if isinstance(strinput,datetime.date):
                self.strDateCreated = strinput
                return True
            else:
                return False

        except:
            return False
    def createEventID(self):
        import string,random
        try:

            strEventID = ""
            for i in range(128):
                strEventID += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strEventID

        except:
            return None
    def writeEventID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventID = strinput
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
    def writeCreatorID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCreatorID = strinput
                return True
            else:
                return False

        except:
            return False
    def writeEventType(self,strinput):
        try:
            strinput = str(strinput)
            findRequest = EventTypes.query()
            EventTypesList = findRequest.fetch()

            strEventList = []
            for strEvent in EventTypesList:
                strEventList.append(strEvent.strEventType)

            if strinput in strEventList:
                self.strEventType = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEventName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEventIntro(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventIntro = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDescription = strinput
                return True
            else:
                return False
        except:
            return False




    def setStartDate(self,strinput):
        try:
            if strinput != None:
                self.strStartDate = strinput
                return True
            else:
                return False
        except:
            return False
    def setEndDate(self,strinput):
        try:

            if strinput != None:
                self.strEndDate = strinput
                return True
            else:
                return False
        except:
            return False
    def setStartTime(self,strinput):
        try:

            if strinput != None:
                self.strStartTime = strinput
                return True
            else:
                return False

        except:
            return False
    def setEndTime(self,strinput):
        try:
            if strinput != None:
                self.strEndTime = strinput
                return True
            else:
                return False
        except:
            return False
    def setSendEventNotification(self,strinput):
        try:
            if (strinput == True) or (strinput == False):
                self.strSendEventNotification = strinput
                return True
            else:
                return False
        except:
            return False
class EventAgendas(ndb.Expando):
    strEventID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strCreatorID = ndb.StringProperty()
    strAgendaTitle = ndb.StringProperty()
    strAgendaDescription = ndb.StringProperty()

    strStartDate = ndb.DateProperty()
    strStartTime = ndb.TimeProperty()
    strEndDate = ndb.DateProperty()
    strEndTime = ndb.TimeProperty()

    strSpeakerID = ndb.StringProperty()


    def writeStartDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strStartDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStartTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strStartTime = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEndDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strEndDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEndTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strEndTime = strinput
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

    def writeEventID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventID = strinput
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

    def writeCreatorID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCreatorID = strinput
                return True
            else:
                return False

        except:
            return False

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

    def writeAgendaDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAgendaDescription = strinput
                return True
            else:
                return False

        except:
            return False
class EventRegistrations(ndb.Expando):
    strEventID = ndb.StringProperty()
    strMemberID = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strDateRegistered = ndb.DateProperty()
    strTimeRegistered = ndb.TimeProperty()
    strVerified = ndb.BooleanProperty(default=False)
    strVerificationCode = ndb.BooleanProperty()
    strSMSCode = ndb.StringProperty()


    def writeEventID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventID = strinput
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
    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTel = strinput
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
    def writeDateRegistered(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateRegistered = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeRegistered(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeRegistered = strinput
                return True
            else:
                return False
        except:
            return False
    def writeVerified(self,strinput):
        try:
            if strinput in [True,False]:
                self.strVerified = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateVerificationCode(self):
        import string,random
        try:

            strVerificationCode = ""
            for i in range(256):
                strVerificationCode += random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)
            return strVerificationCode
        except:
            return None
    def writeVerificationCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strVerificationCode = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateSMSCode(self):
        import random,string
        try:
            strSMSCode = ""
            for i in range(4):
                strSMSCode += random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)
            return strSMSCode
        except:
            return None
    def writeSMSCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSMSCode = strinput
                return True
            else:
                return False

        except:
            return False
#TODO- Improve the Surveys Modules so that it can be completed online and also through SMS
class EventSurveys(ndb.Expando):
    strEventID = ndb.StringProperty()
    strSurveyID = ndb.StringProperty()
    strSurveyName = ndb.StringProperty()
    strSurveyDescription = ndb.StringProperty()

    def writeEventID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventID = strinput
                return True
            else:
                return False

        except:
            return False
    def writeSurveyID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateSurveyID(self):
        import random,string
        try:
            strSurveyID = ""
            for i in range(128):
                strSurveyID += random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)
            return strSurveyID
        except:
            return None
    def writeSurveyName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSurveyDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyName = strinput
                return True
            else:
                return False
        except:
            return False
class SurveyQuestions(ndb.Expando):
    strSurveyID = ndb.StringProperty()
    strQuestionID = ndb.StringProperty()
    strQuestion = ndb.StringProperty()
    strAnswer1 = ndb.StringProperty()
    strAnswer2 = ndb.StringProperty()
    strAnswer3 = ndb.StringProperty()
    strAnswer4 = ndb.StringProperty()

    def writeSurveryID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSurveyID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeQuestionID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strQuestionID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateQuestionID(self):
        import random,string
        try:

            strQuestionID = ""
            for i in range(64):
                strQuestionID += random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)
            return strQuestionID
        except:
            return None
    def writeQuestion(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strQuestion = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAnswer1(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAnswer1 = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAnswer2(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAnswer2 = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAnswer3(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAnswer3 = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAnswer4(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAnswer4 = strinput
                return True
            else:
                return False
        except:
            return False
class SurveyAnswers(ndb.Expando):
    strQuestionID = ndb.StringProperty()
    strMemberID = ndb.StringProperty()
    strAnswer = ndb.StringProperty()

    def writeQuestionID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strQuestionID = strinput
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

    def writeAnswer(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAnswer =strinput
                return True
            else:
                return False
        except:
            return False
class EventNotes(ndb.Expando):
    strEventID = ndb.StringProperty()
    strEventNotes = ndb.StringProperty()
    strNoteDate = ndb.DateProperty()
    strNoteTime = ndb.TimeProperty()

    def writeEventID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeEventNotes(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventNotes = strinput
                return True
            else:
                return False
        except:
            return False

    def writeNoteDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strNoteDate = strinput
                return True
            else:
                return False
        except:
            return False

    def writeNoteTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strNoteTime = strinput
                return True
            else:
                return False
        except:
            return False
class AttendeePreferences(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strEventID = ndb.StringProperty()

    strPreferenceTitle = ndb.StringProperty()
    strPreferenceDescription = ndb.StringProperty()


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

    def writeEventID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventID = strinput
                return True
            else:
                return False
        except:
            return False


    def writePreferenceTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPreferenceTitle = strinput
                return True
            else:
                return False
        except:
            return False

    def writePreferenceDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPreferenceDescription = strinput
                return True
            else:
                return False
        except:
            return False
class EventSponsors(ndb.Expando):
    strEventID = ndb.StringProperty()
    strSponsorID = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strDateRegistered = ndb.DateProperty()
    strTimeRegistered = ndb.TimeProperty()
    strVerified = ndb.BooleanProperty(default=False)
    strVerificationCode = ndb.BooleanProperty()
    strSMSCode = ndb.StringProperty()

    def writeEventID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSponsorID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSponsorID = strinput
                return True
            else:
                return False

        except:
            return False
    def CreateSponsorID(self):
        import random,string
        try:
            strSponsorID = ""
            for i in range(4):
                strSponsorID += random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)
            return strSponsorID

        except:
            return None
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
    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTel = strinput
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


    def writeDateRegistered(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.strDateRegistered = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeRegistered(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.strTimeRegistered = strinput
                return True
            else:
                return False
        except:
            return False
    def writeVerified(self, strinput):
        try:
            if strinput in [True, False]:
                self.strVerified = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateVerificationCode(self):
        import string, random
        try:

            strVerificationCode = ""
            for i in range(256):
                strVerificationCode += random.SystemRandom().choice(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)
            return strVerificationCode
        except:
            return None
    def writeVerificationCode(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strVerificationCode = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateSMSCode(self):
        import random, string
        try:
            strSMSCode = ""
            for i in range(4):
                strSMSCode += random.SystemRandom().choice(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)
            return strSMSCode
        except:
            return None
    def writeSMSCode(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strSMSCode = strinput
                return True
            else:
                return False

        except:
            return False
class EventExhibitors(ndb.Expando):
    strEventID = ndb.StringProperty()
    strExhibitorID = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strDateRegistered = ndb.DateProperty()
    strTimeRegistered = ndb.TimeProperty()
    strVerified = ndb.BooleanProperty(default=False)
    strVerificationCode = ndb.BooleanProperty()
    strSMSCode = ndb.StringProperty()

    def writeEventID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeExhibitorID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strExhibitorID = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateExhibitorID(self):
        import random, string
        try:
            strExhibitorID = ""
            for i in range(128):
                strExhibitorID += random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)
            return strExhibitorID
        except:
            return None
    def writeNames(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNames = strinput
                return True

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
    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTel = strinput
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


    def writeDateRegistered(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.strDateRegistered = strinput
                return True
            else:
                return False
        except:
            return False


    def writeTimeRegistered(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.strTimeRegistered = strinput
                return True
            else:
                return False
        except:
            return False


    def writeVerified(self, strinput):
        try:
            if strinput in [True, False]:
                self.strVerified = strinput
                return True
            else:
                return False
        except:
            return False


    def CreateVerificationCode(self):
        import string, random
        try:

            strVerificationCode = ""
            for i in range(256):
                strVerificationCode += random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)
            return strVerificationCode
        except:
            return None


    def writeVerificationCode(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strVerificationCode = strinput
                return True
            else:
                return False
        except:
            return False


    def CreateSMSCode(self):
        import random, string
        try:
            strSMSCode = ""
            for i in range(4):
                strSMSCode += random.SystemRandom().choice(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)
            return strSMSCode
        except:
            return None


    def writeSMSCode(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strSMSCode = strinput
                return True
            else:
                return False

        except:
            return False
class Speakers(ndb.Expando):
    strEventID = ndb.StringProperty()
    strSpeakerID = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strDateRegistered = ndb.DateProperty()
    strTimeRegistered = ndb.TimeProperty()
    strVerified = ndb.BooleanProperty(default=False)
    strVerificationCode = ndb.BooleanProperty()
    strSMSCode = ndb.StringProperty()

    def writeEventID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventID = strinput
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
    def CreatSpeakerID(self):
        import random,string
        try:
            strSpeakerID = ""
            for i in range(128):
                strSpeakerID += random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)

            return strSpeakerID
        except:
            return strSpeakerID
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
    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTel = strinput
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
    def writeDateRegistered(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.strDateRegistered = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeRegistered(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.strTimeRegistered = strinput
                return True
            else:
                return False
        except:
            return False
    def writeVerified(self, strinput):
        try:
            if strinput in [True, False]:
                self.strVerified = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateVerificationCode(self):
        import string, random
        try:

            strVerificationCode = ""
            for i in range(256):
                strVerificationCode += random.SystemRandom().choice(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)
            return strVerificationCode
        except:
            return None
    def writeVerificationCode(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strVerificationCode = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateSMSCode(self):
        import random, string
        try:
            strSMSCode = ""
            for i in range(4):
                strSMSCode += random.SystemRandom().choice(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase + string.digits)
            return strSMSCode
        except:
            return None
    def writeSMSCode(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strSMSCode = strinput
                return True
            else:
                return False

        except:
            return False

class EventMarketingCampaign(ndb.Expando):
    strEventID = ndb.StringProperty()
    strCampaignID = ndb.StringProperty()
    strDeliveryChannel = ndb.StringProperty(default="SMS") # Email,Social
    strCampaignName = ndb.StringProperty()
    strCampaignDescription = ndb.StringProperty()

    def writeEventID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCampaignID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCampaignID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDeliveryChannel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDeliveryChannel = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCampaignName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCampaignName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCampaignDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCampaignDescription = strinput
                return True
            else:
                return False

        except:
            return False
class CampaignMessages(ndb.Expando):
    strEventID = ndb.StringProperty()
    strCampaignID = ndb.StringProperty()
    strSMSMessage = ndb.StringProperty()
    strEmailSubject = ndb.StringProperty()
    strEmailBody = ndb.StringProperty()
    strCampaignURL = ndb.StringProperty()

    def writeEventID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventID = strinput
                return True
            else:
                return False

        except:
            return False
    def writeCampaignID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCampaignID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSMSMessage(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSMSMessage = strinput
                return True
            else:
                return False
        except:
            return False
    def writeEmailSubject(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmailSubject = strinput
                return True
            else:
                return False

        except:
            return False

    def writeEmailBody(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmailBody = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCampaignURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCampaignURL = strinput
                return True
            else:
                return False
        except:
            return False
class CampaignHostedPage(ndb.Expando):
    strCampaignURL = ndb.StringProperty()
    strCampaignID = ndb.StringProperty()
    strPageTitle = ndb.StringProperty()
    strPageHeading = ndb.StringProperty()
    strPageBody = ndb.StringProperty()

    def writeCampaignURL(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCampaignURL = strinput
                return True
            else:
                return False

        except:
            return False

    def writeCampaignID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCampaignID = strinput
                return True
            else:
                return False
        except:
            return False

    def writePageTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPageTitle = strinput
                return True
            else:
                return False
        except:
            return False

    def writePageHeading(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPageHeading = strinput
                return True
            else:
                return False
        except:
            return False

    def writePageBody(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPageBody = strinput
                return True
            else:
                return False

        except:
            return False
class EventAccomodation(ndb.Expando):
    strEventID = ndb.StringProperty()
    strAccomodationName = ndb.StringProperty()
    strAccomodationDescription = ndb.StringProperty()
    strCapacity = ndb.IntegerProperty()
    strRate = ndb.IntegerProperty()

    def writeEventID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEventID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccomodationName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccomodationName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAccomodationDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccomodationDescription = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCapacity(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strCapacity = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeRate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strRate = int(strinput)
                return True
            else:
                return False
        except:
            return False
class Birthdays(ndb.Expando):
    strChurchID = ndb.StringProperty()
    strBirthdayMessage = ndb.StringProperty()
    strAutoSend = ndb.BooleanProperty(default=True)

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

    def writeBirthdayMessage(self,strinput):
        try:

            if strinput != None:
                self.strBirthdayMessage = strinput
                return True
            else:
                return False
        except:
            return False

    def writeAutoSend(self,strinput):
        try:
            if strinput in [True,False]:
                self.strAutoSend = strinput
                return True
            else:
                return False
        except:
            return False

    def SendBirthdayWishes(self,strMessage,strCell,strPortal):
        from mysms import SMSPortalVodacom,SMSPortalBudget,SMSAccount
        try:

            if strPortal == "Vodacom":
                findRequests = SMSPortalVodacom.query()
                thisVodaList = findRequests.fetch()

                if len(thisVodaList) > 0:
                    thisVoda = thisVodaList[0]
                else:
                    thisVoda = SMSPortalVodacom()
                    thisVoda.put()

                NumbersList = []
                NumbersList.append(strCell)
                if thisVoda.CronSendMessages(strCellNumberList=NumbersList,strMessage=strMessage,strAccountID=self.strChurchID):
                    return True
                else:
                    return False
            elif strPortal == "Budget":
                findRequests = SMSPortalBudget.query()
                thisPortalList = findRequests.fetch()

                if len(thisPortalList) > 0:
                    thisPortal = thisPortalList[0]
                else:
                    thisPortal = SMSPortalBudget()

                    strRef = thisPortal.SendCronMessage(strMessage=strMessage,strCell=strCell)
                    if not(strRef == None):
                        return True
                    else:
                        return False
            else:
                return False







        except:
            return False
class Holidays(ndb.Expando):
    strChurchID = ndb.StringProperty()
    strHolidayName = ndb.StringProperty()
    strDate = ndb.DateProperty()

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

    def writeHolidayName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strHolidayName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDate = strinput
                return True
            else:
                return False
        except:
            return False

def CreateBirthdayVariables():
    try:

        findRequest = ChurchMember.query()
        thisChurchMemberList = findRequest.fetch()

        for thisChurchMember in thisChurchMemberList:

            thisBirthDate = thisChurchMember.strMemberDateOfBirth
            if (thisBirthDate != None):
                strYear = thisBirthDate.year
                strMonth = thisBirthDate.month
                strDay = thisBirthDate.day
                thisChurchMember.writeYear(strinput=strYear)
                thisChurchMember.writeMonth(strinput=strMonth)
                thisChurchMember.writeDay(strinput=strDay)
                thisChurchMember.put()

        return True
    except:
        return False


class EventsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = Event.query(Event.strChurchID == thisChurchMember.strChurchID)
            MyChurchEventList = findRequest.fetch()

            findRequest = Event.query(Event.strEventIsPrivate == False,Event.strChurchID != thisChurchMember.strChurchID)
            PublicEventList = findRequest.fetch()

            thisDate = datetime.datetime.now()
            UpcomingDate = thisDate + timedelta(days=5)
            RecentDate = thisDate - timedelta(days=5)

            findRequest = Event.query(Event.strEventIsPrivate == False, Event.strStartDate <= UpcomingDate)
            UpcomingEventsList = findRequest.fetch(limit=5)

            findRequest = Event.query(Event.strEventIsPrivate == False,Event.strDateCreated >= RecentDate)
            RecentEventsList = findRequest.fetch()



            template = template_env.get_template('templates/events/events.html')
            context = {'MyChurchEventList':MyChurchEventList,'PublicEventList':PublicEventList,'UpcomingEventsList':UpcomingEventsList,
                       'RecentEventsList':RecentEventsList}
            self.response.write(template.render(context))

        else:
            findRequest = Event.query(Event.strEventIsPrivate == False)
            PublicEventList = findRequest.fetch()
            thisDate = datetime.datetime.now()
            UpcomingDate = thisDate + timedelta(days=5)
            RecentDate = thisDate - timedelta(days=5)

            findRequest = Event.query(Event.strEventIsPrivate == False, Event.strStartDate <= UpcomingDate)
            UpcomingEventsList = findRequest.fetch(limit=5)

            findRequest = Event.query(Event.strEventIsPrivate == False,Event.strDateCreated >= RecentDate)
            RecentEventsList = findRequest.fetch()


            template = template_env.get_template('templates/events/events.html')
            context = {'PublicEventList':PublicEventList,'UpcomingEventsList':UpcomingEventsList,'RecentEventsList':RecentEventsList}
            self.response.write(template.render(context))




    def post(self):
        Guser = users.get_current_user()
        import datetime
        from datetime import timedelta
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":

                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                if CreateBirthdayVariables():

                    findRequest = Birthdays.query(Birthdays.strChurchID == thisChurchMember.strChurchID)
                    thisBirthDayList = findRequest.fetch()

                    if len(thisBirthDayList) > 0:
                        thisBirthDay = thisBirthDayList[0]
                    else:
                        thisBirthDay = Birthdays()


                    thisDate = datetime.datetime.now()
                    thisDate = thisDate.date()

                    thisHigherDate = thisDate + timedelta(days=5)



                    findRequest = ChurchMember.query(ChurchMember.strChurchID == thisChurchMember.strChurchID,ChurchMember.strMonth == thisDate.month,ChurchMember.strDay == thisDate.day)
                    thisTodaysBirthdayList = findRequest.fetch()

                    findRequest = ChurchMember.query(ChurchMember.strChurchID == thisChurchMember.strChurchID,ChurchMember.strMonth == thisHigherDate.month,ChurchMember.strDay < thisHigherDate.day)
                    thisUpcomingBirthdaysList = findRequest.fetch()

                    thisUpcomingBirthList = []
                    for thisUpcoming in thisUpcomingBirthdaysList:
                        if thisUpcoming.strMemberDateOfBirth != None:
                            if thisUpcoming.strDay > thisDate.day:
                                thisUpcomingBirthList.append(thisUpcoming)


                    template = template_env.get_template('templates/birthdays/birthdays.html')
                    context = {'thisTodaysBirthdayList':thisTodaysBirthdayList,'thisUpcomingBirthList':thisUpcomingBirthList,'thisBirthDay':thisBirthDay,'vstrChurchID':thisChurchMember.strChurchID}
                    self.response.write(template.render(context))


            elif vstrChoice == "1":
                vstrChurchID = self.request.get('vstrChurchID')
                vstrBirthdayWishes = self.request.get('vstrBirthdayWishes')
                vstrAutoSendMessages = self.request.get('vstrAutoSendMessages')


                findRequest = Birthdays.query(Birthdays.strChurchID == vstrChurchID)
                thisBirthDayList = findRequest.fetch()

                if len(thisBirthDayList) > 0:
                    thisBirthDay = thisBirthDayList[0]
                else:
                    thisBirthDay = Birthdays()

                thisBirthDay.writeChurchID(strinput=vstrChurchID)
                thisBirthDay.writeBirthdayMessage(strinput=vstrBirthdayWishes)
                if vstrAutoSendMessages == "YES":
                    thisBirthDay.writeAutoSend(strinput=True)
                else:
                    thisBirthDay.writeAutoSend(strinput=False)

                thisBirthDay.put()
                self.response.write('Mulaedza wa duvha la mabebo wo vhulungea udo rumelwa kha vhathu vhane maduvha avho a mabebo akho sendela')

            elif vstrChoice == "2":

                findRequest = Event.query(Event.strEventIsPrivate == False)
                thisEventList = findRequest.fetch()

                findRequest = EventTypes.query()
                thisEventTypesList = findRequest.fetch()


                template = template_env.get_template('templates/events/sub/eventsUser.html')
                context = {'thisEventList':thisEventList,'EventTypeList':thisEventTypesList}
                self.response.write(template.render(context))

            elif vstrChoice == "3":
                vstrEventName = self.request.get('vstrEventName')
                vstrDescription = self.request.get('vstrDescription')
                vstrEventIntro = self.request.get('vstrEventIntro')
                vstrStartDate = self.request.get('vstrStartDate')

                vstrStartTime = self.request.get('vstrStartTime')
                vstrEndDate = self.request.get('vstrEndDate')
                vstrEndTime = self.request.get('vstrEndTime')
                vstrEventType = self.request.get('vstrEventType')
                vstrSendNotifications = self.request.get('vstrSendNotifications')

                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    findRequest = ChurchMember.query(ChurchMember.strEmail == Guser.email())
                    thisChurchMemberList = findRequest.fetch()

                    if len(thisChurchMemberList) > 0:
                        thisChurchMember = thisChurchMemberList[0]
                    else:
                        thisChurchMember = None

                vstrStartDateList = vstrStartDate.split("/")
                strYear = vstrStartDateList[2]
                strMonth = vstrStartDateList[0]
                strDay = vstrStartDateList[1]

                vstrStartTimeList = vstrStartTime.split(" ")
                strStartTime = vstrStartTimeList[0]
                strStartTimeList = strStartTime.split(":")
                strStartHour = strStartTimeList[0]
                strStartHour = int(strStartHour)
                strStartMinute = int(strStartTimeList[1])


                strDayNight = vstrStartTimeList[1]
                strDayNight = strDayNight.strip()
                strDayNight = strDayNight.upper()

                if strDayNight == "PM":
                    strStartHour += 12
                else:
                    pass


                vstrEndDateList = vstrEndDate.split("/")
                strEYear = vstrEndDateList[2]
                strEMonth = vstrEndDateList[0]
                strEDay = vstrEndDateList[1]


                vstrEndTimeList = vstrEndTime.split(" ")
                strETime = vstrEndTimeList[0]
                strEDayNight = vstrEndTimeList[1]
                strEDayNight = strEDayNight.strip().upper()

                strETimeList = strETime.split(":")
                strEHour = int(strETimeList[0])
                strEMinute = int(strETimeList[1])

                if strEDayNight == "PM":
                    strEHour += 12
                else:
                    pass

                vstrStartDate = datetime.date(year=int(strYear),month=int(strMonth),day=int(strDay))
                vstrStartTime = datetime.time(hour=int(strStartHour),minute=int(strStartMinute))


                vstrEndDate = datetime.date(year=int(strEYear),month=int(strEMonth),day=int(strEDay))
                vstrEndTime = datetime.time(hour=int(strEHour),minute=int(strEMinute))

                thisDate = datetime.datetime.now()
                thisDate = thisDate.date()

                if thisChurchMember != None:
                    findRequest = Event.query(Event.strEventName == vstrEventName,Event.strChurchID == thisChurchMember.strChurchID,Event.strStartDate == vstrStartDate)
                    thisEventList = findRequest.fetch()
                    if len(thisEventList) > 0:
                        self.response.write("Duplicate Event please edit the present event...")
                    else:

                        thisEvent = Event()
                        thisEvent.writeChurchID(strinput=thisChurchMember.strChurchID)
                        thisEvent.writeCreatorID(strinput=thisChurchMember.strMemberID)
                        thisEvent.writeEventID(strinput=thisEvent.createEventID())
                        thisEvent.writeEventName(strinput=vstrEventName)
                        thisEvent.writeDescription(strinput=vstrDescription)
                        thisEvent.writeEventIntro(strinput=vstrEventIntro)
                        thisEvent.setStartDate(strinput=vstrStartDate)
                        thisEvent.setStartTime(strinput=vstrStartTime)
                        thisEvent.setEndDate(strinput=vstrEndDate)
                        thisEvent.setEndTime(strinput=vstrEndTime)
                        thisEvent.writeDateCreated(strinput=thisDate)
                        thisEvent.writeEventType(strinput=vstrEventType)
                        if vstrSendNotifications == "YES":
                            thisEvent.setSendEventNotification(strinput=True)
                        else:
                            thisEvent.setSendEventNotification(strinput=False)

                        thisEvent.put()
                        self.response.write("Event Created successfully")

            elif vstrChoice == "4":
                vstrNewEventType = self.request.get('vstrNewEventType')
                vstrNewEventDescription = self.request.get('vstrNewEventDescription')

                findRequest = EventTypes.query(EventTypes.strEventType == vstrNewEventType)
                thisEventList = findRequest.fetch()

                if len(thisEventList) > 0:
                    self.response.write("Duplicate error")
                else:
                    thisEvent = EventTypes()
                    thisEvent.writeEventType(strinput=vstrNewEventType)
                    thisEvent.writeDescription(strinput=vstrNewEventDescription)
                    thisEvent.writeIndex(strinput=thisEvent.CreateIndex())
                    thisEvent.put()
                    self.response.write("Successfully updated event type")

            elif vstrChoice == "5":
                findRequest = Event.query(Event.strCreatorID == Guser.user_id())
                thisEventList = findRequest.fetch()

                template = template_env.get_template('templates/events/sub/subManage.html')
                context = {'thisEventList':thisEventList}
                self.response.write(template.render(context))




        else:
            findRequest = Event.query(Event.strEventIsPrivate == False)
            thisEventList = findRequest.fetch()

            template = template_env.get_template('templates/events/sub/publicEvent.html')
            context = {'thisEventList': thisEventList}
            self.response.write(template.render(context))


class ThisPublicEventHandler(webapp2.RequestHandler):
    def get(self):
        URL = self.request.url

        strURLlist = URL.split("/")
        strEventID = strURLlist[len(strURLlist) - 1]

        findRequest = Event.query(Event.strEventID == strEventID)
        thisEventList = findRequest.fetch()

        if len(thisEventList) > 0:
            thisEvent = thisEventList[0]
        else:
            thisEvent = Event()

        findRequest = EventSponsors.query(EventSponsors.strEventID == strEventID)
        thisSponsorList = findRequest.fetch()

        findRequest = EventExhibitors.query(EventExhibitors.strEventID == strEventID)
        thisExhibitorList = findRequest.fetch()

        findRequest = Speakers.query(Speakers.strEventID == strEventID)
        thisSpeakersList = findRequest.fetch()


        findRequest = EventAgendas.query(EventAgendas.strEventID == strEventID)
        thisEventAgendaList = findRequest.fetch()

        findRequest = EventSurveys.query(EventSurveys.strEventID == strEventID)
        thisSurveyList = findRequest.fetch()



        template = template_env.get_template('templates/events/public/publicevent.html')
        context = {'thisEvent':thisEvent,'thisSponsorList':thisSponsorList,'thisExhibitorList':thisExhibitorList,'thisSpeakersList':thisSpeakersList,
                   'thisEventAgendaList':thisEventAgendaList,'thisSurveyList':thisSurveyList}
        self.response.write(template.render(context))

    def post(self):

        URL = self.request.url
        strURLlist = URL.split("/")
        vstrChoice = strURLlist[len(strURLlist) - 1]

        if vstrChoice == "0":
            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrCell = self.request.get('vstrCell')
            vstrEmail = self.request.get('vstrEmail')
            vstrEventID = self.request.get('vstrEventID')

            Guser = users.get_current_user()

            if Guser:
                strUserID = Guser.user_id()

                findRequest = EventRegistrations.query(EventRegistrations.strMemberID == strUserID, EventRegistrations.strEventID == vstrEventID)
                thisRegistrationList = findRequest.fetch()

                if len(thisRegistrationList) > 0:
                    thisRegistration = thisRegistrationList[0]
                else:
                    thisRegistration = EventRegistrations()

                thisRegistration.writeEventID(strinput=vstrEventID)
                thisRegistration.writeMemberID(strinput=strUserID)
                thisRegistration.writeNames(strinput=vstrNames)
                thisRegistration.writeSurname(strinput=vstrSurname)
                thisRegistration.writeCell(strinput=vstrCell)
                thisRegistration.writeEmail(strinput=vstrEmail)
                thisRegistration.put()
                self.response.write("You where successfully registered for the Event")

            else:
                self.response.write("You cannot Register for this Event if you are not logged in please login...")



class ThisSurveyHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            pass






class ThisManagerHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = self.request.url
            strURLlist = URL.split("/")
            strEventID = strURLlist[len(strURLlist) - 1]

            findRequest = Event.query(Event.strEventID == strEventID,Event.strCreatorID == Guser.user_id())
            thisEventList = findRequest.fetch()

            if len(thisEventList) > 0:
                thisEvent = thisEventList[0]
            else:
                thisEvent = Event()

            template = template_env.get_template('templates/events/manage/manage.html')
            context = {'thisEvent':thisEvent}
            self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrEventID = self.request.get('vstrEventID')

                findRequest = EventRegistrations.query(EventRegistrations.strEventID == vstrEventID)
                thisEventRegistrationList = findRequest.fetch()

                template = template_env.get_template('templates/events/manage/sub/RegisteredAttendees.html')
                context = {'vstrEventID':vstrEventID,'thisEventRegistrationList':thisEventRegistrationList}
                self.response.write(template.render(context))

            elif vstrChoice == "1":
                vstrEventID = self.request.get('vstrEventID')

                findRequest = Speakers.query(Speakers.strEventID == vstrEventID)
                thisSpeakerList = findRequest.fetch()

                template = template_env.get_template('templates/events/manage/sub/speakers.html')
                context = {'vstrEventID':vstrEventID,'thisSpeakerList':thisSpeakerList}
                self.response.write(template.render(context))

            elif vstrChoice == "2":
                vstrEventID = self.request.get('vstrEventID')

                findRequest = EventSponsors.query(EventSponsors.strEventID == vstrEventID)
                thisEventSponsorList = findRequest.fetch()

                template = template_env.get_template('templates/events/manage/sub/sponsors.html')
                context = {'vstrEventID':vstrEventID,'thisEventSponsorList':thisEventSponsorList}
                self.response.write(template.render(context))

            elif vstrChoice == "3":
                vstrEventID = self.request.get('vstrEventID')

                findRequest = EventExhibitors.query(EventExhibitors.strEventID == vstrEventID)
                thisExhibitorsList = findRequest.fetch()

                template  = template_env.get_template('templates/events/manage/sub/exhibitors.html')
                context = {'vstrEventID':vstrEventID,'thisExhibitorsList':thisExhibitorsList}
                self.response.write(template.render(context))

            elif vstrChoice == "4":
                vstrEventID = self.request.get('vstrEventID')

                findRequest = EventAgendas.query(EventAgendas.strEventID == vstrEventID)
                thisAgendaList = findRequest.fetch()

                findRequest = Speakers.query(Speakers.strEventID == vstrEventID)
                thisSpeakerList = findRequest.fetch()

                template = template_env.get_template('templates/events/manage/agenda/agenda.html')
                context = {'vstrEventID':vstrEventID,'thisAgendaList':thisAgendaList,'thisSpeakerList':thisSpeakerList}
                self.response.write(template.render(context))


class EventManagerHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()

        if Guser:
            #TODO-Correct this , it must load all the events from the same church or organization

            findRequest  = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisAdminList = findRequest.fetch()

            if len(thisAdminList) > 0:
                ThisAdmin = thisAdminList[0]
            else:
                ThisAdmin = ChurchMember()


            findRequest = Event.query(Event.strChurchID == ThisAdmin.strChurchID)
            thisEventList = findRequest.fetch()

            template = template_env.get_template('templates/events/sub/subManage.html')
            context = {'thisEventList': thisEventList}
            self.response.write(template.render(context))
        else:
            self.response.write("Please Login in order to manage your events...")

    def post(self):
        Guser = users.get_current_user()

        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                findRequest = Event.query(Event.strCreatorID == Guser.user_id())
                thisEventList = findRequest.fetch()

                template = template_env.get_template('templates/events/sub/myevents.html')
                context = {'thisEventList': thisEventList}
                self.response.write(template.render(context))
        else:
            pass




class ThisRegisteredHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Attendee Registrations... ")

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrEventID = self.request.get('vstrEventID')
                vstrNames = self.request.get('vstrNames')
                vstrSurname = self.request.get('vstrSurname')
                vstrCell = self.request.get('vstrCell')
                vstrTel = self.request.get('vstrTel')
                vstrEmail = self.request.get('vstrEmail')

                findRequest = EventRegistrations.query(EventRegistrations.strCell == vstrCell,EventRegistrations.strEventID == vstrEventID)
                thisEventRegistrationList = findRequest.fetch()

                if len(thisEventRegistrationList) > 0:
                    thisRegistration = thisEventRegistrationList[0]
                else:
                    thisRegistration = EventRegistrations()


                strthisDate = datetime.datetime.now()
                thisDate = strthisDate.date()
                thisTime = strthisDate.time()
                thisRegistration.writeEventID(strinput=vstrEventID)
                thisRegistration.writeNames(strinput=vstrNames)
                thisRegistration.writeSurname(strinput=vstrSurname)
                thisRegistration.writeCell(strinput=vstrCell)
                thisRegistration.writeTel(strinput=vstrTel)
                thisRegistration.writeEmail(strinput=vstrEmail)
                thisRegistration.writeDateRegistered(strinput=thisDate)
                thisRegistration.writeTimeRegistered(strinput=thisTime)
                thisRegistration.writeSMSCode(strinput=thisRegistration.CreateSMSCode())
                thisRegistration.writeVerificationCode(strinput=thisRegistration.CreateVerificationCode())
                thisRegistration.put()

                self.response.write("Attendee successfully registered for the event an Email or SMS Message will be sent to the Attendee for Verification")

            elif vstrChoice == "1":
                vstrEventID = self.request.get('vstrEventID')
                vstrNames = self.request.get('vstrNames')
                vstrSurname = self.request.get('vstrSurname')
                vstrCell = self.request.get('vstrCell')
                vstrTel = self.request.get('vstrTel')
                vstrEmail = self.request.get('vstrEmail')

                findRequest = Speakers.query(Speakers.strCell == vstrCell,Speakers.strEventID == vstrEventID)
                thisSpeakerList = findRequest.fetch()

                if len(thisSpeakerList) > 0:
                    thisSpeaker = thisSpeakerList[0]
                else:
                    thisSpeaker = Speakers()

                thisSpeaker.writeEventID(strinput=vstrEventID)
                thisSpeaker.writeNames(strinput=vstrNames)
                thisSpeaker.writeSurname(strinput=vstrSurname)
                thisSpeaker.writeCell(strinput=vstrCell)
                thisSpeaker.writeTel(strinput=vstrTel)
                thisSpeaker.writeEmail(strinput=vstrEmail)

                strthisDate = datetime.datetime.now()

                thisDate = strthisDate.date()
                thisTime = strthisDate.time()

                thisSpeaker.writeDateRegistered(strinput=thisDate)
                thisSpeaker.writeTimeRegistered(strinput=thisTime)

                thisSpeaker.writeSMSCode(strinput=thisSpeaker.CreateSMSCode())
                thisSpeaker.writeVerificationCode(strinput=thisSpeaker.CreateVerificationCode())
                thisSpeaker.writeSpeakerID(strinput=thisSpeaker.CreatSpeakerID())

                thisSpeaker.put()

                self.response.write("Speaker successfully registered for the event an Email or SMS Message will be sent for Verification...")

            elif vstrChoice == "2":
                vstrEventID = self.request.get('vstrEventID')
                vstrNames = self.request.get('vstrNames')
                vstrSurname = self.request.get('vstrSurname')
                vstrCell = self.request.get('vstrCell')
                vstrTel = self.request.get('vstrTel')
                vstrEmail = self.request.get('vstrEmail')

                findRequest = EventSponsors.query(EventSponsors.strEventID == vstrEventID,EventSponsors.strCell == vstrCell)
                thisSponsorList = findRequest.fetch()

                if len(thisSponsorList) > 0:
                    thisSponsor = thisSponsorList[0]
                else:
                    thisSponsor = EventSponsors()

                thisSponsor.writeEventID(strinput=vstrEventID)
                thisSponsor.writeNames(strinput=vstrNames)
                thisSponsor.writeSurname(strinput=vstrSurname)
                thisSponsor.writeCell(strinput=vstrCell)
                thisSponsor.writeTel(strinput=vstrTel)
                thisSponsor.writeEmail(strinput=vstrEmail)
                strthisDate = datetime.datetime.now()
                thisDate = strthisDate.date()
                thisTime = strthisDate.time()
                thisSponsor.writeDateRegistered(strinput=thisDate)
                thisSponsor.writeTimeRegistered(strinput=thisTime)
                thisSponsor.writeSMSCode(strinput=thisSponsor.CreateSMSCode())
                thisSponsor.writeVerificationCode(strinput=thisSponsor.CreateVerificationCode())

                thisSponsor.put()

                self.response.write("Sponsor successfully registered for the event an Email or SMS will be sent for Sponsor Verification...")

            elif vstrChoice == "3":
                vstrEventID = self.request.get('vstrEventID')
                vstrNames = self.request.get('vstrNames')
                vstrSurname = self.request.get('vstrSurname')
                vstrCell = self.request.get('vstrCell')
                vstrTel = self.request.get('vstrTel')
                vstrEmail = self.request.get('vstrEmail')

                findRequest = EventExhibitors.query(EventExhibitors.strEventID == vstrEventID, EventExhibitors.strCell == vstrCell)
                thisExhibitorsList = findRequest.fetch()

                if len(thisExhibitorsList) > 0:
                    thisExhibitor = thisExhibitorsList[0]
                else:
                    thisExhibitor = EventExhibitors()

                thisExhibitor.writeEventID(strinput=vstrEventID)
                thisExhibitor.writeNames(strinput=vstrNames)
                thisExhibitor.writeSurname(strinput=vstrSurname)
                thisExhibitor.writeCell(strinput=vstrCell)
                thisExhibitor.writeTel(strinput=vstrTel)
                thisExhibitor.writeEmail(strinput=vstrEmail)
                strthisDate = datetime.datetime.now()
                thisDate = strthisDate.date()
                thisTime = strthisDate.time()
                thisExhibitor.writeDateRegistered(strinput=thisDate)
                thisExhibitor.writeTimeRegistered(strinput=thisTime)
                thisExhibitor.writeSMSCode(strinput=thisExhibitor.CreateSMSCode())
                thisExhibitor.writeVerificationCode(strinput=thisExhibitor.CreateVerificationCode())
                thisExhibitor.put()

                self.response.write("Event Exhibitor successfully registered for the event an Email or SMS will be sent for Exhibitor Verification...")

            elif vstrChoice == "4":
                vstrEventID = self.request.get('vstrEventID')
                vstrTitle = self.request.get('vstrTitle')
                vstrAgendaDescription = self.request.get('vstrAgendaDescription')
                vstrSpeaker = self.request.get('vstrSpeaker')
                vstrStartDate = self.request.get('vstrStartDate')
                vstrStartTime = self.request.get('vstrStartTime')
                vstrEndDate = self.request.get('vstrEndDate')
                vstrEndTime = self.request.get('vstrEndTime')
                vstrStartTimeList = vstrStartTime.split(" ")
                strStartTime = vstrStartTimeList[0]
                strStartTime = strStartTime.strip()
                vstrAMPM = vstrStartTimeList[1]
                vstrAMPM = vstrAMPM.strip()

                strStartTimeList = strStartTime.split(":")
                if vstrAMPM == "AM":
                    strStartHour = int(strStartTimeList[0])
                else:
                    strStartHour = int(strStartTimeList[0]) + 12

                strStartMinute = int(strStartTimeList[1])
                strStartTime = datetime.time(hour=strStartHour,minute=strStartMinute,second=0)

                vstrEndTimeList = vstrEndTime.split(" ")
                strEndTime = vstrEndTimeList[0]
                strEndTime = strEndTime.strip()
                strAMPM = vstrEndTimeList[1]
                strAMPM = strAMPM.strip()


                strEndTimeList = strEndTime.split(":")
                if strAMPM == "AM":
                    strEndHour = int(strEndTimeList[0])
                else:
                    strEndHour = int(strEndTimeList[0]) + 12

                strEndMinute = int(strEndTimeList[0])
                strEndTime = datetime.time(hour=strEndHour,minute=strEndMinute,second=0)



                vstrStartDateList = vstrStartDate.split("/")
                strStartDate = datetime.date(year=int(vstrStartDateList[2]),month=int(vstrStartDateList[0]),day=int(vstrStartDateList[1]))

                vstrEndDateList = vstrEndDate.split("/")
                strEndDate = datetime.date(year=int(vstrEndDateList[2]),month=int(vstrEndDateList[0]),day=int(vstrEndDateList[1]))

                findRequest = EventAgendas.query(EventAgendas.strEventID  == vstrEventID,EventAgendas.strAgendaTitle == vstrTitle)
                thisAgendaList = findRequest.fetch()

                if len(thisAgendaList) > 0:
                    thisAgenda = thisAgendaList[0]
                else:
                    thisAgenda = EventAgendas()

                thisAgenda.writeSpeakerID(strinput=vstrSpeaker)
                thisAgenda.writeEventID(strinput=vstrEventID)
                thisAgenda.writeAgendaDescription(strinput=vstrAgendaDescription)
                thisAgenda.writeStartDate(strinput=strStartDate)
                thisAgenda.writeStartTime(strinput=strStartTime)
                thisAgenda.writeEndDate(strinput=strEndDate)
                thisAgenda.writeEndTime(strinput=strEndTime)
                thisAgenda.put()
                self.response.write("Event Agenda Successfully updated")


app = webapp2.WSGIApplication([
    ('/events', EventsHandler),
    ('/events/public/.*', ThisPublicEventHandler),
    ('/events/surveys/.*', ThisSurveyHandler),
    ('/events/manager', EventManagerHandler),
    ('/events/manager/.*', ThisManagerHandler),
    ('/events/registrations/.*', ThisRegisteredHandler)

], debug=True)
