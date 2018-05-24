
var thisUpdateBankDetailsButt = document.getElementById("UpdateBankDetailsButt");

thisUpdateBankDetailsButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrAccountOwner = document.getElementById('strAccountOwner').value;
        var vstrAccountNumber = document.getElementById('strAccountNumber').value;
        var vstrBankName = document.getElementById('strBankName').value;
        var vstrBranchName =document.getElementById('strBranchName').value;
        var vstrBranchCode = document.getElementById('strBranchCode').value;
        var vstrAccountType = document.getElementById('strAccountType').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;


        var thisURL = "/employees/" + vstrIDNumber;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrBranchName=' + vstrBranchName + '&vstrAccountOwner=' + vstrAccountOwner +
            '&vstrAccountNumber=' + vstrAccountNumber + '&vstrBankName=' +vstrBankName + '&vstrBranchCode=' + vstrBranchCode +
                '&vstrAccountType=' + vstrAccountType + '&vstrIDNumber=' +  vstrIDNumber;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateBankDetailsINFDIV').html(html)
              }
          })
});