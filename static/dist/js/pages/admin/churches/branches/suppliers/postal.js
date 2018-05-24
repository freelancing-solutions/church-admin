

var thisUpdatePostalAddressButt = document.getElementById("UpdatePostalAddressButt");

thisUpdatePostalAddressButt.addEventListener("click", function () {
        var vstrChoice = 7;
        var vstrSupplierID = document.getElementById('strSupplierID').value;
        var vstrPostalAddress = document.getElementById('strPostalAddress').value;
        var vstrCityTown = document.getElementById('strCityTown').value;
        var vstrProvince = document.getElementById('strProvince').value;
        var vstrCountry = document.getElementById('strCountry').value;
        var vstrPostalCode = document.getElementById('strPostalCode').value;

        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID + '&vstrPostalAddress=' + vstrPostalAddress +
            '&vstrCityTown=' + vstrCityTown + '&vstrProvince=' + vstrProvince + '&vstrCountry=' + vstrCountry +
            '&vstrPostalCode=' + vstrPostalCode;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdatePostalINFDIV').html(html)
              }
          })
});