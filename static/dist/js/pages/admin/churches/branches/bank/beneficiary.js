var thisUpdateBeneficiaryButt = document.getElementById("UpdateBeneficiaryButt");
var thisUpdateBenBankButt = document.getElementById("UpdateBenBankButt");

thisUpdateBeneficiaryButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var vstrCompanyName = document.getElementById('strCompanyName').value;
        var vstrCompanyReg = document.getElementById('strCompanyReg').value;
        var vstrCompanyVAT = document.getElementById('strCompanyVAT').value;
        var vstrBeneficiaryIndex = document.getElementById('strBeneficiaryIndex').value;
        var vstrNotes = document.getElementById('strNotes').value;
        var thisURL = "/monetary/beneficiaries/"+ vstrBeneficiaryIndex;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
                '&vstrIDNumber=' + vstrIDNumber + '&vstrCompanyName=' + vstrCompanyName + '&vstrCompanyReg=' + vstrCompanyReg +
                '&vstrCompanyVAT=' + vstrCompanyVAT  + '&vstrBeneficiaryIndex=' + vstrBeneficiaryIndex + '&vstrNotes=' + vstrNotes;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateBeneficiaryINFDIV').html(html)
              }
          })
});

thisUpdateBenBankButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrAccountHolder = document.getElementById('strAccountHolder').value;
        var vstrAccountNumber = document.getElementById('strAccountNumber').value;
        var vstrAccountType = document.getElementById('strAccountType').value;
        var vstrBankName = document.getElementById('strBankName').value;
        var vstrBranchName = document.getElementById('strBranchName').value;
        var vstrBranchCode = document.getElementById('strBranchCode').value;
        var vstrRoutingNumber = document.getElementById('strRoutingNumber').value;
        var vstrBeneficiaryIndex = document.getElementById('strBeneficiaryIndex').value;
        var thisURL = "/monetary/beneficiaries/"+ vstrBeneficiaryIndex;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrAccountHolder=' + vstrAccountHolder + '&vstrAccountNumber=' + vstrAccountNumber +
                '&vstrAccountType=' + vstrAccountType + '&vstrBankName=' + vstrBankName + '&vstrBranchName=' + vstrBranchName + '&vstrBranchCode=' + vstrBranchCode +
                '&vstrRoutingNumber=' + vstrRoutingNumber;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateBenBankINFDIV').html(html)
              }
          })
});