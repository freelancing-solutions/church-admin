var thisSendMessageButt = document.getElementById("SendMessageButt");

thisSendMessageButt.addEventListener("click", function () {
        var vstrChoice = 12;
        var vstrMemberID = document.getElementById('strMemberID').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrMessage = document.getElementById('strMessage').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID + '&vstrCell=' + vstrCell +
        '&vstrMessage=' + vstrMessage;
          $.ajax({
                type: "get",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#SendMessageINFDIV').html(html)
              }
          })
});