

var thisUpdateContactsButt = document.getElementById("UpdateContactsButt");

thisUpdateContactsButt.addEventListener("click", function () {
        var vstrChoice = 6;
        var vstrSupplierID = document.getElementById('strSupplierID').value;

        var vstrCell = document.getElementById('strCell').value;
        var vstrTel = document.getElementById('strTel').value;
        var vstrFax = document.getElementById('strFax').value;
        var vstrEmail = document.getElementById('strEmail').value;
        var vstrWebsite = document.getElementById('strWebsite').value;
        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID+
                '&vstrCell=' + vstrCell + '&vstrTel=' + vstrTel + '&vstrFax=' + vstrFax +
            '&vstrEmail=' + vstrEmail + '&vstrWebsite=' + vstrWebsite;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateContactINFDIV').html(html)
              }
          })
});