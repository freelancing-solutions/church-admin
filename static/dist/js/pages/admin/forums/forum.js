
var thisTopicsButt = document.getElementById("TopicsButt");
var thisSubscribeButt = document.getElementById("SubscribeButt");
thisTopicsButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrForumID = document.getElementById('strForumID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrForumID=' + vstrForumID;
          $.ajax({
                type: "post",
                url: "/forums/public",
                data: dataString,
                cache: false,
              success: function(html){
                $('#ForumDIVINF').html(html)
              }
          })
});
thisSubscribeButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrForumID = document.getElementById('strForumID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrForumID=' + vstrForumID;
          $.ajax({
                type: "post",
                url: "/forums/public",
                data: dataString,
                cache: false,
              success: function(html){
                $('#SubscribeINFDIV').html(html)
              }
          })
});