var thisContactsButt = document.getElementById("ContactsButt");
var thisCreateGroupMessageButt = document.getElementById("CreateGroupMessageButt");
var thisEditSMSGroupButt = document.getElementById("EditSMSGroupButt");
var thisDeleteSMSGroupButt = document.getElementById("DeleteSMSGroupButt");
var thisMessageDeliveryReports = document.getElementById("MessageDeliveryReports");

thisContactsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var thisURL = "/sms/groupman/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#GroupSMSINFDIV').html(html)
              }
          })
});
thisCreateGroupMessageButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var thisURL = "/sms/groupman/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#GroupSMSINFDIV').html(html)
              }
          })
});
thisEditSMSGroupButt.addEventListener("click", function () {
        var vstrChoice = 5;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var thisURL = "/sms/groupman/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#GroupSMSINFDIV').html(html)
              }
          })
});
thisDeleteSMSGroupButt.addEventListener("click", function () {
        var vstrChoice = 7;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var thisURL = "/sms/groupman/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#GroupSMSINFDIV').html(html)
              }
          })
});
thisMessageDeliveryReports.addEventListener("click", function () {
        var vstrChoice = 10;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var thisURL = "/sms/groupman/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#GroupSMSINFDIV').html(html)
              }
          })
});