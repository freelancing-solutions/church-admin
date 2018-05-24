

var thisCreateAssetCodeButt = document.getElementById("CreateAssetCodeButt");
var thisAddAssetButt = document.getElementById("AddAssetButt");

thisCreateAssetCodeButt.addEventListener("click", function () {
          var vstrChoice = 1;
        var vstrBranchName = document.getElementById('strBranchName').value;
        var vstrBranchMotto = document.getElementById('strBranchMotto').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrBranchName=' + vstrBranchName + '&vstrBranchMotto=' + vstrBranchMotto;
          $.ajax({
                type: "post",
                url: "/admin/branches",
                data: dataString,
                cache: false,
              success: function(html){
                $('#CreateAssetINFDIV').html(html)
              }
          })
});
thisAddAssetButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrAssetCode = document.getElementById('strAssetCode').value;
        var vstrAssetName = document.getElementById('strAssetName').value;
        var vstrAssetDescription = document.getElementById('strAssetDescription').value;
        var vstrPurchasePrice = document.getElementById('strPurchasePrice').value;
        var vstrDepreciation = document.getElementById('strDepreciation').value;
        var vstrCurrentValue = document.getElementById('strCurrentValue').value;
        var vstrAssetType = document.getElementById('strAssetType').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/branches/" + vstrChurchBranchID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrAssetCode=' + vstrAssetCode + '&vstrAssetName=' + vstrAssetName +
            '&vstrAssetDescription=' + vstrAssetDescription + '&vstrPurchasePrice=' + vstrPurchasePrice + '&vstrDepreciation=' + vstrDepreciation +
            '&vstrCurrentValue=' + vstrCurrentValue + '&vstrAssetType=' + vstrAssetType + '&vstrChurchBranchID=' + vstrChurchBranchID +
            '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddAssetINFDIV').html(html)
              }
          })
});