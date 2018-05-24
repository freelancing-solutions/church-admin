var thisClientDetailsButt = document.getElementById("ClientDetailsButt");
var thisPhysicalAddressButt = document.getElementById("PhysicalAddressButt");
var thisPostalAddressButt = document.getElementById("PostalAddressButt");
var thisContactButt = document.getElementById("ContactButt");
var thisBankDetailsButt = document.getElementById("BankDetailsButt");
var thisListProductsButt = document.getElementById("ListProductsButt");
var thisListServicesButt = document.getElementById("ListServicesButt");
var thisMessagingButt = document.getElementById("MessagingButt");

thisClientDetailsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ClientINFDIV').html(html)
              }
          })
    });
thisPhysicalAddressButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;

        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ClientINFDIV').html(html)
              }
          })
});
thisPostalAddressButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ClientINFDIV').html(html)
              }
          })
});
thisContactButt.addEventListener("click", function () {
        var vstrChoice = 5;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ClientINFDIV').html(html)
              }
          })
});
thisBankDetailsButt.addEventListener("click", function () {
        var vstrChoice = 7;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ClientINFDIV').html(html)
              }
          })
});
thisListProductsButt.addEventListener("click", function () {
        var vstrChoice = 9;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ClientINFDIV').html(html)
              }
          })
});
thisListServicesButt.addEventListener("click", function () {
        var vstrChoice = 11;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ClientINFDIV').html(html)
              }
          })
});
thisMessagingButt.addEventListener("click", function () {
        var vstrChoice = 13;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;

        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ClientINFDIV').html(html)
              }
          })
});