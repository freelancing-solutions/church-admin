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
import jinja2
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users
import datetime
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))

class Employees(ndb.Expando):
    strReference = ndb.StringProperty()

    strNames = ndb.StringProperty()
    strSurname = ndb.StringProperty()
    strIDNumber = ndb.StringProperty()
    strPosition = ndb.StringProperty(default="Admin")
    strContract = ndb.StringProperty(default="Permanent")

    strPhyStandNumber = ndb.StringProperty()
    strPhyStreetName = ndb.StringProperty()
    strPhyCityTown = ndb.StringProperty()
    strPhyProvince = ndb.StringProperty()
    strPhyCountry = ndb.StringProperty()
    strPhyPostalCode = ndb.StringProperty()

    strBoxNumber = ndb.StringProperty()
    strCityTown = ndb.StringProperty()
    strProvince = ndb.StringProperty()
    strCountry = ndb.StringProperty()
    strPostalCode = ndb.StringProperty()

    strDateOfEmployment = ndb.DateProperty()
    strSuspended = ndb.BooleanProperty(default=False)
    strDateOfSuspension = ndb.DateProperty()

    strChurchBranchID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strEmployeeID = ndb.StringProperty()

    def writePosition(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPosition = strinput
                return True
            else:
                return False
        except:
            return False

    def writeContract(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strContract = strinput
                return True
            else:
                return False
        except:
            return False

    def writeEmployeeID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmployeeID = strinput
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
            strinput = strinput(strinput)
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
    def writeBoxNumber(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strBoxNumber = strinput
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
            if strinput != None:
                self.strPostalCode = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateOfEmployment(self,strinput):
        try:
            if strinput is not None:
                self.strDateOfEmployment = strinput
                return True
            else:
                return False
        except:
            return False
    def setSuspended(self,strinput):
        try:
            if strinput in [True,False]:
                self.strSuspended = strinput
                return True
            else:
                return False
        except:
            return False
    def writeDateOfSuspension(self,strinput):
        try:

            if strinput != None:
                self.strDateOfSuspension = strinput
                return True
            else:
                return False
        except:
            return False

class Salaries(ndb.Expando):
    strReference = ndb.StringProperty()

    strNormalRate = ndb.StringProperty()
    strNormalHoursWorked = ndb.StringProperty()
    strTotalBasicSalary = ndb.StringProperty()

    strOverTimeRate = ndb.StringProperty()
    strOverTimeWorked = ndb.StringProperty()
    strTotalOverTimeEarned = ndb.StringProperty()

    strUIF = ndb.StringProperty()
    strPaye = ndb.StringProperty()
    strOtherDeductions = ndb.StringProperty()

    strTotalDeductions = ndb.StringProperty()

    strYear = ndb.StringProperty()
    strMonth = ndb.StringProperty()
    strThisDate = ndb.DateProperty()

    strChurchBranchID = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strEmployeeID = ndb.StringProperty()
    strIDNumber = ndb.StringProperty()

    def writeThisDate(self,strinput):
        try:

            if isinstance(strinput,datetime.date):
                self.strThisDate = strinput
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
    def writeEmployeeID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmployeeID = strinput
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
    def writeNormalRate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNormalRate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeNormalHoursWorked(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strNormalHoursWorked = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTotalBasicsSalary(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTotalBasicSalary = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOvertimeRate(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOverTimeRate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOverTimeWorked(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOverTimeWorked = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTotalOverTimeEarned(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTotalOverTimeEarned = strinput
                return True
            else:
                return False
        except:
            return False
    def writeUIF(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strUIF = strinput
                return True
            else:
                return False
        except:
            return False
    def writePaye(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strPaye = strinput
                return True
            else:
                return False
        except:
            return False
    def writeOtherDeductions(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strOtherDeductions = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTotalDeductions(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strTotalDeductions = strinput
                return True
            else:
                return False
        except:
            return False
    def writeYear(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) > 2016) and (int(strinput) < 2050):
                self.strYear = strinput
                return True
            else:
                return False
        except:
            return False
    def writeMonth(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit() and (int(strinput) > 0) and (int(strinput) < 13):
                self.strMonth = strinput
                return True
            else:
                return False
        except:
            return False

class BankingDetails(ndb.Expando):

    strReference = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strEmployeeID = ndb.StringProperty()

    strIDNumber = ndb.StringProperty()

    strAccountOwner = ndb.StringProperty()
    strAccountNumber = ndb.StringProperty()
    strBankName = ndb.StringProperty()
    strBranchName = ndb.StringProperty()
    strBranchCode = ndb.StringProperty()
    strAccountType = ndb.StringProperty()

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
    def writeEmployeeID(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strEmployeeID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeAccountOwner(self,strinput):
        try:
            strinput = str(strinput)
            if strinput != None:
                self.strAccountOwner = strinput
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

class AttendanceRegister(ndb.Expando):
    strReference = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strEmployeeID = ndb.StringProperty()

    strIDNumber = ndb.StringProperty()

    strThisDate = ndb.DateProperty()
    strTimeIn = ndb.TimeProperty()
    strTimeOut = ndb.TimeProperty()

    strBreakTimeOut = ndb.TimeProperty()
    strBreakTimeIN = ndb.TimeProperty()

    strLunchTimeOut = ndb.TimeProperty()
    strLunchTimeIN = ndb.TimeProperty()

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
    def writeEmployeeID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strEmployeeID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeThisDate(self,strinput):
        try:
            if isinstance(strinput,datetime.date):
                self.strThisDate = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeIn(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeIn = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTimeOut(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strTimeOut = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBreakTimeOut(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strBreakTimeOut = strinput
                return True
            else:
                return False
        except:
            return False
    def writeBreakTimeIn(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strBreakTimeIN = strinput
                return True
            else:
                return False
        except:
            return False
    def writeLunchTimeOut(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strLunchTimeOut = strinput
                return True
            else:
                return False
        except:
            return False
    def writeLunchTimeIn(self,strinput):
        try:
            if isinstance(strinput,datetime.time):
                self.strLunchTimeIN = strinput
                return True
            else:
                return False
        except:
            return False

class Leave(ndb.Expando):
    strReference = ndb.StringProperty()
    strChurchID = ndb.StringProperty()
    strChurchBranchID = ndb.StringProperty()
    strEmployeeID = ndb.StringProperty()
    strTotalLeaveDays = ndb.IntegerProperty(default=22)
    strTotalSickDays = ndb.IntegerProperty(default=11)
    strFamilyResponsibility = ndb.IntegerProperty(default=5)


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

    def writeEmployeeID(self, strinput):
        try:
            strinput = str(strinput)
            if not (strinput == None):
                self.strEmployeeID = strinput
                return True
            else:
                return False
        except:
            return False
    def writeTotalLeaveDays(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalLeaveDays = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeTotalSickDays(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strTotalSickDays = int(strinput)
                return True
            else:
                return False
        except:
            return False
    def writeFamilyResponsibility(self,strinput):
        try:
            strinput = str(strinput)
            if strinput.isdigit():
                self.strFamilyResponsibility = int(strinput)
                return True
            else:
                return False
        except:
            return False

class EmployeeHandler(webapp2.RequestHandler):
    def get(self):
        Guser = users.get_current_user()
        from church import UserRights,Branches
        if Guser:
            findRequest = UserRights.query(UserRights.strMemberID == Guser.user_id())
            thisUserRightsList = findRequest.fetch()

            if len(thisUserRightsList) > 0:
                thisUserRight = thisUserRightsList[0]
            else:
                thisUserRight = UserRights()

            if thisUserRight.strAdminUser:

                URL = self.request.url
                URLlist = URL.split("/")
                vstrIDNumber = URLlist[len(URLlist) - 1]
                findRequest = Employees.query(Employees.strIDNumber == vstrIDNumber)
                thisEmployeeList = findRequest.fetch()

                if len(thisEmployeeList) > 0:
                    thisEmployee = thisEmployeeList[0]
                else:
                    thisEmployee = Employees()


                findRequest = Branches.query(Branches.strChurchID == thisEmployee.strChurchID)
                thisBranchList = findRequest.fetch()

                template = template_env.get_template('templates/admin/churches/employees/employees.html')
                context = {'thisEmployee':thisEmployee,'thisBranchList':thisBranchList}
                self.response.write(template.render(context))

    def post(self):
        Guser = users.get_current_user()
        from church import UserRights,ChurchMember,Branches

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

                    URL = self.request.url
                    URLlist = URL.split("/")
                    vstrIDNumber = URLlist[len(URLlist) - 1]
                    findRequest = Employees.query(Employees.strIDNumber == vstrIDNumber)
                    thisEmployeeList = findRequest.fetch()

                    if len(thisEmployeeList) > 0:
                        thisEmployee = thisEmployeeList[0]
                    else:
                        thisEmployee = Employees()

                    findRequest = Branches.query(Branches.strChurchID == thisEmployee.strChurchID)
                    thisBranchList = findRequest.fetch()

                    template = template_env.get_template('templates/admin/churches/employees/personal.html')
                    context = {'thisEmployee':thisEmployee,'thisBranchList':thisBranchList}
                    self.response.write(template.render(context))

                elif vstrChoice == "1":


                    URL = self.request.url
                    URLlist = URL.split("/")
                    vstrIDNumber = URLlist[len(URLlist) - 1]

                    findRequest = Salaries.query(Salaries.strIDNumber == vstrIDNumber)
                    thisSalariesList = findRequest.fetch()

                    try:
                        thisSalary = thisSalariesList[0]
                    except:
                        thisSalary = Salaries()

                    template = template_env.get_template('templates/admin/churches/employees/SalariesPayslips.html')
                    context = {'thisSalariesList':thisSalariesList,'vstrIDNumber':vstrIDNumber,'vstrEmployeeID':thisSalary.strEmployeeID}
                    self.response.write(template.render(context))

                elif vstrChoice == "2":

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisChurchMemberList = findRequest.fetch()

                    if len(thisChurchMemberList) > 0:
                        thisChurchMember = thisChurchMemberList[0]
                    else:
                        thisChurchMember = ChurchMember()


                    vstrIDNumber = self.request.get('vstrIDNumber')
                    vstrOverTimeRate = self.request.get('vstrOverTimeRate')
                    vstrNormalRate = self.request.get('vstrNormalRate')
                    vstrUIF = self.request.get('vstrUIF')
                    vstrPaye = self.request.get('vstrPaye')
                    vstrOtherDeductions = self.request.get('vstrOtherDeductions')
                    vstrThisDate = self.request.get('vstrThisDate')
                    vstrEmployeeID = self.request.get('vstrEmployeeID')

                    try:
                        vstrThisDateList = vstrThisDate.split("-")

                        strYear = int(vstrThisDateList[0])
                        strMonth = int(vstrThisDateList[1])
                        strDay = int(vstrThisDateList[2])
                        vstrThisDate = datetime.date(year=strYear,month=strMonth,day=strDay)
                    except:
                        vstrThisDate = datetime.datetime.now()
                        vstrThisDate = vstrThisDate.date()
                        strYear = vstrThisDate.year
                        strMonth = vstrThisDate.month


                    findRequest = Salaries.query(Salaries.strIDNumber == vstrIDNumber,Salaries.strYear == str(strYear),Salaries.strMonth == str(strMonth))
                    thisSalaryList = findRequest.fetch(1)

                    if len(thisSalaryList) > 0:
                        thisSalary = thisSalaryList[0]
                    else:
                        thisSalary = Salaries()

                    thisSalary.writeChurchID(strinput=thisChurchMember.strChurchID)
                    thisSalary.writeChurchBranchID(strinput=thisChurchMember.strChurchBranchID)
                    thisSalary.writeEmployeeID(strinput=vstrEmployeeID)
                    thisSalary.writeIDNumber(strinput=vstrIDNumber)
                    thisSalary.writeOvertimeRate(strinput=vstrOverTimeRate)
                    thisSalary.writeNormalRate(strinput=vstrNormalRate)
                    thisSalary.writeUIF(strinput=vstrUIF)
                    thisSalary.writePaye(strinput=vstrPaye)
                    thisSalary.writeOtherDeductions(strinput=vstrOtherDeductions)

                    thisSalary.put()

                    self.response.write("Salary Successfully updated")

                elif vstrChoice == "3":
                    vstrIDNumber = self.request.get('vstrIDNumber')

                    findRequest = BankingDetails.query(BankingDetails.strIDNumber == vstrIDNumber)
                    thisBankingDetailsList = findRequest.fetch()

                    if len(thisBankingDetailsList) > 0:
                        thisBankingDetails = thisBankingDetailsList[0]
                    else:
                        thisBankingDetails = BankingDetails()

                    template = template_env.get_template('templates/admin/churches/employees/BankDetails.html')
                    context = {'thisBankDetails':thisBankingDetails}
                    self.response.write(template.render(context))

                elif vstrChoice == "4":
                    vstrIDNumber = self.request.get('vstrIDNumber')
                    vstrAccountOwner = self.request.get('vstrAccountOwner')
                    vstrAccountNumber = self.request.get('vstrAccountNumber')
                    vstrBankName = self.request.get('vstrBankName')
                    vstrBranchName = self.request.get('vstrBranchName')
                    vstrBranchCode = self.request.get('vstrBranchCode')
                    vstrAccountType = self.request.get('vstrAccountType')


                    findRequest = BankingDetails.query(BankingDetails.strIDNumber == vstrIDNumber)
                    thisBankingDetailsList = findRequest.fetch()

                    if len(thisBankingDetailsList) > 0:
                        thisBankingDetails = thisBankingDetailsList[0]
                    else:
                        thisBankingDetails = BankingDetails()

                    thisBankingDetails.writeIDNumber(strinput=vstrIDNumber)
                    thisBankingDetails.writeAccountOwner(strinput=vstrAccountOwner)
                    thisBankingDetails.writeAccountNumber(strinput=vstrAccountNumber)
                    thisBankingDetails.writeBankName(strinput=vstrBankName)
                    thisBankingDetails.writeBranchName(strinput=vstrBranchName)
                    thisBankingDetails.writeBranchCode(strinput=vstrBranchCode)
                    thisBankingDetails.writeAccountType(strinput=vstrAccountType)
                    thisBankingDetails.put()

                    self.response.write("Banking Details Successfully updated")

                elif vstrChoice == "5":
                    vstrIDNumber = self.request.get('vstrIDNumber')

                    findRequest = AttendanceRegister.query(AttendanceRegister.strIDNumber == vstrIDNumber)
                    thisAttendanceRegisterList = findRequest.fetch()

                    if len(thisAttendanceRegisterList) > 0:
                        thisAttendance = thisAttendanceRegisterList[0]
                    else:
                        thisAttendance = AttendanceRegister()


                    template = template_env.get_template('templates/admin/churches/employees/AttendanceRegister.html')
                    context = {'thisAttendanceRegisterList':thisAttendanceRegisterList,'thisAttendance':thisAttendance,'vstrIDNumber':vstrIDNumber}
                    self.response.write(template.render(context))

                elif vstrChoice == "6":
                    vstrNames = self.request.get('vstrNames')
                    vstrSurname = self.request.get('vstrSurname')
                    vstrIDNumber = self.request.get('vstrIDNumber')
                    vstrPosition = self.request.get('vstrPosition')
                    vstrContract = self.request.get('vstrContract')
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
                    vstrSelectBranch = self.request.get('vstrSelectBranch')

                    findRequest = ChurchMember.query(ChurchMember.strMemberID == Guser.user_id())
                    thisAdminList = findRequest.fetch()

                    if len(thisAdminList) > 0:
                        thisAdmin = thisAdminList[0]
                    else:
                        thisAdmin = ChurchMember()

                    findRequest = Employees.query(Employees.strChurchID == thisAdmin.strChurchID,Employees.strIDNumber == vstrIDNumber)
                    thisEmployeeList = findRequest.fetch()
                    if len(thisEmployeeList) > 0:
                        thisEmployee = thisEmployeeList[0]
                    else:
                        thisEmployee = Employees()

                    thisEmployee.writeNames(strinput=vstrNames)
                    thisEmployee.writeSurname(strinput=vstrSurname)
                    thisEmployee.writeIDNumber(strinput=vstrIDNumber)
                    thisEmployee.writePosition(strinput=vstrPosition)
                    thisEmployee.writeContract(strinput=vstrContract)
                    thisEmployee.writePhyStandNumber(strinput=vstrPhyStandNumber)
                    thisEmployee.writePhyStreetName(strinput=vstrPhyStreetName)
                    thisEmployee.writePhyCityTown(strinput=vstrPhyCityTown)
                    thisEmployee.writePhyProvince(strinput=vstrPhyProvince)
                    thisEmployee.writePhyCountry(strinput=vstrPhyCountry)
                    thisEmployee.writePhyCountry(strinput=vstrPhyCountry)
                    thisEmployee.writePhyPostalCode(strinput=vstrPhyPostalCode)
                    thisEmployee.writeBoxNumber(strinput=vstrBoxNumber)
                    thisEmployee.writeCityTown(strinput=vstrCityTown)
                    thisEmployee.writeProvince(strinput=vstrProvince)
                    thisEmployee.writeCountry(strinput=vstrCountry)
                    thisEmployee.writePostalCode(strinput=vstrPostalCode)
                    thisEmployee.writeChurchBranchID(strinput=vstrSelectBranch)
                    thisEmployee.writeChurchID(strinput=thisAdmin.strChurchID)
                    thisEmployee.put()


app = webapp2.WSGIApplication([
    ('/employees/.*', EmployeeHandler),

], debug=True)





