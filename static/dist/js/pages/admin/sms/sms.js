var thisGroupsButt = document.getElementById("GroupsButt");
var thisAccountButt = document.getElementById("AccountButt");
var thisReportsButt = document.getElementById("ReportsButt");
thisGroupsButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/admin/sms/groups",
                data: dataString,
                cache: false,
              success: function(html){
                $('#MySMSINFDIV').html(html)
              }
          })
});
thisAccountButt.addEventListener("click", function () {
        var vstrChoice =4;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/admin/sms/groups",
                data: dataString,
                cache: false,
              success: function(html){
                $('#MySMSINFDIV').html(html)
              }
          })
});
thisReportsButt.addEventListener("click", function () {
        var vstrChoice =5;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/admin/sms/groups",
                data: dataString,
                cache: false,
              success: function(html){
                $('#MySMSINFDIV').html(html)
              }
          })
});
