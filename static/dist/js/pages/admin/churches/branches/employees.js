

var thisAddEmployeeButt = document.getElementById("AddEmployeeButt");
thisAddEmployeeButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
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
        var vstrDateOfEmployment = document.getElementById('strDateOfEmployment').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var vstrSelectBranch = document.getElementById('strSelectBranch').value;

        var thisURL = "/admin/branches/" + vstrChurchBranchID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID +
                '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname + '&vstrIDNumber=' + vstrIDNumber + '&vstrPhyStandNumber=' + vstrPhyStandNumber +
                '&vstrPhyStreetName=' + vstrPhyStreetName + '&vstrPhyCityTown=' + vstrPhyCityTown + '&vstrPhyProvince=' + vstrPhyProvince +
                '&vstrPhyCountry=' + vstrPhyCountry + '&vstrPhyPostalCode=' + vstrPhyPostalCode + '&vstrBoxNumber=' + vstrBoxNumber +
                '&vstrCityTown=' + vstrCityTown + '&vstrProvince=' + vstrProvince + '&vstrCountry=' + vstrCountry +
                '&vstrPostalCode=' + vstrPostalCode + '&vstrDateOfEmployment=' + vstrDateOfEmployment + '&vstrSelectBranch=' + vstrSelectBranch;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddEmployeeINFDIV').html(html)
              }
          })
});