

var thisAddPledgeButt = document.getElementById("AddPledgeButt");
thisAddPledgeButt.addEventListener("click", function () {
        var vstrChoice = 5;
        var vstrMemberID = document.getElementById('strMemberID').value;
        var vstrPledgeAmount = document.getElementById('strPledgeAmount').value;
        var vstrDate = document.getElementById('strDate').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID + '&vstrPledgeAmount=' + vstrPledgeAmount +
        '&vstrDate=' + vstrDate;
          $.ajax({
                type: "get",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddPledgeStatusINFDIV').html(html)
              }
          })
});