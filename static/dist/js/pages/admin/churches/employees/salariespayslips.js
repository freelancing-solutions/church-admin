var thisUpdateSalaryRecordButt = document.getElementById("UpdateSalaryRecordButt");

thisUpdateSalaryRecordButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var vstrOverTimeRate = document.getElementById('strOverTimeRate').value;
        var vstrNormalRate = document.getElementById('strNormalRate').value;
        var vstrUIF = document.getElementById('strUIF').value;
        var vstrPaye = document.getElementById('strPaye').value;
        var vstrOtherDeductions = document.getElementById('strOtherDeductions').value;
        var vstrThisDate = document.getElementById('strThisDate').value;
        var vstrEmployeeID = document.getElementById('strEmployeeID').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrIDNumber=' + vstrIDNumber + '&vstrOverTimeRate=' + vstrOverTimeRate +
                '&vstrNormalRate=' + vstrNormalRate  + '&vstrUIF=' + vstrUIF + '&vstrPaye=' + vstrPaye + '&vstrOtherDeductions=' + vstrOtherDeductions +
                '&vstrThisDate=' + vstrThisDate + '&vstrEmployeeID=' + vstrEmployeeID;
          $.ajax({
                type: "post",
                url: "/employees/" + vstrIDNumber,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateSalaryRecordINFDIV').html(html)
              }
          })
});