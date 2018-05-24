
var thisBranchDetailsButt = document.getElementById("BranchDetailsButt");

thisBranchDetailsButt.addEventListener("click", function () {
        var vstrChoice = 16;
        var vstrBranchName = document.getElementById('strBranchName').value;
        var vstrBranchMotto = document.getElementById('strBranchMotto').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrBranchName=' + vstrBranchName + '&vstrBranchMotto=' + vstrBranchMotto +
            '&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: "/admin/branches/" + vstrChurchBranchID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateBranchINFDIV').html(html)
              }
          })
});