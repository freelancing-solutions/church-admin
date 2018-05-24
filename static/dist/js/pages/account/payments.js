var thisMakePaymentButt = document.getElementById("MakePaymentButt");

thisMakePaymentButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrPaymentMethod = document.getElementById('strPaymentMethod').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrPaymentMethod=' + vstrPaymentMethod;
          $.ajax({
                type: "post",
                url: "/accounts/payments",
                data: dataString,
                cache: false,
              success: function(html){
                $('#MakePaymentINFDIV').html(html)
              }
          });
});