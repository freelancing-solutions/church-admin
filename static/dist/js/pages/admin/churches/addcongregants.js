var thisUpdateMemberDataButt = document.getElementById("UpdateMemberDataButt");

thisUpdateMemberDataButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrMemberName = document.getElementById('strMemberName').value;
        var vstrMemberSurname = document.getElementById('strMemberSurname').value;
        var vstrMemberTitle = document.getElementById('strMemberTitle').value;
        var vstrMemberIDNumber = document.getElementById('strMemberIDNumber').value;
        var vstrMemberGender = document.getElementById('strMemberGender').value;
        var vstrMemberDateOfBirth = document.getElementById('strMemberDateOfBirth').value;
        var vstrMemberDateOfMemberShip = document.getElementById('strMemberDateOfMemberShip').value;
        var vstrMemberDateBaptised = document.getElementById('strMemberDateBaptised').value;
        var vstrTel = document.getElementById('strTel').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrEmail = document.getElementById('strEmail').value;
        var vstrWorkTel = document.getElementById('strWorkTel').value;
        var vstrWorkCell = document.getElementById('strWorkCell').value;
        var vstrSelectBranch = document.getElementById('strSelectBranch').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberName=' + vstrMemberName + '&vstrMemberSurname=' + vstrMemberSurname +
            '&vstrMemberTitle=' + vstrMemberTitle + '&vstrMemberIDNumber=' + vstrMemberIDNumber + '&vstrMemberGender=' +
            vstrMemberGender + '&vstrMemberDateOfBirth=' + vstrMemberDateOfBirth +
            '&vstrMemberDateOfMemberShip=' + vstrMemberDateOfMemberShip + '&vstrMemberDateBaptised=' + vstrMemberDateBaptised + '&vstrTel=' + vstrTel +
            '&vstrCell='+ vstrCell + '&vstrEmail=' + vstrEmail + '&vstrWorkTel=' + vstrWorkTel + '&vstrWorkCell=' + vstrWorkCell +
        '&vstrSelectBranch=' + vstrSelectBranch;

          $.ajax({
                type: "post",
                url: "/admin/congregants",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateMemberDataINFDIV').html(html)
              }
          })
});