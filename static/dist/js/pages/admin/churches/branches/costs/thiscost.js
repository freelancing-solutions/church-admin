var thisCostsUpdateButt = document.getElementById("CostsUpdateButt");
thisCostsUpdateButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrOfficeRentals = document.getElementById('strOfficeRentals').value;
        var vstrBuildingMaintenance = document.getElementById('strBuildingMaintenance').value;
        var vstrMunicipalCharges = document.getElementById('strMunicipalCharges').value;
        var vstrSalaries = document.getElementById('strSalaries').value;
        var vstrTelephone = document.getElementById('strTelephone').value;
        var vstrTransport = document.getElementById('strTransport').value;
        var vstrStationery = document.getElementById('strStationery').value;
        var vstrElectricity = document.getElementById('strElectricity').value;
        var vstrAdvertising =document.getElementById('strAdvertising').value;
        var vstrInsurance = document.getElementById('strInsurance').value;
        var vstrOverHeads =document.getElementById('strOverHeads').value;
        var vstrYear = document.getElementById('strYear').value;
        var vstrMonth = document.getElementById('strMonth').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchID=' + vstrChurchID + '&vstrChurchBranchID=' + vstrChurchBranchID +
            '&vstrOfficeRentals=' + vstrOfficeRentals + '&vstrBuildingMaintenance=' + vstrBuildingMaintenance + '&vstrMunicipalCharges=' + vstrMunicipalCharges +
            '&vstrSalaries=' + vstrSalaries + '&vstrTelephone=' + vstrTelephone + '&vstrTransport=' + vstrTransport  + '&vstrStationery=' +
            '&vstrElectricity=' + vstrElectricity + '&vstrAdvertising=' + vstrAdvertising + '&vstrInsurance=' + vstrInsurance +
            '&vstrOverHeads=' + vstrOverHeads + '&vstrYear=' + vstrYear + '&vstrMonth=' + vstrMonth;
          $.ajax({
                type: "get",
                url: "/monetary/costs",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddCostsStatusINFDIV').html(html)
              }
          });

});