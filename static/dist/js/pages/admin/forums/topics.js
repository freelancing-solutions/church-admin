function showArticles(clicked_id) {
        var vstrChoice = 5;
        var vstrTopicID = clicked_id;
        var vstrForumID = document.getElementById('strForumID').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrTopicID=' + vstrTopicID + '&vstrForumID=' + vstrForumID;
        var returnDivTag = "#showArticlesINFDIV"+clicked_id;
          $.ajax({
                type: "post",
                url: "/forums/public",
                data: dataString,
                cache: false,
              success: function(html){
                $(returnDivTag).html(html)
              }
          });
}
var thisUploadTopicButt = document.getElementById("UploadTopicButt");
var thisshowArticlesButt = document.getElementById("showArticlesButt");
thisUploadTopicButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrForumID = document.getElementById('strForumID').value;
        var vstrTopicName = document.getElementById('strTopicName').value;
        var vstrTopicDescription = document.getElementById('strTopicDescription').value;


        var dataString = '&vstrChoice='+ vstrChoice + '&vstrForumID=' + vstrForumID + '&vstrTopicName=' + vstrTopicName +
                '&vstrTopicDescription=' + vstrTopicDescription;
          $.ajax({
                type: "post",
                url: "/forums/public",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadTopicINFDIV').html(html)
              }
          })
});
thisshowArticlesButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrForumID = document.getElementById('strForumID').value;
        var vstrTopicName = document.getElementById('strTopicName').value;
        var vstrTopicDescription = document.getElementById('strTopicDescription').value;


        var dataString = '&vstrChoice='+ vstrChoice + '&vstrForumID=' + vstrForumID + '&vstrTopicName=' + vstrTopicName +
                '&vstrTopicDescription=' + vstrTopicDescription;

          $.ajax({
                type: "post",
                url: "/forums/public",
                data: dataString,
                cache: false,
              success: function(html){
                $('#showArticlesINFDIV').html(html)
              }
          })
});