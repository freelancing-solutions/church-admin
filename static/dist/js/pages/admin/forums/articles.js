
var thisNewArticleButt = document.getElementById("NewArticleButt");

thisNewArticleButt.addEventListener("click", function () {
        var vstrChoice = 6;
        var vstrForumID = document.getElementById('strForumID').value;
        var vstrTopicID = document.getElementById('strTopicID').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrForumID=' + vstrForumID + '&vstrTopicID=' + vstrTopicID;
          $.ajax({
                type: "post",
                url: "/forums/public",
                data: dataString,
                cache: false,
              success: function(html){
                $('#EditArticlesINFDIV').html(html)
              }
          })
});