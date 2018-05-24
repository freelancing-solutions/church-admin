try{
var config =
{
    apiKey: "AIzaSyBhNkqMr7zXi4r_bToSFiqPQ8BQLja47_g",
    authDomain: "sa-sms-b.firebaseapp.com",
    databaseURL: "https://sa-sms-b.firebaseio.com",
    projectId: "sa-sms-b",
    storageBucket: "sa-sms-b.appspot.com",
    messagingSenderId: "3221236137"
};
if (!firebase.apps.length) {
    firebase.initializeApp(config);
}else {
}
}catch (err){

}

var thisSendMessageButt = document.getElementById("SendMessageButt");

thisSendMessageButt.addEventListener("click", function () {
    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
            user.getIdToken().then(function (accessToken) {
                // User is signed in.
                var displayName = user.displayName;
                var email = user.email;
                var photoURL = user.photoURL;
                var isAnonymous = user.isAnonymous;
                var providerData = user.providerData;
                var struid = user.uid;


                var vstrChoice = 0;
                var vstrComment = document.getElementById("strComment").value;
                var vstrTicketID = document.getElementById("strTicketID").value;
                var vstrThreadID = document.getElementById("strThreadID").value;
                var vstrUserID = document.getElementById("strUserID").value;
                var dataString = "&vstrChoice=" + vstrChoice + '&vstrComment=' + vstrComment + '&vstrTicketID=' + vstrTicketID +
                    '&vstrThreadID=' + vstrThreadID + '&vstrUserID=' + vstrUserID + '$vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/contact/tickets/" + vstrTicketID,
                    data: dataString,
                    cache: false,
                    success: function (data) {
                        $('#TicketSystemINFDIV').html(data);
                        document.getElementById("strComment").value = "";
                    }
                });
            })
        }
    })
});
function UpdateChat() {
    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
            user.getIdToken().then(function (accessToken) {
                // User is signed in.
                var displayName = user.displayName;
                var email = user.email;
                var photoURL = user.photoURL;
                var isAnonymous = user.isAnonymous;
                var providerData = user.providerData;
                var struid = user.uid;


                var vstrChoice = 1;
                var vstrTicketID = document.getElementById("strTicketID").value;
                var vstrThreadID = document.getElementById("strThreadID").value;
                var vstrUserID = document.getElementById("strUserID").value;

                var dataString = "&vstrChoice=" + vstrChoice + '&vstrTicketID=' + vstrTicketID +
                    '&vstrThreadID=' + vstrThreadID + '&vstrUserID=' + vstrUserID + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/contact/tickets/" + vstrTicketID,
                    data: dataString,
                    cache: false,
                    success: function (data) {
                        $('#TicketSystemINFDIV').html(data)
                    }
                });
            })
        }
    })
}
// TODO- Note it might be easier to just implement push notifications as this methods uses up resources
setInterval(UpdateChat,5000);