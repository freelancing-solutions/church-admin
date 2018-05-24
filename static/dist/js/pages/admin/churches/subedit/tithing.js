var thisAddTithingButt = document.getElementById("AddTithingButt");

thisAddTithingButt.addEventListener("click", function () {
        var vstrChoice = 9;
        var vstrMemberID = document.getElementById('strMemberID').value;
        var vstrTithingAmount = document.getElementById('strTithingAmount').value;
        var vstrDate = document.getElementById('strDate').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID + '&vstrTithingAmount=' + vstrTithingAmount +
        '&vstrDate=' + vstrDate;
          $.ajax({
                type: "get",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddTithingStatusINFDIV').html(html)
              }
          })
});