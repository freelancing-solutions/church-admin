var thisCreateChurchAccountButt = document.getElementById("CreateChurchAccountButt");
var thisUpdateChurchAccountButt = document.getElementById("UpdateChurchAccountButt");
var thisProfileInfoButt = document.getElementById("ProfileInfoButt");
var thisProductsInfoButt = document.getElementById("ProductsInfoButt");
var thisPaymentSettingsInfoButt = document.getElementById("PaymentSettingsInfoButt");

thisCreateChurchAccountButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrEmail = document.getElementById('strEmail').value;
        var vstrSelectProduct = document.getElementById('strSelectProduct').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSelectProduct=' + vstrSelectProduct + '&vstrNames=' + vstrNames +
            '&vstrSurname=' + vstrSurname + '&vstrIDNumber=' + vstrIDNumber + '&vstrCell=' + vstrCell + '&vstrEmail=' + vstrEmail +
            '';
          $.ajax({
                type: "post",
                url: "/accounts",
                data: dataString,
                cache: false,
              success: function(html){
                $('#CreateChurchINFDIV').html(html)
              }
          })
});
thisUpdateChurchAccountButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrEmail = document.getElementById('strEmail').value;
        var vstrSelectProduct = document.getElementById('strSelectProduct').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSelectProduct=' + vstrSelectProduct + '&vstrNames=' + vstrNames +
            '&vstrSurname=' + vstrSurname + '&vstrIDNumber=' + vstrIDNumber + '&vstrCell=' + vstrCell + '&vstrEmail=' + vstrEmail +
            '';
          $.ajax({
                type: "post",
                url: "/accounts/update",
                data: dataString,
                cache: false,
              success: function(html){
                $('#CreateChurchINFDIV').html(html)
              }
          });
});
thisProfileInfoButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/accounts/proinfo",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AccountInfDiv').html(html)
              }
          })
});
thisProductsInfoButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/accounts/products",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AccountInfDiv').html(html)
              }
          })
});
thisPaymentSettingsInfoButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var dataString = '&vstrChoice='+ vstrChoice ;
          $.ajax({
                type: "get",
                url: "/accounts/payments",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AccountInfDiv').html(html)
              }
          });
});



