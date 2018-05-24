

var thisUpdatePhysicalButt = document.getElementById("UpdatePhysicalButt");

thisUpdatePhysicalButt.addEventListener("click", function () {
        var vstrChoice = 8;
        var vstrSupplierID = document.getElementById('strSupplierID').value;

        var vstrStandNumber = document.getElementById('strStandNumber').value;
        var vstrStreetName = document.getElementById('strStreetName').value;
        var vstrCityTown = document.getElementById('strCityTown').value;
        var vstrProvince = document.getElementById('strProvince').value;
        var vstrCountry = document.getElementById('strCountry').value;
        var vstrPostalCode = document.getElementById('strPostalCode').value;


        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID +
                '&vstrStandNumber=' + vstrStandNumber + '&vstrStreetName=' + vstrStreetName + '&vstrCityTown=' + vstrCityTown +
                '&vstrProvince=' + vstrProvince + '&vstrCountry=' + vstrCountry + '&vstrPostalCode=' + vstrPostalCode;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdatePhysicalINFDIV').html(html)
              }
          })
});