var thisAddServiceButt = document.getElementById("AddServiceButt");

thisAddServiceButt.addEventListener("click", function () {
        var vstrChoice = 13;
        var vstrSupplierID = document.getElementById('strSupplierID').value;

        var vstrServiceName = document.getElementById('strServiceName').value;
        var vstrDescription = document.getElementById('strDescription').value;
        var vstrServiceCost = document.getElementById('strServiceCost').value;
        var vstrDepositAmount = document.getElementById('strDepositAmount').value;

        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID +
                '&vstrServiceName=' + vstrServiceName + '&vstrDescription=' + vstrDescription +
                '&vstrServiceCost=' + vstrServiceCost + '&vstrDepositAmount=' + vstrDepositAmount;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddServiceINFDIV').html(html)
              }
          })
});