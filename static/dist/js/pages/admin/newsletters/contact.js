function isEmpty(str) {return (!str || 0 === str.length);}
var thisBulkUploadContactsButt = document.getElementById("BulkUploadContactsButt");
var thisUploadContactButt = document.getElementById("UploadContactButt");
var thisRemoveButt = document.getElementById("RemoveButt");
thisBulkUploadContactsButt.addEventListener("click", function () {
        var vstrChoice = 3;
        //var vstrContactList = $('strContacts').val().split('\n');
        var vstrContactList = document.getElementById('strContacts').value;
        alert(vstrContactList);
        vstrContactList = vstrContactList.split('\n');
        var vstrThisContactList = "";
        for (thisContact in vstrContactList){
            if (isEmpty(vstrThisContactList) === true){
                vstrThisContactList= vstrContactList[thisContact];
            }else{
                vstrThisContactList = vstrThisContactList + "|" + vstrContactList[thisContact];
            }
        }
        var vstrListID = document.getElementById('strListID').value;
        var thisURL = "/admin/newsletters/" + vstrListID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrContacts=' + vstrThisContactList + '&vstrListID=' +vstrListID;
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
thisUploadContactButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrNames = document.getElementById('strNames').value;
        var vstrSurname = document.getElementById('strSurname').value;
        var vstrCellNumber = document.getElementById('strCellNumber').value;
        var vstrEmail = document.getElementById('strEmail').value;
        var vstrListID = document.getElementById('strListID').value;
        var thisURL = "/admin/newsletters/" + vstrListID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
                '&vstrCellNumber=' + vstrCellNumber + '&vstrListID=' + vstrListID + '&vstrEmail=' + vstrEmail;
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
thisRemoveButt.addEventListener("click", function () {
        var vstrChoice = 5;
        var vstrListID = document.getElementById('strListID').value;
        var vstrRemoveEmail = document.getElementById('strRemoveEmail').value;

        var thisURL = "/admin/newsletters/" + vstrListID;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrListID =' + vstrListID + '&vstrRemoveEmail=' + vstrRemoveEmail;
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