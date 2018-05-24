

var thisUpdateContactButt = document.getElementById("UpdateContactButt");

thisUpdateContactButt.addEventListener("click", function () {
        var vstrChoice = 6;
        var vstrClientID = document.getElementById('strClientID').value;

        var vstrCell = document.getElementById('strCell').value;
        var vstrTel = document.getElementById('strTel').value;
        var vstrFax = document.getElementById('strFax').value;
        var vstrEmail = document.getElementById('strEmail').value;
        var vstrWebsite = document.getElementById('strWebsite').value;
        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID +
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