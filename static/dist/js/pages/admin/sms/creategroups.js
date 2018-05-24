var thisCreateGroupButt = document.getElementById("CreateGroupButt");
thisCreateGroupButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrGroupName = document.getElementById('strGroupName').value;
        var vstrGroupDescription = document.getElementById('strGroupDescription').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrGroupName=' + vstrGroupName + '&vstrGroupDescription=' + vstrGroupDescription;
          $.ajax({
                type: "get",
                url: "/admin/sms/groups",
                data: dataString,
                cache: false,
              success: function(html){
                $('#CreateGroupsINFDIV').html(html)
              }
          })
});