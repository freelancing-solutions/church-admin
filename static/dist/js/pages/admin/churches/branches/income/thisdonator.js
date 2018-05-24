
var thisDonatorsDetailsButt = document.getElementById("DonatorsDetailsButt");
var thisDonationsButt = document.getElementById("DonationsButt");
var thisMessagingButt = document.getElementById("MessagingButt");
thisDonatorsDetailsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrDonatorID = document.getElementById('strDonatorID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/monetary/donators/" + vstrDonatorID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrDonatorID=' + vstrDonatorID + '&vstrChurchID=' + vstrChurchID +
                '&vstrChurchBranchID=' + vstrChurchBranchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#DonatorINFDIV').html(html)
              }
          })
});

thisDonationsButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrDonatorID = document.getElementById('strDonatorID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/monetary/donators/" + vstrDonatorID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrDonatorID=' + vstrDonatorID + '&vstrChurchID=' + vstrChurchID +
                '&vstrChurchBranchID=' + vstrChurchBranchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#DonatorINFDIV').html(html)
              }
          })
});
thisMessagingButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrDonatorID = document.getElementById('strDonatorID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var thisURL = "/monetary/donators/" + vstrDonatorID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrDonatorID=' + vstrDonatorID + '&vstrChurchID=' + vstrChurchID +
                '&vstrChurchBranchID=' + vstrChurchBranchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#DonatorINFDIV').html(html)
              }
          })
});