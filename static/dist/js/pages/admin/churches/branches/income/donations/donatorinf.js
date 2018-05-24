var thisUpdateDonatorButt = document.getElementById("UpdateDonatorButt");


thisUpdateDonatorButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrDonatorID = document.getElementById('strDonatorID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var vstrInstitutionName = document.getElementById('strInstitutionName').value;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var vstrPhyStandNumber = document.getElementById('strPhyStandNumber').value;
        var vstrPhyStreetName = document.getElementById('strPhyStreetName').value;
        var vstrPhyCityTown = document.getElementById('strPhyCityTown').value;
        var vstrPhyProvince = document.getElementById('strPhyProvince').value;
        var vstrPhyCountry = document.getElementById('strPhyCountry').value;
        var vstrPhyPostalCode = document.getElementById('strPhyPostalCode').value;
        var vstrPosBoxNumber = document.getElementById('strPosBoxNumber').value;
        var vstrPosCityTown = document.getElementById('strPosCityTown').value;
        var vstrPosProvince = document.getElementById('strPosProvince').value;
        var vstrPosCountry = document.getElementById('strPosCountry').value;
        var vstrPosPostalCode = document.getElementById('strPosPostalCode').value;
        var vstrTel = document.getElementById('strTel').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrEmail = document.getElementById('strEmail').value;
        var vstrWebsite = document.getElementById('strWebsite').value;
        var thisURL = "/monetary/donators/" + vstrDonatorID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrDonatorID=' + vstrDonatorID + '&vstrChurchID=' + vstrChurchID +
                '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrInstitutionName=' + vstrInstitutionName + '&vstrNames=' + vstrNames +
                '&vstrSurname=' + vstrSurname + '&vstrIDNumber=' + vstrIDNumber + '&vstrPhyStandNumber=' + vstrPhyStandNumber + '&vstrPhyStreetName=' + vstrPhyStreetName +
                '&vstrPhyCityTown=' + vstrPhyCityTown + '&vstrPhyProvince=' + vstrPhyProvince + '&vstrPhyCountry=' + vstrPhyCountry +
                '&vstrPhyPostalCode=' + vstrPhyPostalCode + '&vstrPosBoxNumber=' + vstrPosBoxNumber + '&vstrPosCityTown=' + vstrPosCityTown +
                '&vstrPosProvince=' + vstrPosProvince + '&vstrPosCountry=' + vstrPosCountry + '&vstrPosPostalCode=' + vstrPosPostalCode +
                '&vstrTel=' + vstrTel + '&vstrCell=' + vstrCell + '&vstrEmail=' + vstrEmail + '&vstrWebsite=' + vstrWebsite;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdatedDonatorINFDIV').html(html)
              }
          });

});