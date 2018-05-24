var thisUpdateFacilitatorButt = document.getElementById("UpdateFacilitatorButt");
thisUpdateFacilitatorButt.addEventListener("click", function () {
        var vstrChoice = 9;
        var vstrMeetingID = document.getElementById('strMeetingID').value;
        var vstrFacilitatorName = document.getElementById('strFacilitatorName').value;
        var vstrFacilitatorSurname = document.getElementById('strFacilitatorSurname').value;
        var vstrFacilitatorCell = document.getElementById('strFacilitatorCell').value;
        var vstrFacilitatorEmail = document.getElementById('strFacilitatorEmail').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMeetingID=' + vstrMeetingID + '&vstrFacilitatorName=' + vstrFacilitatorName +
                '&vstrFacilitatorSurname=' + vstrFacilitatorSurname + '&vstrFacilitatorCell=' + vstrFacilitatorCell +
                '&vstrFacilitatorEmail=' + vstrFacilitatorEmail;
          $.ajax({
                type: "post",
                url: "/admin/meetings/" + vstrMeetingID,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateFacilitatorINFDIV').html(html)
              }
          })
});