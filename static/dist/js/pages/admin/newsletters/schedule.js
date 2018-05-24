var thisUpdateScheduleButt = document.getElementById("UpdateScheduleButt");

thisUpdateScheduleButt.addEventListener("click", function () {
        var vstrChoice = 7;
        var vstrListID = document.getElementById('strListID').value;
        var vstrDate = document.getElementById('strDate').value;
        var vstrTime = document.getElementById('strTime').value;

        var thisURL = "/admin/newsletters/" + vstrListID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrListID=' + vstrListID + '&vstrDate=' + vstrDate +
                '&vstrTime=' + vstrTime;
          $.ajax({
                type: "post",
                url:thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateScheduleINFDIV').html(html)
              }
          })
});