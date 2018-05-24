
var thisPublicEventCalendarButt = document.getElementById("PublicEventCalendarButt");
var thisManageEventButt = document.getElementById("ManageEventButt");
var thisMyEventsButt = document.getElementById("getAnonymousElementByAttribute()");

thisPublicEventCalendarButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var dataString = '&vstrChoice='+ vstrChoice;
          $.ajax({
                type: "post",
                url: "/events",
                data: dataString,
                cache: false,
              success: function(html){
                $('#EventINFDIV').html(html)
              }
          })
});
thisManageEventButt.addEventListener("click", function () {
        var vstrChoice =0;
        var dataString = '&vstrChoice='+ vstrChoice;
          $.ajax({
                type: "get",
                url: "/events/manager",
                data: dataString,
                cache: false,
              success: function(html){
                $('#EventINFDIV').html(html)
              }
          })
});
thisMyEventsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var dataString = '&vstrChoice='+ vstrChoice;
          $.ajax({
                type: "post",
                url: "/events/manager",
                data: dataString,
                cache: false,
              success: function(html){
                $('#EventINFDIV').html(html)
              }
          })
});