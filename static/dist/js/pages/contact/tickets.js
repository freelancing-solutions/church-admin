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

//CreateTicketINFDIV
var thisCreateTicketButt = document.getElementById("CreateTicketButt");
thisCreateTicketButt.addEventListener("click", function () {
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


                var vstrChoice = 3;
                var vstrNames = document.getElementById('strNames').value;
                var vstrSurname = document.getElementById('strSurname').value;
                var vstrCell = document.getElementById('strCell').value;
                var vstrEmail = document.getElementById('strEmail').value;
                var vstrSubject = document.getElementById('strSubject').value;
                var vstrBody = document.getElementById('strBody').value;

                var vstrTicketPreference = document.getElementById('strTicketPreference').value;
                var vstrDepartment = document.getElementById('strDepartment').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrSubject=' + vstrSubject + '&vstrBody=' + vstrBody +
                    '&vstrTicketPreference=' + vstrTicketPreference + '&vstrDepartment=' + vstrDepartment + '&vstrNames=' + vstrNames +
                    '&vstrSurname=' + vstrSurname + '&vstrCell=' + vstrCell + '&vstrEmail=' + email + '&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/contact",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#CreateTicketINFDIV').html(html)
                    }
                });
            })
        }
    })
});
