var thisUploadContactsButt = document.getElementById("UploadContactsButt");
thisUploadContactsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrTel = document.getElementById('strTel').value;
        var vstrFax = document.getElementById('strFax').value;
        var vstrEmail = document.getElementById('strEmail').value;
        var vstrWebsite = document.getElementById('strWebsite').value;
        var vstrTitle = document.getElementById('strTitle').value;
        var vstrDateCreated = document.getElementById('strDateCreated').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname + '&vstrSurname=' + vstrSurname +
            '&vstrCell=' + vstrCell + '&vstrTel=' + vstrTel + '&vstrFax=' + vstrFax + '&vstrEmail=' + vstrEmail + '&vstrWebsite=' + vstrWebsite +
            '&vstrDateCreated=' + vstrDateCreated + '&vstrTitle=' + vstrTitle;
          $.ajax({
                type: "post",
                url: "/admin/contacts",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadContactINFDIV').html(html)
              }
          })
});