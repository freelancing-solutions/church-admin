function countChar(val)
{
    var len = val.value.length;
    if (len >= 150) {
      val.value = val.value.substring(0, 150);
    } else {
      $('#charNum').html("Character Limit = " + (150 - len));
    }
}

var thisSendSMSInviteButt = document.getElementById("SendSMSInviteButt");
var thisUpdateAttendeeButt = document.getElementById("UpdateAttendeeButt");
var thisRemoveAttendeeButt = document.getElementById("RemoveAttendeeButt");

thisSendSMSInviteButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var vstrInviteMessage = document.getElementById('strInviteMessage').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID + '&vstrInviteMessage=' + vstrInviteMessage;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#MessagingResultINFDIV').html(html)
              }
          })
});
thisUpdateAttendeeButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrEmail = document.getElementById('strEmail').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID + '&vstrNames=' + vstrNames +
                '&vstrSurname=' + vstrSurname + '&vstrCell=' + vstrCell + '&vstrEmail=' + vstrEmail;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateAttendeeINFDIV').html(html)
              }
          })
});
thisRemoveAttendeeButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var vstrCell = document.getElementById('strRemoveCell').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID + '&vstrCell=' + vstrCell;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#RemoveAttendeeINFDIV').html(html)
              }
          })
});