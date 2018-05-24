var thisLettersButt = document.getElementById("LettersButt");
var thisContactsButt = document.getElementById("ContactsButt");
var thisScheduleButt = document.getElementById("ScheduleButt");

thisLettersButt.addEventListener("click", function () {
        var vstrChoice = 0;
        var vstrListID = document.getElementById('strListID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrListID=' + vstrListID;
          $.ajax({
                type: "post",
                url: "/admin/newsletters/"+vstrListID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#thisNewsLetterINFDIV').html(html)
              }
          })
});
thisContactsButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrListID = document.getElementById('strListID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrListID=' + vstrListID;
          $.ajax({
                type: "post",
                url: "/admin/newsletters/"+vstrListID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#thisNewsLetterINFDIV').html(html)
              }
          })
});
thisScheduleButt.addEventListener("click", function () {
        var vstrChoice = 6;
        var vstrListID = document.getElementById('strListID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrListID=' + vstrListID;
          $.ajax({
                type: "post",
                url: "/admin/newsletters/"+vstrListID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#thisNewsLetterINFDIV').html(html)
              }
          })
});