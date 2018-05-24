

var thisSendMessageButt = document.getElementById("SendMessageButt");

thisSendMessageButt.addEventListener("click", function () {

            var varstrNames = document.getElementById('strnames').value;
            var varstrCell = document.getElementById('strcell').value;
            var varstrEmail = document.getElementById('stremail').value;
            var varstrsubject = document.getElementById('strsubject').value;
            var varstrmessage = document.getElementById('strmessage').value;


            var dataString = '&vstrNames=' + varstrNames + '&vstrCell='+ varstrCell + '&vstrEmail=' + varstrEmail +
                    '&vstrSubject='+ varstrsubject + '&vstrMessage='+ varstrmessage;
              $.ajax({
                    type: "post",
                    url: "/contact",
                    data: dataString,
                    cache: false,
                  success: function(html){
                    $('#FormResponseDiv').html(html)
                  }
              })
});