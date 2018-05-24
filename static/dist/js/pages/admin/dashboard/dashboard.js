

var thisAdminRequestsButt = document.getElementById("AdminRequestsButt");
var thisAdminsButt = document.getElementById("AdminsButt");
var thisPaymentsButt = document.getElementById("PaymentsButt");
var thisContactMessagesButt = document.getElementById("ContactMessagesButt");
var thisBulkSMSButt = document.getElementById("BulkSMSButt");

thisAdminRequestsButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/dashboard/adminrequests",
                data: dataString,
                cache: false,
              success: function(html){
                $('#dashboardINFDIV').html(html)
              }
          })
});
thisAdminsButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/dashboard/adminslist",
                data: dataString,
                cache: false,
              success: function(html){
                $('#dashboardINFDIV').html(html)
              }
          })
});
thisPaymentsButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/dashboard/payments",
                data: dataString,
                cache: false,
              success: function(html){
                $('#dashboardINFDIV').html(html)
              }
          })
});
thisContactMessagesButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/dashboard/contacts",
                data: dataString,
                cache: false,
              success: function(html){
                $('#dashboardINFDIV').html(html)
              }
          })
});
thisBulkSMSButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/dashboard/bulksms",
                data: dataString,
                cache: false,
              success: function(html){
                $('#dashboardINFDIV').html(html)
              }
          })
});