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
import datetime
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/splash.html')
        context = {}
        self.response.write(template.render(context))

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        from events import Event
        from forums import ForumKeys
        from newsletter import Letters
        from datetime import timedelta

        thisDate = datetime.datetime.now()
        thisDate = thisDate.date()
        thisLatestDate = thisDate - timedelta(days=90)
        findRequest = ForumKeys.query(ForumKeys.strForumType == "Public",ForumKeys.strDate >= thisLatestDate)
        thisLatestForumsList = findRequest.fetch(limit=10)
        findRequest = ForumKeys.query()
        thisForumsList = findRequest.fetch(limit=10)
        findRequest = Event.query(Event.strDateCreated  >= thisLatestDate)
        thisEventList = findRequest.fetch(limit=10)
        findRequest = Letters.query(Letters.strDateCreated >= thisLatestDate)
        thisLettersList = findRequest.fetch(limit=10)




        template = template_env.get_template('templates/index.html')
        context = {'thisEventList':thisEventList,'thisLatestForumsList':thisLatestForumsList,'thisForumsList':thisForumsList,'thisLettersList':thisLettersList}
        self.response.write(template.render(context))



app = webapp2.WSGIApplication([

    ('/', IndexHandler)
], debug=True)
