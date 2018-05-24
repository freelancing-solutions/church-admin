      function countChar(val) {
        var len = val.value.length;
        if (len >= 150) {
          val.value = val.value.substring(0, 150);
        } else {
          $('#charNum').html("Character Limit = " + (150 - len));
        }
      }

var thisUploadMessageButt = document.getElementById("UploadMessageButt");
thisUploadMessageButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var vstrMessageID = document.getElementById('strMessageID').value;
        var vstrMessage = document.getElementById('strMessage').value;

        var thisURL = "/sms/manage/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrMessageID=' + vstrMessageID +
            '&vstrMessage=' + vstrMessage;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SMSMessageINfDIV').html(html)
              }
          })
});