    var strSelectedGroupsList = [];
    function GetGroup(clicked_id){
        if (strSelectedGroupsList.indexOf(clicked_id) < 0){
            strSelectedGroupsList.push(clicked_id);
        }else{
                for(var i = strSelectedGroupsList.length - 1; i >= 0; i--) {
                    if(strSelectedGroupsList[i] === clicked_id) {
                       strSelectedGroupsList.splice(i, 1);
                    }
                }
        }
    }

    var thisJoinGroupsButt = document.getElementById("JoinGroupsButt");
    
    thisJoinGroupsButt.addEventListener("click", function () {
        var vstrChoice = 4;

        var vstrMemberID = document.getElementById('strMemberID').value;
        var vstrGroupList = "";
        for (thisGroup in strSelectedGroupsList){
            if(vstrGroupList === ""){
                vstrGroupList = thisGroup;
            }else{
                vstrGroupList = vstrGroupList + "," + thisGroup;
            }
        }
        var thisURL = "/sms/groupman/" + vstrMemberID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID + '&vstrGroupList=' + vstrGroupList;
          $.ajax({
                type: "post",
                url:thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#ProcessMembershipINFDIV').html(html)
              }
          })
    });