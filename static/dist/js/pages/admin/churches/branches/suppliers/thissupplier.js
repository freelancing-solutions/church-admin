
var thisClientDetailsButt = document.getElementById("ClientDetailsButt");
var thisPhysicalAddressButt = document.getElementById("PhysicalAddressButt");
var thisPostalAddressButt = document.getElementById("PostalAddressButt");
var thisContactButt = document.getElementById("ContactButt");
var thisBankDetailsButt = document.getElementById("BankDetailsButt");
var thisListProductsButt = document.getElementById("ListProductsButt");
var thisListServicesButt = document.getElementById("ListServicesButt");
var thisSendMessagesButt = document.getElementById("SendMessagesButt");

thisClientDetailsButt,addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrSupplierID = document.getElementById('strSupplierID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/suppliers/" +  vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SupplierINFDIV').html(html)
              }
          })
});
thisPhysicalAddressButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrSupplierID = document.getElementById('strSupplierID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SupplierINFDIV').html(html)
              }
          })
});
thisPostalAddressButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrSupplierID = document.getElementById('strSupplierID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
    
        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SupplierINFDIV').html(html)
              }
          })
});
thisContactButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrSupplierID = document.getElementById('strSupplierID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SupplierINFDIV').html(html)
              }
          })
});
thisBankDetailsButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrSupplierID = document.getElementById('strSupplierID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SupplierINFDIV').html(html)
              }
          })
});
thisListProductsButt.addEventListener("click", function () {
        var vstrChoice = 10;
        var vstrSupplierID = document.getElementById('strSupplierID').value;


        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID ;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SupplierINFDIV').html(html)
              }
          })
});
thisListServicesButt.addEventListener("click", function () {
        var vstrChoice = 12;
        var vstrSupplierID = document.getElementById('strSupplierID').value;

        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID ;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SupplierINFDIV').html(html)
              }
          })
});
thisSendMessagesButt.addEventListener("click", function () {
            var vstrChoice = 11;
        var vstrSupplierID = document.getElementById('strSupplierID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#SupplierINFDIV').html(html)
              }
          })
});