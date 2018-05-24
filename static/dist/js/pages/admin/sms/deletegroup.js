var thisDeleteGroupButt = document.getElementById("DeleteGroupButt");
thisDeleteGroupButt.addEventListener("click", function () {
        var vstrChoice =8;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var thisURL = "/sms/groupman/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#DeleteSMSGroupINFDIV').html(html)
              }
          })
});