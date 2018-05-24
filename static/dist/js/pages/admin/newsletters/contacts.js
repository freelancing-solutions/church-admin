var thisUploadContactButt = document.getElementById("UploadContactButt");
thisUploadContactButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrListID = document.getElementById('strListID').value;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrEmail = document.getElementById('strEmail').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrListID=' + vstrListID + '&vstrEmail=' + vstrEmail + '&vstrCell=' + vstrCell +
                '&vstrSurname=' + vstrSurname + '&vstrNames=' + vstrNames;
          $.ajax({
                type: "post",
                url: "/admin/newsletters/" + vstrListID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadContactINFDIV').html(html)
              }
          })
});