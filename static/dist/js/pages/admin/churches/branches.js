var thisAddBranchButt = document.getElementById("AddBranchButt");

thisAddBranchButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrBranchName = document.getElementById('strBranchName').value;
        var vstrBranchMotto = document.getElementById('strBranchMotto').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrBranchName=' + vstrBranchName + '&vstrBranchMotto=' + vstrBranchMotto;
          $.ajax({
                type: "post",
                url: "/admin/branches",
                data: dataString,
                cache: false,
              success: function(html){
                $('#BranchINFDIV').html(html)
              }
          })
});