

var thisUpdateAssetButt = document.getElementById("UpdateAssetButt");
var thisUpdateAssetLocationButt = document.getElementById("UpdateAssetLocationButt");

thisUpdateAssetButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrAssetCode = document.getElementById('strAssetCode').value;
        var vstrAssetID = document.getElementById('strAssetID').value;
        var vstrAssetName = document.getElementById('strAssetName').value;
        var vstrAssetDescription = document.getElementById('strAssetDescription').value;
        var vstrPurchasePrice = document.getElementById('strPurchasePrice').value;
        var vstrDepreciation = document.getElementById('strDepreciation').value;
        var vstrCurrentValue = document.getElementById('strCurrentValue').value;
        var vstrAssetType = document.getElementById('strAssetType').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrAssetCode=' + vstrAssetCode + '&vstrAssetName=' + vstrAssetName  +
            '&vstrAssetDescription=' + vstrAssetDescription + '&vstrPurchasePrice=' + vstrPurchasePrice + '&vstrDepreciation=' + vstrDepreciation +
            '&vstrCurrentValue=' + vstrCurrentValue + '&vstrAssetType=' + vstrAssetType + '&vstrAssetID=' + vstrAssetID;
          $.ajax({
                type: "get",
                url: "/assets",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateAssetINFDIV').html(html)
              }
          })
});
thisUpdateAssetLocationButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrAssetID = document.getElementById('strAssetID').value;
        var vstrBuildingName = document.getElementById('strBuildingName').value;
        var vstrOfficeNumber = document.getElementById('strOfficeNumber').value;
        var vstrStandNumber = document.getElementById('strStandNumber').value;
        var vstrStreetName = document.getElementById('strStreetName').value;
        var vstrCityTown = document.getElementById('strCityTown').value;
        var vstrProvince = document.getElementById('strProvince').value;
        var vstrCountry = document.getElementById('strCountry').value;
        var vstrPostalCode = document.getElementById('strPostalCode').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrBuildingName=' + vstrBuildingName + '&vstrOfficeNumber=' + vstrOfficeNumber +
            '&vstrStandNumber=' + vstrStandNumber + '&vstrStreetName=' + vstrStreetName + '&vstrCityTown='+ vstrCityTown + '&vstrProvince=' + vstrProvince +
            '&vstrCountry=' + vstrCountry + '&=vstrPostalCode=' + vstrPostalCode + '&vstrAssetID=' + vstrAssetID;
          $.ajax({
                type: "get",
                url: "/assets",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AssetLocationINFDIV').html(html)
              }
          })
});