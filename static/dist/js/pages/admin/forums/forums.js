var thisForumsButt = document.getElementById("ForumsButt");
thisForumsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var dataString = '&vstrChoice='+ vstrChoice;
          $.ajax({
                type: "post",
                url: "/forums",
                data: dataString,
                cache: false,
              success: function(html){
                $('#LoadForumsDIVINF').html(html)
              }
          })
});