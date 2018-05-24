var thisUpdateGroupDetailButt = document.getElementById("UpdateGroupDetailButt");
thisUpdateGroupDetailButt.addEventListener("click", function () {
        var vstrChoice = 6;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var vstrGroupName = document.getElementById('strGroupName').value;
        var vstrGroupDescription = document.getElementById('strGroupDescription').value;
        var thisURL = "/sms/groupman/" + vstrGroupID;
        var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrGroupName=' + vstrGroupName +
                '&vstrGroupDescription=' + vstrGroupDescription;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#GroupDetailUpdateINFDIV').html(html)
              }
          })
});