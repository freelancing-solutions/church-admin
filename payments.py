import os

import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

from accounts import Accounts

strTransactionTypes = ['EFT','Cash','DirectDeposit','DebitOrder','CreditCard','PayPal']

class Transaction(ndb.Expando):
    strReference = ndb.StringProperty()
    strPaymentAmount = ndb.IntegerProperty()

    strDateOfPayment = ndb.DateProperty(auto_now_add=True)
    strTimeOfPayment = ndb.TimeProperty(auto_now_add=True)

    strPaymentMethod = ndb.StringProperty(default="EFT") # Cash, Direct Deposit, Debit Order, Credit Card , PayPal

    strTransactionVerified = ndb.StringProperty(default=False)

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strReference = strinput
                return True
            else:
                return False

        except:
            return False

    def writePaymentAmount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strPaymentAmount = strinput
                return True
            else:
                return False
        except:
            return False

    def writePaymentMethod(self,strinput):
        try:
            strinput = str(strinput)

            if strinput in strTransactionTypes:
                self.strPaymentMethod = strinput
                return True
            else:
                return False

        except:
            return False


    def setVerified(self,strinput):
        try:
            if strinput in [True,False]:
                self.strTransactionVerified = strinput
                return True
            else:
                return False
        except:
            return False


class AccountsPaymentsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = Transaction.query(Transaction.strReference == Guser.user_id())
            thisTransactionList = findRequest.fetch()

            template = template_env.get_template('templates/account/payments.html')
            context = {'thisTransactionList':thisTransactionList}
            self.response.write(template.render(context))


    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrPaymentMethod = self.request.get('vstrPaymentMethod').value

            if vstrPaymentMethod == "Cash":
                findRequest = Accounts.query(Accounts.strReference == Guser.user_id())
                thisAccountsList = findRequest.fetch()

                if len(thisAccountsList) > 0:
                    thisAccount = thisAccountsList[0]
                else:
                    thisAccount = Accounts()


app = webapp2.WSGIApplication([
    ('/accounts/payments', AccountsPaymentsHandler),

], debug=True)




