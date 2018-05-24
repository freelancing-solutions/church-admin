var thisUploadNewsLetterButt = document.getElementById("UploadNewsLetterButt");

thisUploadNewsLetterButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrListName = document.getElementById('strListName').value;
        var vstrListDescription = document.getElementById('strListDescription').value;
        var vstrStartSendingDate = document.getElementById('strStartSendingDate').value;
        var vstrStartSendingTime = document.getElementById('strStartSendingTime').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrListName=' + vstrListName + '&vstrListDescription=' + vstrListDescription +
                '&vstrStartSendingDate=' + vstrStartSendingDate + '&vstrStartSendingTime=' + vstrStartSendingTime;
          $.ajax({
                type: "post",
                url: "/admin/newsletters",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadNewsLetterINFDIV').html(html)
              }
          })
});