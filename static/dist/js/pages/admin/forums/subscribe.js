var thisDOSubscribeButt = document.getElementById("DOSubscribeButt");

thisDOSubscribeButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrForumID = document.getElementById('strForumID').value;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrEmail = document.getElementById('strEmail').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrForumID=' + vstrForumID + '&vstrNames=' + vstrNames +
                '&vstrSurname=' + vstrSurname + '&vstrCell=' + vstrCell + '&vstrEmail=' + vstrEmail;
          $.ajax({
                type: "post",
                url: "/forums/public",
                data: dataString,
                cache: false,
              success: function(html){
                $('#DoSubscribeINFDIV').html(html)
              }
          })
});