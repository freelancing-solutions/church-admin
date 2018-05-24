var thisAuthorizePaymentButt = document.getElementById("AuthorizePaymentButt");
var thisRejectPaymentButt = document.getElementById("RejectPaymentButt");

thisAuthorizePaymentButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrPaymentType = document.getElementById('strPaymentType').value;
        var vstrPaymentAmount = document.getElementById('strPaymentAmount').value;
        var vstrReasonForPayment = document.getElementById('strReasonForPayment').value;
        var vstrPaidToClient = document.getElementById('strPaidToClient').value;
        var vstrPayFrom = document.getElementById('strPayFrom').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var vstrAuthorizedBy = document.getElementById('strAuthorizedBy').value;
        var vstrPaymentIndex = document.getElementById('strPaymentIndex').value;
        var vstrManagementNotes  = document.getElementById('strManagementNotes').value;

        var thisURL = "/monetary/payments/authorize/" + vstrPaymentIndex;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID +
                '&vstrPaymentType=' + vstrPaymentType + '&vstrPaymentAmount=' + vstrPaymentAmount + '&vstrReasonForPayment=' + vstrReasonForPayment +
            '&vstrPayFrom=' + vstrPayFrom + '&vstrPaidToClient=' + vstrPaidToClient + '&vstrAuthorizedBy=' + vstrAuthorizedBy + '&vstrPaymentIndex=' + vstrPaymentIndex;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#PaymentINFDIV').html(html)
              }
          })
});

thisRejectPaymentButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrPaymentType = document.getElementById('strPaymentType').value;
        var vstrPaymentAmount = document.getElementById('strPaymentAmount').value;
        var vstrReasonForPayment = document.getElementById('strReasonForPayment').value;
        var vstrPaidToClient = document.getElementById('strPaidToClient').value;
        var vstrPayFrom = document.getElementById('strPayFrom').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var vstrAuthorizedBy = document.getElementById('strAuthorizedBy').value;
        var vstrPaymentIndex = document.getElementById('strPaymentIndex').value;

        var thisURL = "/monetary/payments/authorize/" + vstrPaymentIndex;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID +
                '&vstrPaymentType=' + vstrPaymentType + '&vstrPaymentAmount=' + vstrPaymentAmount + '&vstrReasonForPayment=' + vstrReasonForPayment +
            '&vstrPayFrom=' + vstrPayFrom + '&vstrPaidToClient=' + vstrPaidToClient + '&vstrAuthorizedBy=' + vstrAuthorizedBy + '&vstrPaymentIndex=' + vstrPaymentIndex;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#PaymentINFDIV').html(html)
              }
          });

});
