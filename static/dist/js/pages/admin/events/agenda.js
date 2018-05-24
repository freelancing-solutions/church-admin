var thisUpdateAgendaButt = document.getElementById("UpdateAgendaButt");

thisUpdateAgendaButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrTitle = document.getElementById('strTitle').value;
        var vstrAgendaDescription = document.getElementById('strAgendaDescription').value;
        var vstrSpeaker = document.getElementById('strSpeaker').value;
        var vstrStartDate = document.getElementById('strStartDate').value;
        var vstrStartTime = document.getElementById('strStartTime').value;
        var vstrEndDate = document.getElementById('strEndDate').value;
        var vstrEndTime = document.getElementById('strEndTime').value;
        var vstrEventID = document.getElementById('strEventID').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrTitle=' + vstrTitle + '&vstrAgendaDescription=' + vstrAgendaDescription +
                        '&vstrSpeaker=' + vstrSpeaker + '&vstrStartDate=' + vstrStartDate + '&vstrStartTime=' + vstrStartTime +
                        '&vstrEndDate=' + vstrEndDate + '&vstrEndTime=' + vstrEndTime + '&vstrEventID=' + vstrEventID;
          $.ajax({
                type: "post",
                url: "/events/registrations/" + vstrEventID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#AgendaINFDIV').html(html)
              }
          })
});