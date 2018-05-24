var thisAcceptRequestButt = document.getElementById("AcceptRequestButt");

thisAcceptRequestButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrReference = document.getElementById('strReference').value;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrIDNumber = document.getElementById('strIDNumber').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrEmail = document.getElementById('strEmail').value;
        var vstrPaymentReceived = document.getElementById('strPaymentReceived').value;
        var vstrRequestAccepted = document.getElementById('strRequestAccepted').value;
        var vstrDateRequestSent = document.getElementById('strDateRequestSent').value;
        var vstrProduct = document.getElementById('strProduct').value;

        var thisURL = "/accounts/request/" + vstrReference;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
            '&vstrIDNumber=' + vstrIDNumber + '&vstrCell=' + vstrCell + '&vstrEmail=' + vstrEmail +
            '&vstrPaymentReceived=' + vstrPaymentReceived + '&vstrRequestAccepted=' + vstrRequestAccepted +
            '&vstrDateRequestSent=' + vstrDateRequestSent + '&vstrProduct=' + vstrProduct + '&vstrReference=' + vstrReference;
          $.ajax({
                type: "post",
                url:thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UserDetailINFDIV').html(html)
              }
          });
});
