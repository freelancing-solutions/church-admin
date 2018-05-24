var thisAddProductButt = document.getElementById("AddProductButt");

thisAddProductButt.addEventListener("click", function () {
        var vstrChoice = 11;
        var vstrSupplierID = document.getElementById('strSupplierID').value;

        var vstrProductName = document.getElementById('strProductName').value;
        var vstrDescription = document.getElementById('strDescription').value;
        var vstrProductCost = document.getElementById('strProductCost').value;
        var vstrDepositAmount = document.getElementById('strDepositAmount').value;

        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID +
                '&vstrProductName=' + vstrProductName + '&vstrDescription=' + vstrDescription +
                '&vstrProductCost=' + vstrProductCost + '&vstrDepositAmount=' + vstrDepositAmount;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddProductINFDIV').html(html)
              }
          })
});