
var thisUpdateBranchContactsButt = document.getElementById("UpdateBranchContactsButt");
thisUpdateBranchContactsButt.addEventListener("click", function () {
        var vstrChoice = 11;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var vstrPhyStandNumber = document.getElementById('strPhyStandNumber').value;
        var vstrPhyStreetName = document.getElementById('strPhyStreetName').value;
        var vstrPhyCityTown = document.getElementById('strPhyCityTown').value;
        var vstrPhyProvince = document.getElementById('strPhyProvince').value;
        var vstrPhyCountry = document.getElementById('strPhyCountry').value;
        var vstrPhyPostalCode = document.getElementById('strPhyPostalCode').value;
        var vstrPosAddress = document.getElementById('strPosAddress').value;
        var vstrPosCityTown = document.getElementById('strPosCityTown').value;
        var vstrPosProvince = document.getElementById('strPosProvince').value;
        var vstrPosCountry = document.getElementById('strPosCountry').value;
        var vstrPostPostalCode = document.getElementById('strPostPostalCode').value;
        var vstrTel = document.getElementById('strTel').value;
        var vstrFax = document.getElementById('strFax').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrEmail = document.getElementById('strEmail').value;
        var vstrWebsite = document.getElementById('strWebsite').value;
        var vstrCPNames = document.getElementById('strCPNames').value;
        var vstrCPTitle = document.getElementById('strCPTitle').value;
        var vstrCPGender = document.getElementById('strCPGender').value;
        var thisURL = "/admin/branches/" + vstrChurchBranchID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID +
                '&vstrPhyStandNumber=' + vstrPhyStandNumber + '&vstrPhyStreetName=' + vstrPhyStreetName + '&vstrPhyCityTown=' + vstrPhyCityTown +
                '&vstrPhyProvince=' + vstrPhyProvince + '&vstrPhyCountry=' + vstrPhyCountry + '&vstrPhyPostalCode=' + vstrPhyPostalCode +
                '&vstrPosAddress=' + vstrPosAddress + '&vstrPosCityTown=' + vstrPosCityTown + '&vstrPosProvince=' + vstrPosProvince +
                '&vstrPosCountry=' + vstrPosCountry + '&vstrPostPostalCode=' + vstrPostPostalCode + '&vstrTel=' + vstrTel + '&vstrFax=' + vstrFax +
                '&vstrCell=' + vstrCell + '&vstrEmail=' + vstrEmail + '&vstrWebsite=' + vstrWebsite + '&vstrCPNames=' + vstrCPNames +
                '&vstrCPTitle=' + vstrCPTitle + '&vstrCPGender=' + vstrCPGender;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchContactINFDIV').html(html)
              }
          });
});