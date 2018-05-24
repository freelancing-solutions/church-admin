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
import logging
import datetime
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

from userRights import UserRights
from employees import Employees, Salaries
from assets import Asset,AssetLocation
from monetary import Costs,Bank,BankAccount,PaymentsMade,Beneficiary,Pledge,Donation,Tithing
class Churches(ndb.Expando):
    strChurchID = ndb.StringProperty()
    strChurchName = ndb.StringProperty()
    strRegNumber = ndb.StringProperty()
    strChurchMotto = ndb.StringProperty()

    strDateFounded = ndb.DateProperty()
    strFounderTitle = ndb.StringProperty()
    strFounder = ndb.StringProperty()
    strFounderMemberID = ndb.StringProperty() # a Member ID of Founder
    strVision = ndb.StringProperty()
    strMission = ndb.StringProperty()
    strPropheticWords = ndb.StringProperty()

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

    def createChurchID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                findRequest = Churches.query(Churches.strFounderMemberID == strinput)
                thisChurchesList = findRequest.fetch()
                self.strChurchID = strinput +  str(len(thisChurchesList))
                return True
            else:
                return False
        except:
            return False

    def writeChurchName(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChurchName = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFounderTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFounderTitle = strinput
                return True
            else:
                return False
        except:
            return False
    def writeRegNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strRegNumber = strinput
                return True
            else:
                return False
        except:
            return False

    def writeFounderMemberID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFounderMemberID = strinput
                return True
            else:
                return False
        except:
            return False

    def writeChurchMotto(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strChurchMotto = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateFounded(self,strinput):
        try:
            if strinput != None:
                self.strDateFounded = strinput
                return True
            else:
                return False
        except:
            return False
    def writeFounder(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFounder = strinput
                return True
            else:
                return False
        except:
            return False
    def writeVision(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strVision = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMission(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMission = strinput
                return True
            else:
                return False
        except:
            return False
    def writePropheticWord(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPropheticWords = strinput
                return True
            else:
                return False
        except:
            return False
class Branches(ndb.Expando):
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strBranchName = ndb.StringProperty()
    strBranchMotto = ndb.StringProperty()

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
    def writeBranchMotto(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBranchMotto = strinput
                return True
            else:
                return False
        except:
            return False
    def CreateBranchID(self):


        try:
            Guser = users.get_current_user()
            if Guser:

                findRequest = Branches.query()
                thisBranchesList = findRequest.fetch()

                thisIndex = len(thisBranchesList)

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

                vstrChurchName = thisChurch.strChurchName
                subChurchName = vstrChurchName[0:2]
                subChurchName = subChurchName.upper()

                strBranchID = subChurchName + str(thisIndex)
                return strBranchID
            else:
                return None
        except:
            return None
class BranchContactDetails(ndb.Expando):
    strChurchBranchID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()

    strPhyStandNumber = ndb.StringProperty()
    strPhyStreetName = ndb.StringProperty()
    strPhyCityTown = ndb.StringProperty()
    strPhyProvince = ndb.StringProperty()
    strPhyCountry = ndb.StringProperty()
    strPhyPostalCode = ndb.StringProperty()

    strPosAddress = ndb.StringProperty()
    strPosCityTown = ndb.StringProperty()
    strPosProvince = ndb.StringProperty()
    strPosCountry = ndb.StringProperty()
    strPostPostalCode = ndb.StringProperty()

    strTel = ndb.StringProperty()
    strFax = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strWebsite = ndb.StringProperty()

    strCPNames = ndb.StringProperty()
    strCPTitle = ndb.StringProperty()
    strCPGender = ndb.StringProperty()

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
    def writePosAddress(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPosAddress = strinput
                return True
            else:
                return False
        except:
            return True
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
                self.strPostPostalCode = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
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
    def writeFax(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strFax = strinput
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
    def writeCPNames(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCPNames = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCPTitle = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCPGender(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCPGender = strinput
                return True
            else:
                return False
        except:
            return False
class ChurchFixedAssets(ndb.Expando):

    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()

    strAssetType = ndb.StringProperty(default="Church Building") # Office, Halls,
    strAssetCode = ndb.StringProperty()
    strAssetCapacity = ndb.IntegerProperty(default=0)

    strAssetValue = ndb.IntegerProperty(default=0)

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
    def writeAssetType(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAssetType = strinput
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
    def writeAssetCapacity(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strAssetCapacity = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeAssetValue(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strAssetValue = int(strinput)
                return True
            else:
                return False
        except:
            return False
class ChurchMember(ndb.Expando):

    strMemberID = ndb.StringProperty()

    strProfileClaimed = ndb.BooleanProperty(default=False)

    strPositionInChurch = ndb.StringProperty(default="Member") # Priest, Decon, Asher,

    strChurchID = ndb.StringProperty() # The Church a Member Belongs to
    strChurchBranchID = ndb.StringProperty()

    strMemberNames = ndb.StringProperty()
    strMemberSurname = ndb.StringProperty()
    strMemberTitle = ndb.StringProperty()

    strMemberIDNumber = ndb.StringProperty()
    strMemberGender = ndb.StringProperty()

    strMemberDateOfBirth = ndb.DateProperty()
    strMemberDateOfMemberShip = ndb.DateProperty()
    strMemberDateBaptised = ndb.DateProperty()

    #For birthday purposes
    strYear = ndb.IntegerProperty()
    strMonth = ndb.IntegerProperty()
    strDay = ndb.IntegerProperty()

    strTel = ndb.StringProperty()
    strCell = ndb.StringProperty()
    strEmail = ndb.StringProperty()

    strWorkTel = ndb.StringProperty()
    strWorkCell = ndb.StringProperty()
    strWorkEmail = ndb.StringProperty()

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

    def writeProfileClaimed(self,strinput):
        """
            if profile is claimed Member ID Changes to the Users Own Reference Number
        :param strinput:
        :return:
        """
        try:
            if strinput in [True,False]:
                self.strProfileClaimed = strinput
                return  True
            else:
                return False
        except:
            return False
    def writeYear(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strYear = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeMonth(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strMonth = int(strinput)
                return True
            else:
                return False
        except:
            return False

    def writeDay(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strDay = int(strinput)
                return True
            else:
                return False
        except:
            return False


    def writePositionInChurch(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPositionInChurch = strinput
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
    def writeMemberNames(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMemberNames = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMemberSurname(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMemberSurname = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMemberTitle(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMemberTitle = strinput
                return True
            else:
                return False

        except:
            return False
    def writeMemberIDNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMemberIDNumber = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMemberGender(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMemberGender = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMemberDateOfBirth(self,strinput):
        try:

            if strinput != None:
                self.strMemberDateOfBirth = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMemberDateOfMembership(self,strinput):
        try:
            if strinput != None:
                self.strMemberDateOfMemberShip = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMemberDateBaptised(self,strinput):
        try:
            if strinput != None:
                self.strMemberDateBaptised = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTel = strinput
                return True
            else:
                return False
        except:
            return False
    def writeCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
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
    def writeWorkTel(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strWorkTel = strinput
                return True
            else:
                return False
        except:
            return False
    def writeWorkCell(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strWorkCell = strinput
                return True
            else:
                return False
        except:
            return False
    def writeWorkEmail(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strWorkEmail = strinput
                return True
            else:
                return False
        except:
            return False
class MemberAddresses(ndb.Expando):
    strMemberID = ndb.StringProperty()

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
class CurrentBranch(ndb.Expando):
    strMemberID = ndb.StringProperty()
    strCurrentBranchID = ndb.StringProperty()

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

    def writeCurrentBranchID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strCurrentBranchID = strinput
                return True
            else:
                return False

        except:
            return False

class MemberMessaging(ndb.Expando):
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

    def writeMessage(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strMessage = strinput
                return True
            else:
                return False
        except:
            return False
    def writeResponse(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strResponse = strinput
                return True

            else:
                return False
        except:
            return False
    def writeRef(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
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










class ChurchDetailsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRights = thisUserRightsList[0]
            else:
                thisUserRights = UserRights()

            if thisUserRights.strAdminUser:
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


                template = template_env.get_template('templates/admin/churches/churchdetails.html')
                context = {'thisChurch':thisChurch}
                self.response.write(template.render(context))
            else:
                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                template = template_env.get_template('templates/subRestricted.html')
                context = {'thisChurchMember':thisChurchMember}
                self.response.write(template.render(context))


    def post(self):
        Guser = users.get_current_user()
        if Guser:

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRights = thisUserRightsList[0]
            else:
                thisUserRights = UserRights()

            if thisUserRights.strAdminUser:
                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                logging.info("Church Member : " + str(thisChurchMember.strMemberID))
                logging.info("Reference : " + Guser.user_id())

                vstrChurchName = self.request.get('vstrChurchName')
                vstrRegNumber = self.request.get('vstrRegNumber')
                vstrChurchMotto = self.request.get('vstrChurchMotto')
                vstrVision = self.request.get('vstrVision')
                vstrMission = self.request.get('vstrMission')
                vstrPropheticWord = self.request.get('vstrPropheticWord')
                vstrFounderTitle = self.request.get('vstrFounderTitle')
                vstrFounder = self.request.get('vstrFounder')
                vstrDateFounded = self.request.get('vstrDateFounded')

                DateList = vstrDateFounded.split("-")
                thisYear = DateList[0]
                thisMonth = DateList[1]
                thisDay = DateList[2]

                vstrDateFounded = datetime.date(year=int(thisYear),month=int(thisMonth),day=int(thisDay))

                findRequest = Churches.query(Churches.strChurchID == thisChurchMember.strChurchID)
                thisChurchList = findRequest.fetch()

                if len(thisChurchList) > 0:
                    thisChurch = thisChurchList[0]
                else:
                    thisChurch = Churches()

                thisChurch.writeChurchID(thisChurchMember.strChurchID)
                thisChurch.writeFounderMemberID(thisChurchMember.strMemberID)
                thisChurch.writeChurchName(strinput=vstrChurchName)
                thisChurch.writeRegNumber(strinput=vstrRegNumber)
                thisChurch.writeChurchMotto(strinput=vstrChurchMotto)
                thisChurch.writeVision(strinput=vstrVision)
                thisChurch.writeMission(strinput=vstrMission)
                thisChurch.writePropheticWord(strinput=vstrPropheticWord)
                thisChurch.writeFounderTitle(strinput=vstrFounderTitle)
                thisChurch.writeFounder(strinput=vstrFounder)
                thisChurch.writeDateFounded(strinput=vstrDateFounded)

                thisChurch.put()

                self.response.write("Church Details Successfully Saved...")

class BranchesHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRights = thisUserRightsList[0]
            else:
                thisUserRights = UserRights()

            if thisUserRights.strAdminUser:
                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                findRequest = Branches.query(Branches.strChurchID == thisChurchMember.strChurchID)
                thisBranchesList = findRequest.fetch()


                template = template_env.get_template('templates/admin/churches/branches.html')
                context = {'thisBranchesList':thisBranchesList}
                self.response.write(template.render(context))
            else:
                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                template = template_env.get_template('templates/subRestricted.html')
                context = {'thisChurchMember':thisChurchMember}
                self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRights = thisUserRightsList[0]
            else:
                thisUserRights = UserRights()

            if thisUserRights.strAdminUser:
                findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                vstrBranchName = self.request.get('vstrBranchName')
                vstrBranchMotto = self.request.get('vstrBranchMotto')

                thisBranch = Branches()
                thisBranch.writeBranchName(strinput=vstrBranchName)
                thisBranch.writeBranchMotto(strinput=vstrBranchMotto)
                thisBranch.writeChurchBranchID(strinput=thisBranch.CreateBranchID())
                thisBranch.writeBranchMotto(vstrBranchMotto)
                thisBranch.writeChurchID(strinput=thisChurchMember.strChurchID)
                thisChurchMember.writeChurchBranchID(strinput=thisBranch.strChurchBranchID)
                thisChurchMember.put()

                thisBranch.put()

                self.response.write("Branch is successfully updated")

class thisBranchHandler(webapp2.RequestHandler):
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

                URL = self.request.url
                URLlist = URL.split("/")
                vstrBranchID = URLlist[len(URLlist) - 1]

                findRequest = Branches.query(Branches.strChurchBranchID == vstrBranchID)
                thisBranchesList = findRequest.fetch()

                if len(thisBranchesList) > 0:
                    thisBranch = thisBranchesList[0]
                    findRequest = CurrentBranch.query(CurrentBranch.strMemberID == Guser.user_id())
                    thisCurrentBranchList = findRequest.fetch()

                    if len(thisCurrentBranchList) > 0:
                        thisCurrentBranch = thisCurrentBranchList[0]
                    else:
                        thisCurrentBranch = CurrentBranch()

                    thisCurrentBranch.writeMemberID(strinput=Guser.user_id())
                    thisCurrentBranch.writeCurrentBranchID(strinput=thisBranch.strChurchBranchID)
                    thisCurrentBranch.put()
                    template = template_env.get_template('templates/admin/churches/branches/thisBranch.html')
                    context = {'thisBranch':thisBranch}
                    self.response.write(template.render(context))
                else:
                    thisBranch = Branches()


            else:
                self.response.write("Not Authorised to use this resource")


    def post(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()
            if len(thisUserRightsList) > 0:
                thisUserRights = thisUserRightsList[0]
            else:
                thisUserRights = UserRights()

            if thisUserRights.strAdminUser or thisUserRights.strSuperUser:
                vstrChoice = self.request.get('vstrChoice')
                if vstrChoice == "10":
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrChurchID = self.request.get('vstrChurchID')

                    findRequest = BranchContactDetails.query(BranchContactDetails.strChurchBranchID == vstrChurchBranchID, BranchContactDetails.strChurchID == vstrChurchID)
                    thisBranchContactDetailsList = findRequest.fetch()

                    if len(thisBranchContactDetailsList) > 0:
                        thisBranchContact = thisBranchContactDetailsList[0]
                    else:
                        thisBranchContact = BranchContactDetails()
                        thisBranchContact.writeChurchID(strinput=vstrChurchID)
                        thisBranchContact.writeChurchBranchID(strinput=vstrChurchBranchID)
                        thisBranchContact.put()

                    template = template_env.get_template('templates/admin/churches/branches/branchcontact.html')
                    context = {'thisBranchContact':thisBranchContact}
                    self.response.write(template.render(context))

                elif vstrChoice == "11":
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrChurchID = self.request.get('vstrChurchID')


                    findRequest = BranchContactDetails.query(BranchContactDetails.strChurchID == vstrChurchID, BranchContactDetails.strChurchBranchID == vstrChurchBranchID )
                    thisBranchContactDetailsList = findRequest.fetch()

                    if len(thisBranchContactDetailsList) > 0:
                        thisBranchContact = thisBranchContactDetailsList[0]
                    else:
                        thisBranchContact = BranchContactDetails()

                    thisBranchContact.writeChurchID(strinput=vstrChurchID)
                    thisBranchContact.writeChurchBranchID(strinput=vstrChurchBranchID)
                    thisBranchContact.writePhyStandNumber(strinput=str(self.request.get('vstrPhyStandNumber')))
                    thisBranchContact.writePhyStreetName(strinput=str(self.request.get('vstrPhyStreetName')))
                    thisBranchContact.writePhyCityTown(strinput=str(self.request.get('vstrPhyCityTown')))
                    thisBranchContact.writePhyProvince(strinput=str(self.request.get('vstrPhyProvince')))
                    thisBranchContact.writePhyCountry(strinput=str(self.request.get('vstrPhyCountry')))
                    thisBranchContact.writePhyPostalCode(strinput=str(self.request.get('vstrPhyPostalCode')))
                    thisBranchContact.writePosAddress(strinput=str(self.request.get('vstrPosAddress')))
                    thisBranchContact.writePosCityTown(strinput=str(self.request.get('vstrPosCityTown')))
                    thisBranchContact.writePosProvince(strinput=str(self.request.get('vstrPosProvince')))
                    thisBranchContact.writePosCountry(strinput=str(self.request.get('vstrPosCountry')))
                    thisBranchContact.writePosPostalCode(strinput=str(self.request.get('vstrPostPostalCode')))
                    thisBranchContact.writeTel(strinput=str(self.request.get('vstrTel')))
                    thisBranchContact.writeCell(strinput=str(self.request.get('vstrCell')))
                    thisBranchContact.writeFax(strinput=str(self.request.get('vstrFax')))
                    thisBranchContact.writeEmail(strinput=str(self.request.get('vstrEmail')))
                    thisBranchContact.writeWebsite(strinput=str(self.request.get('vstrWebsite')))
                    thisBranchContact.writeCPNames(strinput=str(self.request.get('vstrCPNames')))
                    thisBranchContact.writeTitle(strinput=str(self.request.get('vstrCPTitle')))
                    thisBranchContact.writeCPGender(strinput=str(self.request.get('vstrCPGender')))

                    thisBranchContact.put()

                    self.response.write('Branch Contacts Successfully Updated')

                elif vstrChoice == "12":
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrChurchID = self.request.get('vstrChurchID')

                    findRequest = Bank.query(Bank.strChurchID == vstrChurchID, Bank.strChurchBranchID == vstrChurchBranchID)
                    thisBankList = findRequest.fetch()

                    findRequest = BankAccount.query(BankAccount.strChurchID == vstrChurchID, BankAccount.strChurchBranchID == vstrChurchBranchID)
                    thisBankAccountList = findRequest.fetch()

                    findRequest = PaymentsMade.query(PaymentsMade.strChurchID == vstrChurchID, PaymentsMade.strChurchBranchID == vstrChurchBranchID, PaymentsMade.strAuthorised == True)
                    thisPaymentsList = findRequest.fetch()

                    findRequest = Beneficiary.query()
                    thisClientList = findRequest.fetch()

                    findRequest = PaymentsMade.query(PaymentsMade.strChurchID == vstrChurchID, PaymentsMade.strChurchBranchID == vstrChurchBranchID, PaymentsMade.strAuthorised == False)
                    thisAuthorisePaymentsList = findRequest.fetch()

                    template = template_env.get_template('templates/admin/churches/branches/bank.html')
                    context = {'thisBankList':thisBankList,'thisBankAccountList':thisBankAccountList,'vstrChurchBranchID':vstrChurchBranchID,
                               'vstrChurchID':vstrChurchID,'thisPaymentsList':thisPaymentsList,'thisClientList': thisClientList,'thisAuthorisePaymentsList':thisAuthorisePaymentsList }
                    self.response.write(template.render(context))

                elif vstrChoice == "13":
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrChurchID = self.request.get('vstrChurchID')

                    findRequest = BankAccount.query(BankAccount.strChurchID == vstrChurchID, BankAccount.strChurchBranchID == vstrChurchBranchID)
                    thisBankAccountList = findRequest.fetch()

                    if len(thisBankAccountList) > 0:
                        thisBankAccount = thisBankAccountList[0]
                    else:
                        thisBankAccount = BankAccount()

                    thisBankAccount.writeChurchBranchID(strinput=vstrChurchBranchID)
                    thisBankAccount.writeChurchID(strinput=vstrChurchID)
                    thisBankAccount.writeAccountHolder(strinput=str(self.request.get('vstrAccountHolder')))
                    thisBankAccount.writeAccountNumber(strinput=str(self.request.get('vstrAccountNumber')))
                    thisBankAccount.writeAccountType(strinput=str(self.request.get('vstrAccountType')))
                    thisBankAccount.writeBankName(strinput=str(self.request.get('vstrBankName')))
                    thisBankAccount.writeBranchName(strinput=str(self.request.get('vstrBranchName')))
                    thisBankAccount.writeBranchCode(strinput=str(self.request.get('vstrBranchCode')))
                    thisBankAccount.writeRoutingNumber(strinput=str(self.request.get('vstrRoutingNumber')))

                    thisBankAccount.put()

                    self.response.write("Bank Account Number updated Successfully")


                elif vstrChoice == "14":
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrChurchID = self.request.get('vstrChurchID')
                    vstrPaymentType = self.request.get('vstrPaymentType')
                    vstrPaymentAmount = self.request.get('vstrPaymentAmount')
                    vstrReasonForPayment = self.request.get('vstrReasonForPayment')
                    vstrPayFrom = self.request.get('vstrPayFrom')
                    vstrPaidToClient = self.request.get('vstrPaidToClient')

                    findRequest = PaymentsMade.query()
                    thisPaymentsList = findRequest.fetch()

                    strIndex = len(thisPaymentsList)

                    thisPayment = PaymentsMade()
                    thisPayment.writeChurchID(strinput=vstrChurchID)
                    thisPayment.writeChurchBranchID(strinput=vstrChurchBranchID)
                    thisPayment.writeReference(strinput=Guser.user_id())
                    thisPayment.writePaymentIndex(strinput=str(strIndex+1))
                    thisPayment.writePaymentType(strinput=vstrPaymentType)
                    thisPayment.writePaymentAmount(strinput=vstrPaymentAmount)
                    thisPayment.writePayFrom(strinput=vstrPayFrom)
                    thisPayment.writeReasonForPayment(strinput=vstrReasonForPayment)
                    thisDay = datetime.datetime.now()
                    thisDay = thisDay.date()
                    thisPayment.writeYear(strinput=thisDay.year)
                    thisPayment.writeMonth(strinput=thisDay.month)
                    thisPayment.writeDay(strinput=thisDay.day)
                    thisTime = datetime.datetime.now()
                    thisTime = thisTime.time()
                    strTime = datetime.time(hour=thisTime.hour,minute=thisTime.minute,second=thisTime.second)
                    thisPayment.writePaymentTime(strinput=strTime)
                    thisPayment.writePaidToClient(strinput=vstrPaidToClient)
                    thisPayment.put()

                    self.response.write("Payment request was saved successfully")

                elif vstrChoice == "15":
                    vstrNames = self.request.get('vstrNames')
                    vstrSurname = self.request.get('vstrSurname')
                    vstrIDNumber = self.request.get('vstrIDNumber')
                    vstrCompanyName = self.request.get('vstrCompanyName')
                    vstrCompanyReg = self.request.get('vstrCompanyReg')
                    vstrCompanyVAT = self.request.get('vstrCompanyVAT')
                    vstrRecipientType = self.request.get('vstrRecipientType')
                    vstrNotes = self.request.get('vstrNotes')
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrChurchID = self.request.get('vstrChurchID')

                    findRequest = Beneficiary.query(Beneficiary.strIDNumber == vstrIDNumber,Beneficiary.strChurchID == vstrChurchID,Beneficiary.strChurchBranchID == vstrChurchBranchID)
                    thisBeneficiaryList = findRequest.fetch()
                    if len(thisBeneficiaryList) > 0:
                        thisBeneficiary = thisBeneficiaryList[0]
                    else:
                        thisBeneficiary = Beneficiary()

                    thisBeneficiary.writeChurchID(strinput=vstrChurchID)
                    thisBeneficiary.writeChurchBranchID(strinput=vstrChurchBranchID)
                    thisBeneficiary.writeNames(strinput=vstrNames)
                    thisBeneficiary.writeSurname(strinput=vstrSurname)
                    thisBeneficiary.writeIDNumber(strinput=vstrIDNumber)
                    thisBeneficiary.writeCompanyName(strinput=vstrCompanyName)
                    thisBeneficiary.writeCompanyReg(strinput=vstrCompanyReg)
                    thisBeneficiary.writeCompanyVAT(strinput=vstrCompanyVAT)
                    thisBeneficiary.writeRecipientType(strinput=vstrRecipientType)
                    thisBeneficiary.writeNotes(strinput=vstrNotes)
                    thisBeneficiary.writeBeneficiaryIndex(strinput=str(thisBeneficiary.createBeneficiaryIndex()))
                    thisBeneficiary.writeReference(strinput=Guser.user_id())
                    thisBeneficiary.put()

                    self.response.write("Beneficiary Successfully Added")


                elif vstrChoice == "16":
                    vstrBranchName = self.request.get('vstrBranchName')
                    vstrBranchMotto = self.request.get('vstrBranchMotto')
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrChurchID = self.request.get('vstrChurchID')



                    findRequest = Branches.query(Branches.strChurchID == vstrChurchID,Branches.strChurchBranchID == vstrChurchBranchID)
                    thisBranchList = findRequest.fetch()

                    if len(thisBranchList) > 0:
                        thisBranch = thisBranchList[0]
                    else:
                        thisBranch = Branches()

                    thisBranch.writeBranchMotto(strinput=vstrBranchMotto)
                    thisBranch.writeBranchName(strinput=vstrBranchName)
                    thisBranch.writeChurchBranchID(strinput=vstrChurchBranchID)
                    thisBranch.writeChurchID(strinput=vstrChurchID)
                    thisBranch.put()

                    self.response.write("Branch Successfully updated")




                elif vstrChoice == "0":

                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrChurchID = self.request.get('vstrChurchID')

                    findRequest = Branches.query(Branches.strChurchID == vstrChurchID, Branches.strChurchBranchID == vstrChurchBranchID)
                    thisBranchesList = findRequest.fetch()

                    if len(thisBranchesList) > 0:
                        thisBranch = thisBranchesList[0]
                    else:
                        thisBranch = Branches()

                    template = template_env.get_template('templates/admin/churches/branches/subBranch.html')
                    context = {'thisBranch':thisBranch}
                    self.response.write(template.render(context))


                elif vstrChoice == "1":
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrChurchID = self.request.get('vstrChurchID')

                    findRequest = Employees.query(Employees.strChurchID == vstrChurchID, Employees.strChurchBranchID == vstrChurchBranchID)
                    thisEmployeesList = findRequest.fetch()

                    findRequest = Branches.query(Branches.strChurchID == vstrChurchID)
                    thisBranchList = findRequest.fetch()

                    template = template_env.get_template('templates/admin/churches/branches/employees.html')
                    context = {'thisEmployeesList':thisEmployeesList,'thisBranchList':thisBranchList}
                    self.response.write(template.render(context))
                elif vstrChoice == "2":
                    vstrNames = self.request.get('vstrNames')
                    vstrSurname = self.request.get('vstrSurname')
                    vstrIDNumber = self.request.get('vstrIDNumber')
                    vstrPhyStandNumber = self.request.get('vstrPhyStandNumber')
                    vstrPhyStreetName = self.request.get('vstrPhyStreetName')
                    vstrPhyCityTown = self.request.get('vstrPhyCityTown')
                    vstrPhyProvince = self.request.get('vstrPhyProvince')
                    vstrPhyCountry = self.request.get('vstrPhyCountry')
                    vstrPhyPostalCode = self.request.get('vstrPhyPostalCode')
                    vstrBoxNumber = self.request.get('vstrBoxNumber')
                    vstrCityTown = self.request.get('vstrCityTown')
                    vstrProvince = self.request.get('vstrProvince')
                    vstrCountry = self.request.get('vstrCountry')
                    vstrPostalCode = self.request.get('vstrPostalCode')
                    vstrDateOfEmployment = self.request.get('vstrDateOfEmployment')
                    vstrChurchID = self.request.get('vstrChurchID')
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrSelectBranch = self.request.get('vstrSelectBranch')

                    findRequest = Employees.query(Employees.strIDNumber == vstrIDNumber)
                    thisEmployeesList = findRequest.fetch()
                    if len(thisEmployeesList) > 0:
                        thisEmployee = thisEmployeesList[0]
                    else:
                        thisEmployee = Employees()

                    thisEmployee.writeNames(strinput=vstrNames)
                    thisEmployee.writeSurname(strinput=vstrSurname)
                    thisEmployee.writeIDNumber(strinput=vstrIDNumber)
                    thisEmployee.writePhyStandNumber(strinput=vstrPhyStandNumber)
                    thisEmployee.writePhyStreetName(strinput=vstrPhyStreetName)
                    thisEmployee.writePhyCityTown(strinput=vstrPhyCityTown)
                    thisEmployee.writePhyProvince(strinput=vstrPhyProvince)
                    thisEmployee.writePhyCountry(strinput=vstrPhyCountry)
                    thisEmployee.writePhyPostalCode(strinput=vstrPhyPostalCode)
                    thisEmployee.writeBoxNumber(strinput=vstrBoxNumber)
                    thisEmployee.writeCityTown(strinput=vstrCityTown)
                    thisEmployee.writeProvince(strinput=vstrProvince)
                    thisEmployee.writeCountry(strinput=vstrCountry)
                    thisEmployee.writePostalCode(strinput=vstrPostalCode)
                    thisEmployee.writeDateOfEmployment(strinput=vstrDateOfEmployment)
                    thisEmployee.writeChurchID(strinput=vstrChurchID)

                    thisEmployee.writeChurchBranchID(strinput=vstrSelectBranch)
                    thisEmployee.put()
                    self.response.write("Successfully added a new employee")

                elif vstrChoice == "3":
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrChurchID = self.request.get('vstrChurchID')

                    findRequest = Asset.query(Asset.strChurchID == vstrChurchID, Asset.strChurchBranchID == vstrChurchBranchID)
                    thisAssetsList = findRequest.fetch()

                    template = template_env.get_template('templates/admin/churches/branches/Assets.html')
                    context = {'thisAssetsList':thisAssetsList}
                    self.response.write(template.render(context))

                elif vstrChoice == "4":
                    vstrChurchID = self.request.get('vstrChurchID')
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')
                    vstrAssetCode = self.request.get('vstrAssetCode')
                    vstrAssetName = self.request.get('vstrAssetName')
                    vstrAssetDescription = self.request.get('vstrAssetDescription')
                    vstrPurchasePrice = self.request.get('vstrPurchasePrice')
                    vstrDepreciation = self.request.get('vstrDepreciation')
                    vstrCurrentValue = self.request.get('vstrCurrentValue')
                    vstrAssetType = self.request.get('vstrAssetType')

                    findRequest = Asset.query(Asset.strAssetCode == vstrAssetCode)
                    thisAssetsList = findRequest.fetch()

                    if len(thisAssetsList) > 0:
                        thisAsset = thisAssetsList[0]
                    else:
                        thisAsset = Asset()

                    thisAsset.writeChurchBranchID(strinput=vstrChurchBranchID)
                    thisAsset.writeChurchID(strinput=vstrChurchID)
                    thisAsset.writeAssetCode(strinput=vstrAssetCode)
                    thisAsset.writeAssetName(strinput=vstrAssetName)
                    thisAsset.writeAssetDescription(strinput=vstrAssetDescription)
                    thisAsset.writePurchasePrice(strinput=vstrPurchasePrice)
                    thisAsset.writeDepreciation(strinput=vstrDepreciation)
                    thisAsset.writeCurrentValue(strinput=vstrCurrentValue)
                    thisAsset.writeAssetType(strinput=vstrAssetType)
                    vstrAssetID = thisAsset.createAssetID()
                    thisAsset.writeAssetID(strinput=vstrAssetID)
                    thisAsset.put()
                    self.response.write("Successfully added Asset with Asset ID : " + str(thisAsset.strAssetID))

                elif vstrChoice == "5":
                    vstrChurchID = self.request.get('vstrChurchID')
                    vstrChurchBranchID = self.request.get('vstrChurchBranchID')

                    findRequest = Costs.query(Costs.strChurchID == vstrChurchID, Costs.strChurchBranchID == vstrChurchBranchID)
                    thisCostsList = findRequest.fetch()

                    template = template_env.get_template('templates/admin/churches/branches/costs.html')
                    context = {'thisCostsList':thisCostsList,'vstrChurchID':vstrChurchID,'vstrChurchBranchID':vstrChurchBranchID}
                    self.response.write(template.render(context))




            else:
                self.response.write("Not Authorised to use this resource")



class CongregantsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:


            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()

            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRights = thisUserRightsList[0]
            else:
                thisUserRights = UserRights()

            if thisUserRights.strAdminUser or thisUserRights.strSuperUser:
                findRequest = CurrentBranch.query(CurrentBranch.strMemberID == Guser.user_id())
                thisCurrentBranchList = findRequest.fetch()
                if len(thisCurrentBranchList) > 0:
                    thisCurrentBranch = thisCurrentBranchList[0]
                else:
                    thisCurrentBranch = CurrentBranch()
                findRequest = ChurchMember.query(ChurchMember.strChurchID == thisChurchMember.strChurchID,ChurchMember.strChurchBranchID == thisCurrentBranch.strCurrentBranchID)
                thisChurchMembersList = findRequest.fetch()

                findRequest = Branches.query(Branches.strChurchID == thisChurchMember.strChurchID)
                thisBranchList = findRequest.fetch()


                template = template_env.get_template('templates/admin/churches/addCongregants.html')
                context = {'thisChurchMember':thisChurchMember,'thisChurchMembersList':thisChurchMembersList,'thisBranchList':thisBranchList}
                self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        from dashboard import Administrators
        if Guser:
            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisAdminList = findRequest.fetch()
            if len(thisAdminList) > 0:
                thisAdmin = thisAdminList[0]
            else:
                thisAdmin = ChurchMember()

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRights = thisUserRightsList[0]
            else:
                thisUserRights = UserRights()

            if thisUserRights.strAdminUser or thisUserRights.strSuperUser:
                vstrMemberName = self.request.get('vstrMemberName')
                vstrMemberSurname = self.request.get('vstrMemberSurname')
                vstrMemberTitle = self.request.get('vstrMemberTitle')
                vstrMemberIDNumber = self.request.get('vstrMemberIDNumber')
                vstrMemberGender = self.request.get('vstrMemberGender')
                vstrMemberDateOfBirth = self.request.get('vstrMemberDateOfBirth')
                vstrMemberDateOfMemberShip = self.request.get('vstrMemberDateOfMemberShip')
                vstrMemberDateBaptised = self.request.get('vstrMemberDateBaptised')
                vstrTel = self.request.get('vstrTel')
                vstrCell = self.request.get('vstrCell')
                vstrEmail = self.request.get('vstrEmail')
                vstrWorkTel = self.request.get('vstrWorkTel')
                vstrWorkCell = self.request.get('vstrWorkCell')
                vstrWorkEmail = self.request.get('vstrWorkEmail')
                vstrSelectBranch = self.request.get('vstrSelectBranch')

                findRequest = ChurchMember.query(ChurchMember.strMemberIDNumber == vstrMemberIDNumber)
                addChurchMemberList = findRequest.fetch()

                if len(addChurchMemberList) > 0:
                    addChurchMember = addChurchMemberList[0]
                else:
                    addChurchMember = ChurchMember()

                addChurchMember.writeChurchID(strinput=thisAdmin.strChurchID)
                addChurchMember.writeChurchBranchID(strinput=vstrSelectBranch)

                addChurchMember.writeMemberNames(strinput=vstrMemberName)
                addChurchMember.writeMemberSurname(strinput=vstrMemberSurname)
                addChurchMember.writeMemberTitle(strinput=vstrMemberTitle)
                addChurchMember.writeMemberGender(strinput=vstrMemberGender)
                addChurchMember.writeMemberIDNumber(strinput=vstrMemberIDNumber)

                if "-" in vstrMemberDateOfBirth:
                    strDateList = vstrMemberDateOfBirth.split("-")
                    thisYear = int(strDateList[0])
                    thisMonth = int(strDateList[1])
                    thisDay = int(strDateList[2])
                    vstrThisdate = datetime.date(year=thisYear,month=thisMonth,day=thisDay)
                elif "/" in vstrMemberDateOfBirth:
                    strDateList = vstrMemberDateOfBirth.split("/")
                    thisYear = int(strDateList[0])
                    thisMonth = int(strDateList[1])
                    thisDay = int(strDateList[2])
                    vstrThisdate = datetime.date(year=thisYear,month=thisMonth,day=thisDay)
                else:
                    vstrThisdate = datetime.datetime.now()
                    vstrThisdate = datetime.date(year=vstrThisdate.year,month=vstrThisdate.month,day=vstrThisdate.day)


                vstrMemberDateOfBirth = vstrThisdate

                addChurchMember.writeMemberDateOfBirth(strinput=vstrMemberDateOfBirth)

                if "-" in vstrMemberDateBaptised:
                    strDateList = vstrMemberDateBaptised.split("-")
                    thisYear = int(strDateList[0])
                    thisMonth = int(strDateList[1])
                    thisDay = int(strDateList[2])
                    vstrThisdate = datetime.date(year=thisYear,month=thisMonth,day=thisDay)
                elif "/" in vstrMemberDateBaptised:
                    strDateList = vstrMemberDateBaptised.split("/")
                    thisYear = int(strDateList[0])
                    thisMonth = int(strDateList[1])
                    thisDay = int(strDateList[2])
                    vstrThisdate = datetime.date(year=thisYear,month=thisMonth,day=thisDay)
                else:
                    vstrThisdate = datetime.datetime.now()
                    vstrThisdate = datetime.date(year=vstrThisdate.year,month=vstrThisdate.month,day=vstrThisdate.day)

                vstrMemberDateBaptised = vstrThisdate

                addChurchMember.writeMemberDateBaptised(strinput=vstrMemberDateBaptised)

                if "-" in vstrMemberDateOfMemberShip:
                    strDateList = vstrMemberDateOfMemberShip.split("-")
                    thisYear = int(strDateList[0])
                    thisMonth = int(strDateList[1])
                    thisDay = int(strDateList[2])
                    vstrThisdate = datetime.date(year=thisYear,month=thisMonth,day=thisDay)
                elif "/" in vstrMemberDateOfMemberShip:
                    strDateList = vstrMemberDateOfMemberShip.split("/")
                    thisYear = int(strDateList[0])
                    thisMonth = int(strDateList[1])
                    thisDay = int(strDateList[2])
                    vstrThisdate = datetime.date(year=thisYear,month=thisMonth,day=thisDay)
                else:
                    vstrThisdate = datetime.datetime.now()
                    vstrThisdate = datetime.date(year=vstrThisdate.year,month=vstrThisdate.month,day=vstrThisdate.day)

                vstrMemberDateOfMemberShip = vstrThisdate

                addChurchMember.writeMemberDateOfMembership(strinput=vstrMemberDateOfMemberShip)

                addChurchMember.writeTel(strinput=vstrTel)
                addChurchMember.writeCell(strinput=vstrCell)
                addChurchMember.writeEmail(strinput=vstrEmail)
                addChurchMember.writeWorkTel(strinput=vstrWorkTel)
                addChurchMember.writeWorkCell(strinput=vstrWorkCell)
                addChurchMember.writeWorkEmail(strinput=vstrWorkEmail)
                addChurchMember.writeMemberID(strinput=vstrMemberIDNumber)
                addChurchMember.writeProfileClaimed(strinput=False)

                addChurchMember.put()

                self.response.write("Member Successfully updated--")

class BrowseCongregantsHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()
            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = CurrentBranch.query(CurrentBranch.strMemberID == Guser.user_id())
            thisCurrentBranchList = findRequest.fetch()

            if len(thisCurrentBranchList) > 0:
                thisCurrentBranch = thisCurrentBranchList[0]
            else:
                thisCurrentBranch = CurrentBranch()
            findRequest = ChurchMember.query(ChurchMember.strChurchID == thisChurchMember.strChurchID,ChurchMember.strChurchBranchID == thisCurrentBranch.strCurrentBranchID)
            thisChurchMemberList = findRequest.fetch()

            template = template_env.get_template('templates/admin/churches/browseCongregants.html')
            context = {'thisChurchMemberList':thisChurchMemberList}
            self.response.write(template.render(context))

class EditThisCongregantHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()
            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRights = thisUserRightsList[0]
            else:
                thisUserRights = UserRights()

            if thisUserRights.strAdminUser or thisUserRights.strSuperUser:
                strURL = self.request.url
                URLlist = strURL.split("/")
                vstrReference = URLlist[len(URLlist) - 1]

                findRequest = ChurchMember.query(ChurchMember.strMemberID == vstrReference)
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                findRequest = MemberAddresses.query(MemberAddresses.strMemberID == vstrReference)
                thisMemberAddressList = findRequest.fetch()

                if len(thisMemberAddressList) > 0:
                    thisMemberAddress = thisMemberAddressList[0]
                else:
                    thisMemberAddress = MemberAddresses()

                findRequest = UserRights.query(UserRights.strMemberID == vstrReference)
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisUserRight = thisUserRightsList[0]
                else:
                    thisUserRight = UserRights()

                findRequest = Branches.query(Branches.strChurchID == thisChurchMember.strChurchID)
                thisBranchList = findRequest.fetch()

                template = template_env.get_template('templates/admin/churches/editThisMember.html')
                context = {'thisChurchMember':thisChurchMember ,'thisMemberAddress':thisMemberAddress,'thisUserRight':thisUserRight,
                           'thisBranchList':thisBranchList}
                self.response.write(template.render(context))

class EditCongregantHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        if Guser:
            findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
            thisChurchMemberList = findRequest.fetch()
            if len(thisChurchMemberList) > 0:
                thisChurchMember = thisChurchMemberList[0]
            else:
                thisChurchMember = ChurchMember()

            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRights = thisUserRightsList[0]
            else:
                thisUserRights = UserRights()

            if thisUserRights.strAdminUser or thisUserRights.strSuperUser:

                findRequest = CurrentBranch.query(CurrentBranch.strMemberID == Guser.user_id())
                thisCurrentBranchList = findRequest.fetch()

                if len(thisCurrentBranchList) > 0:
                    thisCurrentBranch = thisCurrentBranchList[0]
                else:
                    thisCurrentBranch = CurrentBranch()


                findRequest = ChurchMember.query(ChurchMember.strChurchID == thisChurchMember.strChurchID,ChurchMember.strChurchBranchID == thisCurrentBranch.strCurrentBranchID)
                thisChurchMembersList = findRequest.fetch()

                template = template_env.get_template('templates/admin/churches/editCongregants.html')
                context = {'thisChurchMembersList':thisChurchMembersList}
                self.response.write(template.render(context))



class GetChurchMemberHandler(webapp2.RequestHandler):


    def get(self):
        Guser = users.get_current_user()
        from mysms import Groups,SMSContacts,SMSAccount,SMSPortalBudget
        if Guser:
            vstrMemberID = self.request.get('vstrMemberID')
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "1":

                findRequest = ChurchMember.query(ChurchMember.strMemberID == vstrMemberID)
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisUserRights = thisUserRightsList[0]
                else:
                    thisUserRights = UserRights()

                if thisUserRights.strAdminUser or thisUserRights.strSuperUser:

                    template = template_env.get_template('templates/admin/churches/subeditmember/personaldetails.html')
                    context = {'thisChurchMember':thisChurchMember}
                    self.response.write(template.render(context))
                else:
                    pass
            elif vstrChoice == "2":

                findRequest = MemberAddresses.query(MemberAddresses.strMemberID == vstrMemberID)
                thisMemberAddressesList = findRequest.fetch()

                if len(thisMemberAddressesList) > 0:
                    thisMemberAddress = thisMemberAddressesList[0]
                else:
                    thisMemberAddress = MemberAddresses()

                findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisUserRights = thisUserRightsList[0]
                else:
                    thisUserRights = UserRights()

                if thisUserRights.strAdminUser or thisUserRights.strSuperUser:

                    template = template_env.get_template('templates/admin/churches/subeditmember/memberaddress.html')
                    context = {'thisMemberAddress':thisMemberAddress}
                    self.response.write(template.render(context))

            elif vstrChoice == "3":
                vstrMemberID = self.request.get('vstrMemberID')
                findRequest = UserRights.query(UserRights.strMemberID == vstrMemberID)
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisAcessRights = thisUserRightsList[0]
                else:
                    thisAcessRights = UserRights()

                findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisUserRights = thisUserRightsList[0]
                else:
                    thisUserRights = UserRights()

                if thisUserRights.strAdminUser == True:
                    vstrAdminUser = "YES"
                else:
                    vstrAdminUser = "NO"

                if thisUserRights.strChurchMember == True:
                    vstrChurchMember = "YES"
                else:
                    vstrChurchMember = "NO"

                if thisUserRights.strSuperUser == True:
                    vstrSuperUser = "YES"
                else:
                    vstrSuperUser = "NO"

                if thisUserRights.strVisitor == True:
                    vstrVisitor = "YES"
                else:
                    vstrVisitor = "NO"

                if thisUserRights.strAdminUser:
                    template = template_env.get_template('templates/admin/churches/subeditmember/AccessRights.html')
                    context = {'vstrAdminUser':vstrAdminUser,'vstrChurchMember':vstrChurchMember,'vstrSuperUser':vstrSuperUser,
                               'vstrVisitor':vstrVisitor}
                    self.response.write(template.render(context))

            elif vstrChoice == "4":
                vstrMemberID = self.request.get('vstrMemberID')

                findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisUserRight = thisUserRightsList[0]
                else:
                    thisUserRight = UserRights()

                if thisUserRight.strAdminUser or thisUserRight.strSuperUser:

                    findRequest = Pledge.query(Pledge.strMemberID == vstrMemberID)
                    thisPledgeList = findRequest.fetch()

                    template = template_env.get_template('templates/admin/churches/subeditmember/pledges.html')
                    context = {'thisPledgeList':thisPledgeList,'vstrMemberID':vstrMemberID}
                    self.response.write(template.render(context))

            elif vstrChoice == "5":
                vstrMemberID = self.request.get('vstrMemberID')
                vstrPledgeAmount = self.request.get('vstrPledgeAmount')
                vstrDate = self.request.get('vstrDate')
                try:
                    vstrDateList = vstrDate.split("-")
                    vstrYear = int(vstrDateList[0])
                    vstrMonth = int(vstrDateList[1])
                    vstrDay = int(vstrDateList[2])
                except:
                    Today = datetime.datetime.now()
                    vstrYear = Today.year
                    vstrMonth = Today.month
                    vstrDay = Today.day


                findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisUserRight = thisUserRightsList[0]
                else:
                    thisUserRight = UserRights()

                if thisUserRight.strAdminUser or thisUserRight.strSuperUser:

                    thisPledge = Pledge()

                    findRequest =ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisChurchMemberList = findRequest.fetch()

                    if len(thisChurchMemberList) > 0:
                        thisChurchMember = thisChurchMemberList[0]


                        thisPledge.writeMemberID(strinput=vstrMemberID)
                        thisPledge.writeChurchID(strinput=thisChurchMember.strChurchID)
                        thisPledge.writeChurchBranchID(strinput=thisChurchMember.strChurchBranchID)
                        thisPledge.writeTransactionCode(strinput=thisPledge.createTransactionCode())
                        thisPledge.writePledgeAmount(strinput=vstrPledgeAmount)

                        thisPledge.writeYear(strinput=vstrYear)
                        thisPledge.writeMonth(strinput=vstrMonth)
                        thisPledge.writeDay(strinput=vstrDay)

                        thisPledge.put()

                        self.response.write("Pledge Amount uploaded successfully")

            elif vstrChoice == "6":
                vstrMemberID = self.request.get('vstrMemberID')

                findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisUserRight = thisUserRightsList[0]
                else:
                    thisUserRight = UserRights()

                if thisUserRight.strAdminUser or thisUserRight.strSuperUser:

                    findRequest = Donation.query(Donation.strDonatorID == vstrMemberID)
                    thisDonationList = findRequest.fetch()

                    template = template_env.get_template('templates/admin/churches/subeditmember/donation.html')
                    context = {'thisDonationList':thisDonationList,'vstrMemberID':vstrMemberID}
                    self.response.write(template.render(context))

            elif vstrChoice == "7":
                vstrMemberID = self.request.get('vstrMemberID')

                findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisUserRight = thisUserRightsList[0]
                else:
                    thisUserRight = UserRights()


                if thisUserRight.strAdminUser or thisUserRight.strSuperUser:

                    findRequest = Tithing.query(Tithing.strMemberID == vstrMemberID)
                    thisTithingList = findRequest.fetch()

                    template = template_env.get_template('templates/admin/churches/subeditmember/tithing.html')
                    context = {'thisTithingList':thisTithingList}
                    self.response.write(template.render(context))


            elif vstrChoice == "8":
                vstrMemberID = self.request.get('vstrMemberID')
                vstrDonationAmount = self.request.get('vstrDonationAmount')
                vstrDate = self.request.get('vstrDate')
                try:
                    vstrDateList = vstrDate.split("-")
                    vstrYear = int(vstrDateList[0])
                    vstrMonth = int(vstrDateList[1])
                    vstrDay = int(vstrDateList[2])
                except:
                    Today = datetime.datetime.now()
                    vstrYear = Today.year
                    vstrMonth = Today.month
                    vstrDay = Today.day

                findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisUserRight = thisUserRightsList[0]
                else:
                    thisUserRight = UserRights()

                if thisUserRight.strAdminUser or thisUserRight.strSuperUser:

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisAdminList = findRequest.fetch()


                    if len(thisAdminList) > 0:
                        thisAdmin = thisAdminList[0]

                        thisDonation = Donation()
                        thisDonation.writeDonatorID(strinput=vstrMemberID)
                        thisDonation.writeChurchID(strinput=thisAdmin.strChurchID)
                        thisDonation.writeChurchBranchID(strinput=thisAdmin.strChurchBranchID)
                        thisDonation.writeDonationAmount(strinput=vstrDonationAmount)
                        thisDonation.writeTransactionID(strinput=thisDonation.createTransactionID())

                        thisDonation.writeYear(strinput=vstrYear)
                        thisDonation.writeMonth(strinput=vstrMonth)
                        thisDonation.writeDay(strinput=vstrDay)
                        thisDonation.put()

                        self.response.write("Donation successfully uploaded")

            elif vstrChoice == "9":
                vstrMemberID = self.request.get('vstrMemberID')
                vstrTithingAmount = self.request.get('vstrTithingAmount')
                vstrDate = self.request.get('vstrDate')



                try:
                    vstrDateList = vstrDate.split("-")
                    vstrYear = int(vstrDateList[0])
                    vstrMonth = int(vstrDateList[1])
                    vstrDay = int(vstrDateList[2])
                except:
                    Today = datetime.datetime.now()
                    vstrYear = Today.year
                    vstrMonth = Today.month
                    vstrDay = Today.day






                findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisUserRight = thisUserRightsList[0]
                else:
                    thisUserRight = UserRights()

                if thisUserRight.strAdminUser or thisUserRight.strSuperUser:

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisAdminList = findRequest.fetch()


                    if len(thisAdminList) > 0:
                        thisAdmin = thisAdminList[0]

                        thisTithe = Tithing()
                        thisTithe.writeMemberID(strinput=vstrMemberID)
                        thisTithe.writeChurchID(strinput=thisAdmin.strChurchID)
                        thisTithe.writeChurchBranchID(strinput=thisAdmin.strChurchBranchID)
                        thisTithe.writeTithingAmount(strinput=vstrTithingAmount)
                        thisTithe.writeTransactionCode(strinput=thisTithe.createTransactionCode())

                        thisTithe.writeYear(strinput=vstrYear)
                        thisTithe.writeMonth(strinput=vstrMonth)
                        thisTithe.writeDay(strinput=vstrDay)
                        thisTithe.put()
                        self.response.write("Tithing Successfully updated")
                    else:
                        self.response.write("Cannot Edit records because you have not successfully created your own record")

            elif vstrChoice == "10":
                vstrMemberID = self.request.get('vstrMemberID')

                findRequest = ChurchMember.query(ChurchMember.strMemberID == vstrMemberID)
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                findRequest = Groups.query(Groups.strChurchID == thisChurchMember.strChurchID)
                thisGroupsList = findRequest.fetch()

                findRequest = SMSContacts.query(SMSContacts.strMemberID == thisChurchMember.strMemberID)
                thisSMSContactsList = findRequest.fetch()

                thisMyGroupList = []
                for thisSMSContact in thisSMSContactsList:
                    for thisGroup in thisGroupsList:
                        if thisSMSContact.strGroupID == thisGroup.strGroupID:
                            thisMyGroupList.append(thisGroup)
                            thisGroupsList.remove(thisGroup)
                        else:
                            pass


                template = template_env.get_template('templates/sms/groups/grouplist.html')
                context = {'thisMyGroupList':thisMyGroupList,'thisGroupsList':thisGroupsList,'vstrMemberID':vstrMemberID}
                self.response.write(template.render(context))


            elif vstrChoice == "11":
                vstrMemberID = self.request.get('vstrMemberID')

                findRequest = ChurchMember.query(ChurchMember.strMemberID == vstrMemberID)
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()


                findRequest = MemberMessaging.query(MemberMessaging.strMemberID == vstrMemberID)
                thisMessagingList = findRequest.fetch()


                template  =template_env.get_template('templates/admin/churches/subeditmember/messaging.html')
                context = {'thisMessagingList':thisMessagingList,'thisChurchMember':thisChurchMember}
                self.response.write(template.render(context))

            elif vstrChoice == "12":
                vstrMemberID = self.request.get('vstrMemberID')
                vstrCell = self.request.get('vstrCell')
                vstrMessage = self.request.get('vstrMessage')

                findRequest = ChurchMember.query(ChurchMember.strMemberID == vstrMemberID)
                thisChurchMemberList = findRequest.fetch()

                if len(thisChurchMemberList) > 0:
                    thisChurchMember = thisChurchMemberList[0]
                else:
                    thisChurchMember = ChurchMember()

                findRequest = SMSAccount.query(SMSAccount.strChurchID == thisChurchMember.strChurchID)
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
                            thisMessaging = MemberMessaging()
                            thisMessaging.writeChurchID(strinput=thisChurchMember.strChurchID)
                            thisMessaging.writeChurchBranchID(strinput=thisChurchMember.strChurchBranchID)
                            thisMessaging.writeMemberID(strinput=vstrMemberID)
                            thisMessaging.writeMessage(strinput=vstrMessage)
                            thisMessaging.writeRef(strinput=strRef)
                            thisMessaging.writeDateSent(strinput=strThisDate)
                            thisMessaging.writeTimeSent(strinput=strThisTime)
                            thisMessaging.put()
                            thisSMSAccount.strTotalSMS = thisSMSAccount.strTotalSMS - 1
                            thisSMSAccount.put()
                            self.response.write("Message successfully sent")
                        else:
                            self.response.write("Error sending message")
                    else:
                        self.response.write("Insufficient credit")
                else:
                    self.response.write("Fatal error sending message")





















    def post(self):
        Guser = users.get_current_user()
        if Guser:
            vstrMemberID = self.request.get('vstrMemberID')
            vstrChoice = self.request.get('vstrChoice')

            if vstrChoice == "2":
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

                findRequest = MemberAddresses.query(MemberAddresses.strMemberID == vstrMemberID)
                thisMemberAddressList = findRequest.fetch()

                if len(thisMemberAddressList) > 0:
                    thisMemberAddress = thisMemberAddressList[0]
                else:
                    thisMemberAddress = MemberAddresses()


                logging.info(msg="Member Addresses Executing")

                thisMemberAddress.writeMemberID(strinput=vstrMemberID)
                thisMemberAddress.writePhyStandNumber(strinput=vstrPhyStandNumber)
                thisMemberAddress.writePhyStreetName(strinput=vstrPhyStreetName)
                thisMemberAddress.writePhyCityTown(strinput=vstrPhyCityTown)
                thisMemberAddress.writePhyProvince(strinput=vstrPhyProvince)
                thisMemberAddress.writePhyCountry(strinput=vstrPhyCountry)
                thisMemberAddress.writePhyPostalCode(strinput=vstrPhyPostalCode)
                thisMemberAddress.writePhyPostalCode(strinput=vstrPhyPostalCode)
                thisMemberAddress.writePosBoxNumber(strinput=vstrPosBoxNumber)
                thisMemberAddress.writePosCityTown(strinput=vstrPosCityTown)
                thisMemberAddress.writePosProvince(strinput=vstrPosProvince)
                thisMemberAddress.writePosCountry(strinput=vstrPosCountry)

                thisMemberAddress.put()

                self.response.write("Member Addresses successfully updated")
            elif vstrChoice == "3":
                vstrAdminUser = self.request.get('vstrAdminUser')
                vstrSuperUser = self.request.get('vstrSuperUser')
                vstrVisitor = self.request.get('vstrVisitor')
                vstrChurchMember = self.request.get('vstrChurchMember')

                findRequest = UserRights.query(UserRights.strMemberID == vstrMemberID)
                thisUserRightsList = findRequest.fetch()

                if len(thisUserRightsList) > 0:
                    thisUserRights = thisUserRightsList[0]
                else:
                    thisUserRights = UserRights()

                thisUserRights.writeMemberID(strinput=vstrMemberID)

                if vstrAdminUser == "YES":
                    thisUserRights.setAdminUser(strinput=True)
                else:
                    thisUserRights.setAdminUser(strinput=False)

                if vstrSuperUser == "YES":
                    thisUserRights.setSuperUser(strinput=True)
                else:
                    thisUserRights.setSuperUser(strinput=False)

                if vstrChurchMember == "YES":
                    thisUserRights.setChurchMember(strinput=True)
                else:
                    thisUserRights.setChurchMember(strinput=False)

                if vstrVisitor == "YES":
                    thisUserRights.setVisitor(strinput=True)
                else:
                    thisUserRights.setVisitor(strinput=False)

                thisUserRights.put()

                self.response.write("Successfully updated Access Rights")



app = webapp2.WSGIApplication([
    ('/admin/churchdetails', ChurchDetailsHandler),
    ('/admin/branches', BranchesHandler),
    ('/admin/branches/.*', thisBranchHandler),
    ('/admin/congregants', CongregantsHandler),
    ('/church/congregants/browse', BrowseCongregantsHandler),
    ('/church/member/edit', EditCongregantHandler),
    ('/church/member/edit/.*', EditThisCongregantHandler),
    ('/church/member/get', GetChurchMemberHandler)

], debug=True)