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

import webapp2
import jinja2
from google.appengine.api import users
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class AdminHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from church import Churches,ChurchMember,Branches
        if Guser:
            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()
            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = Churches.query(Churches.strChurchID == thisChurchMember.strChurchID)
            thisChurchList = findRequest.fetch()

            if len(thisChurchList) > 0:
                thisChurch = thisChurchList[0]
            else:
                thisChurch = Churches()

            findRequest = Branches.query(Branches.strChurchID == thisChurch.strChurchID)
            thisBranchesList = findRequest.fetch()

            vstrTotalBranches = str(len(thisBranchesList))

            findRequest = ChurchMember.query(ChurchMember.strChurchID == thisChurch.strChurchID)
            thisChurchMebersList = findRequest.fetch()

            vstrTotalChurchMembers = str(len(thisChurchMebersList))

            template = template_env.get_template('templates/admin.html')
            context = {'thisChurch':thisChurch,'thisChurchMember':thisChurchMember,'vstrTotalBranches':vstrTotalBranches,
                       'vstrTotalChurchMembers':vstrTotalChurchMembers}
            self.response.write(template.render(context))


app = webapp2.WSGIApplication([
    ('/admin', AdminHandler)

], debug=True)