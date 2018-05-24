
function isEmpty(str) {return (!str || 0 === str.length);}
 function LoadAgendaItems(){
        var vstrChoice = 12;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                console.log(html);
                html = html.trim();
                var thisListItems = html.split("|");
                var arrayLength = thisListItems.length;
                select = document.getElementById('strSelectAgendaItem');
                for (var i = 0; i < arrayLength; i++){
                    var thisItem = thisListItems[i];
                    thisItem = thisItem.trim();
                    if (!isEmpty(thisItem)){
                    var thisItemsList = thisItem.split(",");
                    var strItemsID = thisItemsList[0];
                    var strItemName = thisItemsList[1];
                    var opt = document.createElement('option');

                    opt.value = strItemsID;
                    opt.innerHTML = strItemName;
                    select.appendChild(opt);
                    }
                }
              }
          });
    }
var thisUpdateMinutesButt = document.getElementById("UpdateMinutesButt");
var thisUploadMinutesButt = document.getElementById("UploadMinutesButt");
thisUpdateMinutesButt.addEventListener("click", function () {
        var vstrChoice = 11;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var vstrMinutesTitle = document.getElementById('strMinutesTitle').value;
        var vstrDateTaken = document.getElementById('strDateTaken').value;
        var vstrTimeTaken = document.getElementById('strTimeTaken').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID + '&vstrMinutesTitle=' + vstrMinutesTitle +
        '&vstrDateTaken=' + vstrDateTaken + '&vstrTimeTaken=' + vstrTimeTaken;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateMinutesINFDIV').html(html)
              }
          })
});
thisUploadMinutesButt.addEventListener("click", function () {
        var vstrChoice = 13;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var vstrMinutesID = document.getElementById('strMinutesID').value;
        var vstrSelectAgendaItem = document.getElementById('strSelectAgendaItem').value;
        var vstrAgenda = document.getElementById('strSelectAgendaItem').innerHTML;
        var vstrAddMinutesTitle = document.getElementById('strAddMinutesTitle').value;
        var vstrMinutes = document.getElementById('strMinutes').value;
        var vstrNotes = document.getElementById('strNotes').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID + '&vstrSelectAgendaItem=' + vstrSelectAgendaItem +
        '&vstrAddMinutesTitle=' + vstrAddMinutesTitle + '&vstrMinutes=' + vstrMinutes + '&vstrNotes=' + vstrNotes + '&vstrMinutesID=' + vstrMinutesID +
        '&vstrAgenda=' + vstrAgenda;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadMinutesINFDIV').html(html)
              }
          })
});