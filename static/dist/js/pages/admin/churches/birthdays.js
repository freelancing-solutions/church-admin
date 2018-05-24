
var thisUploadMessageButt = document.getElementById("UploadMessageButt");

thisUploadMessageButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrBirthdayWishes = document.getElementById('strBirthdayWishes').value;
        var vstrAutoSendMessages = document.getElementById('strAutoSendMessages').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrBirthdayWishes=' + vstrBirthdayWishes + '&vstrChurchID=' + vstrChurchID +
            '&vstrAutoSendMessages=' + vstrAutoSendMessages;
          $.ajax({
                type: "post",
                url: "/events",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadMessageINFDIV').html(html)
              }
          })
});