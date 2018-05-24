    function CreateQuote(clicked_id) {
        var vstrSMSAmount = parseInt(document.getElementById(clicked_id).value);
        var vstrBudgetSystemCredit = parseInt(document.getElementById('strBudgetSystemCredit').value);
        var vstrVodacomSystemCredit = parseInt(document.getElementById('strVodacomSystemCredit').value);
        var vstrBudgetSellPrice = parseInt(document.getElementById('strBudgetSellPrice').value);
        var vstrVodacomSellPrice = parseInt(document.getElementById('strVodacomSellPrice').value);
        if (vstrSMSAmount <= vstrBudgetSystemCredit){
            document.getElementById('strDepositAmount').value = ((vstrBudgetSellPrice)/100) * vstrSMSAmount;

        }else{
            document.getElementById('strDepositAmount').value = ((vstrVodacomSellPrice)/100) * vstrSMSAmount;
        }
    }

var thisCreditAccountButt = document.getElementById("CreditAccountButt");
thisCreditAccountButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrCellNumber = document.getElementById('strCellNumber').value;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var thisURL = "/sms/groupman/" + vstrGroupID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
                '&vstrCellNumber=' + vstrCellNumber + '&vstrGroupID=' + vstrGroupID;
          $.ajax({
                type: "post",
                url:thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#AccountINFDIV').html(html)
              }
          })
});
