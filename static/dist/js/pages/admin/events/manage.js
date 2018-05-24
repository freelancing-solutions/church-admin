
var thisRegisteredManagerButt = document.getElementById("RegisteredManagerButt");
var thisEventSpeakersButt = document.getElementById("EventSpeakersButt");
var thisEventSponsorsButt = document.getElementById("EventSponsorsButt");
var thisEventExhibitorsButt = document.getElementById("EventExhibitorsButt");
var thisEventAgendasButt = document.getElementById("EventAgendasButt");

thisRegisteredManagerButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrEventID = document.getElementById('strEventID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrEventID=' + vstrEventID;
          $.ajax({
                type: "post",
                url: "/events/manager/" + vstrEventID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#EventManagerINFDIV').html(html)
              }
          })
});
thisEventSpeakersButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrEventID = document.getElementById('strEventID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrEventID=' + vstrEventID;
          $.ajax({
                type: "post",
                url: "/events/manager/" + vstrEventID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#EventManagerINFDIV').html(html)
              }
          })
});
thisEventSponsorsButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrEventID = document.getElementById('strEventID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrEventID=' + vstrEventID;
          $.ajax({
                type: "post",
                url: "/events/manager/" + vstrEventID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#EventManagerINFDIV').html(html)
              }
          })
});
thisEventExhibitorsButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrEventID = document.getElementById('strEventID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrEventID=' + vstrEventID;
          $.ajax({
                type: "post",
                url: "/events/manager/" + vstrEventID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#EventManagerINFDIV').html(html)
              }
          })
});
thisEventAgendasButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrEventID = document.getElementById('strEventID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrEventID=' + vstrEventID;
          $.ajax({
                type: "post",
                url: "/events/manager/" + vstrEventID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#EventManagerINFDIV').html(html)
              }
          })
});
