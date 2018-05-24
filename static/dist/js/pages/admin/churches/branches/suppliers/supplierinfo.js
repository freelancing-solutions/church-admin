

var thisUpdateSupplierButt = document.getElementById("UpdateSupplierButt");

thisUpdateSupplierButt.addEventListener("click", function () {
        var vstrChoice = 9;
        var vstrSupplierID = document.getElementById('strSupplierID').value;
        var vstrCompanyName = document.getElementById('strCompanyName').value;
        var vstrCompanyReg = document.getElementById('strCompanyReg').value;
        var vstrVAT = document.getElementById('strVAT').value;
        var vstrCPNames = document.getElementById('strCPNames').value;
        var vstrCPSurname = document.getElementById('strCPSurname').value;
        var vstrCPIDNumber = document.getElementById('strCPIDNumber').value;
        var vstrCPPosition = document.getElementById('strCPPosition').value;

        var thisURL = "/admin/suppliers/" + vstrSupplierID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSupplierID=' + vstrSupplierID +
                '&vstrCompanyName=' + vstrCompanyName + '&vstrCompanyReg=' + vstrCompanyReg + '&vstrVAT=' + vstrVAT +
                '&vstrCPNames=' + vstrCPNames + '&vstrCPSurname=' + vstrCPSurname + '&vstrCPIDNumber=' + vstrCPIDNumber +
        '&vstrCPPosition=' + vstrCPPosition;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateSupplierINFDIV').html(html)
              }
          })
});