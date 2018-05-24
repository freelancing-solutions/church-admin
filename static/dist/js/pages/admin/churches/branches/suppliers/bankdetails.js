var thisUpdateBankButt = document.getElementById("UpdateBankButt");
thisUpdateBankButt.addEventListener("click", function () {
        var vstrChoice = 8;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrAccountHolder = document.getElementById('strAccountHolder').value;
        var vstrAccountNumber = document.getElementById('strAccountNumber').value;
        var vstrAccountType = document.getElementById('strAccountType').value;
        var vstrBankName = document.getElementById('strBankName').value;
        var vstrBranchCode = document.getElementById('strBranchCode').value;
        var vstrRoutingNumber = document.getElementById('strRoutingNumber').value;
        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID + '&vstrAccountHolder=' + vstrAccountHolder +
                '&vstrAccountNumber=' + vstrAccountNumber + '&vstrAccountType=' + vstrAccountType + '&vstrBankName=' + vstrBankName +
                '&vstrBranchCode=' + vstrBranchCode + '&vstrRoutingNumber=' + vstrRoutingNumber;
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