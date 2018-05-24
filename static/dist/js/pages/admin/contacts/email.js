
var thisMessageButt = document.getElementById("MessageButt");

thisMessageButt.addEventListener("click", function () {
        var vstrChoice = 7;
        var vstrSubject = document.getElementById('strSubject').value;
        var vstrMessage = document.getElementById('strMessage').value;
        var vstrCell = document.getElementById('strCell').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrSubject=' + vstrSubject + '&vstrMessage=' + vstrMessage + '&vstrCell=' + vstrCell;
          $.ajax({
                type: "post",
                url: "/admin/contacts/" + vstrCell,
                data: dataString,
                cache: false,
              success: function(html){
                $('#MessageINFDIV').html(html)
              }
          })
});