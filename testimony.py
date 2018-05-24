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


class Testimony(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()


    strDate = ndb.DateProperty()

    strOccasion = ndb.StringProperty()
    strTextTestament = ndb.StringProperty()
    strAudioTestament = ndb.BlobKeyProperty()
    strVideoTestament = ndb.BlobKeyProperty()

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
    def writeDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOccasion(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strOccasion = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTestament(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strTextTestament = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAudioTestament(self,strinput):
        try:
            if not(strinput == None):
                self.strAudioTestament = strinput
                return True
            else:
                return False
        except:
            return False
    def writeVideoTestament(self,strinput):
        try:

            if not(strinput == None):
                self.strVideoTestament = strinput
                return True
            else:
                return False
        except:
            return False




class TestimonyHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        if Guser:

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()


            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:

                findRequest = Testimony.query(Testimony.strChurchID == thisChurchMember.strChurchID,Testimony.strChurchBranchID == thisChurchMember.strChurchBranchID)
                thisTestimonyList = findRequest.fetch()

                template = template_env.get_template('templates/testimony/testimony.html')
                context = {'thisTestimonyList':thisTestimonyList}
                self.response.write(template.render(context))
            else:
                template = template_env.get_template('templates/subRestricted.html')
                context = {'thisChurchMember':thisChurchMember}
                self.response.write(template.render(context))





    def post(self):
        Guser = users.get_current_user()
        from church import ChurchMember,UserRights
        if Guser:
            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()


            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                vstrChoice = self.request.get('vstrChoice')

                if vstrChoice == "0":
                    vstrNames = self.request.get('vstrNames')
                    vstrSurname = self.request.get('vstrSurname')
                    vstrOccasion = self.request.get('vstrOccasion')
                    vstrTextTestament = self.request.get('vstrTextTestament')

                    thisTestament = Testimony()

                    thisTestament.writeChurchBranchID(strinput=thisChurchMember.strChurchBranchID)
                    thisTestament.writeChurchID(strinput=thisChurchMember.strChurchID)
                    thisTestament.writeNames(strinput=vstrNames)
                    thisTestament.writeSurname(strinput=vstrSurname)
                    thisTestament.writeOccasion(strinput=vstrOccasion)
                    thisTestament.writeTestament(strinput=vstrTextTestament)
                    thisTestament.put()

                    self.response.write("Testament successfully uploaded")








app = webapp2.WSGIApplication([
    ('/admin/testimony', TestimonyHandler),



], debug=True)

