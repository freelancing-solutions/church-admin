

var thisAddClientButt = document.getElementById("AddClientButt");

thisAddClientButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var vstrChurchID = document.getElementById('strChurchID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' +vstrSurname +
                '&vstrIDNumber=' + vstrIDNumber + '&vstrChurchID=' + vstrChurchID + '&vstrChurchBranchID=' + vstrChurchBranchID;
          $.ajax({
                type: "post",
                url: "/admin/clients",
                data: dataString,
                cache: false,
              success: function(html){
                $('#AddClientINFDIV').html(html)
              }
          })
});