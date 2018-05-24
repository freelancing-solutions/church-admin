var thisSaveChurchButt = document.getElementById("SaveChurchButt");

thisSaveChurchButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrChurchName = document.getElementById('strChurchName').value;
        var vstrRegNumber = document.getElementById('strRegNumber').value;
        var vstrChurchMotto = document.getElementById('strChurchMotto').value;
        var vstrVision = document.getElementById('strVision').value;
        var vstrMission = document.getElementById('strMission').value;
        var vstrPropheticWord = document.getElementById('strPropheticWord').value;
        var vstrFounderTitle = document.getElementById('strFounderTitle').value;
        var vstrFounder = document.getElementById('strFounder').value;
        var vstrDateFounded = document.getElementById('strDateFounded').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrChurchName=' + vstrChurchName + '&vstrRegNumber=' + vstrRegNumber +
            '&vstrChurchMotto=' + vstrChurchMotto + '&vstrVision=' + vstrVision + '&vstrMission=' + vstrMission + '&vstrPropheticWord=' + vstrPropheticWord +
            '&vstrFounderTitle=' + vstrFounderTitle + '&vstrFounder=' + vstrFounder + '&vstrDateFounded=' + vstrDateFounded;
          $.ajax({
                type: "post",
                url: "/admin/churchdetails",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdatedChurchDetailsINFDIV').html(html)
              }
          })
});