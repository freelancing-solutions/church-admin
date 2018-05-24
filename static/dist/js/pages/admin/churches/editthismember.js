var thisUpdateChurchMemberButt = document.getElementById("UpdateChurchMemberButt");
var thisMemberInfoButt = document.getElementById("MemberInfoButt");
var thisMemberAddressButt = document.getElementById("MemberAddressButt");
var thisMemberAccessRightsButt = document.getElementById("MemberAccessRightsButt");
var thisMemberPledgesButt = document.getElementById("MemberPledgesButt");
var thisMemberDonationsButt = document.getElementById("MemberDonationsButt");
var thisMemberTithingsButt = document.getElementById("MemberTithingsButt");
var thisSMSButt = document.getElementById("SMSButt");
var thisMessagingButt  = document.getElementById("MessagingButt");

thisUpdateChurchMemberButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrMemberName = document.getElementById('strMemberName').value;
        var vstrMemberSurname = document.getElementById('strMemberSurname').value;
        var vstrMemberTitle = document.getElementById('strMemberTitle').value;
        var vstrMemberIDNumber = document.getElementById('strMemberIDNumber').value;
        var vstrMemberGender = document.getElementById('strMemberGender').value;
        var vstrMemberDateOfBirth = document.getElementById('strMemberDateOfBirth').value;
        var vstrMemberDateOfMemberShip = document.getElementById('strMemberDateOfMemberShip').value;
        var vstrMemberDateBaptised = document.getElementById('strMemberDateBaptised').value;
        var vstrTel = document.getElementById('strTel').value;
        var vstrCell = document.getElementById('strCell').value;
        var vstrEmail = document.getElementById('strEmail').value;
        var vstrWorkTel = document.getElementById('strWorkTel').value;
        var vstrWorkCell = document.getElementById('strWorkCell').value;
        var vstrWorkEmail = document.getElementById('strWorkEmail').value;
        var vstrSelectBranch = document.getElementById('strSelectBranch').value;

        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberName=' + vstrMemberName + '&vstrMemberSurname=' + vstrMemberSurname +
            '&vstrMemberTitle=' + vstrMemberTitle + '&vstrMemberIDNumber=' + vstrMemberIDNumber + '&vstrMemberGender=' +
            vstrMemberGender + '&vstrMemberDateOfBirth=' + vstrMemberDateOfBirth +
            '&vstrMemberDateOfMemberShip=' + vstrMemberDateOfMemberShip + '&vstrMemberDateBaptised=' + vstrMemberDateBaptised + '&vstrTel=' + vstrTel +
            '&vstrCell='+ vstrCell + '&vstrEmail=' + vstrEmail + '&vstrWorkTel=' + vstrWorkTel + '&vstrWorkCell=' + vstrWorkCell + '&vstrWorkEmail=' + vstrWorkEmail +
            '&vstrSelectBranch=' + vstrSelectBranch;

          $.ajax({
                type: "post",
                url: "/admin/congregants",
                data: dataString,
                cache: false,
              success: function(html){
                $('#UpdateChurchMemberINFDIV').html(html)
              }
          })
});
thisMemberInfoButt.addEventListener("click", function () {
        var vstrChoice = 1;
        var vstrMemberID = document.getElementById('strMemberID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID;
          $.ajax({
                type: "get",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#editThisINFDIV').html(html)
              }
          })
});
thisMemberAddressButt.addEventListener("click", function () {
        var vstrChoice = 2;
        var vstrMemberID = document.getElementById('strMemberID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID;
          $.ajax({
                type: "get",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#editThisINFDIV').html(html)
              }
          })
});
thisMemberAccessRightsButt.addEventListener("click", function () {
        var vstrChoice = 3;
        var vstrMemberID = document.getElementById('strMemberID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID;
          $.ajax({
                type: "get",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#editThisINFDIV').html(html)
              }
          })
});
thisMemberPledgesButt.addEventListener("click", function () {
        var vstrChoice = 4;
        var vstrMemberID = document.getElementById('strMemberID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID;
          $.ajax({
                type: "get",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#editThisINFDIV').html(html)
              }
          })
});
thisMemberDonationsButt.addEventListener("click", function () {
        var vstrChoice = 6;
        var vstrMemberID = document.getElementById('strMemberID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID;
          $.ajax({
                type: "get",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#editThisINFDIV').html(html)
              }
          })
});
thisMemberTithingsButt.addEventListener("click", function () {
        var vstrChoice = 7;
        var vstrMemberID = document.getElementById('strMemberID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID;
          $.ajax({
                type: "get",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#editThisINFDIV').html(html)
              }
          })
});
thisSMSButt.addEventListener("click", function () {
        var vstrChoice = 10;
        var vstrMemberID = document.getElementById('strMemberID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID;
          $.ajax({
                type: "get",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#editThisINFDIV').html(html)
              }
          })
});
thisMessagingButt.addEventListener("click", function () {
        var vstrChoice = 11;
        var vstrMemberID = document.getElementById('strMemberID').value;
        var dataString = '&vstrChoice='+ vstrChoice + '&vstrMemberID=' + vstrMemberID;
          $.ajax({
                type: "get",
                url: "/church/member/get",
                data: dataString,
                cache: false,
              success: function(html){
                $('#editThisINFDIV').html(html)
              }
          })
});
