var thisEditSMSButt = document.getElementById("EditSMSButt");
var thisManageScheduleButt = document.getElementById("ManageScheduleButt");
var thisSendNowButt = document.getElementById("SendNowButt");
var thisMessageDeliveryReportsButt = document.getElementById("MessageDeliveryReportsButt");

thisEditSMSButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var vstrMessageID = document.getElementById('strMessageID').value;
        var thisURL = "/sms/manage/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrMessageID=' + vstrMessageID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SMSINFDIV').html(html)
              }
          })
});
thisManageScheduleButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var vstrMessageID = document.getElementById('strMessageID').value;
        var thisURL = "/sms/manage/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrMessageID=' + vstrMessageID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SMSINFDIV').html(html)
              }
          })
});
thisSendNowButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var vstrMessageID = document.getElementById('strMessageID').value;
        var thisURL = "/sms/manage/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrMessageID=' + vstrMessageID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SMSINFDIV').html(html)
              }
          })
});
thisMessageDeliveryReportsButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var vstrMessageID = document.getElementById('strMessageID').value;
        var thisURL = "/sms/manage/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrMessageID=' + vstrMessageID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SMSINFDIV').html(html)
              }
          })
});