
var thisUploadPostalAddressButt = document.getElementById("UploadPostalAddressButt");
var thisUploadNotesButt = document.getElementById("UploadNotesButt");
var thisUploadPhysicalAddressButt = document.getElementById("UploadPhysicalAddressButt");

thisUploadPostalAddressButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrBox = document.getElementById('strBox').value;
        var vstrCityTown = document.getElementById('strCityTown').value;
        var vstrProvince = document.getElementById('strProvince').value;
        var vstrCountry = document.getElementById('strCountry').value;
        var vstrPostalCode = document.getElementById('strPostalCode').value;
        var vstrContactID = document.getElementById('strContactID').value;
        var vstrCell = document.getElementById('strCell').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrBox=' + vstrBox + '&vstrCityTown=' + vstrCityTown +
                '&vstrProvince=' + vstrProvince + '&vstrCountry=' + vstrCountry + '&vstrPostalCode=' + vstrPostalCode +
                '&vstrContactID=' + vstrContactID + '&vstrCell=' + vstrCell;
          $.ajax({
                type: "post",
                url: "/admin/contacts/" + vstrCell,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadAddressINFDIV').html(html)
              }
          })
});
thisUploadNotesButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrCell = document.getElementById('strCell').value;
        var vstrSubject = document.getElementById('strSubject').value;
        var vstrNotes = document.getElementById('strNotes').value;
        var vstrContactID = document.getElementById('strContactID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSubject=' + vstrSubject + '&vstrNotes=' + vstrNotes + '&vstrContactID=' + vstrContactID;
          $.ajax({
                type: "post",
                url: "/admin/contacts/" + vstrCell,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadNotesINFDIV').html(html)
              }
          })
});

thisUploadPhysicalAddressButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrStandNumber = document.getElementById('strStandNumber').value;
        var vstrStreetName = document.getElementById('strStreetName').value;
        var vstrPhyCityTown = document.getElementById('strPhyCityTown').value;
        var vstrPhyProvince = document.getElementById('strPhyProvince').value;
        var vstrPhyCountry = document.getElementById('strPhyCountry').value;
        var vstrPhyPostalCode = document.getElementById('strPhyPostalCode').value;
        var vstrContactID = document.getElementById('strContactID').value;
        var dataString = '&vstrChoice='+ vstrChoice +'&vstrStandNumber=' + vstrStandNumber + '&vstrStreetName=' + vstrStreetName +
                '&vstrPhyCityTown=' + vstrPhyCityTown + '&vstrPhyProvince=' + vstrPhyProvince + '&vstrPhyCountry=' + vstrPhyCountry +
                '&vstrPhyPostalCode=' + vstrPhyPostalCode + '&vstrContactID=' + vstrContactID;
          $.ajax({
                type: "post",
                url: "/admin/contacts/" + vstrCell,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadPhysicalAddressINFDIV').html(html)
              }
          })
});