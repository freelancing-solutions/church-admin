var thisMeetingDetailsButt = document.getElementById("MeetingDetailsButt");
var thisAttendeesButt = document.getElementById("AttendeesButt");
var thisAgendaButt = document.getElementById("AgendaButt");
var thisMeetingFacilitatorButt = document.getElementById("MeetingFacilitatorButt");
var thisMeetingMinutesButt = document.getElementById("MeetingMinutesButt");
var thisPrintMeetingDetailsButt = document.getElementById("PrintMeetingDetailsButt");

thisMeetingDetailsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#MeetingsINFDIV').html(html)
              }
          })
});
thisAttendeesButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#MeetingsINFDIV').html(html)
              }
          })
});
thisAgendaButt.addEventListener("click", function () {
        var vstrChoice = 5;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#MeetingsINFDIV').html(html)
              }
          })
});
thisMeetingFacilitatorButt.addEventListener("click", function () {
        var vstrChoice = 8;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#MeetingsINFDIV').html(html)
              }
          })
});
thisMeetingMinutesButt.addEventListener("click", function () {
        var vstrChoice = 10;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#MeetingsINFDIV').html(html)
              }
          })
});
thisPrintMeetingDetailsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrMeetingID = document.getElementById('strMeetingID').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID;
          $.ajax({
                type: "get",
                url: "/admin/meetings/print",
                data: dataString,
                cache: false,
              success: function(html){
                $('#MeetingsINFDIV').html(html)
              }
          })
});