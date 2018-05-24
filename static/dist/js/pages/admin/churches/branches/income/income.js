var thisAddOfferingButt = document.getElementById("AddOfferingButt");
thisAddOfferingButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrDateOffering = document.getElementById('strDateOffering').value;
        var vstrOfferingAmount = document.getElementById('strOfferingAmount').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrDateOffering=' + vstrDateOffering + '&vstrOfferingAmount=' + vstrOfferingAmount +
                '&vstrChurchID=' + vstrChurchID + '&vstrChurchBranchID=' + vstrChurchBranchID;
          $.ajax({
                type: "post",
                url: "/monetary/income",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddOfferingStatusINFDIV').html(html)
              }
          });
});
