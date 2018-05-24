
var thisAddAccountNumberButt = document.getElementById("AddAccountNumberButt");
var thisAddPaymentButt = document.getElementById("AddPaymentButt");
var thisUploadBeneficiaryButt = document.getElementById("UploadBeneficiaryButt");

thisAddAccountNumberButt.addEventListener("click", function () {
        var vstrChoice = 13;

        var vstrAccountHolder = document.getElementById('strAccountHolder').value;
        var vstrAccountNumber = document.getElementById('strAccountNumber').value;
        var vstrAccountType = document.getElementById('strAccountType').value;
        var vstrBankName = document.getElementById('strBankName').value;
        var vstrBranchName = document.getElementById('strBranchName').value;
        var vstrBranchCode = document.getElementById('strBranchCode').value;
        var vstrRoutingNumber = document.getElementById('strRoutingNumber').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/branches/" + vstrChurchBranchID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrAccountHolder=' + vstrAccountHolder + '&vstrAccountNumber=' + vstrAccountNumber +
                '&vstrAccountType=' + vstrAccountType + '&vstrBankName=' + vstrBankName + '&vstrBranchName=' + vstrBranchName +
                '&vstrBranchCode=' + vstrBranchCode + '&vstrRoutingNumber=' + vstrRoutingNumber + '&vstrChurchBranchID=' + vstrChurchBranchID +
                '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddAccountINFDIV').html(html)
              }
          });

});
thisAddPaymentButt.addEventListener("click", function () {
        var vstrChoice = 14;
        var vstrPaymentType = document.getElementById('strPaymentType').value;
        var vstrPaymentAmount = document.getElementById('strPaymentAmount').value;
        var vstrReasonForPayment = document.getElementById('strReasonForPayment').value;
        var vstrPaidToClient = document.getElementById('strPaidToClient').value;
        var vstrPayFrom = document.getElementById('strPayFrom').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;

        var thisURL = "/admin/branches/" + vstrChurchBranchID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID +
                '&vstrPaymentType=' + vstrPaymentType + '&vstrPaymentAmount=' + vstrPaymentAmount + '&vstrReasonForPayment=' + vstrReasonForPayment +
            '&vstrPayFrom=' + vstrPayFrom + '&vstrPaidToClient=' + vstrPaidToClient;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddPaymentINFDIV').html(html)
              }
          });
});
thisUploadBeneficiaryButt.addEventListener("click", function () {
        var vstrChoice = 15;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var vstrCompanyName = document.getElementById('strCompanyName').value;
        var vstrCompanyReg = document.getElementById('strCompanyReg').value;
        var vstrCompanyVAT = document.getElementById('strCompanyVAT').value;
        var vstrRecipientType = document.getElementById('strRecipientType').value;
        var vstrNotes = document.getElementById('strNotes').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;

        var thisURL = "/admin/branches/" + vstrChurchBranchID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname + '&vstrIDNumber=' + vstrIDNumber +
                '&vstrCompanyName=' + vstrCompanyName + '&vstrCompanyReg=' + vstrCompanyReg + '&vstrCompanyVAT=' + vstrCompanyVAT +
                '&vstrRecipientType=' + vstrRecipientType + '&vstrNotes=' + vstrNotes + '&vstrChurchBranchID=' + vstrChurchBranchID +
                '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadBeneficiaryINFDIV').html(html)
              }
          });
});