
import os
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
import logging
import datetime
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
from church import MemberAddresses, ChurchMember
from userRights import UserRights





class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/about/about.html')
        context = {}
        self.response.write(template.render(context))





app = webapp2.WSGIApplication([
    ('/about', AboutHandler),

], debug=True)


