function countChar(val) {
    var len = val.value.length;
    if (len >= 600)
    {
      val.value = val.value.substring(0, 600);
    } else
        {
            $('#charNum').html("Character Limit = " + (600 - len));
        }
}

var thisSendMessageButt = document.getElementById("SendMessageButt");

thisSendMessageButt.addEventListener("click", function () {
        var vstrChoice = 5;
        var vstrContactID = document.getElementById('strContactID').value;
        var vstrMessage = document.getElementById('strMessage').value;
        var vstrCell = document.getElementById('strCell').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMessage=' + vstrMessage + '&vstrContactID=' + vstrContactID + '&vstrCell=' + vstrCell;
          $.ajax({
                type: "post",
                url: "/admin/contacts/" + vstrCell,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SMSMessageINfDIV').html(html)
              }
          })
});