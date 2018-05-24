

var thisPhysicalAddressButt = document.getElementById("PhysicalAddressButt");

thisPhysicalAddressButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrClientID = document.getElementById('strClientID').value;

        var vstrStandNumber = document.getElementById('strStandNumber').value;
        var vstrStreetName = document.getElementById('strStreetName').value;
        var vstrCityTown = document.getElementById('strCityTown').value;
        var vstrProvince = document.getElementById('strProvince').value;
        var vstrCountry = document.getElementById('strCountry').value;
        var vstrPostalCode = document.getElementById('strPostalCode').value;


        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID +
                '&vstrStandNumber=' + vstrStandNumber + '&vstrStreetName=' + vstrStreetName + '&vstrCityTown=' + vstrCityTown +
                '&vstrProvince=' + vstrProvince + '&vstrCountry=' + vstrCountry + '&vstrPostalCode=' + vstrPostalCode;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#PhysicalAddressINFDIV').html(html)
              }
          })
});