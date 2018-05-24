var thisUpdatedMemberAddressButt = document.getElementById("UpdatedMemberAddressButt");
thisUpdatedMemberAddressButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrMemberID = document.getElementById('strMemberID').value;
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

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID + '&vstrPhyStandNumber=' + vstrPhyStandNumber +
            '&vstrPhyStreetName=' + vstrPhyStreetName + '&vstrPhyCityTown=' + vstrPhyCityTown + '&vstrPhyProvince=' + vstrPhyProvince +
            '&vstrPhyCountry=' + vstrPhyCountry + '&vstrPhyPostalCode=' + vstrPhyPostalCode + '&vstrPosBoxNumber=' + vstrPosBoxNumber +
            '&vstrPosCityTown=' + vstrPosCityTown + '&vstrPosProvince=' + vstrPosProvince + '&vstrPosCountry=' + vstrPosCountry +
            '&vstrPosPostalCode=' + vstrPosPostalCode;
          $.ajax({
                type: "post",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddressINFDIV').html(html)
              }
          })
});