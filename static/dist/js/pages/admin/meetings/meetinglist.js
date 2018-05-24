var thisSaveMeetingButt = document.getElementById("SaveMeetingButt");
thisSaveMeetingButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrMeetingSubject = document.getElementById('strMeetingSubject').value;
        var vstrIntroduction = document.getElementById('strIntroduction').value;
        var vstrDateSchedule = document.getElementById('strDateSchedule').value;
        var vstrTimeScheduled = document.getElementById('strTimeScheduled').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingSubject=' + vstrMeetingSubject + '&vstrIntroduction=' + vstrIntroduction +
                '&vstrDateSchedule=' + vstrDateSchedule + '&vstrTimeScheduled=' + vstrTimeScheduled;
          $.ajax({
                type: "post",
                url: "/admin/meetings",
                data: dataString,
                cache: false,
              success: function(html){
                $('#SaveMeetingINFDIV').html(html)
              }
          })
});