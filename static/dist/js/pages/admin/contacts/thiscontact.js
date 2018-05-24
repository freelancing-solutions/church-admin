var thisManageContactButt = document.getElementById("ManageContactButt");
var thisSendSMSMessageButt = document.getElementById("SendSMSMessageButt");
var thisSendEmailMessageButt = document.getElementById("SendEmailMessageButt");

thisManageContactButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrCell= document.getElementById('strCell').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrCell=' + vstrCell;
          $.ajax({
                type: "post",
                url: "/admin/contacts/" + vstrCell,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ContactsINFDIV').html(html)
              }
          })
});
thisSendSMSMessageButt.addEventListener("click", function () {
        var vstrChoice = 4;

        var vstrCell= document.getElementById('strCell').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrCell=' + vstrCell;
          $.ajax({
                type: "post",
                url: "/admin/contacts/" + vstrCell,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ContactsINFDIV').html(html)
              }
          })
});
thisSendEmailMessageButt.addEventListener("click", function () {
        var vstrChoice = 6;

        var vstrCell= document.getElementById('strCell').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrCell=' + vstrCell;
          $.ajax({
                type: "post",
                url: "/admin/contacts/" + vstrCell,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ContactsINFDIV').html(html)
              }
          })
});