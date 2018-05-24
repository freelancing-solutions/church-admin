var thisSendMessageButt = document.getElementById("SendMessageButt");
thisSendMessageButt.addEventListener("click", function () {
        var vstrChoice = 5;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var vstrMessageID = document.getElementById('strMessageID').value;
        var thisURL = "/sms/manage/" + vstrGroupID;
        document.getElementById('SendMessageButt').classList.add('hidden');
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrMessageID=' + vstrMessageID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SendNowINFDIV').html(html)
              }
          })
});