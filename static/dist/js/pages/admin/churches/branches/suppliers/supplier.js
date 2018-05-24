var thisAddSuppliersButt = document.getElementById("AddSuppliersButt");

thisAddSuppliersButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrCompanyName = document.getElementById('strCompanyName').value;
        var vstrCompanyReg = document.getElementById('strCompanyReg').value;
        var vstrVAT = document.getElementById('strVAT').value;
        var vstrCPNames = document.getElementById('strCPNames').value;
        var vstrCPSurname = document.getElementById('strCPSurname').value;
        var vstrCPIDNumber = document.getElementById('strCPIDNumber').value;
        var vstrCPPosition = document.getElementById('strCPPosition').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrCompanyName=' + vstrCompanyName + '&vstrCompanyReg=' + vstrCompanyReg +
                '&vstrVAT=' + vstrVAT + '&vstrCPNames=' + vstrCPNames + '&vstrCPSurname=' + vstrCPSurname + '&vstrCPIDNumber=' + vstrCPIDNumber +
                '&vstrCPPosition=' + vstrCPPosition + '&vstrChurchID=' + vstrChurchID + '&vstrChurchBranchID=' + vstrChurchBranchID;
          $.ajax({
                type: "post",
                url: "/admin/supplier",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddSupplierINFDIV').html(html)
              }
          })
});