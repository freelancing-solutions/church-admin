var thisSendMessageButt = document.getElementById("SendMessageButt");

thisSendMessageButt.addEventListener("click", function () {
        var vstrChoice = 5;
        var vstrDonatorID = document.getElementById('strDonatorID').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrMessage = document.getElementById('strMessage').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrDonatorID=' + vstrDonatorID + '&vstrCell=' + vstrCell +
        '&vstrMessage=' + vstrMessage;
          $.ajax({
                type: "post",
                url: "/monetary/donators/" + vstrDonatorID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SendMessageINFDIV').html(html)
              }
          });
});