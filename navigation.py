import os
import webapp2
import jinja2

from google.appengine.api import users


import logging
#Jinja Loader

template_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.getcwd()))


class HeaderHandler(webapp2.RequestHandler):

    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrUsername = Guser.nickname()
            vstrLogoutURL = users.create_logout_url(dest_url="/")
            template = template_env.get_template('templates/dynamic/navigation/header.html')
            context = {'vstrUsername': vstrUsername, 'vstrLogoutURL': vstrLogoutURL}
            self.response.write(template.render(context))
        else:
            vstrLoginURL = users.create_login_url(dest_url="/")

            template = template_env.get_template('templates/dynamic/navigation/header.html')
            context = {'vstrLoginURL':vstrLoginURL}
            self.response.write(template.render(context))



class SideBarHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        vstrLogoutURL = users.create_logout_url(dest_url="/")
        vstrLoginURL = users.create_login_url(dest_url="/")

        if Guser:
            vstrUsername = Guser.nickname()
            template = template_env.get_template('templates/dynamic/navigation/sidebar.html')
            context = {'vstrUsername': vstrUsername,'vstrLogoutURL': vstrLogoutURL,}
            self.response.write(template.render(context))

        else:
            template = template_env.get_template('templates/dynamic/navigation/sidebar.html')
            context = {'vstrLoginURL': vstrLoginURL}
            self.response.write(template.render(context))

class FooterHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/dynamic/navigation/footer.html')
        context = {}
        self.response.write(template.render(context))






app = webapp2.WSGIApplication([
    ('/navigation/header', HeaderHandler),
    ('/navigation/sidebar', SideBarHandler),
    ('/navigation/footer', FooterHandler),
], debug=True)
