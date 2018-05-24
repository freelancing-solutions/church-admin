var thisUploadLetterButt = document.getElementById("UploadLetterButt");
thisUploadLetterButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrLetterHeading = document.getElementById('strLetterHeading').value;
        var vstrLetterBody = document.getElementById('strLetterBody').value;
        var vstrListID = document.getElementById('strListID').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrLetterHeading=' + vstrLetterHeading + '&vstrLetterBody=' + vstrLetterBody +
            '&vstrListID=' + vstrListID;
          $.ajax({
                type: "post",
                url: "/admin/newsletters/" + vstrListID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadLetterINFDIV').html(html)
              }
          })
});