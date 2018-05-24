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
        var vstrChoice = 3;
        var vstrMessage = document.getElementById('strMessage').value;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var thisURL = "/sms/groupman/" + vstrGroupID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMessage=' + vstrMessage +'&vstrGroupID=' + vstrGroupID;
          $.ajax({
                type: "post",
                url:thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadMessageStatusINFDIV').html(html)
              }
          })
});