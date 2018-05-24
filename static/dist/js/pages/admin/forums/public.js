var thisUploadForumButt = document.getElementById("UploadForumButt");

thisUploadForumButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrForumName = document.getElementById('strForumName').value;
        var vstrForumDescription = document.getElementById('strForumDescription').value;
        var vstrForumLandingPage = tinyMCE.activeEditor.getContent();


        alert(vstrForumLandingPage);

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrForumName=' + vstrForumName + '&vstrForumDescription=' + vstrForumDescription + '&vstrForumLandingPage=' + vstrForumLandingPage;
          $.ajax({
                type: "post",
                url: "/forums/public",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadForumINFDIV').html(html)
              }
          })
});
 tinymce.init({
          selector: '#strForumLandingPage',
          height: 600,
          theme: 'modern',
          plugins: [
            'advlist autolink lists link image charmap print preview hr anchor pagebreak',
            'searchreplace wordcount visualblocks visualchars code fullscreen',
            'insertdatetime media nonbreaking save table contextmenu directionality',
            'emoticons template paste textcolor colorpicker textpattern imagetools codesample toc help'
          ],

          toolbar1: 'undo redo | insert | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
          toolbar2: 'print preview media | forecolor backcolor emoticons | codesample help',
          image_advtab: true,
          templates: [
            { title: 'Test template 1', content: 'Test 1' },
            { title: 'Test template 2', content: 'Test 2' }
          ],
          content_css: [
            '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
            '//www.tinymce.com/css/codepen.min.css'
          ]
         });