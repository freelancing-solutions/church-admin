

var thisEmployeeDetailsButt = document.getElementById("EmployeeDetailsButt");
var thisSalaryDetailsButt = document.getElementById("SalaryDetailsButt");
var thisBankingDetailsButt = document.getElementById("BankingDetailsButt");
var thisAttendanceButt = document.getElementById("AttendanceButt");
var thisUpdatePersonalButt = document.getElementById("UpdatePersonalButt");

thisEmployeeDetailsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var thisURL = "/employees/" + vstrIDNumber;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID + '&vstrIDNumber=' + vstrIDNumber;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#EmployeeDetailsINFDIV').html(html)
              }
          })
});
thisSalaryDetailsButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var thisURL = "/employees/" + vstrIDNumber;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID + '&vstrIDNumber=' + vstrIDNumber;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#EmployeeDetailsINFDIV').html(html)
              }
          })
});
thisBankingDetailsButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var thisURL = "/employees/" + vstrIDNumber;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID + '&vstrIDNumber=' + vstrIDNumber;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#EmployeeDetailsINFDIV').html(html)
              }
          })
});
thisAttendanceButt.addEventListener("click", function () {
        var vstrChoice = 5;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var thisURL = "/employees/" + vstrIDNumber;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID + '&vstrIDNumber=' + vstrIDNumber;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#EmployeeDetailsINFDIV').html(html)
              }
          })
});
thisUpdatePersonalButt.addEventListener("click", function () {
        var vstrChoice = 6;

        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var vstrPosition = document.getElementById('strPosition').value;
        var vstrContract = document.getElementById('strContract').value;
        var vstrPhyStandNumber = document.getElementById('strPhyStandNumber').value;
        var vstrPhyStreetName = document.getElementById('strPhyStreetName').value;
        var vstrPhyCityTown = document.getElementById('strPhyCityTown').value;
        var vstrPhyProvince = document.getElementById('strPhyProvince').value;
        var vstrPhyCountry = document.getElementById('strPhyCountry').value;
        var vstrPhyPostalCode = document.getElementById('strPhyPostalCode').value;

        var vstrBoxNumber = document.getElementById('strBoxNumber').value;
        var vstrCityTown = document.getElementById('strCityTown').value;
        var vstrProvince = document.getElementById('strProvince').value;
        var vstrCountry = document.getElementById('strCountry').value;
        var vstrPostalCode = document.getElementById('strPostalCode').value;

        var vstrSelectBranch = document.getElementById('strSelectBranch').value;


        var thisURL = "/employees/" + vstrIDNumber;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrIDNumber=' + vstrIDNumber +
        '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname + '&vstrPosition=' + vstrPosition +
        '&vstrContract=' + vstrContract + '&vstrPhyStandNumber=' + vstrPhyStandNumber + '&vstrPhyStreetName=' + vstrPhyStreetName +
        '&vstrPhyCityTown=' + vstrPhyCityTown + '&vstrPhyProvince=' + vstrPhyProvince + '&vstrPhyCountry=' + vstrPhyCountry +
        '&vstrPhyPostalCode=' + vstrPhyPostalCode + '&vstrBoxNumber=' + vstrBoxNumber + '&vstrCityTown=' + vstrCityTown +
        '&vstrProvince=' + vstrProvince + '&vstrCountry=' + vstrCountry + '&vstrPostalCode=' + vstrPostalCode +
        '&vstrSelectBranch=' + vstrSelectBranch;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#EmployeeDetailsINFDIV').html(html)
              }
          })
});