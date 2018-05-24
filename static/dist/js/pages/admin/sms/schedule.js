var thisSetScheduleButt = document.getElementById("SetScheduleButt");
thisSetScheduleButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var vstrMessageID = document.getElementById('strMessageID').value;
        var vstrScheduleTime = document.getElementById('strScheduleTime').value;
        if ($('#strNotifyOnStart').is(":checked")){
            vstrNotifyOnStart = "Yes"
        }else{
            vstrNotifyOnStart = "No"
        }
        if ($('#strNotifyOnEnd').is(":checked")){

            vstrNotifyOnEnd = "Yes"
        }else{
            vstrNotifyOnEnd = "No"
        }
        var thisURL = "/sms/manage/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrMessageID=' + vstrMessageID +
                '&vstrScheduleTime=' + vstrScheduleTime + '&vstrNotifyOnStart=' + vstrNotifyOnStart + '&vstrNotifyOnEnd=' + vstrNotifyOnEnd;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SetScheduleINFDIV').html(html)
              }
          })
});