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
from google.appengine.api import users
import logging
import math
import datetime
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

sixtySixBooks = ["Genesis 50",
"Exodus 40",
"Leviticus 27",
"Numbers 36",
"Deuteronomy 34",
"Joshua 24",
"Judges 21",
"Ruth 4",
"1 samuel 31",
"2 samuel 24",
"1 kings 22",
"2 kings 25",
"1 Chronicles 29",
"2 Chronicles 36",
"Ezra 10",
"Nehemiah 13",
"Esther 10",
"Job 42",
"Psalms 150",
"Proverbs 31",
"Ecclesiastes 12",
"Song of Solomon 8",
"Isaiah 66",
"Jeremiah 52",
"Lamentations 5",
"Ezekiel 48",
"Daniel 12",
"Hosea 14",
"Joel 3",
"Amos 9",
"Obadiah 1",
"Jonah 4",
"Micah 7",
"Nahum 3",
"Habakkuk 3",
"Zephaniah 3",
"Haggai 2",
"Zechariah 14",
"Malachi 4",
"Matthew 28",
"Mark 16",
"Luke 24",
"John 21",
"Acts 28",
"Romans 16",
"1 Corinthians 16",
"2 Corinthians 13",
"Galatians 6",
"Ephesians 6",
"Philippians 4",
"Colossians 4",
"1 Thessalonians 5",
"2 Thessalonians 3",
"1 Timothy 6",
"2 Timothy 4",
"Titus 3",
"Philemon 1",
"Hebrews 13",
"James 5",
"1 Peter 5",
"2 Peter 3",
"1 John 5",
"2 John 1",
"3 John 1",
"Jude 1",
"Revelation 22"]


#TODO Consider storing the whole bible using this class
class BibleVerses(ndb.Expando):
    strBookID = ndb.StringProperty()
    strBookNumber = ndb.StringProperty()
    strChapter = ndb.StringProperty()
    strBookName = ndb.StringProperty()
    strBookContents = ndb.StringProperty()


    def writeBookID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strBookID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBookNumber(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strBookNumber = strinput
                return True
            else:
                return False
        except:
            return False

    def writeChapter(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strChapter = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBookName(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strBookName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBookContents(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strBookContents = strinput
                return True
            else:
                return False

        except:
            return False


#TODO- Extend Sermons to include YOUTUBE extensions for video sermons, and also consider making it publish on the forums
class Sermons(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strTitle = ndb.StringProperty()
    strExcerpt = ndb.StringProperty()
    strSermon = ndb.StringProperty()
    strDateOfDelivery = ndb.DateProperty()


    def writeExcerpt(self,strinput):
        try:
            strinput = str(strinput)

            if not(strinput == None):
                strLimit = len(strinput)

                if strLimit > 256:
                    strExcerptLen = 256
                else:
                    strExcerptLen = strLimit
                #TODO- Actually cut the excetp at the excerpt length
                self.strExcerpt = strinput
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

    def writeSermon(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSermon = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateOfDelivery(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateOfDelivery = strinput
                return True
            else:
                return False
        except:
            return False



class SermonsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        if Guser:

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()


            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:


                newBookList = []
                for thisBook in sixtySixBooks:
                    strBookSplit = thisBook.split(" ")
                    if len(strBookSplit) == 2:
                        strBookName = strBookSplit[0]
                        strBookChapter = int(strBookSplit[1])
                        strBookNumber = 0
                    elif len(strBookSplit) == 3:
                        strBookName = strBookSplit[1]
                        strBookChapter = int(strBookSplit[2])
                        strBookNumber = int(strBookSplit[0])
                        # Song of Solomon 8
                    else:
                        strBookName = "Song of Solomon"
                        strBookChapter = 8
                        strBookNumber = 0


                    for i in range(strBookChapter):
                        if strBookNumber == 0:
                            strBook = strBookName + " " + str(i+1)
                        else:
                            strBook = str(strBookNumber) + " " + strBookName + " " +str(i+1)

                        newBookList.append(strBook)

                findRequest = Sermons.query(Sermons.strChurchID == thisChurchMember.strChurchID,Sermons.strChurchBranchID == thisChurchMember.strChurchBranchID)
                thisSermonsList = findRequest.fetch()

                logging.info("Sixty Six Books : " + str(len(newBookList)))

                template = template_env.get_template('templates/sermons/sermons.html')
                context = {"sixtySixBooks":newBookList,'thisSermonsList':thisSermonsList}
                self.response.write(template.render(context))

            else:
                template = template_env.get_template('templates/subRestricted.html')
                context = {'thisChurchMember':thisChurchMember}
                self.response.write(template.render(context))


    def post(self):
        Guser = users.get_current_user()
        from church import ChurchMember, Churches, UserRights
        if Guser:
            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()


            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                vstrTitle = self.request.get('vstrTitle')
                vstrSermon = self.request.get('vstrSermon')
                vstrDateDelivery = self.request.get('vstrDateDelivery')

                vstrDateList = vstrDateDelivery.split("-")
                vstrYear = vstrDateList[0]
                vstrMonth = vstrDateList[1]
                vstrDay = vstrDateList[2]

                vstrThisDate = datetime.date(year=int(vstrYear),month=int(vstrMonth),day=int(vstrDay))


                findRequest = Sermons.query(Sermons.strChurchID == thisChurchMember.strChurchID,Sermons.strChurchBranchID == thisChurchMember.strChurchBranchID,Sermons.strDateOfDelivery ==vstrThisDate)
                thisSermonsList = findRequest.fetch()

                if len(thisSermonsList) > 0:
                    thisSermon = thisSermonsList[0]

                else:
                    thisSermon = Sermons()
                thisSermon.writeMemberID(strinput=thisChurchMember.strMemberID)
                thisSermon.writeChurchID(strinput=thisChurchMember.strChurchID)
                thisSermon.writeChurchBranchID(strinput=thisChurchMember.strChurchBranchID)
                thisSermon.writeTitle(strinput=vstrTitle)
                thisSermon.writeSermon(strinput=vstrSermon)
                thisSermon.writeExcerpt(strinput=vstrSermon)
                thisSermon.writeDateOfDelivery(strinput=vstrThisDate)
                thisSermon.put()
                self.response.write("Successfully updated sermons")

            else:
                template = template_env.get_template('templates/subRestricted.html')
                context = {'thisChurchMember':thisChurchMember}
                self.response.write(template.render(context))




app = webapp2.WSGIApplication([
    ('/admin/sermons', SermonsHandler),


], debug=True)
