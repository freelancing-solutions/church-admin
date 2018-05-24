
var thisBranchEmployeesButt = document.getElementById("BranchEmployeesButt");
var thisAssetsButt = document.getElementById("AssetsButt");
var thisCostsButt = document.getElementById("CostsButt");
var thisBranchDetailsButt = document.getElementById("BranchDetailsButt");
var thisBranchContactDetailsButt = document.getElementById("BranchContactDetailsButt");
var thisBankButt = document.getElementById("BankButt");
var thisClientsButt = document.getElementById("ClientsButt");
var thisSuppliersButt = document.getElementById("SuppliersButt");
var thisIncomeButt = document.getElementById("IncomeButt");
var thisDonatorsButt = document.getElementById("DonatorsButt");
var thisAddCongregantsButt = document.getElementById("AddCongregantsButt");
var thisStatementsButt = document.getElementById("StatementsButt");

thisBranchEmployeesButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/admin/branches/" + vstrChurchBranchID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchDetailsINFDIV').html(html)
              }
          })
    });
thisAssetsButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/admin/branches/" + vstrChurchBranchID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchDetailsINFDIV').html(html)
              }
          });
});
thisCostsButt.addEventListener("click", function () {
        var vstrChoice = 5;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/admin/branches/" + vstrChurchBranchID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchDetailsINFDIV').html(html)
              }
          })
});
thisBranchDetailsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/admin/branches/" + vstrChurchBranchID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchDetailsINFDIV').html(html)
              }
          })
});
thisBranchContactDetailsButt.addEventListener("click", function () {
        var vstrChoice = 10;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/admin/branches/" + vstrChurchBranchID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchDetailsINFDIV').html(html)
              }
          })
});
thisBankButt.addEventListener("click", function () {
        var vstrChoice = 12;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/admin/branches/" + vstrChurchBranchID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchDetailsINFDIV').html(html)
              }
          })
});
thisClientsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/admin/clients";
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "get",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchDetailsINFDIV').html(html)
              }
          })
});
thisSuppliersButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/admin/supplier";
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "get",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchDetailsINFDIV').html(html)
              }
          })
});
thisIncomeButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/monetary/income";
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "get",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchDetailsINFDIV').html(html)
              }
          })
});
thisDonatorsButt.addEventListener("click", function () {
       var vstrChoice = 0;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/monetary/donators";
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "get",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchDetailsINFDIV').html(html)
              }
          })
});
thisAddCongregantsButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/admin/congregants",
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchDetailsINFDIV').html(html)
              }
          })
});
thisStatementsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/monetary/statements",
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchDetailsINFDIV').html(html)
              }
          })
});