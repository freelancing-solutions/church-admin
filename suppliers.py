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


class SupProducts(ndb.Expando):
    strReference = ndb.StringProperty()
    strSupplierID = ndb.StringProperty()

    strProductName = ndb.StringProperty()
    strDescription = ndb.StringProperty()
    strProductCost = ndb.StringProperty()
    strDepositAmount = ndb.StringProperty()

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSupplierID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSupplierID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeProductName(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strProductName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDescription(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strDescription = strinput
                return True
            else:
                return False
        except:
            return False


    def writeProductCost(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strProductCost = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDepositAmount(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strDepositAmount = strinput
                return True
            else:
                return False
        except:
            return False

class SupServices(ndb.Expando):
    """
        Reference of the Employee/Member who created the entry
    """
    strReference = ndb.StringProperty()
    strSupplierID = ndb.StringProperty()

    strServiceName = ndb.StringProperty()
    strDescription = ndb.StringProperty()
    strServiceCost = ndb.StringProperty()
    strDepositAmount = ndb.StringProperty()


    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSupplierID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSupplierID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeServiceName(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strServiceName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDescription(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strDescription = strinput
                return True
            else:
                return False
        except:
            return False

    def writeServiceCost(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strServiceCost = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDepositAmount(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strDepositAmount = strinput
                return True
            else:
                return False
        except:
            return False

class SupPhyAddress(ndb.Expando):
    strReference = ndb.StringProperty()

    strSupplierID = ndb.StringProperty()

    strStandNumber = ndb.StringProperty()
    strStreetName = ndb.StringProperty()
    strCityTown = ndb.StringProperty()
    strProvince = ndb.StringProperty()
    strCountry = ndb.StringProperty()
    strPostalCode = ndb.StringProperty()

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSupplierID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSupplierID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStandNumber(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strStandNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStreetName(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strStreetName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCityTown(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCityTown = strinput
                return True
            else:
                return False

        except:
            return False
    def writeProvince(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strProvince = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCountry(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCountry  = strinput
                return True
            else:
                return False
        except:
            return False
    def writePostalCode(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strPostalCode = strinput
                return True
            else:
                return False
        except:
            return False

class SupPosAddress(ndb.Expando):
    strReference = ndb.StringProperty()
    strSupplierID = ndb.StringProperty()

    strPostalAddress = ndb.StringProperty()
    strCityTown = ndb.StringProperty()
    strProvince = ndb.StringProperty()
    strCountry = ndb.StringProperty()
    strPostalCode = ndb.StringProperty()

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False
    def writeSupplierID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSupplierID = strinput
                return True
            else:
                return False

        except:
            return False
    def writePostalAddress(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strPostalAddress = strinput
                return True
            else:
                return False

        except:
            return False

    def writeCityTown(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCityTown = strinput
                return True
            else:
                return False
        except:
            return False

    def writeProvince(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strProvince = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCountry(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCountry = strinput
                return True
            else:
                return False
        except:
            return False

    def writePostalCode(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strPostalCode = strinput
                return True
            else:
                return False
        except:
            return False

class SupContact(ndb.Expando):
    strReference = ndb.StringProperty()
    strSupplierID = ndb.StringProperty()

    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strFax = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebsite = ndb.StringProperty()

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeSupplierID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSupplierID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strTel = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFax(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strFax = strinput
                return True
            else:
                return False
        except:
            return False

    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False

    def writeWebsite(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strWebsite = strinput
                return True
            else:
                return False
        except:
            return False

class Suppliers(ndb.Expando):
    strReference = ndb.StringProperty()

    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strSupplierID = ndb.StringProperty()
    strCompanyName = ndb.StringProperty()
    strCompanyReg = ndb.StringProperty()
    strVAT = ndb.StringProperty()

    strCPNames = ndb.StringProperty()
    strCPSurname = ndb.StringProperty()
    strCPIDNumber = ndb.StringProperty()
    strCPPosition = ndb.StringProperty()

    strYear = ndb.StringProperty()
    strMonth = ndb.StringProperty()
    strDay = ndb.StringProperty()
    strTimeRegistered = ndb.TimeProperty(auto_now_add=True)


    def writeCPNames(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCPNames = strinput
                return True
            else:
                return False

        except:
            return False
    def writeCPSurname(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCPSurname = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCPIDNumber(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCPIDNumber = strinput
                return True
            else:
                return False

        except:
            return False
    def writeCPPostion(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCPPosition = strinput
                return True
            else:
                return False
        except:
            return False
    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
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
    def writeSupplierID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSupplierID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCompanyName(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCompanyName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCompanyReg(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCompanyReg = strinput
                return True
            else:
                return False
        except:
            return False
    def writeVAT(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strVAT = strinput
                return True
            else:
                return False
        except:
            return False
    def writeYearRegistered(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit()  and (int(strinput) >= 2016) and (int(strinput) <= 2100):
                self.strYear = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonthRegistered(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1 ) and (int(strinput) <= 12):
                self.strMonth = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDayRegistered(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) >= 1) and (int(strinput) <= 31):
                self.strDay = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeRegistered(self,strinput):
        try:
            if not(strinput == None):
                self.strTimeRegistered = strinput
                return True
            else:
                return False
        except:
            return False

    def createSupplierID(self):
        try:
            Guser = users.get_current_user()
            strReference = Guser.user_id()
            findRequest = Suppliers.query()
            thisSupplierList = findRequest.fetch()
            strReference = strReference + str(len(thisSupplierList) + 1)
            return strReference
        except:
            return None

class Clients(ndb.Expando):
    strReference = ndb.StringProperty()
    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strIDNumber = ndb.StringProperty()

    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strClientID = ndb.StringProperty()

    strYear = ndb.StringProperty()
    strMonth = ndb.StringProperty()
    strDay = ndb.StringProperty()
    strTimeRegistered = ndb.TimeProperty(auto_now_add=True)




    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
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

    def writeIDNumber(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strIDNumber = strinput
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
            strinput= str(strinput)
            if not(strinput == None):
                self.strChurchBranchID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeClientID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strClientID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeYear(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strYear = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMonth(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strMonth = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDay(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strDay = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTimeRegistered(self,strinput):
        try:

            if not(strinput == None):
                self.strTimeRegistered = strinput
                return True
            else:
                return False
        except:
            return False

    def createClientID(self):
        try:
            Guser = users.get_current_user()
            strReference = Guser.user_id()
            findRequest = Clients.query()
            thisClientList = findRequest.fetch()
            strReference = strReference + str(len(thisClientList) + 1)
            return strReference
        except:
            return None

class CliProducts(ndb.Expando):
    strReference = ndb.StringProperty()


    strClientID = ndb.StringProperty()

    strProductName = ndb.StringProperty()
    strDescription = ndb.StringProperty()
    strProductCost = ndb.StringProperty()
    strDepositAmount = ndb.StringProperty()


    def writeReference(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False


    def writeClientID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strClientID = strinput
                return True
            else:
                return False
        except:
            return False


    def writeProductName(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strProductName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeProductDescription(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strDescription = strinput
                return True
            else:
                return False
        except:
            return False



    def writeProductCost(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strProductCost = strinput
                return True
            else:
                return False
        except:
            return False


    def writeDepositAmount(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strDepositAmount = strinput
                return True
            else:
                return False
        except:
            return False

class CliServices(ndb.Expando):

    """
        Reference of the Employee/Member who created the entry
    """
    strReference = ndb.StringProperty()
    strClientID = ndb.StringProperty()

    strServiceName = ndb.StringProperty()
    strDescription = ndb.StringProperty()
    strServiceCost = ndb.StringProperty()
    strDepositAmount = ndb.StringProperty()


    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeClientID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strClientID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeServiceName(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strServiceName = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDescription(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strDescription = strinput
                return True
            else:
                return False
        except:
            return False

    def writeServiceCost(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strServiceCost = strinput
                return True
            else:
                return False
        except:
            return False

    def writeDepositAmount(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strDepositAmount = strinput
                return True
            else:
                return False
        except:
            return False

class CliPhyAddress(ndb.Expando):
    strReference = ndb.StringProperty()

    strClientID = ndb.StringProperty()

    strStandNumber = ndb.StringProperty()
    strStreetName = ndb.StringProperty()
    strCityTown = ndb.StringProperty()
    strProvince = ndb.StringProperty()
    strCountry = ndb.StringProperty()
    strPostalCode = ndb.StringProperty()

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False
    def writeClientID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strClientID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStandNumber(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strStandNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStreetName(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strStreetName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCityTown(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCityTown = strinput
                return True
            else:
                return False

        except:
            return False
    def writeProvince(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strProvince = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCountry(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCountry  = strinput
                return True
            else:
                return False
        except:
            return False
    def writePostalCode(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strPostalCode = strinput
                return True
            else:
                return False
        except:
            return False

class CliPosAddress(ndb.Expando):
    strReference = ndb.StringProperty()
    strClientID = ndb.StringProperty()

    strPostalAddress = ndb.StringProperty()
    strCityTown = ndb.StringProperty()
    strProvince = ndb.StringProperty()
    strCountry = ndb.StringProperty()
    strPostalCode = ndb.StringProperty()

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False
    def writeClientID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strClientID = strinput
                return True
            else:
                return False

        except:
            return False
    def writePostalAddress(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strPostalAddress = strinput
                return True
            else:
                return False

        except:
            return False

    def writeCityTown(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCityTown = strinput
                return True
            else:
                return False
        except:
            return False

    def writeProvince(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strProvince = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCountry(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCountry = strinput
                return True
            else:
                return False
        except:
            return False

    def writePostalCode(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strPostalCode = strinput
                return True
            else:
                return False
        except:
            return False

class CliContact(ndb.Expando):
    strReference = ndb.StringProperty()
    strClientID = ndb.StringProperty()

    strCell = ndb.StringProperty()
    strTel = ndb.StringProperty()
    strFax = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebsite = ndb.StringProperty()

    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False

    def writeClientID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strClientID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strCell = strinput
                return True
            else:
                return False
        except:
            return False

    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strTel = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFax(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strFax = strinput
                return True
            else:
                return False
        except:
            return False

    def writeEmail(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strEmail = strinput
                return True
            else:
                return False
        except:
            return False

    def writeWebsite(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strWebsite = strinput
                return True
            else:
                return False
        except:
            return False

class CliBankDetails(ndb.Expando):

    strReference = ndb.StringProperty()
    strClientID = ndb.StringProperty()

    strAccountHolder = ndb.StringProperty()
    strAccountNumber = ndb.StringProperty()
    strAccountType = ndb.StringProperty()
    strBankName = ndb.StringProperty()
    strBranchName = ndb.StringProperty()
    strBranchCode = ndb.StringProperty()
    strRoutingNumber = ndb.StringProperty()


    def writeReference(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False


    def writeClientID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strClientID = strinput
                return True
            else:
                return False

        except:
            return False


    def writeAccountHolder(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput) > 0:
                self.strAccountHolder = strinput
                return True
            else:
                return False
        except:
            return False


    def writeAccountNumber(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strAccountNumber = strinput
                return True
            else:
                return False
        except:
            return False


    def writeAccountType(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strAccountType = strinput
                return True
            else:
                return False
        except:
            return False


    def writeBankName(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strBankName = strinput
                return True
            else:
                return False
        except:
            return False


    def writeBranchName(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strBranchName = strinput
                return True
            else:
                return False
        except:
            return False


    def writeBranchCode(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strBranchCode = strinput
                return True
            else:
                return False
        except:
            return False


    def writeRoutingNumber(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strRoutingNumber = strinput
                return True
            else:
                return False
        except:
            return False

class SupBankDetails(ndb.Expando):
    strReference = ndb.StringProperty()
    strSupplierID = ndb.StringProperty()

    strAccountHolder = ndb.StringProperty()
    strAccountNumber = ndb.StringProperty()
    strAccountType = ndb.StringProperty()
    strBankName = ndb.StringProperty()
    strBranchName = ndb.StringProperty()
    strBranchCode = ndb.StringProperty()
    strRoutingNumber = ndb.StringProperty()


    def writeReference(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strReference = strinput
                return True
            else:
                return False
        except:
            return False


    def writeSupplierID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strSupplierID = strinput
                return True
            else:
                return False

        except:
            return False


    def writeAccountHolder(self, strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strAccountHolder = strinput
                return True
            else:
                return False
        except:
            return False


    def writeAccountNumber(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strAccountNumber = strinput
                return True
            else:
                return False
        except:
            return False


    def writeAccountType(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strAccountType = strinput
                return True
            else:
                return False
        except:
            return False


    def writeBankName(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strBankName = strinput
                return True
            else:
                return False
        except:
            return False


    def writeBranchName(self, strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strBranchName = strinput
                return True
            else:
                return False
        except:
            return False


    def writeBranchCode(self, strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strBranchCode = strinput
                return True
            else:
                return False
        except:
            return False


    def writeRoutingNumber(self, strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strRoutingNumber = strinput
                return True
            else:
                return False
        except:
            return False


class SupplierMessaging(ndb.Expando):

    strReference = ndb.StringProperty()

    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strSupplierID = ndb.StringProperty()
    strMessage = ndb.StringProperty()
    strResponse = ndb.StringProperty()
    strRef = ndb.StringProperty()
    strDateSent = ndb.DateProperty()
    strTimeSent = ndb.TimeProperty()
    strDateResponse = ndb.DateProperty()
    strTimeResponse = ndb.TimeProperty()


    def writeReference(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strReference = strinput
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



    def writeSupplierID(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strSupplierID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeMessage(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strMessage = strinput
                return True
            else:
                return False
        except:
            return False
    def writeResponse(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strResponse = strinput
                return True

            else:
                return False
        except:
            return False
    def writeRef(self,strinput):
        try:
            strinput = str(strinput)
            if not(strinput == None):
                self.strRef = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateSent(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateSent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeSent(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeSent = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateResponse(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strDateResponse = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeResponse(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeResponse = strinput
                return True
            else:
                return False
        except:
            return False




class ClientsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChurchID = self.request.get('vstrChurchID')
            vstrChurchBranchID = self.request.get('vstrChurchBranchID')


            findRequest = Clients.query(Clients.strChurchID == vstrChurchID, Clients.strChurchBranchID == vstrChurchBranchID)
            thisClientsList = findRequest.fetch()

            template = template_env.get_template('templates/admin/churches/branches/suppliers/clients.html')
            context = {'thisClientsList':thisClientsList,'vstrChurchID':vstrChurchID,'vstrChurchBranchID':vstrChurchBranchID}
            self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChurchID = self.request.get('vstrChurchID')
            vstrChurchBranchID = self.request.get('vstrChurchBranchID')
            vstrNames = self.request.get('vstrNames')
            vstrSurname = self.request.get('vstrSurname')
            vstrIDNumber = self.request.get('vstrIDNumber')

            findRequest = Clients.query(Clients.strChurchID == vstrChurchID,Clients.strChurchBranchID == vstrChurchBranchID,Clients.strIDNumber == vstrIDNumber)
            thisClientsList = findRequest.fetch()

            if len(thisClientsList) > 0:
                thisClient = thisClientsList[0]
            else:
                thisClient = Clients()

            thisClient.writeReference(strinput=Guser.user_id())
            thisClient.writeChurchID(strinput=vstrChurchID)
            thisClient.writeChurchBranchID(strinput=vstrChurchBranchID)
            thisClient.writeNames(strinput=vstrNames)
            thisClient.writeSurname(strinput=vstrSurname)
            thisClient.writeIDNumber(strinput=vstrIDNumber)
            thisDay = datetime.datetime.now()
            thisDay = thisDay.date()
            strYear = thisDay.year
            strMonth = thisDay.month
            strDay = thisDay.day
            thisClient.writeYear(strinput=strYear)
            thisClient.writeMonth(strinput=strMonth)
            thisClient.writeDay(strinput=strDay)
            thisTime = datetime.datetime.now()
            thisTime = thisTime.time()

            strHour = thisTime.hour
            strMin = thisTime.minute
            strSecond = thisTime.second

            thisTime = datetime.time(hour=strHour,minute=strMin,second=strSecond)

            thisClient.writeTimeRegistered(strinput=thisTime)
            thisClient.writeClientID(strinput=thisClient.createClientID())
            thisClient.put()

            self.response.write("Clients List Updated")




class thisClientHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = self.request.url
            URLlist = URL.split("/")
            vstrClientID = URLlist[len(URLlist) - 1]

            findRequest = Clients.query(Clients.strClientID == vstrClientID)
            thisClientsList = findRequest.fetch()

            if len(thisClientsList) > 0:
                thisClient = thisClientsList[0]
            else:
                thisClient = Clients()

            findRequest = CliProducts.query(CliProducts.strClientID  == vstrClientID)
            thisProductsList = findRequest.fetch()

            findRequest = CliServices.query(CliServices.strClientID == vstrClientID)
            thisServicesList = findRequest.fetch()

            findRequest = CliPhyAddress.query(CliPhyAddress.strClientID == vstrClientID)
            thisClientPhysicalList = findRequest.fetch()

            if len(thisClientPhysicalList) > 0:
                thisClientPhyAddress = thisClientPhysicalList[0]
            else:
                thisClientPhyAddress = CliPhyAddress()

            findRequest = CliPosAddress.query(CliPosAddress.strClientID == vstrClientID)
            thisClientPosAddressList = findRequest.fetch()

            if len(thisClientPosAddressList) > 0:
                thisClientPosAddress = thisClientPosAddressList[0]
            else:
                thisClientPosAddress = CliPosAddress()

            findRequest = CliBankDetails.query(CliBankDetails.strClientID == vstrClientID)
            thisClientBankDetailsList = findRequest.fetch()

            if len(thisClientBankDetailsList) > 0:
                thisClientBankDetails = thisClientBankDetailsList[0]
            else:
                thisClientBankDetails = CliBankDetails()

            template = template_env.get_template('templates/admin/churches/branches/suppliers/thisClient.html')
            context = {'thisClient':thisClient,'thisProductsList':thisProductsList,'thisServicesList':thisServicesList,
                       'thisClientPhyAddress':thisClientPhyAddress,'thisClientPosAddress':thisClientPosAddress,'thisClientBankDetails':thisClientBankDetails}
            self.response.write(template.render(context))



    def post(self):
        Guser = users.get_current_user()
        from church import ChurchMember
        from mysms import SMSAccount,SMSPortalBudget
        if Guser:

            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrClientID = self.request.get('vstrClientID')
                vstrChurchID = self.request.get('vstrChurchID')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')


                findRequest = Clients.query(Clients.strClientID == vstrClientID, Clients.strChurchID == vstrChurchID, Clients.strChurchBranchID == vstrChurchBranchID)
                thisClientList = findRequest.fetch()

                if len(thisClientList) > 0:
                    thisClient = thisClientList[0]
                else:
                    thisClient = Clients()

                template = template_env.get_template('templates/admin/churches/branches/suppliers/cldetails.html')
                context = {'thisClient':thisClient}
                self.response.write(template.render(context))

            elif vstrChoice == "1":
                vstrClientID = self.request.get('vstrClientID')
                vstrChurchID = self.request.get('vstrChurchID')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')

                findRequest = CliPhyAddress.query(CliPhyAddress.strClientID == vstrClientID)
                thisClientPhyList = findRequest.fetch()

                if len(thisClientPhyList) > 0:
                    thisClientPhy = thisClientPhyList[0]
                else:
                    thisClientPhy = CliPhyAddress()

                template = template_env.get_template('templates/admin/churches/branches/suppliers/phdetails.html')
                context = {'thisClientPhy':thisClientPhy}
                self.response.write(template.render(context))

            elif vstrChoice == "2":
                vstrClientID = self.request.get('vstrClientID')
                vstrStandNumber = self.request.get('vstrStandNumber')
                vstrStreetName = self.request.get('vstrStreetName')
                vstrCityTown  = self.request.get('vstrCityTown')
                vstrProvince = self.request.get('vstrProvince')
                vstrCountry = self.request.get('vstrCountry')
                vstrPostalCode = self.request.get('vstrPostalCode')

                findRequest = CliPhyAddress.query(CliPhyAddress.strClientID == vstrClientID)
                thisClientPhyList = findRequest.fetch()

                if len(thisClientPhyList) > 0:
                    thisClientPhy = thisClientPhyList[0]
                else:
                    thisClientPhy = CliPhyAddress()

                thisClientPhy.writeReference(strinput=Guser.user_id())
                thisClientPhy.writeClientID(strinput=vstrClientID)
                thisClientPhy.writeStandNumber(strinput=vstrStandNumber)
                thisClientPhy.writeStreetName(strinput=vstrStreetName)
                thisClientPhy.writeCityTown(strinput=vstrCityTown)
                thisClientPhy.writeProvince(strinput=vstrProvince)
                thisClientPhy.writeCountry(strinput=vstrCountry)
                thisClientPhy.writePostalCode(strinput=vstrPostalCode)

                thisClientPhy.put()

                self.response.write("Physical Address updated successfully")

            elif vstrChoice == "3":
                vstrClientID = self.request.get('vstrClientID')

                findRequest = CliPosAddress.query(CliPosAddress.strClientID == vstrClientID)
                thisClientPosAddressList = findRequest.fetch()

                if len(thisClientPosAddressList) > 0:
                    thisCLientPosAddress = thisClientPosAddressList[0]
                else:
                    thisCLientPosAddress = CliPosAddress()

                template = template_env.get_template('templates/admin/churches/branches/suppliers/posdetails.html')
                context = {'thisCLientPosAddress':thisCLientPosAddress}
                self.response.write(template.render(context))

            elif vstrChoice == "4":

                vstrClientID = self.request.get('vstrClientID')
                vstrPostalAddress = self.request.get('vstrPostalAddress')
                vstrCityTown = self.request.get('vstrCityTown')
                vstrProvince = self.request.get('vstrProvince')
                vstrCountry = self.request.get('vstrCountry')
                vstrPostalCode = self.request.get('vstrPostalCode')

                findRequest = CliPosAddress.query(CliPosAddress.strClientID == vstrClientID)
                thisPosAddressList = findRequest.fetch()

                if len(thisPosAddressList) > 0:
                    thisPosAddress = thisPosAddressList[0]
                else:
                    thisPosAddress = CliPosAddress()

                thisPosAddress.writeClientID(strinput=vstrClientID)
                thisPosAddress.writePostalAddress(strinput=vstrPostalAddress)
                thisPosAddress.writeCityTown(strinput=vstrCityTown)
                thisPosAddress.writeProvince(strinput=vstrProvince)
                thisPosAddress.writeCountry(strinput=vstrCountry)
                thisPosAddress.writePostalCode(strinput=vstrPostalCode)

                thisPosAddress.put()

                self.response.write("Postal Address updated successfully")
            elif vstrChoice == "5":
                vstrClientID = self.request.get('vstrClientID')

                findRequest = CliContact.query(CliContact.strClientID == vstrClientID)
                thisContactList = findRequest.fetch()

                if len(thisContactList) > 0:
                    thisContact = thisContactList[0]
                else:
                    thisContact = CliContact()

                template = template_env.get_template("templates/admin/churches/branches/suppliers/clcontact.html")
                context = {'thisContact':thisContact,'vstrClientID':vstrClientID}
                self.response.write(template.render(context))
            elif vstrChoice == "6":
                vstrClientID = self.request.get('vstrClientID')
                vstrCell = self.request.get('vstrCell')
                vstrTel = self.request.get('vstrTel')
                vstrFax = self.request.get('vstrFax')
                vstrEmail = self.request.get('vstrEmail')
                vstrWebsite = self.request.get('vstrWebsite')

                findRequest = CliContact.query(CliContact.strClientID == vstrClientID)
                thisContactList = findRequest.fetch()

                if len(thisContactList) > 0:
                    thisContact = thisContactList[0]
                else:
                    thisContact = CliContact()

                thisContact.writeClientID(strinput=vstrClientID)
                thisContact.writeCell(strinput=vstrCell)
                thisContact.writeTel(strinput=vstrTel)
                thisContact.writeFax(strinput=vstrFax)
                thisContact.writeEmail(strinput=vstrEmail)
                thisContact.writeWebsite(strinput=vstrWebsite)
                thisContact.put()

                self.response.write("Contact Updated Successfully")

            elif vstrChoice == "7":
                vstrClientID = self.request.get('vstrClientID')

                findRequest = CliBankDetails.query(CliBankDetails.strClientID == vstrClientID)
                thisBankDetailsList = findRequest.fetch()

                if len(thisBankDetailsList) > 0:
                    thisBankDetails = thisBankDetailsList[0]
                else:
                    thisBankDetails = CliBankDetails()

                template = template_env.get_template("templates/admin/churches/branches/suppliers/clbankdetails.html")
                context = {'thisBankDetails':thisBankDetails,'vstrClientID':vstrClientID}
                self.response.write(template.render(context))

            elif vstrChoice == "8":
                vstrClientID = self.request.get('vstrClientID')
                vstrAccountHolder = self.request.get('vstrAccountHolder')
                vstrAccountNumber = self.request.get('vstrAccountNumber')
                vstrAccountType = self.request.get('vstrAccountType')
                vstrBankName = self.request.get('vstrBankName')
                vstrBranchCode = self.request.get('vstrBranchCode')
                vstrRoutingNumber = self.request.get('vstrRoutingNumber')

                findRequest = CliBankDetails.query(CliBankDetails.strClientID == vstrClientID)
                thisBankDetailsList = findRequest.fetch()

                if len(thisBankDetailsList) > 0:
                    thisBankDetail = thisBankDetailsList[0]
                else:
                    thisBankDetail = CliBankDetails()

                thisBankDetail.writeReference(strinput=Guser.user_id())
                thisBankDetail.writeAccountHolder(strinput=vstrAccountHolder)
                thisBankDetail.writeAccountNumber(strinput=vstrAccountNumber)
                thisBankDetail.writeAccountType(strinput=vstrAccountType)
                thisBankDetail.writeBankName(strinput=vstrBankName)
                thisBankDetail.writeBranchCode(strinput=vstrBranchCode)
                thisBankDetail.writeRoutingNumber(strinput=vstrRoutingNumber)
                thisBankDetail.put()

                self.response.write("Bank Details successfully updated")

            elif vstrChoice == "9":
                vstrClientID = self.request.get('vstrClientID')

                findRequest = CliProducts.query(CliProducts.strClientID == vstrClientID)
                thisProductsList = findRequest.fetch()


                template = template_env.get_template("templates/admin/churches/branches/suppliers/clproducts.html")
                context = {'thisProductsList':thisProductsList}
                self.response.write(template.render(context))

            elif vstrChoice == "10":
                vstrClientID = self.request.get('vstrClientID')
                vstrProductName = self.request.get('vstrProductName')
                vstrDescription = self.request.get('vstrDescription')
                vstrProductCost = self.request.get('vstrProductCost')
                vstrDepositAmount = self.request.get('vstrDepositAmount')

                findRequest = CliProducts.query(CliProducts.strClientID == vstrClientID,CliProducts.strProductName == vstrProductName)
                thisProductsList = findRequest.fetch()

                if len(thisProductsList) > 0:
                    thisProduct = thisProductsList[0]
                else:
                    thisProduct = CliProducts()

                thisProduct.writeClientID(strinput=vstrClientID)
                thisProduct.writeProductName(strinput=vstrProductName)
                thisProduct.writeProductDescription(strinput=vstrDescription)
                thisProduct.writeProductCost(strinput=vstrProductCost)
                thisProduct.writeDepositAmount(strinput=vstrDepositAmount)
                thisProduct.put()
                self.response.write("Product successfully updated")

            elif vstrChoice == "11":
                vstrClientID = self.request.get('vstrClientID')

                findRequest = CliServices.query(CliServices.strClientID == vstrClientID)
                thisServicesList = findRequest.fetch()

                template = template_env.get_template("templates/admin/churches/branches/suppliers/clservice.html")
                context = {'thisServiceList':thisServicesList}
                self.response.write(template.render(context))
            elif vstrChoice == "12":
                vstrClientID = self.request.get('vstrClientID')

                vstrServiceName = self.request.get('vstrServiceName')
                vstrDescription = self.request.get('vstrDescription')
                vstrServiceCost = self.request.get('vstrServiceCost')
                vstrDepositAmount = self.request.get('vstrDepositAmount')

                findRequest = CliServices.query(CliServices.strClientID == vstrClientID,CliServices.strServiceName == vstrServiceName)
                thisServiceList = findRequest.fetch()

                if len(thisServiceList) > 0:
                    thisService = thisServiceList[0]
                else:
                    thisService = CliServices()

                thisService.writeClientID(strinput=vstrClientID)
                thisService.writeServiceName(strinput=vstrServiceName)
                thisService.writeDescription(strinput=vstrDescription)
                thisService.writeServiceCost(strinput=vstrServiceCost)
                thisService.writeDepositAmount(strinput=vstrDepositAmount)
                thisService.put()

                self.response.write("Service Uploaded Successfully")

            elif vstrChoice == "13":
                vstrClientID = self.request.get('vstrClientID')
                vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                vstrChurchID = self.request.get('vstrChurchID')

                findRequest = CliContact.query(CliContact.strClientID == vstrClientID)
                thisClientList = findRequest.fetch()

                if len(thisClientList) > 0:
                    thisClient = thisClientList[0]
                else:
                    thisClient = CliContact()

                findRequest = SupplierMessaging.query(SupplierMessaging.strSupplierID == vstrClientID)
                thisClientMessagingList = findRequest.fetch()

                template = template_env.get_template('templates/admin/churches/branches/serviceprovider/messaging.html')
                context = {'thisClientMessagingList':thisClientMessagingList,'thisClient':thisClient}
                self.response.write(template.render(context))



                #TODO- Write the messaging module for suppliers and service providers and donators, the module will rest inside suppliers.py

            elif vstrChoice == "14":
                vstrClientID = self.request.get('vstrClientID')
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

                    findRequest = SMSPortalBudget.query()
                    thisPortalList = findRequest.fetch()
                    if len(thisPortalList) > 0:
                        thisPortal = thisPortalList[0]
                    else:
                        thisPortal = SMSPortalBudget()

                    if thisSMSAccount.strTotalSMS > 0:
                        strRef = thisPortal.SendCronMessage(strMessage=vstrMessage,strCell=vstrCell)
                        vstrThisDate = datetime.datetime.now()
                        strThisDate = vstrThisDate.date()
                        strThisTime = datetime.time(hour=vstrThisDate.hour,minute=vstrThisDate.minute,second=vstrThisDate.second)
                        if not(strRef == None):
                            thisMessaging = SupplierMessaging()
                            thisMessaging.writeSupplierID(strinput=vstrClientID)
                            thisMessaging.writeRef(strinput=strRef)
                            thisMessaging.writeMessage(strinput=vstrMessage)
                            thisMessaging.writeChurchBranchID(strinput=thisAdmin.strChurchBranchID)
                            thisMessaging.writeChurchID(strinput=thisAdmin.strChurchID)
                            thisMessaging.writeDateSent(strinput=strThisDate)
                            thisMessaging.writeTimeSent(strinput=strThisTime)
                            thisMessaging.put()
                            thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS  - 1
                            thisSMSAccount.put()
                            self.response.write("Message Sent successfully")
                        else:
                            self.response.write("Error Sending Message")

                    else:
                        self.response.write("Insufficient SMS Credit")
                else:
                    self.response.write("Fatal Error accessing your SMS Account")



































class SupplierHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChurchID = self.request.get('vstrChurchID')
            vstrChurchBranchID = self.request.get('vstrChurchBranchID')

            findRequest = Suppliers.query(Suppliers.strChurchID == vstrChurchID, Suppliers.strChurchBranchID == vstrChurchBranchID)
            thisSuppliersList = findRequest.fetch()

            template = template_env.get_template('templates/admin/churches/branches/suppliers/supplier.html')
            context = {'thisSuppliersList':thisSuppliersList}
            self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChurchID = self.request.get('vstrChurchID')
            vstrChurchBranchID = self.request.get('vstrChurchBranchID')
            vstrCompanyName = self.request.get('vstrCompanyName')
            vstrCompanyReg = self.request.get('vstrCompanyReg')
            vstrVAT = self.request.get('vstrVAT')
            vstrCPNames = self.request.get('vstrCPNames')
            vstrCPSurname = self.request.get('vstrCPSurname')
            vstrCPIDNumber = self.request.get('vstrCPIDNumber')
            vstrCPPosition = self.request.get('vstrCPPosition')


            findRequest = Suppliers.query(Suppliers.strChurchID == vstrChurchID,Suppliers.strChurchBranchID == vstrChurchBranchID)
            thisSuppliersList = findRequest.fetch()

            if len(thisSuppliersList) > 0:
                thisSupplier = thisSuppliersList[0]
            else:
                thisSupplier = Suppliers()

            thisSupplier.writeChurchID(strinput=vstrChurchID)
            thisSupplier.writeChurchBranchID(strinput=vstrChurchBranchID)
            thisSupplier.writeCompanyName(strinput=vstrCompanyName)
            thisSupplier.writeCompanyReg(strinput=vstrCompanyReg)
            thisSupplier.writeVAT(strinput=vstrVAT)
            thisSupplier.writeCPNames(strinput=vstrCPNames)
            thisSupplier.writeCPSurname(strinput=vstrCPSurname)
            thisSupplier.writeCPIDNumber(strinput=vstrCPIDNumber)

            thisDay = datetime.datetime.now()
            thisDay = thisDay.date()
            strYear = thisDay.year
            strMonth = thisDay.month
            strDay = thisDay.day

            thisTime = datetime.datetime.now()
            thisTime = thisTime.time()

            strHour = thisTime.hour
            strMin = thisTime.minute
            strSecond = thisTime.second

            thisTime = datetime.time(hour=strHour,minute=strMin,second=strSecond)

            thisSupplier.writeYearRegistered(strinput=str(strYear))
            thisSupplier.writeMonthRegistered(strinput=str(strMonth))
            thisSupplier.writeDayRegistered(strinput=str(strDay))

            thisSupplier.writeTimeRegistered(strinput=thisTime)

            thisSupplier.writeReference(strinput=Guser.user_id())
            thisSupplier.writeSupplierID(strinput=thisSupplier.createSupplierID())
            thisSupplier.writeCPPostion(strinput=vstrCPPosition)

            thisSupplier.put()

            self.response.write("Supplier Added Successfully")



class thisSupplierHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            URL = self.request.url
            URLlist = URL.split('/')

            vstrSupplierID = URLlist[len(URLlist) - 1]

            findRequest = Suppliers.query(Suppliers.strSupplierID == vstrSupplierID)
            thisSuppliersList = findRequest.fetch()

            if len(thisSuppliersList) > 0:
                thisSupplier = thisSuppliersList[0]
            else:
                thisSupplier = Suppliers()

            template  =template_env.get_template('templates/admin/churches/branches/suppliers/thisSupplier.html')
            context = {'thisSupplier':thisSupplier}
            self.response.write(template.render(context))


    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "0":
                vstrSupplierID = self.request.get('vstrSupplierID')
                vstrChurchID = self.request.get('vstrChurchID')

                findRequest = Suppliers.query(Suppliers.strSupplierID == vstrSupplierID)
                thisSupplierList = findRequest.fetch()

                if len(thisSupplierList) > 0:
                    thisSupplier = thisSupplierList[0]
                else:
                    thisSupplier = Suppliers()

                template = template_env.get_template('templates/admin/churches/branches/suppliers/sub/supinf.html')
                context = {'thisSupplier':thisSupplier}
                self.response.write(template.render(context))

            elif vstrChoice == "1":
                vstrSupplierID = self.request.get('vstrSupplierID')

                findRequest = SupPhyAddress.query(SupPhyAddress.strSupplierID == vstrSupplierID)
                thisPhysicalList = findRequest.fetch()

                if len(thisPhysicalList) > 0:
                    thisPhysical = thisPhysicalList[0]
                else:
                    thisPhysical = SupPhyAddress()

                template = template_env.get_template('templates/admin/churches/branches/suppliers/sub/physical.html')
                context = {'thisPhysical':thisPhysical,'vstrSupplierID':vstrSupplierID}
                self.response.write(template.render(context))

            elif vstrChoice == "2":
                vstrSupplierID = self.request.get('vstrSupplierID')

                findRequest = SupPosAddress.query(SupPosAddress.strSupplierID == vstrSupplierID)
                thisPosAddressList = findRequest.fetch()
                if len(thisPosAddressList) > 0:
                    thisPostal = thisPosAddressList[0]
                else:
                    thisPostal = SupPosAddress()

                template = template_env.get_template('templates/admin/churches/branches/suppliers/sub/postal.html')
                context = {'thisPostal':thisPostal,'vstrSupplierID':vstrSupplierID}
                self.response.write(template.render(context))

            elif vstrChoice == "3":
                vstrSupplierID = self.request.get('vstrSupplierID')

                findRequest = SupContact.query(SupContact.strSupplierID == vstrSupplierID)
                thisContactList = findRequest.fetch()

                if len(thisContactList) > 0:
                    thisContact = thisContactList[0]
                else:
                    thisContact = SupContact()

                template = template_env.get_template('templates/admin/churches/branches/suppliers/sub/contacts.html')
                context = {'thisContact':thisContact,'vstrSupplierID':vstrSupplierID}
                self.response.write(template.render(context))

            elif vstrChoice == "4":
                vstrSupplierID = self.request.get('vstrSupplierID')

                findRequest = SupBankDetails.query(SupBankDetails.strSupplierID == vstrSupplierID)
                thisBankDetailsList = findRequest.fetch()

                if len(thisBankDetailsList) > 0:
                    thisBankDetail = thisBankDetailsList[0]
                else:
                    thisBankDetail = SupBankDetails()

                template = template_env.get_template('templates/admin/churches/branches/suppliers/sub/bank.html')
                context = {'thisBankDetail':thisBankDetail,'vstrSupplierID':vstrSupplierID}
                self.response.write(template.render(context))

            elif vstrChoice == "5":

                vstrSupplierID = self.request.get('vstrSupplierID')
                vstrAccountHolder = self.request.get('vstrAccountHolder')
                vstrAccountNumber = self.request.get('vstrAccountNumber')
                vstrAccountType = self.request.get('vstrAccountType')
                vstrBankName = self.request.get('vstrBankName')
                vstrBranchCode = self.request.get('vstrBranchCode')



                findRequest = SupBankDetails.query(SupBankDetails.strSupplierID == vstrSupplierID)
                thisBankDetailList = findRequest.fetch()

                if len(thisBankDetailList) > 0:
                    thisBankDetail = thisBankDetailList[0]
                else:
                    thisBankDetail = SupBankDetails()

                thisBankDetail.writeSupplierID(strinput=vstrSupplierID)
                thisBankDetail.writeAccountHolder(strinput=vstrAccountHolder)
                thisBankDetail.writeAccountNumber(strinput=vstrAccountNumber)
                thisBankDetail.writeAccountType(strinput=vstrAccountType)
                thisBankDetail.writeBankName(strinput=vstrBankName)
                thisBankDetail.writeBranchCode(strinput=vstrBranchCode)

                thisBankDetail.put()
                self.response.write("Successfully updated Bank Details")

            elif vstrChoice == "6":
                vstrSupplierID = self.request.get('vstrSupplierID')
                vstrCell = self.request.get('vstrCell')
                vstrTel = self.request.get('vstrTel')
                vstrFax = self.request.get('vstrFax')
                vstrEmail = self.request.get('vstrEmail')
                vstrWebsite = self.request.get('vstrWebsite')

                findRequest = SupContact.query(SupContact.strSupplierID == vstrSupplierID)
                thisContactList = findRequest.fetch()

                if len(thisContactList) > 0:
                    thisContact = thisContactList[0]
                else:
                    thisContact = SupContact()

                thisContact.writeSupplierID(strinput=vstrSupplierID)
                thisContact.writeCell(strinput=vstrCell)
                thisContact.writeTel(strinput=vstrTel)
                thisContact.writeFax(strinput=vstrFax)
                thisContact.writeEmail(strinput=vstrEmail)
                thisContact.writeWebsite(strinput=vstrWebsite)
                thisContact.put()
                self.response.write("Supplier Contact Updated Successfully")
                
            elif vstrChoice == "7":
                vstrSupplierID = self.request.get('vstrSupplierID')
                vstrPostalAddress = self.request.get('vstrPostalAddress')
                vstrCityTown = self.request.get('vstrCityTown')
                vstrProvince = self.request.get('vstrProvince')
                vstrCountry = self.request.get('vstrCountry')
                vstrPostalCode = self.request.get('vstrPostalCode')
                
                findRequest = SupPosAddress.query(SupPosAddress.strSupplierID == vstrSupplierID)
                thisPostalList = findRequest.fetch()

                if len(thisPostalList) > 0:
                    thisPostal = thisPostalList[0]
                else:
                    thisPostal = SupPosAddress()

                thisPostal.writeSupplierID(strinput=vstrSupplierID)
                thisPostal.writePostalAddress(strinput=vstrPostalAddress)
                thisPostal.writeCityTown(strinput=vstrCityTown)
                thisPostal.writeProvince(strinput=vstrProvince)
                thisPostal.writeCountry(strinput=vstrCountry)
                thisPostal.writePostalCode(strinput=vstrPostalCode)
                thisPostal.put()

                self.response.write("Postal Address Successfully updated")

            elif vstrChoice == "8":
                vstrSupplierID = self.request.get('vstrSupplierID')
                vstrStandNumber = self.request.get('vstrStandNumber')
                vstrStreetName = self.request.get('vstrStreetName')
                vstrCityTown = self.request.get('vstrCityTown')
                vstrProvince = self.request.get('vstrProvince')
                vstrCountry = self.request.get('vstrCountry')
                vstrPostalCode = self.request.get('vstrPostalCode')

                findRequest = SupPhyAddress.query(SupPhyAddress.strSupplierID == vstrSupplierID)
                thisPhysicalList = findRequest.fetch()

                if len(thisPhysicalList) > 0:
                    thisPhysical = thisPhysicalList[0]
                else:
                    thisPhysical = SupPhyAddress()

                thisPhysical.writeSupplierID(strinput=vstrSupplierID)
                thisPhysical.writeStandNumber(strinput=vstrStandNumber)
                thisPhysical.writeStreetName(strinput=vstrStreetName)
                thisPhysical.writeCityTown(strinput=vstrCityTown)
                thisPhysical.writeProvince(strinput=vstrProvince)
                thisPhysical.writeCountry(strinput=vstrCountry)
                thisPhysical.writePostalCode(strinput=vstrPostalCode)
                thisPhysical.put()
                self.response.write("Successfully updated physical address")


            elif vstrChoice == "9":
                vstrSupplierID = self.request.get('vstrSupplierID')
                vstrCompanyName = self.request.get('vstrCompanyName')
                vstrCompanyReg = self.request.get('vstrCompanyReg')
                vstrVAT = self.request.get('vstrVAT')
                vstrCPNames = self.request.get('vstrCPNames')
                vstrCPSurname = self.request.get('vstrCPSurname')
                vstrCPIDNumber = self.request.get('vstrCPIDNumber')
                vstrCPPosition = self.request.get('vstrCPPosition')


                findRequest = Suppliers.query(Suppliers.strSupplierID == vstrSupplierID)
                thisSupplierList = findRequest.fetch()

                if len(thisSupplierList) > 0:
                    thisSupplier = thisSupplierList[0]
                else:
                    thisSupplier = Suppliers()

                thisSupplier.writeSupplierID(strinput=vstrSupplierID)
                thisSupplier.writeCompanyName(strinput=vstrCompanyName)
                thisSupplier.writeCompanyReg(strinput=vstrCompanyReg)
                thisSupplier.writeVAT(strinput=vstrVAT)
                thisSupplier.writeCPNames(strinput=vstrCPNames)
                thisSupplier.writeCPSurname(strinput=vstrCPSurname)
                thisSupplier.writeCPIDNumber(strinput=vstrCPIDNumber)
                thisSupplier.writeCPPostion(strinput=vstrCPPosition)
                thisSupplier.put()
                self.response.write("Supplier Updated Successfully")

            elif vstrChoice == "10":
                vstrSupplierID = self.request.get('vstrSupplierID')

                findRequest = SupProducts.query(SupProducts.strSupplierID == vstrSupplierID)
                thisProductsList = findRequest.fetch()

                template = template_env.get_template('templates/admin/churches/branches/suppliers/sub/products.html')
                context = {'thisProductsList':thisProductsList}
                self.response.write(template.render(context))


            elif vstrChoice == "11":
                vstrSupplierID = self.request.get('vstrSupplierID')
                vstrProductName = self.request.get('vstrProductName')
                vstrDescription = self.request.get('vstrDescription')
                vstrProductCost = self.request.get('vstrProductCost')
                vstrDepositAmount = self.request.get('vstrDepositAmount')

                findRequest = SupProducts.query(SupProducts.strProductName == vstrProductName,SupProducts.strSupplierID == vstrSupplierID)
                thisProductsList = findRequest.fetch()

                if len(thisProductsList) > 0:
                    thisProducts = thisProductsList[0]
                else:
                    thisProducts = SupProducts()

                thisProducts.writeSupplierID(strinput=vstrSupplierID)
                thisProducts.writeProductName(strinput=vstrProductName)
                thisProducts.writeDescription(strinput=vstrDescription)
                thisProducts.writeProductCost(strinput=vstrProductCost)
                thisProducts.writeDepositAmount(strinput=vstrDepositAmount)
                thisProducts.put()
                self.response.write("Products Successfully updated")

            elif vstrChoice == "12":
                vstrSupplierID = self.request.get('vstrSupplierID')

                findRequest = SupServices.query(SupServices.strSupplierID == vstrSupplierID)
                thisServicesList = findRequest.fetch()

                template = template_env.get_template('templates/admin/churches/branches/suppliers/sub/services.html')
                context = {'thisServicesList':thisServicesList}
                self.response.write(template.render(context))

            elif vstrChoice == "13":
                vstrSupplierID = self.request.get('vstrSupplierID')

                vstrServiceName = self.request.get('vstrServiceName')
                vstrDescription  =self.request.get('vstrDescription')
                vstrServiceCost = self.request.get('vstrServiceCost')
                vstrDepositAmount = self.request.get('vstrDepositAmount')

                findRequest = SupServices.query(SupServices.strSupplierID == vstrSupplierID,SupServices.strServiceName == vstrServiceName)
                thisServicesList = findRequest.fetch()

                if len(thisServicesList) > 0:
                    thisService = thisServicesList[0]
                else:
                    thisService = SupServices()

                thisService.writeSupplierID(strinput=vstrSupplierID)
                thisService.writeServiceName(strinput=vstrServiceName)
                thisService.writeDescription(strinput=vstrDescription)
                thisService.writeServiceCost(strinput=vstrServiceCost)
                thisService.writeDepositAmount(strinput=vstrDepositAmount)
                thisService.put()
                self.response.write("Service Updated Successfully")


app = webapp2.WSGIApplication([
    ('/admin/clients', ClientsHandler),
    ('/admin/clients/.*', thisClientHandler),
    ('/admin/supplier', SupplierHandler),
    ('/admin/suppliers/.*',thisSupplierHandler)

], debug=True)
