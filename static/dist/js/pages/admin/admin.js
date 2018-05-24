var thisChurchDetailsButt = document.getElementById("ChurchDetailsButt");
var thisChurchBranchButt = document.getElementById("ChurchBranchButt");
var thisChurchSermonsButt = document.getElementById("ChurchSermonsButt");
var thisMeetingsButt = document.getElementById("MeetingsButt");
var thisTestimonyButt = document.getElementById("TestimonyButt");
var thisContactsButt = document.getElementById("ContactsButt");
var thisSendReceiveSMSButt = document.getElementById("SendReceiveSMSButt");
var thisNewsLetterButt = document.getElementById("NewsLetterButt");
var thisBirthdaysEventsButt = document.getElementById("BirthdaysEventsButt");
thisChurchDetailsButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/admin/churchdetails",
                data: dataString,
                cache: false,
              success: function(html){
                $('#ChurchAdminINFDIV').html(html)
              }
          })
});
thisChurchBranchButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/admin/branches",
                data: dataString,
                cache: false,
              success: function(html){
                $('#ChurchAdminINFDIV').html(html)
              }
          })
});
thisChurchSermonsButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/admin/sermons",
                data: dataString,
                cache: false,
              success: function(html){
                $('#ChurchAdminINFDIV').html(html)
              }
          })
});
thisMeetingsButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/admin/meetings",
                data: dataString,
                cache: false,
              success: function(html){
                $('#ChurchAdminINFDIV').html(html)
              }
          })
});
thisTestimonyButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/admin/testimony",
                data: dataString,
                cache: false,
              success: function(html){
                $('#ChurchAdminINFDIV').html(html)
              }
          })
});
thisContactsButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/admin/contacts",
                data: dataString,
                cache: false,
              success: function(html){
                $('#ChurchAdminINFDIV').html(html)
              }
          })
});
thisSendReceiveSMSButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/admin/mysms",
                data: dataString,
                cache: false,
              success: function(html){
                $('#ChurchAdminINFDIV').html(html)
              }
          })
});
thisNewsLetterButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/admin/newsletters",
                data: dataString,
                cache: false,
              success: function(html){
                $('#ChurchAdminINFDIV').html(html)
              }
          })
});
thisBirthdaysEventsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "post",
                url: "/events",
                data: dataString,
                cache: false,
              success: function(html){
                $('#ChurchAdminINFDIV').html(html)
              }
          })
});