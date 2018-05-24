

var thisSendMessageButt = document.getElementById("SendMessageButt");

thisSendMessageButt.addEventListener("click", function () {
        var vstrChoice = 14;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrMessage = document.getElementById('strMessage').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID + '&vstrCell=' + vstrCell +
        '&vstrMessage=' + vstrMessage;
          $.ajax({
                type: "post",
                url: "/admin/clients/" + vstrClientID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SendMessageINFDIV').html(html)
              }
          });
});
