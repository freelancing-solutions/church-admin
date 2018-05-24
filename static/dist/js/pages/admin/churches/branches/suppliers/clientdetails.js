
var thisUpdateClientButt = document.getElementById("UpdateClientButt");
thisUpdateClientButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrClientID = document.getElementById('strClientID').value;
        var vstrChurchBranchID = document.getElementById('strChurchBranchID').value;
        var vstrChurchID = document.getElementById('strChurchID').value;


        var thisURL = "/admin/clients/" + vstrClientID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrClientID=' + vstrClientID +'&vstrChurchBranchID=' + vstrChurchBranchID + '&vstrChurchID=' + vstrChurchID;
          $.ajax({
                type: "post",
                url: thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ClientDetailsINFDIV').html(html)
              }
          })
});