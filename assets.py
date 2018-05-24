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
from google.appengine.ext import ndb
from google.appengine.api import users
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class Asset(ndb.Expando):

    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()


    strAssetID = ndb.StringProperty() # For Internall tracking and control
    strAssetCode = ndb.StringProperty() # For Barcodes
    strAssetName = ndb.StringProperty()
    strAssetDescription = ndb.StringProperty()

    strPurchasePrice = ndb.StringProperty()
    strDepreciation = ndb.StringProperty()
    strCurrentValue = ndb.StringProperty()

    strAssetType = ndb.StringProperty(default="movable") # un-movable

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
    def writeAssetID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAssetID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAssetCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAssetCode = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAssetName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAssetName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAssetDescription(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAssetDescription = strinput
                return True
            else:
                return False
        except:
            return False
    def writePurchasePrice(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPurchasePrice = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDepreciation(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strDepreciation = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCurrentValue(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCurrentValue = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAssetType(self,strinput):
        try:
            strinput = str(strinput)
            if strinput in ['movable','un-movable']:
                self.strAssetType = strinput
                return True
            else:
                return False
        except:
            return False
    def createAssetID(self):
        try:
            findRequest = Asset.query()
            thisAssetList = findRequest.fetch()
            strIndex = len(thisAssetList)
            Guser = users.get_current_user()
            strAssetID =  str(Guser.user_id()) + str(strIndex)
            return strAssetID
        except:
            return None

class AssetLocation(ndb.Expando):
    strAssetID = ndb.StringProperty()
    strBuildingName = ndb.StringProperty()
    strOfficeNumber = ndb.StringProperty()
    strStandNumber = ndb.StringProperty()
    strStreetName = ndb.StringProperty()
    strCityTown = ndb.StringProperty()
    strProvince = ndb.StringProperty()
    strCountry = ndb.StringProperty()
    strPostalCode = ndb.StringProperty()

    def writeAssetID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAssetID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBuildingName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBuildingName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOfficeNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOfficeNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStandNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strStandNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeStreetName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strStreetName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCityTown(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCityTown = strinput
                return True
            else:
                return False
        except:
            return False
    def writeProvince(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strProvince = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCountry(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCountry = strinput
                return True
            else:
                return False
        except:
            return False
    def writePostalCode(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strPostalCode = strinput
                return True
            else:
                return False
        except:
            return False

class thisAssetsHandler(webapp2.RequestHandler):
    def get(self):
        URL = self.request.url
        URLlist = URL.split("/")
        vstrAssetID = URLlist[len(URLlist) - 1]

        findRequest = Asset.query(Asset.strAssetID == vstrAssetID)
        thisAssetList = findRequest.fetch()

        if len(thisAssetList) > 0:
            thisAsset = thisAssetList[0]
        else:
            thisAsset = Asset()


        findRequest = AssetLocation.query(Asset.strAssetID == vstrAssetID)
        thisAssetLocationList = findRequest.fetch()

        if len(thisAssetLocationList) > 0:
            thisAssetLocation = thisAssetLocationList[0]
        else:
            thisAssetLocation = AssetLocation()



        template = template_env.get_template('templates/assets/asset.html')
        context = {'thisAssetLocation':thisAssetLocation,'thisAsset':thisAsset}
        self.response.write(template.render(context))

class AssetHandler(webapp2.RequestHandler):
    def get(self):
        vstrChoice = self.request.get('vstrChoice')

        if vstrChoice == "0":
            vstrAssetCode = self.request.get('vstrAssetCode')
            vstrAssetID = self.request.get('vstrAssetID')
            vstrAssetName = self.request.get('vstrAssetName')
            vstrAssetDescription = self.request.get('vstrAssetDescription')
            vstrPurchasePrice = self.request.get('vstrPurchasePrice')
            vstrDepreciation = self.request.get('vstrDepreciation')
            vstrCurrentValue = self.request.get('vstrCurrentValue')
            vstrAssetType = self.request.get('vstrAssetType')

            findRequest = Asset.query(Asset.strAssetID == vstrAssetID)
            thisAssetList = findRequest.fetch()

            if len(thisAssetList) > 0:
                thisAsset = thisAssetList[0]
            else:
                thisAsset = Asset()

            thisAsset.writeAssetCode(strinput=vstrAssetCode)
            thisAsset.writeAssetID(strinput=vstrAssetID)
            thisAsset.writeAssetName(strinput=vstrAssetName)
            thisAsset.writeAssetDescription(strinput=vstrAssetDescription)
            thisAsset.writePurchasePrice(strinput=vstrPurchasePrice)
            thisAsset.writeDepreciation(strinput=vstrDepreciation)
            thisAsset.writeCurrentValue(strinput=vstrCurrentValue)
            thisAsset.writeAssetType(strinput=vstrAssetType)

            thisAsset.put()

            self.response.write('Asset Successfully Updated...')

        elif vstrChoice == "1":
            vstrBuildingName = self.request.get('vstrBuildingName')
            vstrOfficeNumber = self.request.get('vstrOfficeNumber')
            vstrStandNumber = self.request.get('vstrStandNumber')
            vstrStreetName = self.request.get('vstrStreetName')
            vstrCityTown = self.request.get('vstrCityTown')
            vstrProvince = self.request.get('vstrProvince')
            vstrCountry = self.request.get('vstrCountry')
            vstrPostalCode = self.request.get('vstrPostalCode')
            vstrAssetID = self.request.get('vstrAssetID')

            findRequest = AssetLocation.query(AssetLocation.strAssetID == vstrAssetID)
            thisAssetList = findRequest.fetch()

            if len(thisAssetList) > 0:
                thisAsset = thisAssetList[0]
            else:
                thisAsset = AssetLocation()

            thisAsset.writeAssetID(strinput=vstrAssetID)
            thisAsset.writeBuildingName(strinput=vstrBuildingName)
            thisAsset.writeOfficeNumber(strinput=vstrOfficeNumber)
            thisAsset.writeStandNumber(strinput=vstrStandNumber)
            thisAsset.writeStreetName(strinput=vstrStreetName)
            thisAsset.writeCityTown(strinput=vstrCityTown)
            thisAsset.writeProvince(strinput=vstrProvince)
            thisAsset.writeCountry(strinput=vstrCountry)
            thisAsset.writePostalCode(strinput=vstrPostalCode)

            thisAsset.put()

            self.response.write("Successfully updated asset location")


app = webapp2.WSGIApplication([
    ('/assets/.*', thisAssetsHandler),
    ('/assets', AssetHandler)
], debug=True)