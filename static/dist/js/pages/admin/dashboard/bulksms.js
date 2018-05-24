    function UpdateAccount(clicked_id) {
        var vstrChoice = 1;
        var strSMSValueID = "text" + clicked_id;
        var vstrAdditionalCredit = document.getElementById(strSMSValueID).value;
        var vstrChurchID = clicked_id;
        var vstrResponseDIV = 'Response'+ clicked_id;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrChurchID=' + vstrChurchID + '&vstrAdditionalCredit=' + vstrAdditionalCredit;
        alert("Please verify we are about to add :" +  vstrAdditionalCredit + " Credits to this Account");
          $.ajax({
                type: "post",
                url: "/dashboard/bulksms",
                data: dataString,
                cache: false,
              success: function(html){
                document.getElementById(vstrResponseDIV).innerHTML = html;
              }
          });
    }
var thisAddSystemCreditsButt = document.getElementById("AddSystemCreditsButt");
var thisAddBudgetSystemCreditsButt = document.getElementById("AddBudgetSystemCreditsButt");
var thisUpdateVodacomPortalButt = document.getElementById("UpdateVodacomPortalButt");
thisAddSystemCreditsButt.addEventListener("click", function () {
        var vstrAdditionalCredit = document.getElementById('strAdditionalCredit').value;
        var vstrTempValue = document.getElementById('strSystemCredit').value;
        document.getElementById('strSystemCredit').removeAttribute('readonly');
        document.getElementById('strSystemCredit').value = parseInt(vstrTempValue) + parseInt(vstrAdditionalCredit);
        document.getElementById('strSystemCredit').readOnly =true;
      });
thisAddBudgetSystemCreditsButt.addEventListener("click", function () {
        var vstrAdditionalCredit = document.getElementById('strBudgetAdditionalCredit').value;
        var vstrTempValue = document.getElementById('strBudgetSystemCredit').value;
        document.getElementById('strBudgetSystemCredit').removeAttribute('readonly');
        document.getElementById('strBudgetSystemCredit').value = parseInt(vstrTempValue) + parseInt(vstrAdditionalCredit);
        document.getElementById('strBudgetSystemCredit').readOnly =true;
});
thisUpdateVodacomPortalButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrSenderAddress = document.getElementById('strSenderAddress').value;
        var vstrEmailAddress = document.getElementById('strEmailAddress').value;
        var vstrCSVEmail = document.getElementById('strCSVEmail').value;
        var vstrSMSSizeLimit = document.getElementById('strSMSSizeLimit').value;
        var vstrBuyRate = document.getElementById('strBuyRate').value;
        var vstrSellRate = document.getElementById('strSellRate').value;
        var vstrAvailableCredit = document.getElementById('strAvailableCredit').value;
        var vstrSystemCredit = document.getElementById('strSystemCredit').value;
        var vstrPortalLogin = document.getElementById('strPortalLogin').value;
        var vstrPortalPassword = document.getElementById('strPortalPassword').value;
        var vstrPortalAddress = document.getElementById('strPortalAddress').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSenderAddress=' + vstrSenderAddress + '&vstrEmailAddress=' + vstrEmailAddress +
                '&vstrCSVEmail=' + vstrCSVEmail + '&vstrSMSSizeLimit=' + vstrSMSSizeLimit + '&vstrBuyRate=' + vstrBuyRate +
                '&vstrSellRate=' + vstrSellRate + '&vstrAvailableCredit=' + vstrAvailableCredit + '&vstrPortalLogin=' + vstrPortalLogin +
                '&vstrPortalPassword=' + vstrPortalPassword + '&vstrPortalAddress=' + vstrPortalAddress + '&vstrSystemCredit=' + vstrSystemCredit;
          $.ajax({
                type: "post",
                url: "/dashboard/bulksms",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateVodacomPortalINFDIV').html(html)
              }
          })
});