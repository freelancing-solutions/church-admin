__author__ = 'mashudu'
import os

import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
from church import MemberAddresses, ChurchMember
from userRights import UserRights
import datetime
from datetime import timedelta

class ProfilesHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisProfileList = findRequest.fetch()

            if len(thisProfileList) > 0:
                thisProfile = thisProfileList[0]
            else:
                thisProfile = ChurchMember()

            template = template_env.get_template('templates/profile/profiles.html')
            context = {'thisProfile':thisProfile}
            self.response.write(template.render(context))

app = webapp2.WSGIApplication([
    ('/profile', ProfilesHandler),

], debug=True)

