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
import datetime
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
from userRights import UserRights

class Monetary(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strDate = ndb.DateProperty()
    strTime = ndb.TimeProperty()
    strTransactionCode = ndb.StringProperty()


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
    def writeDate(self,strinput):
        try:

            if strinput != None:
                self.strDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTime(self,strinput):
        try:
            if strinput != None:
                self.strTime = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTransactionCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTransactionCode = strinput
                return True
            else:
                return False
        except:
            return False

class Pledge(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strTransactionCode = ndb.StringProperty()
    strPledgeAmount = ndb.IntegerProperty(default=0)

    strYear = ndb.StringProperty()
    strMonth = ndb.StringProperty()
    strDay = ndb.StringProperty()

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
    def writeTransactionCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTransactionCode = strinput
                return True
            else:
                return False
        except:
            return False
    def writePledgeAmount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strPledgeAmount = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeYear(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 2016 ) and (int(strinput) <= 2100):
                self.strYear = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonth(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 12):
                self.strMonth = strinput
                return True
            else:
                return False

        except:
            return False
    def writeDay(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 31):
                self.strDay = strinput
                return True
            else:
                return False
        except:
            return False

    def createTransactionCode(self):
        try:
            Guser = users.get_current_user()

            findRequest = Pledge.query()
            thisTCode = str(Guser.user_id()) + str(len(findRequest.fetch()))
            return thisTCode
        except:
            return None

class Donation(ndb.Expando):
    strDonatorID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strTransactionCode = ndb.StringProperty()
    strDonationAmount = ndb.IntegerProperty(default=0)

    strYear = ndb.StringProperty()
    strMonth = ndb.StringProperty()
    strDay = ndb.StringProperty()

    def writeDonatorID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDonatorID = strinput
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
    def writeTransactionID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTransactionCode = strinput
                return True
            else:
                return False

        except:
            return False
    def createTransactionID(self):
        import string,random
        try:
            strTransCode = ""
            for i in range(256):
                strTransCode += random.SystemRandom().choice(string.digits + string.ascii_lowercase)
            return strTransCode
        except:
            return None
    def writeDonationAmount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strDonationAmount = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeYear(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 2016) and (int(strinput) <= 2100):
                self.strYear = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDay(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 31):
                self.strDay = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonth(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 12):
                self.strMonth = strinput
                return True
            else:
                return False
        except:
            return False

class Donators(ndb.Expando):
    strDonatorID = ndb.StringProperty()

    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strIDNumber = ndb.StringProperty()

    strInstitutionName = ndb.StringProperty()

    strPhyStandNumber = ndb.StringProperty()
    strPhyStreetName = ndb.StringProperty()
    strPhyCityTown = ndb.StringProperty()
    strPhyProvince = ndb.StringProperty()
    strPhyCountry = ndb.StringProperty()
    strPhyPostalCode = ndb.StringProperty()

    strPosBoxNumber = ndb.StringProperty()
    strPosCityTown = ndb.StringProperty()
    strPosProvince = ndb.StringProperty()
    strPosCountry = ndb.StringProperty()
    strPosPostalCode = ndb.StringProperty()

    strTel = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebsite = ndb.StringProperty()


    def writeDonatorID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDonatorID = strinput
                return True
            else:
                return False
        except:
            return False
    def createDonatorID(self):
        try:
            findRequest = Donators.query()
            thisDonatorsList = findRequest.fetch()
            Guser = users.get_current_user()
            vstrUserID = Guser.user_id()
            vstrDonatorID = vstrUserID + str(len(thisDonatorsList))
            return vstrDonatorID
        except:
            return None

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
    def writeIDNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strIDNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeInstitutionName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strInstitutionName = strinput
                return True
            else:
                return False

        except:
            return False
    def writePhyStandNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPhyStandNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writePhyStreetName(self,strinput):
        try:

            strinput = str(strinput)
            if strinput != None:
                self.strPhyStreetName = strinput
                return True
            else:
                return False
        except:
            return False
    def writePhyCityTown(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPhyCityTown = strinput
                return True
            else:
                return False

        except:
            return False
    def writePhyProvince(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPhyProvince = strinput
                return True
            else:
                return False
        except:
            return False
    def writePhyCountry(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPhyCountry = strinput
                return True
            else:
                return False
        except:
            return False
    def writePhyPostalCode(self,strinput):
        try:

            strinput = str(strinput)
            if strinput != None:
                self.strPhyPostalCode = strinput
                return True
            else:
                return False
        except:
            return False
    def writePosBoxNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPosBoxNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writePosCityTown(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.strPosCityTown = strinput
                return True
            else:
                return False
        except:
            return False
    def writePosProvince(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPosProvince = strinput
                return True
            else:
                return False
        except:
            return False
    def writePosCountry(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPosCountry = strinput
                return True
            else:
                return False
        except:
            return False
    def writePosPostalCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPosPostalCode = strinput
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
    def writeWebsite(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strWebsite = strinput
                return True
            else:
                return False
        except:
            return False

class Tithing(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strTransactionCode = ndb.StringProperty()
    strTithingAmount = ndb.IntegerProperty(default=0)

    strYear = ndb.StringProperty()
    strMonth = ndb.StringProperty()
    strDay = ndb.StringProperty()

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

    def writeTransactionCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTransactionCode = strinput
                return True
            else:
                return False
        except:
            return False

    def createTransactionCode(self):
        try:
            Guser = users.get_current_user()
            findRequest = Tithing.query()
            strTCode = str(Guser.user_id()) + str(len(findRequest.fetch()))
            return strTCode
        except:
            return None

    def writeTithingAmount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTithingAmount = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeYear(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 2016) and (int(strinput) <= 2100):
                self.strYear = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMonth(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 12 ):
                self.strMonth = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDay(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 31):
                self.strDay = strinput
                return True
            else:
                return False
        except:
            return False

class Offerings(ndb.Expando):

    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strTransactionCode = ndb.StringProperty()
    strOfferingAmount = ndb.IntegerProperty(default=0)

    strYear = ndb.StringProperty()
    strMonth = ndb.StringProperty()
    strDay = ndb.StringProperty()

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
    def writeTransactionCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTransactionCode = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOfferingAmount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strOfferingAmount = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeYear(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 2016) and (int(strinput) <= 2100):
                self.strYear = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonth(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 12):
                self.strMonth = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDay(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 31):
                self.strDay = strinput
                return True
            else:
                return False
        except:
            return False
    def createTransactionCode(self):
        try:

            findRequest = Offerings.query()
            thisLenList = findRequest.fetch()
            strLen = len(thisLenList)
            Guser = users.get_current_user()
            strUserID = Guser.user_id()
            strTCode = str(strUserID) + str(strLen)
            return strTCode
        except:
            return None

class Costs(ndb.Expando):
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strYear = ndb.StringProperty()
    strMonth = ndb.StringProperty()
    strOfficeRentals = ndb.StringProperty()
    strBuildingMaintenance = ndb.StringProperty()
    strMunicipalCharges = ndb.StringProperty()
    strSalaries = ndb.StringProperty()
    strTelephone = ndb.StringProperty()
    strTransport = ndb.StringProperty()
    strStationery = ndb.StringProperty()
    strElectricity = ndb.StringProperty()
    strAdvertising = ndb.StringProperty()
    strInsurance = ndb.StringProperty()
    strOverHeads = ndb.StringProperty()
    strTotalCost = ndb.StringProperty()

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
    def writeChurchBrancID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChurchBranchID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeYear(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strYear = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonth(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and ((int(strinput) >= 0) and (int(strinput) <= 13)):
                self.strMonth = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOfficeRentals(self,strinput):
        try:

            strinput = str(strinput)
            if strinput != None:
                self.strOfficeRentals = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBuildingMaintenance(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.strBuildingMaintenance = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMunicipalCharges(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMunicipalCharges = strinput
                return True
            else:
                return False

        except:
            return False
    def writeSalaries(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strSalaries = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTelephone(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTelephone = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTransport(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTransport = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStationery(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strStationery = strinput
                return True
            else:
                return False
        except:
            return False
    def writeElectricity(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strElectricity = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAdvertising(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAdvertising = strinput
                return True
            else:
                return False
        except:
            return False
    def writeInsurance(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strInsurance = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOverHeads(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOverHeads = strinput
                return True
            else:
                return False
        except:
            return False

    def CalculateTotal(self):
        try:
            strTotal = 0
            if self.strOfficeRentals.isdigit():
                strTotal = strTotal + int(self.strOfficeRentals)
            if self.strBuildingMaintenance.isdigit():
                strTotal = strTotal + int(self.strBuildingMaintenance)
            if self.strMunicipalCharges.isdigit():
                strTotal = strTotal + int(self.strMunicipalCharges)
            if self.strSalaries.isdigit():
                strTotal = strTotal + int(self.strSalaries)
            if self.strTelephone.isdigit():
                strTotal = strTotal + int(self.strTelephone)
            if self.strTransport.isdigit():
                strTotal  = strTotal + int(self.strTransport)
            if self.strStationery.isdigit():
                strTotal = strTotal + int(self.strStationery)
            if self.strElectricity.isdigit():
                strTotal = strTotal + int(self.strElectricity)
            if self.strAdvertising.isdigit():
                strTotal = strTotal + int(self.strAdvertising)
            if self.strInsurance.isdigit():
                strTotal = strTotal + int(self.strInsurance)
            if self.strOverHeads.isdigit():
                strTotal = strTotal + int(self.strOverHeads)
            self.strTotalCost = str(strTotal)
            return self.strTotalCost
        except:
            return None

class PaymentsMade(ndb.Expando):
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strPaymentIndex = ndb.StringProperty() # Payment Index is the index of this payment

    strReference = ndb.StringProperty() # Reference of the person asking for Payment Authorisation

    strPaymentType = ndb.StringProperty(default="Cash") # EFT Bank Deposit Cheque
    strPaymentAmount = ndb.StringProperty()

    strReasonForPayment = ndb.StringProperty()

    strYear = ndb.StringProperty()
    strMonth = ndb.StringProperty()
    strDay = ndb.StringProperty()

    strTimeOfPayment = ndb.TimeProperty(auto_now_add=True)

    strAuthorised = ndb.BooleanProperty(default=False)
    strAuthorisedBy = ndb.StringProperty()
    strRejected = ndb.BooleanProperty(default=False)
    strRejectionReason = ndb.StringProperty()
    strPayFrom = ndb.StringProperty(default="Branch Account") # Church Account , Available Funds
    strPaidToClient = ndb.StringProperty() # Reference of the client who got paid with this transaction


    def writePayFrom(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPayFrom = strinput
                return True
            else:
                return False
        except:
            return False
    def writePaidToClient(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPaidToClient = strinput
                return True
            else:
                return False
        except:
            return False
    def writePaymentIndex(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPaymentIndex = strinput
                return True
            else:
                return False
        except:
            return False
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
    def writeReasonForPayment(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strReasonForPayment = strinput
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
    def writePaymentType(self,strinput):
        try:

            strinput = str(strinput)
            if strinput != None:
                self.strPaymentType = strinput
                return True
            else:
                return False
        except:
            return False
    def writePaymentAmount(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPaymentAmount = strinput
                return True
            else:
                return False
        except:
            return False
    def writeYear(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 2016) and (int(strinput) <= 2100):
                self.strYear = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonth(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 12):
                self.strMonth = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDay(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) <= 31) and (int(strinput) >= 1):
                self.strDay = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAuthorised(self,strinput):
        try:
            if strinput in [True,False]:
                self.strAuthorised = strinput
                return True
            else:
                return False
        except:
            return False
    def writeRejected(self,strinput):
        try:
            if strinput in [True,False]:
                self.strRejected = strinput
                return True
            else:
                return False
        except:
            return False
    def writeRejectedReason(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRejectionReason = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAuthorisedBy(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAuthorisedBy = strinput
                return True
            else:
                return False
        except:
            return False
    def writePaymentTime(self,strinput):
        try:
            if strinput is not None:
                self.strTimeOfPayment = strinput
                return True
            else:
                return False
        except:
            return False

class BenBank(ndb.Expando):
    strReference = ndb.StringProperty()
    strBeneficiaryIndex = ndb.StringProperty()

    strAccountHolder = ndb.StringProperty()
    strAccountNumber = ndb.StringProperty()
    strAccountType = ndb.StringProperty(default="Savings") # Cheque, Transmission
    strBankName = ndb.StringProperty()
    strBranchName = ndb.StringProperty()
    strBranchCode = ndb.StringProperty()
    strRoutingNumber = ndb.StringProperty()

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
    def writeBeneficiaryIndex(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBeneficiaryIndex = strinput
                return True
            else:
                return False

        except:
            return False
    def writeAccountHolder(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput) > 0:
                self.strAccountHolder = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccountNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccountType(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountType = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBankName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBankName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBranchName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBranchName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBranchCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBranchCode = strinput
                return True
            else:
                return False
        except:
            return False
    def writeRoutingNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRoutingNumber = strinput
                return True
            else:
                return False
        except:
            return False

class Beneficiary(ndb.Expando):
    """
        Receipient List
    """
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strBeneficiaryIndex = ndb.StringProperty() # Beneficiary index equate to strPaidToClient

    strReference = ndb.StringProperty() #

    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strIDNumber = ndb.StringProperty()

    strCompanyName = ndb.StringProperty()
    strCompanyReg = ndb.StringProperty()
    strCompanyVAT = ndb.StringProperty()


    strRecipientType = ndb.StringProperty(default="Supplier") # Client

    strNotes = ndb.StringProperty()


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
    def writeBeneficiaryIndex(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBeneficiaryIndex = strinput
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
    def writeCompanyName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCompanyName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCompanyReg(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCompanyReg = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCompanyVAT(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCompanyVAT = strinput
                return True
            else:
                return False
        except:
            return False
    def writeRecipientType(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRecipientType = strinput
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
    def writeIDNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strIDNumber = strinput
                return True
            else:
                return False

        except:
            return False
    def writeNotes(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNotes = strinput
                return True
            else:
                return False
        except:
            return False
    def createBeneficiaryIndex(self):
        try:
            findRequest = Beneficiary.query()
            thisBeneficiaryList = findRequest.fetch()
            Guser = users.get_current_user()
            strBenIndex = str(Guser.user_id()) + str(len(thisBeneficiaryList) + 1)
            return strBenIndex
        except:
            return None

class Bank(ndb.Expando):
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strTotalBalance = ndb.StringProperty()
    strFundsInBank = ndb.StringProperty()
    strFundsInBranch = ndb.StringProperty()

    strBankDeposits = ndb.StringProperty()
    strBankWithDrawals = ndb.StringProperty()


    strYear = ndb.StringProperty()
    strMonth = ndb.StringProperty()
    strDay = ndb.StringProperty()
    strTime = ndb.TimeProperty(auto_now_add=True)




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

    def writeTotalBalance(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTotalBalance = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFundsInBank(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFundsInBank = strinput
                return True
            else:
                return False

        except:
            return False

    def writeFundsInBranch(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFundsInBranch = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBankDeposits(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBankDeposits = strinput
                return True
            else:
                return False
        except:
            return False

    def writeBankWithDrawals(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBankWithDrawals = strinput
                return True
            else:
                return False
        except:
            return False

    def writeYear(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 2016) and (int(strinput) <= 2100):
                self.strYear = strinput
                return True
            else:
                return False

        except:
            return False

    def writeMonth(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1 ) and (int(strinput) <= 12):
                self.strMonth = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDay(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 31):
                self.strDay = strinput
                return True
            else:
                return False
        except:
            return False

class BankAccount(ndb.Expando):
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strAccountHolder = ndb.StringProperty()
    strAccountNumber = ndb.StringProperty()
    strAccountType = ndb.StringProperty(default="Checking")
    strBankName = ndb.StringProperty()
    strBranchName = ndb.StringProperty()
    strBranchCode = ndb.StringProperty()
    strRoutingNumber = ndb.StringProperty()

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
    def writeAccountHolder(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountHolder = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccountNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccountType(self,strinput):
        try:
            strinput = str(strinput)

            if strinput != None:
                self.strAccountType = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBankName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBankName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBranchName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBranchName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBranchCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBranchCode = strinput
                return True
            else:
                return False
        except:
            return False
    def writeRoutingNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRoutingNumber = strinput
                return True
            else:
                return False
        except:
            return False

class MonetaryMessaging(ndb.Expando):
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strMemberID = ndb.StringProperty()
    strMessage = ndb.StringProperty()
    strResponse = ndb.StringProperty()
    strRef = ndb.StringProperty()
    strDateSent = ndb.DateProperty()
    strTimeSent = ndb.TimeProperty()
    strDateResponse = ndb.DateProperty()
    strTimeResponse = ndb.TimeProperty()


    def writeChurchID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strChurchID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeChurchBranchID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strChurchBranchID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMemberID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strMemberID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMessage(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strMessage = strinput
                return True
            else:
                return False
        except:
            return False

    def writeResponse(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strResponse = strinput
                return True

            else:
                return False
        except:
            return False

    def writeRef(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strRef = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateSent(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.strDateSent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeSent(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.strTimeSent = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDateResponse(self, strinput):
        try:
            if isinstance(strinput, datetime.date):
                self.strDateResponse = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeResponse(self, strinput):
        try:
            if isinstance(strinput, datetime.time):
                self.strTimeResponse = strinput
                return True
            else:
                return False
        except:
            return False


class IncomeHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                vstrChurchID = self.request.get('vstrChurchID')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')

                findRequest = Pledge.query(Pledge.strChurchID == vstrChurchID,Pledge.strChurchBranchID == vstrChurchBranchID)
                thisPledgesList = findRequest.fetch()

                findRequest = Donation.query(Donation.strChurchID == vstrChurchID,Donation.strChurchBranchID == vstrChurchBranchID)
                thisDonationList = findRequest.fetch()

                findRequest = Donators.query(Donators.strChurchID == vstrChurchID,Donators.strChurchBranchID == vstrChurchBranchID)
                thisDonatorsList = findRequest.fetch()


                findRequest = Tithing.query(Tithing.strChurchID == vstrChurchID,Tithing.strChurchBranchID == vstrChurchBranchID)
                thisTithingList = findRequest.fetch()

                findRequest = Offerings.query(Offerings.strChurchID == vstrChurchID,Offerings.strChurchBranchID == vstrChurchBranchID)
                thisOfferingList = findRequest.fetch()


                template = template_env.get_template('templates/admin/churches/branches/income/income.html')
                context = {'thisPledgesList':thisPledgesList,'thisDonationList':thisDonationList,'thisTithingList':thisTithingList,'thisOfferingList':thisOfferingList,
                           'thisDonatorsList':thisDonatorsList,'vstrChurchID':vstrChurchID,'vstrChurchBranchID':vstrChurchBranchID}
                self.response.write(template.render(context))
            else:
                self.response.write("You are not authorised to view this section")
        else:
            pass

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrDateOffering = self.request.get('vstrDateOffering')
                vstrOfferingAmount = self.request.get('vstrOfferingAmount')
                vstrChurchID = self.request.get('vstrChurchID')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')

                try:
                    dateList = vstrDateOffering.split("-")
                    strYear = dateList[0]
                    strMonth = dateList[1]
                    strDay = dateList[2]
                except:
                    Today = datetime.datetime.now()
                    strYear = Today.year
                    strMonth = Today.month
                    strDay = Today.day

                thisOffering = Offerings()

                thisOffering.writeChurchID(strinput=vstrChurchID)
                thisOffering.writeChurchBranchID(strinput=vstrChurchBranchID)
                thisOffering.writeTransactionCode(strinput=thisOffering.createTransactionCode())
                if thisOffering.writeYear(strinput=str(strYear)) and thisOffering.writeMonth(strinput=str(strMonth)) and thisOffering.writeDay(strinput=str(strDay)):
                    pass
                else:
                    Today = datetime.datetime.now()
                    strYear = Today.year
                    strMonth = Today.month
                    strDay = Today.day
                    thisOffering.writeYear(strinput=str(strYear))
                    thisOffering.writeMonth(strinput=str(strMonth))
                    thisOffering.writeDay(strinput=str(strDay))
                thisOffering.writeOfferingAmount(strinput=vstrOfferingAmount)
                thisOffering.put()

                self.response.write("Offering successfully updated")













class DonatorsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRights = thisUserRightsList[0]
            else:
                thisUserRights = UserRights()

            if thisUserRights.strAdminUser or thisUserRights.strSuperUser:
                vstrChurchID = self.request.get('vstrChurchID')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')

                findRequest = Donators.query(Donators.strChurchID == vstrChurchID, Donators.strChurchBranchID == vstrChurchBranchID )
                thisDonatorsList = findRequest.fetch()

                template = template_env.get_template('templates/admin/churches/branches/income/donators.html')
                context = {'thisDonatorsList':thisDonatorsList,'vstrChurchID':vstrChurchID,'vstrChurchBranchID':vstrChurchBranchID}
                self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrIDNumber = self.request.get('vstrIDNumber')
            vstrInstitutionName = self.request.get('vstrInstitutionName')
            vstrPhyStandNumber = self.request.get('vstrPhyStandNumber')
            vstrPhyStreetName = self.request.get('vstrPhyStreetName')
            vstrPhyCityTown = self.request.get('vstrPhyCityTown')
            vstrPhyProvince = self.request.get('vstrPhyProvince')
            vstrPhyCountry = self.request.get('vstrPhyCountry')
            vstrPhyPostalCode = self.request.get('vstrPhyPostalCode')
            vstrPosBoxNumber = self.request.get('vstrPosBoxNumber')
            vstrPosCityTown = self.request.get('vstrPosCityTown')
            vstrPosProvince = self.request.get('vstrPosProvince')
            vstrPosCountry = self.request.get('vstrPosCountry')
            vstrPosPostalCode = self.request.get('vstrPosPostalCode')
            vstrTel = self.request.get('vstrTel')
            vstrCell = self.request.get('vstrCell')
            vstrEmail = self.request.get('vstrEmail')
            vstrWebsite = self.request.get('vstrWebsite')
            vstrChurchBranchID = self.request.get('vstrChurchBranchID')
            vstrChurchID = self.request.get('vstrChurchID')

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:
                findRequest = Donators.query(Donators.strChurchID == vstrChurchID, Donators.strChurchBranchID == vstrChurchBranchID)
                thisDonatorsList = findRequest.fetch()

                if len(thisDonatorsList) > 0:
                    thisDonator = thisDonatorsList[0]
                else:
                    thisDonator = Donators()

                thisDonator.writeChurchID(strinput=vstrChurchID)
                thisDonator.writeChurchBranchID(strinput=vstrChurchBranchID)
                thisDonator.writeNames(strinput=vstrNames)
                thisDonator.writeSurname(strinput=vstrSurname)
                thisDonator.writeIDNumber(strinput=vstrIDNumber)
                thisDonator.writeInstitutionName(strinput=vstrInstitutionName)
                thisDonator.writePhyStandNumber(strinput=vstrPhyStandNumber)
                thisDonator.writePhyStreetName(strinput=vstrPhyStreetName)
                thisDonator.writePhyCityTown(strinput=vstrPhyCityTown)
                thisDonator.writePhyProvince(strinput=vstrPhyProvince)
                thisDonator.writePhyCountry(strinput=vstrPhyCountry)
                thisDonator.writePhyPostalCode(strinput=vstrPhyPostalCode)
                thisDonator.writePosBoxNumber(strinput=vstrPosBoxNumber)
                thisDonator.writePosCityTown(strinput=vstrPosCityTown)
                thisDonator.writePosProvince(strinput=vstrPosProvince)
                thisDonator.writePosCountry(strinput=vstrPosCountry)
                thisDonator.writePosPostalCode(strinput=vstrPosPostalCode)
                thisDonator.writeTel(strinput=vstrTel)
                thisDonator.writeCell(strinput=vstrCell)
                thisDonator.writeEmail(strinput=vstrEmail)
                thisDonator.writeWebsite(strinput=vstrWebsite)
                thisDonator.writeDonatorID(strinput=thisDonator.createDonatorID())

                thisDonator.put()

                self.response.write("Donator successfully uploaded")



class CostsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChoice = self.request.get('vstrChoice')



            if vstrChoice == "0":
                vstrYear = self.request.get('vstrYear')
                vstrMonth = self.request.get('vstrMonth')
                vstrOfficeRentals = self.request.get('vstrOfficeRentals')
                vstrBuildingMaintenance = self.request.get('vstrBuildingMaintenance')
                vstrMunicipalCharges = self.request.get('vstrMunicipalCharges')
                vstrSalaries = self.request.get('vstrSalaries')
                vstrTelephone = self.request.get('vstrTelephone')
                vstrTransport = self.request.get('vstrTransport')
                vstrStationery = self.request.get('vstrStationery')
                vstrElectricity = self.request.get('vstrElectricity')
                vstrAdvertising = self.request.get('vstrAdvertising')
                vstrInsurance = self.request.get('vstrInsurance')
                vstrOverHeads = self.request.get('vstrOverHeads')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                vstrChurchID = self.request.get('vstrChurchID')

                findRequest = Costs.query(Costs.strChurchID == vstrChurchID, Costs.strChurchBranchID == vstrChurchBranchID,Costs.strYear == vstrYear, Costs.strMonth == vstrMonth)
                thisCostsList = findRequest.fetch()

                if len(thisCostsList) > 0:
                    self.response.write("Costs for year : " + vstrYear + " Month : " + vstrMonth + "  has already been entered please open costs history and rather edit your costs")
                else:
                    thisCost = Costs()
                    thisCost.writeYear(strinput=vstrYear)
                    thisCost.writeMonth(strinput=vstrMonth)
                    thisCost.writeOfficeRentals(strinput=vstrOfficeRentals)
                    thisCost.writeBuildingMaintenance(strinput=vstrBuildingMaintenance)
                    thisCost.writeMunicipalCharges(strinput=vstrMunicipalCharges)
                    thisCost.writeSalaries(strinput=vstrSalaries)
                    thisCost.writeTelephone(strinput=vstrTelephone)
                    thisCost.writeTransport(strinput=vstrTransport)
                    thisCost.writeStationery(strinput=vstrStationery)
                    thisCost.writeElectricity(strinput=vstrElectricity)
                    thisCost.writeAdvertising(strinput=vstrAdvertising)
                    thisCost.writeInsurance(strinput=vstrInsurance)
                    thisCost.writeOverHeads(strinput=vstrOverHeads)
                    thisCost.writeChurchBrancID(strinput=vstrChurchBranchID)
                    thisCost.writeChurchID(strinput=vstrChurchID)

                    thisCost.CalculateTotal()

                    thisCost.put()
                    self.response.write("Successfully updated costs")

            elif vstrChoice == "1":

                vstrYear = self.request.get('vstrYear')
                vstrMonth = self.request.get('vstrMonth')
                vstrOfficeRentals = self.request.get('vstrOfficeRentals')
                vstrBuildingMaintenance = self.request.get('vstrBuildingMaintenance')
                vstrMunicipalCharges = self.request.get('vstrMunicipalCharges')
                vstrSalaries = self.request.get('vstrSalaries')
                vstrTelephone = self.request.get('vstrTelephone')
                vstrTransport = self.request.get('vstrTransport')
                vstrStationery = self.request.get('vstrStationery')
                vstrElectricity = self.request.get('vstrElectricity')
                vstrAdvertising = self.request.get('vstrAdvertising')
                vstrInsurance = self.request.get('vstrInsurance')
                vstrOverHeads = self.request.get('vstrOverHeads')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                vstrChurchID = self.request.get('vstrChurchID')

                findRequest = Costs.query(Costs.strChurchID == vstrChurchID, Costs.strChurchBranchID == vstrChurchBranchID,Costs.strYear == vstrYear, Costs.strMonth == vstrMonth)
                thisCostsList = findRequest.fetch()

                if len(thisCostsList) > 0:
                    thisCost = thisCostsList[0]

                    thisCost.writeYear(strinput=vstrYear)
                    thisCost.writeMonth(strinput=vstrMonth)
                    thisCost.writeOfficeRentals(strinput=vstrOfficeRentals)
                    thisCost.writeBuildingMaintenance(strinput=vstrBuildingMaintenance)
                    thisCost.writeMunicipalCharges(strinput=vstrMunicipalCharges)
                    thisCost.writeSalaries(strinput=vstrSalaries)
                    thisCost.writeTelephone(strinput=vstrTelephone)
                    thisCost.writeTransport(strinput=vstrTransport)
                    thisCost.writeStationery(strinput=vstrStationery)
                    thisCost.writeElectricity(strinput=vstrElectricity)
                    thisCost.writeAdvertising(strinput=vstrAdvertising)
                    thisCost.writeInsurance(strinput=vstrInsurance)
                    thisCost.writeOverHeads(strinput=vstrOverHeads)
                    thisCost.writeChurchBrancID(strinput=vstrChurchBranchID)
                    thisCost.writeChurchID(strinput=vstrChurchID)

                    thisCost.CalculateTotal()

                    thisCost.put()
                    self.response.write("Successfully updated costs")


class thisCostHandler(webapp2.RequestHandler):
    def get(self):
        from church import ChurchMember
        Guser = users.get_current_user()
        from church import Churches, Branches
        if Guser:
            URL = self.request.url
            URLlist = URL.split("/")
            vstrYear = URLlist[len(URLlist) - 2]
            vstrMonth = URLlist[len(URLlist) - 1]

            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisAdminList = findRequest.fetch()

            if len(thisAdminList) > 0:
                thisAdmin = thisAdminList[0]
            else:
                thisAdmin = ChurchMember()

            findRequest = Costs.query(Costs.strChurchID == thisAdmin.strChurchID,Costs.strChurchBranchID == thisAdmin.strChurchBranchID,Costs.strYear == vstrYear,Costs.strMonth == vstrMonth)
            thisCostsList = findRequest.fetch()
            if len(thisCostsList) > 0:
                thisCost = thisCostsList[0]
            else:
                thisCost = Costs()

            thisCost.CalculateTotal()
            thisCost.put()

            findRequest = Churches.query(Churches.strChurchID == thisAdmin.strChurchID)
            thisChurchList = findRequest.fetch()

            if len(thisChurchList) > 0:
                thisChurch = thisChurchList[0]
            else:
                thisChurch = Churches()

            findRequest = Branches.query(Branches.strChurchBranchID == thisAdmin.strChurchBranchID)
            thisBranchesList = findRequest.fetch()

            if len(thisBranchesList) > 0:
                thisBranch = thisBranchesList[0]
            else:
                thisBranch = Branches()


            template = template_env.get_template('templates/admin/churches/branches/costs/thiscost.html')
            context = {'thisCost':thisCost,'thisAdmin':thisAdmin,'thisChurch':thisChurch,'thisBranch':thisBranch}
            self.response.write(template.render(context))

class AuthorizeHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from church import Churches, Branches, ChurchMember
        if Guser:

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisAdminList = findRequest.fetch()

            if len(thisAdminList) > 0:
                thisAdmin = thisAdminList[0]
            else:
                thisAdmin = UserRights()

            if thisAdmin.strAdminUser:
                URL = self.request.url
                URLlist = URL.split("/")
                vstrPaymentIndex = URLlist[len(URLlist) - 1]
                findRequest = PaymentsMade.query(PaymentsMade.strPaymentIndex == vstrPaymentIndex)
                thisAuthorizeList = findRequest.fetch()
                if len(thisAuthorizeList) > 0:
                    thisAuthorize = thisAuthorizeList[0]
                else:
                    thisAuthorize = PaymentsMade()

                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisAdminList = findRequest.fetch()

                if len(thisAdminList) > 0:
                    thisAdmin = thisAdminList[0]
                else:
                    thisAdmin = ChurchMember()

                findRequest = Churches.query(Churches.strChurchID == thisAdmin.strChurchID)
                thisChurchList = findRequest.fetch()

                if len(thisChurchList) > 0:
                    thisChurch = thisChurchList[0]
                else:
                    thisChurch = Churches()


                findRequest = Branches.query(Branches.strChurchID == thisAdmin.strChurchID)
                thisBranchList = findRequest.fetch()

                if len(thisBranchList) > 0:
                    thisBranch = thisBranchList[0]
                else:
                    thisBranch = Branches()

                findRequest = Beneficiary.query(Beneficiary.strBeneficiaryIndex == thisAuthorize.strPaidToClient)
                thisBeneficiaryList = findRequest.fetch()

                if len(thisBeneficiaryList) > 0:
                    thisBeneficiary = thisBeneficiaryList[0]
                else:
                    thisBeneficiary = Beneficiary()

                template = template_env.get_template('templates/admin/churches/branches/bank/authorize.html')
                context = {'thisAuthorize':thisAuthorize,'thisAdmin':thisAdmin,'thisChurch':thisChurch,'thisBranch':thisBranch,'thisBeneficiary':thisBeneficiary}
                self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight  = UserRights()

            if thisUserRight.strAdminUser:
                vstrChoice = self.request.get('vstrChoice')

                if vstrChoice == "1":
                    vstrPaymentIndex = self.request.get('vstrPaymentIndex')
                    vstrPaymentType = self.request.get('vstrPaymentType')
                    vstrPaymentAmount = self.request.get('vstrPaymentAmount')
                    vstrReasonForPayment = self.request.get('vstrReasonForPayment')
                    vstrPaidToClient = self.request.get('vstrPaidToClient')
                    vstrPayFrom = self.request.get('vstrPayFrom')
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrChurchID = self.request.get('vstrChurchID')
                    vstrAuthorizedBy = self.request.get('vstrAuthorizedBy')


                    findRequest = PaymentsMade.query(PaymentsMade.strPaymentIndex == vstrPaymentIndex)
                    thisPaymentList = findRequest.fetch()

                    if len(thisPaymentList) > 0:
                        thisPayment = thisPaymentList[0]
                    else:
                        thisPayment = PaymentsMade()

                    thisPayment.writePaymentIndex(strinput=vstrPaymentIndex)
                    thisPayment.writePaymentType(strinput=vstrPaymentType)
                    thisPayment.writePaymentAmount(strinput=vstrPaymentAmount)
                    thisPayment.writeReasonForPayment(strinput=vstrReasonForPayment)
                    thisPayment.writePaidToClient(strinput=vstrPaidToClient)
                    thisPayment.writePayFrom(strinput=vstrPayFrom)
                    thisPayment.writeChurchBranchID(strinput=vstrChurchBranchID)
                    thisPayment.writeChurchID(strinput=vstrChurchID)
                    thisPayment.writeAuthorisedBy(strinput=Guser.user_id())

                    thisPayment.writeAuthorised(strinput=True)
                    thisPayment.put()
                    self.response.write("Payment successfully authorized")

                elif vstrChoice == "2":
                    vstrPaymentIndex = self.request.get('vstrPaymentIndex')
                    vstrPaymentType = self.request.get('vstrPaymentType')
                    vstrPaymentAmount = self.request.get('vstrPaymentAmount')
                    vstrReasonForPayment = self.request.get('vstrReasonForPayment')
                    vstrPaidToClient = self.request.get('vstrPaidToClient')
                    vstrPayFrom = self.request.get('vstrPayFrom')
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrChurchID = self.request.get('vstrChurchID')
                    vstrAuthorizedBy = self.request.get('vstrAuthorizedBy')

                    findRequest = PaymentsMade.query(PaymentsMade.strPaymentIndex == vstrPaymentIndex)
                    thisPaymentList = findRequest.fetch()

                    if len(thisPaymentList) > 0:
                        thisPayment = thisPaymentList[0]
                    else:
                        thisPayment = PaymentsMade()

                    thisPayment.writePaymentIndex(strinput=vstrPaymentIndex)
                    thisPayment.writePaymentType(strinput=vstrPaymentType)
                    thisPayment.writePaymentAmount(strinput=vstrPaymentAmount)
                    thisPayment.writeReasonForPayment(strinput=vstrReasonForPayment)
                    thisPayment.writePaidToClient(strinput=vstrPaidToClient)
                    thisPayment.writePayFrom(strinput=vstrPayFrom)
                    thisPayment.writeChurchBranchID(strinput=vstrChurchBranchID)
                    thisPayment.writeChurchID(strinput=vstrChurchID)
                    thisPayment.writeAuthorised(strinput=Guser.user_id())
                    thisPayment.writeAuthorised(strinput=False)
                    thisPayment.writeRejected(strinput=True)
                    thisPayment.put()



class StatementsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from church import ChurchMember,Churches
        if Guser:

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser:
                vstrChoice = self.request.get('vstrChoice')

                if vstrChoice == "0":
                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisAdminList = findRequest.fetch()

                    if len(thisAdminList) > 0:
                        thisAdmin = thisAdminList[0]
                    else:
                        thisAdmin = ChurchMember()

                    findRequest = PaymentsMade.query(PaymentsMade.strChurchID == thisAdmin.strChurchID,PaymentsMade.strChurchBranchID == thisAdmin.strChurchBranchID)
                    thisPaymentsList = findRequest.fetch()

                    findRequest = Costs.query(Costs.strChurchID == thisAdmin.strChurchID,Costs.strChurchBranchID == thisAdmin.strChurchBranchID)
                    thisCostsList = findRequest.fetch()

                    template = template_env.get_template('templates/admin/churches/branches/statements/statement.html')
                    context = {'thisPaymentsList':thisPaymentsList,'thisCostsList':thisCostsList}
                    self.response.write(template.render(context))





class ThisBeneficiaryHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser or thisUserRight.strSuperUser:

                URL = self.request.url
                URLlist = URL.split("/")
                vstrBeneficiaryIndex = URLlist[len(URLlist) - 1]


                findRequest = Beneficiary.query(Beneficiary.strBeneficiaryIndex == vstrBeneficiaryIndex)
                thisBeneficiaryList = findRequest.fetch()

                if len(thisBeneficiaryList) > 0:
                    thisBeneficiary = thisBeneficiaryList[0]
                else:
                    thisBeneficiary = Beneficiary()

                findRequest = BenBank.query(BenBank.strBeneficiaryIndex == vstrBeneficiaryIndex)
                thisBenBankList = findRequest.fetch()

                if len(thisBenBankList) > 0:
                    thisBenBank = thisBenBankList[0]
                else:
                    thisBenBank = BenBank()

                template = template_env.get_template('templates/admin/churches/branches/bank/beneficiaries.html')
                context = {'thisBeneficiary':thisBeneficiary,'thisBenBank':thisBenBank}
                self.response.write(template.render(context))

    def pos(self):
        Guser = users.get_current_user()
        from church import ChurchMember
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrNames = self.request.get('vstrNames')
                vstrSurname = self.request.get('vstrSurname')
                vstrIDNumber = self.request.get('vstrIDNumber')
                vstrCompanyName = self.request.get('vstrCompanyName')
                vstrCompanyReg = self.request.get('vstrCompanyReg')
                vstrCompanyVAT = self.request.get('vstrCompanyVAT')
                vstrBeneficiaryIndex = self.request.get('vstrBeneficiaryIndex')
                vstrNotes  = self.request.get('vstrNotes')


                findRequest = Beneficiary.query(Beneficiary.strBeneficiaryIndex == vstrBeneficiaryIndex)
                thisBeneficiaryList = findRequest.fetch()

                if len(thisBeneficiaryList) > 0:
                    thisBeneficiary = thisBeneficiaryList[0]
                else:
                    thisBeneficiary = Beneficiary()

                thisBeneficiary.writeBeneficiaryIndex(strinput=vstrBeneficiaryIndex)
                thisBeneficiary.writeNames(strinput=vstrNames)
                thisBeneficiary.writeSurname(strinput=vstrSurname)
                thisBeneficiary.writeIDNumber(strinput=vstrIDNumber)
                thisBeneficiary.writeCompanyName(strinput=vstrCompanyName)
                thisBeneficiary.writeCompanyReg(strinput=vstrCompanyReg)
                thisBeneficiary.writeCompanyVAT(strinput=vstrCompanyVAT)
                thisBeneficiary.writeNotes(strinput=vstrNotes)
                thisBeneficiary.put()

                self.response.write('Successfully updated Beneficiary Information')
            elif vstrChoice == "1":
                vstrAccountHolder = self.request.get('vstrAccountHolder')
                vstrAccountNumber = self.request.get('vstrAccountNumber')
                vstrAccountType = self.request.get('vstrAccountType')
                vstrBankName = self.request.get('vstrBankName')
                vstrBranchName = self.request.get('vstrBranchName')
                vstrBranchCode = self.request.get('vstrBranchCode')
                vstrRoutingNumber = self.request.get('vstrRoutingNumber')
                vstrBeneficiaryIndex = self.request.get('vstrBeneficiaryIndex')



                findRequest = BenBank.query(BenBank.strBeneficiaryIndex == vstrBeneficiaryIndex)
                thisBenBankList = findRequest.fetch()

                if len(thisBenBankList) > 0:
                    thisBenBank = thisBenBankList[0]
                else:
                    thisBenBank = BenBank()

                thisBenBank.writeBeneficiaryIndex(strinput=vstrBeneficiaryIndex)
                thisBenBank.writeAccountHolder(strinput=vstrAccountHolder)
                thisBenBank.writeAccountNumber(strinput=vstrAccountNumber)
                thisBenBank.writeAccountType(strinput=vstrAccountType)
                thisBenBank.writeBankName(strinput=vstrBankName)
                thisBenBank.writeBranchName(strinput=vstrBranchName)
                thisBenBank.writeBranchCode(strinput=vstrBranchCode)
                thisBenBank.writeRoutingNumber(strinput=vstrRoutingNumber)

                thisBenBank.put()

                self.response.write("Beneficiary Bank Account successfully updated")


class ThisMonetaryHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = self.request.url
            URLlist = URL.split('/')
            vstrDonatorID = URLlist[len(URLlist) - 1]

            findRequest = Donators.query(Donators.strDonatorID == vstrDonatorID)
            thisDonatorsList = findRequest.fetch()

            if len(thisDonatorsList) > 0:
                thisDonator = thisDonatorsList[0]
            else:
                thisDonator = Donators()

            template = template_env.get_template('templates/admin/churches/branches/income/thisDonator.html')
            context = {'thisDonator':thisDonator}
            self.response.write(template.render(context))


    def post(self):
        Guser = users.get_current_user()
        from church import ChurchMember
        from mysms import SMSAccount,SMSPortalBudget
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrDonatorID = self.request.get('vstrDonatorID')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                vstrChurchID = self.request.get('vstrChurchID')

                findRequest = Donators.query(Donators.strChurchID == vstrChurchID,Donators.strChurchBranchID == vstrChurchBranchID,Donators.strDonatorID == vstrDonatorID)
                thisDonatorList = findRequest.fetch()

                if len(thisDonatorList) > 0:
                    thisDonator = thisDonatorList[0]
                else:
                    thisDonator = Donators()

                template = template_env.get_template('templates/admin/churches/branches/income/donations/donatorinf.html')
                context = {'thisDonator':thisDonator}
                self.response.write(template.render(context))


            elif vstrChoice == "1":
                vstrDonatorID = self.request.get('vstrDonatorID')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                vstrChurchID = self.request.get('vstrChurchID')

                findRequest = Donation.query(Donation.strDonatorID == vstrDonatorID,Donation.strChurchID == vstrChurchID,Donation.strChurchBranchID == vstrChurchBranchID)
                thisDonationList = findRequest.fetch()

                template = template_env.get_template('templates/admin/churches/branches/income/donations/donations.html')
                context = {'thisDonationList':thisDonationList,'vstrDonatorID':vstrDonatorID,'vstrChurchBranchID':vstrChurchBranchID,'vstrChurchID':vstrChurchID}
                self.response.write(template.render(context))

            elif vstrChoice == "2":
                vstrDonatorID = self.request.get('vstrDonatorID')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                vstrChurchID = self.request.get('vstrChurchID')
                vstrInstitutionName = self.request.get('vstrInstitutionName')
                vstrNames = self.request.get('vstrNames')
                vstrSurname = self.request.get('vstrSurname')
                vstrIDNumber = self.request.get('vstrIDNumber')
                vstrPhyStandNumber = self.request.get('vstrPhyStandNumber')
                vstrPhyStreetName = self.request.get('vstrPhyStreetName')
                vstrPhyCityTown = self.request.get('vstrPhyCityTown')
                vstrPhyProvince = self.request.get('vstrPhyProvince')
                vstrPhyCountry = self.request.get('vstrPhyCountry')
                vstrPhyPostalCode = self.request.get('vstrPhyPostalCode')
                vstrPosBoxNumber = self.request.get('vstrPosBoxNumber')
                vstrPosCityTown = self.request.get('vstrPosCityTown')
                vstrPosProvince = self.request.get('vstrPosProvince')
                vstrPosCountry = self.request.get('vstrPosCountry')
                vstrPosPostalCode = self.request.get('vstrPosPostalCode')
                vstrTel = self.request.get('vstrTel')
                vstrCell = self.request.get('vstrCell')
                vstrEmail = self.request.get('vstrEmail')
                vstrWebsite = self.request.get('vstrWebsite')

                findRequest = Donators.query(Donators.strDonatorID == vstrDonatorID,Donators.strChurchID == vstrChurchID,Donators.strChurchBranchID == vstrChurchBranchID)
                thisDonatorList = findRequest.fetch()

                if len(thisDonatorList) > 0:
                    thisDonator = thisDonatorList[0]
                else:
                    thisDonator = Donators()

                thisDonator.writeInstitutionName(strinput=vstrInstitutionName)
                thisDonator.writeNames(strinput=vstrNames)
                thisDonator.writeSurname(strinput=vstrSurname)
                thisDonator.writeIDNumber(strinput=vstrIDNumber)
                thisDonator.writePhyStandNumber(strinput=vstrPhyStandNumber)
                thisDonator.writePhyStreetName(strinput=vstrPhyStreetName)
                thisDonator.writePhyCityTown(strinput=vstrPhyCityTown)
                thisDonator.writePhyProvince(strinput=vstrPhyProvince)
                thisDonator.writePhyCountry(strinput=vstrPhyCountry)
                thisDonator.writePhyPostalCode(strinput=vstrPhyPostalCode)
                thisDonator.writePosBoxNumber(strinput=vstrPosBoxNumber)
                thisDonator.writePosCityTown(strinput=vstrPosCityTown)
                thisDonator.writePosProvince(strinput=vstrPosProvince)
                thisDonator.writePosCountry(strinput=vstrPosCountry)
                thisDonator.writePosPostalCode(strinput=vstrPosPostalCode)
                thisDonator.writeTel(strinput=vstrTel)
                thisDonator.writeCell(strinput=vstrCell)
                thisDonator.writeEmail(strinput=vstrEmail)
                thisDonator.writeWebsite(strinput=vstrWebsite)

                thisDonator.put()

                self.response.write("Donator Successfully updated")


            #TODo- Finish up the messaging part once done
            elif vstrChoice == "3":
                vstrDonatorID = self.request.get('vstrDonatorID')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                vstrChurchID = self.request.get('vstrChurchID')
                vstrDonationAmount = self.request.get('vstrDonationAmount')
                vstrDate = self.request.get('vstrDate')

                try:
                    vstrDateList = vstrDate.split("-")
                    strYear = vstrDateList[0]
                    strMonth =  vstrDateList[1]
                    strDay = vstrDateList[2]
                except:
                    vstrThisDate = datetime.datetime.now()
                    strYear = vstrThisDate.year
                    strMonth = vstrThisDate.month
                    strDay = vstrThisDate.day

                thisDonation = Donation()
                thisDonation.writeDonatorID(strinput=vstrDonatorID)
                thisDonation.writeChurchID(strinput=vstrChurchID)
                thisDonation.writeChurchBranchID(strinput=vstrChurchBranchID)
                thisDonation.writeDonationAmount(strinput=vstrDonationAmount)
                thisDonation.writeTransactionID(strinput=thisDonation.createTransactionID())
                thisDonation.writeYear(strinput=strYear)
                thisDonation.writeMonth(strinput=strMonth)
                thisDonation.writeDay(strinput=strDay)
                thisDonation.put()


                self.response.write("Successfully updated your donation")



            elif vstrChoice == "4":
                vstrDonatorID = self.request.get('vstrDonatorID')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                vstrChurchID = self.request.get('vstrChurchID')

                findRequest = MonetaryMessaging.query(MonetaryMessaging.strMemberID == vstrDonatorID)
                thisMessagingList = findRequest.fetch()

                findRequest = Donators.query(Donators.strDonatorID == vstrDonatorID,Donators.strChurchID == vstrChurchID)
                thisDonatorList = findRequest.fetch()
                if len(thisDonatorList) > 0:
                    thisDonator = thisDonatorList[0]
                else:
                    thisDonator = Donators()

                template = template_env.get_template('templates/admin/churches/branches/income/messaging/messaging.html')
                context = {'thisMessagingList':thisMessagingList,'thisDonator':thisDonator}
                self.response.write(template.render(context))

            elif vstrChoice == "5":
                vstrDonatorID = self.request.get('vstrDonatorID')
                vstrCell = self.request.get('vstrCell')
                vstrMessage = self.request.get('vstrMessage')

                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisAdminList = findRequest.fetch()

                if len(thisAdminList) > 0:
                    thisAdmin = thisAdminList[0]
                else:
                    thisAdmin = ChurchMember()

                findRequest = SMSAccount.query(SMSAccount.strChurchID == thisAdmin.strChurchID)
                thisSMSAccountList = findRequest.fetch()

                if len(thisSMSAccountList) > 0:
                    thisSMSAccount = thisSMSAccountList[0]

                    if thisSMSAccount.strTotalSMS > 0:
                        findRequest = SMSPortalBudget.query()
                        thisPortalList = findRequest.fetch()

                        if len(thisPortalList) > 0:
                            thisPortal = thisPortalList[0]
                        else:
                            thisPortal = SMSPortalBudget()

                        strRef = thisPortal.SendCronMessage(strMessage=vstrMessage,strCell=vstrCell)

                        if not(strRef == None):
                            vstrThisDate = datetime.datetime.now()
                            strThisDate = vstrThisDate.date()
                            strThisTime = datetime.time(hour=vstrThisDate.hour,minute=vstrThisDate.minute,second=vstrThisDate.second)
                            thisMessage = MonetaryMessaging()
                            thisMessage.writeChurchID(strinput=thisAdmin.strChurchID)
                            thisMessage.writeChurchBranchID(strinput=thisAdmin.strChurchBranchID)
                            thisMessage.writeRef(strinput=strRef)
                            thisMessage.writeMessage(strinput=vstrMessage)
                            thisMessage.writeDateSent(strinput=strThisDate)
                            thisMessage.writeTimeSent(strinput=strThisTime)
                            thisMessage.put()
                            thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - 1
                            thisSMSAccount.put()
                            self.response.write("Message successfully sent")
                        else:
                            self.response.write("Error Sending Message please check your internet connection")
                    else:
                        self.response.write("Insufficient SMS Credit please recharge your account")
                else:
                    self.response.write("Error accessing your SMS Account")























app = webapp2.WSGIApplication([
    ('/monetary/income', IncomeHandler),
    ('/monetary/donators', DonatorsHandler),
    ('/monetary/costs', CostsHandler),
    ('/monetary/costs/.*', thisCostHandler),
    ('/monetary/payments/authorize/.*', AuthorizeHandler),
    ('/monetary/statements', StatementsHandler),
    ('/monetary/beneficiaries/.*', ThisBeneficiaryHandler),
    ('/monetary/donators/.*', ThisMonetaryHandler)


], debug=True)





