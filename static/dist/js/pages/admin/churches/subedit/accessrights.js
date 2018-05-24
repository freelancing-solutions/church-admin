var thisUpdateAccessRightsButt = document.getElementById("UpdateAccessRightsButt");
thisUpdateAccessRightsButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrAdminUser = document.getElementById('strAdminUser').value;
        var vstrSuperUser = document.getElementById('strSuperUser').value;
        var vstrVisitor = document.getElementById('strVisitor').value;
        var vstrChurchMember = document.getElementById('strChurchMember').value;

        var vstrMemberID = document.getElementById('strMemberID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID + '&vstrAdminUser=' + vstrAdminUser +
            '&vstrSuperUser=' + vstrSuperUser + '&vstrVisitor=' + vstrVisitor + '&vstrChurchMember=' + vstrChurchMember;
          $.ajax({
                type: "post",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AccessRightsINFDIV').html(html)
              }
          })
});