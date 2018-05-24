tinymce.init({
      selector: '#strDescription',
      height: 710,
      theme: 'modern',
      plugins: [
        'image media codesample imagetools link',
        'advlist autolink lists link image charmap print preview hr anchor pagebreak',
        'searchreplace wordcount visualblocks visualchars code fullscreen',
        'insertdatetime media nonbreaking save table contextmenu directionality',
        'emoticons template paste textcolor colorpicker textpattern imagetools codesample toc help'
      ],

      toolbar1: 'undo redo | insert | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent',
      toolbar2: 'print preview media | forecolor backcolor emoticons | codesample help | link image media codesample',
      image_advtab: true,
      image_caption: true,
      media_live_embeds: true,
      imagetools_cors_hosts: ['tinymce.com', 'codepen.io'],
      templates: [
        { title: 'Test template 1', content: 'Test 1' },
        { title: 'Test template 2', content: 'Test 2' }
      ],
      content_css: [
        '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
        '//www.tinymce.com/css/codepen.min.css'
      ]
 });

var thisUpdateEventButt = document.getElementById("UpdateEventButt");
var thisUploadEventTypeButt = document.getElementById("UploadEventTypeButt");

thisUpdateEventButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrEventName = document.getElementById('strEventName').value;
        var vstrDescription = tinyMCE.activeEditor.getContent();
        var vstrEventIntro = document.getElementById('strEventIntro').value;
        var vstrStartDate = document.getElementById('strStartDate').value;
        var vstrStartTime = document.getElementById('strStartTime').value;
        var vstrEndDate = document.getElementById('strEndDate').value;
        var vstrEndTime = document.getElementById('strEndTime').value;
        var vstrEventType = document.getElementById('strEventType').value;
        var vstrSendNotifications= document.getElementById('strSendNotifications').value;


        var dataString = '&vstrChoice='+ vstrChoice + '&vstrEventName=' + vstrEventName + '&vstrDescription=' + vstrDescription +
            '&vstrStartDate=' + vstrStartDate + '&vstrStartTime=' + vstrStartTime + '&vstrEndDate=' + vstrEndDate +
            '&vstrEndTime=' + vstrEndTime + '&vstrEventType=' + vstrEventType + '&vstrSendNotifications=' + vstrSendNotifications +
                '&vstrEventIntro=' + vstrEventIntro;
          $.ajax({
                type: "post",
                url: "/events",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateINFDIV').html(html)
              }
          })
});
thisUploadEventTypeButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrNewEventType = document.getElementById('strNewEventType').value;
        var vstrNewEventDescription = document.getElementById('strNewEventDescription').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrNewEventType=' + vstrNewEventType + '&vstrNewEventDescription=' +
                vstrNewEventDescription;
          $.ajax({
                type: "post",
                url: "/events",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadEventTypesINFDIV').html(html)
              }
          })
});
