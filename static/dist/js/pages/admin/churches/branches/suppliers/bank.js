

var thisUpdateBankButt = document.getElementById("UpdateBankButt");

thisUpdateBankButt.addEventListener("click", function () {
        var vstrChoice = 5;
        var vstrSupplierID = document.getElementById('strSupplierID').value;
        var vstrAccountHolder = document.getElementById('strAccountHolder').value;
        var vstrAccountNumber = document.getElementById('strAccountNumber').value;
        var vstrAccountType = document.getElementById('strAccountType').value;
        var vstrBankName = document.getElementById('strBankName').value;
        var vstrBranchCode = document.getElementById('strBranchCode').value;

        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID + '&vstrAccountHolder=' + vstrAccountHolder +
                '&vstrAccountNumber=' + vstrAccountNumber + '&vstrAccountType=' + vstrAccountType + '&vstrBankName=' + vstrBankName +
                '&vstrBranchCode=' + vstrBranchCode ;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateBankINFDIV').html(html)
              }
          })
});