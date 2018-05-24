

var thisUpdatePostalAddressButt = document.getElementById("UpdatePostalAddressButt");

thisUpdatePostalAddressButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrPostalAddress = document.getElementById('strPostalAddress').value;
        var vstrCityTown = document.getElementById('strCityTown').value;
        var vstrProvince = document.getElementById('strProvince').value;
        var vstrCountry = document.getElementById('strCountry').value;
        var vstrPostalCode = document.getElementById('strPostalCode').value;

        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID + '&vstrPostalAddress=' + vstrPostalAddress +
            '&vstrCityTown=' + vstrCityTown + '&vstrProvince=' + vstrProvince + '&vstrCountry=' + vstrCountry +
            '&vstrPostalCode=' + vstrPostalCode;
          $.ajax({
                type: "get",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#PostalAddressINFDIV').html(html)
              }
          })
});