function showInEditor (clicked_id) {CKEDITOR.replace(clicked_id);$(".textarea").wysihtml5();}

var thisstrBibleBookBtn = document.getElementById("strBibleBookBtn");
var thisUpdateSermonsButt = document.getElementById("UpdateSermonsButt");

thisstrBibleBookBtn.addEventListener("click", function () {
            var vstrBibleBook = document.getElementById('strBibleBook').value;
            vstrBibleBook = 'p=' + vstrBibleBook + '&v=kjv';

            jQuery.ajax({
                url: 'http://getbible.net/json',
                dataType: 'jsonp',
                data: vstrBibleBook,
                jsonp: 'getbible',
                success: function (json) {
                    // set text direction
                    if (json.direction === 'RTL') {
                        var direction = 'rtl';
                    } else {
                        var direction = 'ltr';
                    }
                    // check response type
                    if (json.type === 'verse') {
                        var output = '';
                        jQuery.each(json.book, function (index, value) {
                            output += '<center><b>' + value.book_name + ' ' + value.chapter_nr + '</b></center><br/><p class="' + direction + '">';
                            jQuery.each(value.chapter, function (index, value) {
                                output += '  <small class="ltr">' + value.verse_nr + '</small>  ';
                                output += value.verse;
                                output += '<br/>';
                            });
                            output += '</p>';
                        });
                        jQuery('#scripture').html(output);  // <---- this is the div id we update
                    } else if (json.type === 'chapter') {
                        var output = '<center><b>' + json.book_name + ' ' + json.chapter_nr + '</b></center><br/><p class="' + direction + '">';
                        jQuery.each(json.chapter, function (index, value) {
                            output += '  <small class="ltr">' + value.verse_nr + '</small>  ';
                            output += value.verse;
                            output += '<br/>';
                        });
                        output += '</p>';
                        jQuery('#scripture').html(output);  // <---- this is the div id we update
                    } else if (json.type === 'book') {
                        var output = '';
                        jQuery.each(json.book, function (index, value) {
                            output += '<center><b>' + json.book_name + ' ' + value.chapter_nr + '</b></center><br/><p class="' + direction + '">';
                            jQuery.each(value.chapter, function (index, value) {
                                output += '  <small class="ltr">' + value.verse_nr + '</small>  ';
                                output += value.verse;
                                output += '<br/>';
                            });
                            output += '</p>';
                        });
                        if (addTo) {
                            jQuery('#scripture').html(output);  // <---- this is the div id we update
                        }
                    }
                },
                error: function () {
                    jQuery('#scripture').html('<h2>No scripture was returned, please try again!</h2>'); // <---- this is the div id we update
                },
            })
});

thisUpdateSermonsButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrTitle = document.getElementById('strTitle').value;
        var vstrSermon = document.getElementById('strSermonTracker').innerHTML;
        var vstrDateDelivery = document.getElementById('strDateDelivery').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrTitle=' + vstrTitle + '&vstrSermon=' + vstrSermon +
            '&vstrDateDelivery=' + vstrDateDelivery;
          $.ajax({
                type: "post",
                url: "/admin/sermons",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateSermonsINFDIV').html(html)
              }
          })
});