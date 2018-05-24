var thisAddDonationButt = document.getElementById("AddDonationButt");

thisAddDonationButt.addEventListener("click", function () {
        var vstrChoice = 8;
        var vstrMemberID = document.getElementById('strMemberID').value;
        var vstrDonationAmount = document.getElementById('strDonationAmount').value;
        var vstrDate = document.getElementById('strDate').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID + '&vstrDonationAmount=' + vstrDonationAmount +
        '&vstrDate=' + vstrDate;
          $.ajax({
                type: "get",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddDonationStatusINFDIV').html(html)
              }
          })
});