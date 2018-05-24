
var thisUploadSaveButt = document.getElementById("UploadSaveButt");
thisUploadSaveButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrEmail = document.getElementById('strEmail').value;
        var vstrEventID = document.getElementById('strEventID').value;


        var dataString = '&vstrChoice='+ vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
            '&vstrCell=' + vstrCell + '&vstrEmail=' + vstrEmail + '&vstrEventID=' + vstrEventID;
          $.ajax({
                type: "post",
                url: "/events/public/" + vstrChoice,
                data: dataString,
                cache: false,
              success: function(html){
                $('#EventRegistrationINFDIV').html(html)
              }
          })
});