var thisUploadDonationAmountButt = document.getElementById("UploadDonationAmountButt");


thisUploadDonationAmountButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrDonatorID = document.getElementById('strDonatorID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var vstrDonationAmount = document.getElementById('strDonationAmount').value;
        var vstrDate = document.getElementById('strDate').value;
        var thisURL = "/monetary/donators/" + vstrDonatorID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrDonatorID=' + vstrDonatorID + '&vstrChurchID=' + vstrChurchID +
                '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrDonationAmount=' + vstrDonationAmount + '&vstrDate=' + vstrDate;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadDonationAmountINFDIV').html(html)
              }
          });
});