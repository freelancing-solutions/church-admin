var thisUpdateAgendaTitleButt = document.getElementById("UpdateAgendaTitleButt");
var thisUploadAgendaItemsButt = document.getElementById("UploadAgendaItemsButt");
thisUpdateAgendaTitleButt.addEventListener("click", function () {
        var vstrChoice = 6;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var vstrAgendaTitle  = document.getElementById('strAgendaTitle').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID + '&vstrAgendaTitle=' + vstrAgendaTitle;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateAgendaTitleINFDIV').html(html)
              }
          })
});
thisUploadAgendaItemsButt.addEventListener("click", function () {
        var vstrChoice = 7;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var vstrItemName  = document.getElementById('strItemName').value;
        var vstrNotes = document.getElementById('strNotes').value;
        var vstrFromTime = document.getElementById('strFromTime').value;
        var vstrToTime = document.getElementById('strToTime').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID + '&vstrItemName=' + vstrItemName +
                '&vstrNotes=' + vstrNotes + '&vstrFromTime=' + vstrFromTime + '&vstrToTime=' + vstrToTime;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#AgendaItemsINFDIV').html(html)
              }
          })
});