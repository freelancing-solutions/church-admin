var thisUploadContactButt = document.getElementById("UploadContactButt");
var thisBulkUploadContactsButt = document.getElementById("BulkUploadContactsButt");
var thisRemoveButt = document.getElementById("RemoveButt");

thisUploadContactButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrCellNumber = document.getElementById('strCellNumber').value;
        var vstrGroupID = document.getElementById('strGroupID').value;
        var thisURL = "/sms/groupman/" + vstrGroupID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
                '&vstrCellNumber=' + vstrCellNumber + '&vstrGroupID=' + vstrGroupID;
          $.ajax({
                type: "post",
                url:thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#UploadContactINFDIV').html(html)
              }
          })
});
thisBulkUploadContactsButt.addEventListener("click", function () {
        var vstrChoice = 9;
        //var vstrContactList = $('strContacts').val().split('\n');
        var vstrContactList = document.getElementById('strContacts').value;
        alert(vstrContactList);
        var vstrContactList = vstrContactList.split('\n');
        var vstrThisContactList = "";
        for (thisContact in vstrContactList){
            if (vstrThisContactList == ""){
                vstrThisContactList= vstrContactList[thisContact];
            }else{
                vstrThisContactList = vstrThisContactList + "|" + vstrContactList[thisContact];
            }
        }
        var vstrGroupID = document.getElementById('strGroupID').value;
        var thisURL = "/sms/groupman/" + vstrGroupID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrContacts=' + vstrThisContactList + '&vstrGroupID=' +vstrGroupID;
          $.ajax({
                type: "post",
                url:thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#BulkUploadContactsINFDIV').html(html)
              }
          })
});

thisRemoveButt.addEventListener("click", function () {
        var vstrChoice = 11;

        var vstrGroupID = document.getElementById('strGroupID').value;
        var vstrRemoveCell = document.getElementById('strRemoveCell').value;

        var thisURL = "/sms/groupman/" + vstrGroupID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrGroupID=' +vstrGroupID + '&vstrRemoveCell=' + vstrRemoveCell;
          $.ajax({
                type: "post",
                url:thisURL,
                data: dataString,
                cache: false,
              success: function(html){
                $('#RemoveContactINFDIV').html(html)
              }
          })
});