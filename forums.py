


import os
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
import logging
import datetime
from datetime import timedelta
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

#TODO- improve the forums especially the interface and functionality
#TODO-
class ForumKeys(ndb.Expando):
    strOwnerID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strForumID = ndb.StringProperty()
    strForumType = ndb.StringProperty(default="Public") # Private
    strForumName = ndb.StringProperty()
    strForumDescription = ndb.StringProperty()
    strPage = ndb.StringProperty()
    strForumStatus = ndb.StringProperty(default="Active") # Closed
    strForumSubscriptionStatus = ndb.StringProperty(default="Open") # Closed



    strSubscriptions = ndb.IntegerProperty(default=0)
    strLikes = ndb.IntegerProperty(default=0)
    strShares = ndb.IntegerProperty(default=0)

    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()


    def writeDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDate = strinput
                return True
            else:
                return False
        except:
            return False



    def writeOwnerID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOwnerID = strinput
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
    def writeForumID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strForumID = strinput
                return True
            else:
                return False

        except:
            return False
    def writeForumType(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ['Public','Private']:
                self.strForumType = strinput
                return True
            else:
                return False
        except:
            return False
    def writeForumName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strForumName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeForumDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strForumDescription = strinput
                return True
            else:
                return False
        except:
            return False

    def writeForumPage (self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPage = strinput
                return True
            else:
                return False
        except:
            return False


    def writeForumStatus(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ['Active','Closed']:
                self.strForumStatus = strinput
                return True
            else:
                return False

        except:
            return False
    def writeForumSubscriptionStatus(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ['Open','Closed']:
                self.strForumSubscriptionStatus = strinput
                return True
            else:
                return False
        except:
            return False
    def createForumID(self):
        import random,string
        try:
            strForumID = ""
            for i in range(256):
                strForumID += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strForumID
        except:
            return None


    def writeTime(self,strinput):
        try:
            if strinput is not None:
                self.strTime = strinput
                return True
            else:
                return False
        except:
            return False

class ForumSEO(ndb.Expando):
    strForumID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strForumTitle = ndb.StringProperty()
    strSEOTitle = ndb.StringProperty()
    strForumSEODescription = ndb.StringProperty()


    strGoogleWebmasterMetaTag = ndb.StringProperty()
    strYahooWebmasterMetaTag = ndb.StringProperty()

    def writeForumID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strForumID = strinput
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
    def writeForumTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strForumTitle = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSEOTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSEOTitle = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSEODescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strForumSEODescription = strinput
                return True
            else:
                return False
        except:
            return False
    def writeGoogleWebmasterMetaTag(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strGoogleWebmasterMetaTag = strinput
                return True
            else:
                return False
        except:
            return False
    def writeYahooWebmasterMetaTag(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strYahooWebmasterMetaTag = strinput
                return True
            else:
                return False
        except:
            return False

class Topic(ndb.Expando):
    strForumID = ndb.StringProperty()
    strTopicID = ndb.StringProperty()
    strTopicName = ndb.StringProperty()
    strTopicDescription = ndb.StringProperty()
    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()
    strEnableSEO = ndb.BooleanProperty()
    strLikes = ndb.IntegerProperty(default=0)
    strShares = ndb.IntegerProperty(default=0)
    strSubscribers = ndb.IntegerProperty(default=0)


    def writeForumID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strForumID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTopicID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTopicID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTopicName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTopicName = strinput
                return True
            else:
                return False

        except:
            return False
    def writeTopicDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTopicDescription = strinput
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
    def writeTime(self,strinput):
        try:
            if strinput is not None:
                self.strTime = strinput
                return True
            else:
                return False
        except:
            return False
    def createTopicID(self):
        import random,string
        try:
            strTopicID = ""
            for i in range(128):
                strTopicID += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strTopicID
        except:
            return None
    def writeEnableSEO(self,strinput):
        try:
            if strinput in [True,False]:
                self.strEnableSEO = strinput
                return True
            else:
                return False
        except:
            return False

    def AddLikes(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strLikes += int(strinput)
                return True
            else:
                return False
        except:
            return False

    def AddShares(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strShares += int(strinput)
                return True
            else:
                return False
        except:
            return False

class Articles(ndb.Expando):
    strUserID = ndb.StringProperty()
    strTopicID = ndb.StringProperty()
    strThreadID = ndb.StringProperty()
    strArticleIntro = ndb.StringProperty()
    strArticleTitle = ndb.StringProperty()
    strArticle = ndb.StringProperty()
    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()


    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTopicID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTopicID = strinput
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
    def writeArticle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strArticle = strinput
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

    def writeTime(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTime = strinput
                return True
            else:
                return False
        except:
            return False
    def createThreadID(self):
        import random,string
        try:
            strThreadID = ""
            for i in range(128):
                strThreadID += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            return strThreadID
        except:
            return None

class ForumSubscriptions(ndb.Expando):
    strUserID = ndb.StringProperty()
    strForumID = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strSubscribed = ndb.BooleanProperty(default=False)
    strVerified = ndb.BooleanProperty(default=False)

    def writeUserID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUserID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeForumID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strForumID = strinput
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
                self.strSurname = str(strinput)
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
    def writeSubscribed(self,strinput):
        try:

            if strinput in [True,False]:
                self.strSubscribed = strinput
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

class ForumsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from church import ChurchMember
        if Guser:

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
                    thisChurchMember = ChurchMember()

            findRequest = ForumKeys.query(ForumKeys.strChurchID == thisChurchMember.strChurchID)
            thisMyChurchForumsList = findRequest.fetch()

            thisDate = datetime.datetime.now()
            thisRecentDate = thisDate - timedelta(days=5)

            findRequest = ForumKeys.query(ForumKeys.strDate >= thisRecentDate)
            thisLatestForumsList = findRequest.fetch(limit=5)

            findRequest = ForumKeys.query().order(ForumKeys.strLikes, ForumKeys.strShares)
            thisTrendingForumsList = findRequest.fetch()

            template = template_env.get_template('templates/forums/forums.html')
            context = {'thisMyChurchForumsList':thisMyChurchForumsList,'thisLatestForumsList':thisLatestForumsList,'thisTrendingForumsList':thisTrendingForumsList}
            self.response.write(template.render(context))

        else:
            template = template_env.get_template('templates/forums/forums.html')
            context = {}
            self.response.write(template.render(context))


    def post(self):
        Guser = users.get_current_user()

        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                findRequest = ForumKeys.query(ForumKeys.strForumType == "Public")
                thisForumList = findRequest.fetch()

                template = template_env.get_template('templates/forums/sub/public.html')
                context = {'thisForumList':thisForumList}
                self.response.write(template.render(context))

class PublicHandler(webapp2.RequestHandler):
    def get(self):
        vstrChoice  = self.request.get('vstrChoice')

    def post(self):
        from church import ChurchMember
        vstrChoice  = self.request.get('vstrChoice')

        if vstrChoice == "0":

            vstrForumName = self.request.get('vstrForumName')
            vstrForumDescription = self.request.get('vstrForumDescription')
            vstrForumLandingPage = self.request.get('vstrForumLandingPage')

            Guser = users.get_current_user()

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
                    thisChurchMember = ChurchMember()

            findRequest = ForumKeys.query(ForumKeys.strForumName == vstrForumName,ForumKeys.strChurchID == thisChurchMember.strChurchID )
            thisForumList = findRequest.fetch()

            if len(thisForumList) > 0:
                thisForum = thisForumList[0]
            else:
                thisForum = ForumKeys()
                thisForum.writeForumID(strinput=thisForum.createForumID())

            strThisDate = datetime.datetime.now()
            thisDate = strThisDate.date()
            thisTime = strThisDate.time()
            thisForum.writeTime(strinput=thisTime)
            thisForum.writeDate(strinput=thisDate)
            thisForum.writeChurchBranchID(strinput=thisChurchMember.strChurchBranchID)
            thisForum.writeChurchID(strinput=thisChurchMember.strChurchID)
            thisForum.writeForumName(strinput=vstrForumName)
            thisForum.writeForumDescription(strinput=vstrForumDescription)
            thisForum.writeForumPage(strinput=vstrForumLandingPage)
            thisForum.writeForumStatus(strinput="Active")
            thisForum.writeForumType(strinput="Public")
            thisForum.writeOwnerID(strinput=thisChurchMember.strMemberID)
            thisForum.writeForumSubscriptionStatus(strinput="Open")
            thisForum.put()

            self.response.write("Forum Successfully created")



        elif vstrChoice == "1":
            vstrForumID = self.request.get('vstrForumID')

            findRequest = ForumKeys.query(ForumKeys.strForumID == vstrForumID)
            thisForumList = findRequest.fetch()

            findRequest = Topic.query(Topic.strForumID == vstrForumID)
            thisTopicsList = findRequest.fetch()

            template = template_env.get_template('templates/forums/sub/topics.html')
            context = {'thisTopicsList':thisTopicsList}
            self.response.write(template.render(context))

        elif vstrChoice == "2":
            vstrForumID = self.request.get('vstrForumID')
            vstrTopicName = self.request.get('vstrTopicName')
            vstrTopicDescription = self.request.get('vstrTopicDescription')


            findRequest = Topic.query(Topic.strForumID == vstrForumID,Topic.strTopicName == vstrTopicName)
            thisTopicsList = findRequest.fetch()

            if len(thisTopicsList) > 0:
                thisTopic = thisTopicsList[0]
            else:
                thisTopic = Topic()
                thisTopic.writeTopicID(strinput=thisTopic.createTopicID())

            thisTopic.writeTopicName(strinput=vstrTopicName)
            thisTopic.writeForumID(strinput=vstrForumID)
            thisTopic.writeTopicDescription(strinput=vstrTopicDescription)
            strthisDate = datetime.datetime.now()
            thisDate = strthisDate.date()
            thisTime = strthisDate.time()


            thisTopic.writeDate(strinput=thisDate)
            thisTopic.writeTime(strinput=thisTime)
            thisTopic.put()

            self.response.write("Topic successfully uploaded")

        elif vstrChoice == "3":
            vstrForumID = self.request.get('vstrForumID')

            findRequest = ForumKeys.query(ForumKeys.strForumID == vstrForumID)
            thisForumList = findRequest.fetch()
            Guser = users.get_current_user()

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
                    thisChurchMember = ChurchMember()

            findRequest = ForumSubscriptions.query(ForumSubscriptions.strForumID == vstrForumID,ForumSubscriptions.strUserID == thisChurchMember.strMemberID)
            thisSubscriptionList = findRequest.fetch()
            if len(thisSubscriptionList) > 0:
                thisSubscription = thisSubscriptionList[0]
            else:
                thisSubscription = ForumSubscriptions()

            template = template_env.get_template('templates/forums/sub/subscribe.html')
            context = {'thisSubscription':thisSubscription}
            self.response.write(template.render(context))


        elif vstrChoice == "4":
            vstrForumID = self.request.get('vstrForumID')
            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrCell = self.request.get('vstrCell')
            vstrEmail = self.request.get('vstrEmail')

            findRequest = ForumSubscriptions.query(ForumSubscriptions.strForumID == vstrForumID)
            thisSubscriptionList = findRequest.fetch()

            if len(thisSubscriptionList) > 0:
                thisSubscription = thisSubscriptionList[0]
            else:
                thisSubscription = ForumSubscriptions()

            Guser = users.get_current_user()

            thisSubscription.writeForumID(strinput=vstrForumID)
            thisSubscription.writeUserID(strinput=Guser.user_id)
            thisSubscription.writeNames(strinput=vstrNames)
            thisSubscription.writeSurname(strinput=vstrSurname)
            thisSubscription.writeCell(strinput=vstrCell)
            thisSubscription.writeEmail(strinput=vstrEmail)

            thisSubscription.put()

            self.response.write("Subscriptions are done...")

        elif vstrChoice == "5":
            pass
        elif vstrChoice == "6":
            vstrForumID  = self.request.get('vstrForumID')
            vstrTopicID = self.request.get('vstrTopicID')

            findRequest = Topic.query(Topic.strTopicID == vstrTopicID)
            thisTopicList = findRequest.fetch()

            if len(thisTopicList) > 0:
                thisTopic = thisTopicList[0]
            else:
                thisTopic = Topic()

            findRequest = ForumKeys.query(ForumKeys.strForumID == vstrForumID)
            thisForumList = findRequest.fetch()

            if len(thisForumList) > 0:
                thisForum = thisForumList[0]
            else:
                thisForum = ForumKeys()

            template = template_env.get_template('templates/forums/sub/newarticle.html')
            context = {'thisTopic':thisTopic,'thisForum':thisForum}
            self.response.write(template.render(context))


class thisPublicHandler(webapp2.RequestHandler):
    def get(self):

        URL = self.request.url
        URLlist = URL.split("/")

        if len(URLlist) == 6:
            strForumID = URLlist[len(URLlist) - 1]

            findRequest = ForumKeys.query(ForumKeys.strForumID == strForumID)
            thisForumKeysList = findRequest.fetch()

            if len(thisForumKeysList) > 0:
                thisForum = thisForumKeysList[0]
            else:
                thisForum = ForumKeys()

            findRequest = ForumSEO.query(ForumSEO.strForumID == strForumID)
            thisForumSEO = findRequest.fetch()

            findRequest = Topic.query(Topic.strForumID == strForumID)
            thisTopicList = findRequest.fetch()




            template = template_env.get_template('templates/forums/sub/forum.html')
            context = {'thisForum':thisForum,'thisForumSEO':thisForumSEO,'thisTopicList':thisTopicList}
            self.response.write(template.render(context))

        elif len(URLlist) == 7:

            strForumID = URLlist[len(URLlist) - 2]
            strTopicID = URLlist[len(URLlist) - 1]

            findRequest = ForumKeys.query(ForumKeys.strForumID == strForumID)
            thisForumKeysList = findRequest.fetch()

            if len(thisForumKeysList) > 0:
                thisForum = thisForumKeysList[0]
            else:
                thisForum = ForumKeys()


            findRequest = ForumSEO.query(ForumSEO.strForumID == strForumID)
            thisForumSEOList = findRequest.fetch()


            if len(thisForumSEOList) > 0:
                thisForumSEO = thisForumSEOList[0]
            else:
                thisForumSEO = ForumSEO()

            findRequest = Topic.query(Topic.strTopicID == strTopicID)
            thisTopicList = findRequest.fetch()


            if len(thisTopicList) > 0:
                thisTopic = thisTopicList[0]
            else:
                thisTopic = Topic()


            findRequest = Articles.query(Articles.strTopicID == strTopicID)
            ArticleList = findRequest.fetch()

            if len(ArticleList) > 0:
                thisArticle = ArticleList[0]
            else:
                thisArticle = Articles()


            template = template_env.get_template('templates/forums/topics/thistopic.html')
            context = {'thisForum':thisForum,'thisTopic':thisTopic,'thisForumSEO':thisForumSEO,'ArticleList':ArticleList,
                       'thisArticle':thisArticle}
            self.response.write(template.render(context))


class thisTopicHandler(webapp2.RequestHandler):
    def get(self):

        URL = self.request.url
        URLlist = URL.split("/")
        strTopicID = URLlist[len(URLlist) - 1]

        findRequest = Topic.query(Topic.strTopicID == strTopicID)
        thisTopicList = findRequest.fetch()

        if len(thisTopicList) > 0:
            thisTopic = thisTopicList[0]
        else:
            thisTopic = Topic()


        template = template_env.get_template('templates/forums/topics/browsetopic.html')
        context = {'thisTopic':thisTopic}
        self.response.write(template.render(context))






app = webapp2.WSGIApplication([
    ('/forums', ForumsHandler),
    ('/forums/public', PublicHandler),
    ('/forums/public/.*', thisPublicHandler),
    ('/forums/topic/.*', thisTopicHandler)

], debug=True)