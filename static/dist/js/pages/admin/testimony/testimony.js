var thisUploadTestamentButt = document.getElementById("UploadTestamentButt");
thisUploadTestamentButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrOccasion = document.getElementById('strOccasion').value;
        var vstrTextTestament = document.getElementById('strTextTestament').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname + '&vstrOccasion=' + vstrOccasion +
            '&vstrTextTestament=' + vstrTextTestament;
          $.ajax({
                type: "post",
                url: "/admin/testimony",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadTestamentINFDIV').html(html)
              }
          })
});
