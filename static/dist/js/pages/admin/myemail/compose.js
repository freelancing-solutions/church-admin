var thisDraftButt = document.getElementById("DraftButt");
var thisSendButt = document.getElementById("SendButt");
thisDraftButt.addEventListener("click", function () {
        var vstrChoice = 5;
        var vstrToEmail = document.getElementById('strToEmail').value;
        var vstrSubject = document.getElementById('strSubject').value;
        var vstrEmailText = document.getElementById('strEmailText').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrToEmail=' + vstrToEmail + '&vstrSubject=' + vstrSubject +
                '&vstrEmailText=' + vstrEmailText ;
          $.ajax({
                type: "post",
                url: "/admin/myemail",
                data: dataString,
                cache: false,
              success: function(html){
                $('#ComposeStatusINFDIV').html(html)
              }
          })
});
thisSendButt.addEventListener("click", function () {
        var vstrChoice = 6;
        var vstrToEmail = document.getElementById('strToEmail').value;
        var vstrSubject = document.getElementById('strSubject').value;
        var vstrEmailText = document.getElementById('strEmailText').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrToEmail=' + vstrToEmail + '&vstrSubject=' + vstrSubject +
                '&vstrEmailText=' + vstrEmailText ;
          $.ajax({
                type: "post",
                url: "/admin/myemail",
                data: dataString,
                cache: false,
              success: function(html){
                $('#ComposeStatusINFDIV').html(html)
              }
          })
});