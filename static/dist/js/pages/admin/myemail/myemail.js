var thisUpdateEmailSettingsButt = document.getElementById("UpdateEmailSettingsButt");
var thisInboxButt = document.getElementById("InboxButt");
var thisSentButt = document.getElementById("SentButt");
var thisDraftbutt = document.getElementById("Draftbutt");
var thisComposeButt = document.getElementById("ComposeButt");

thisUpdateEmailSettingsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrEmailAddress = document.getElementById('strEmailAddress').value;
        var vstrName = document.getElementById('strName').value;
        var vstrSignature = document.getElementById('strSignature').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrEmailAddress=' + vstrEmailAddress + '&vstrName=' + vstrName + '&vstrSignature=' + vstrSignature;
          $.ajax({
                type: "post",
                url: "/admin/myemail",
                data: dataString,
                cache: false,
              success: function(html){
                $('#EmailSettingsINFDIV').html(html)
              }
          });
});
thisInboxButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "post",
                url: "/admin/myemail",
                data: dataString,
                cache: false,
              success: function(html){
                $('#MyEmailINFDIV').html(html)
              }
          })
});
thisSentButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "post",
                url: "/admin/myemail",
                data: dataString,
                cache: false,
              success: function(html){
                $('#MyEmailINFDIV').html(html)
              }
          })
});
thisDraftbutt.addEventListener("click", function () {
        var vstrChoice = 3;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "post",
                url: "/admin/myemail",
                data: dataString,
                cache: false,
              success: function(html){
                $('#MyEmailINFDIV').html(html)
              }
          })
});
thisComposeButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "post",
                url: "/admin/myemail",
                data: dataString,
                cache: false,
              success: function(html){
                $('#MyEmailINFDIV').html(html)
              }
          })
});
