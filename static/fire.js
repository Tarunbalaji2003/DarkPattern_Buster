const firebaseConfig = {
    apiKey: "AIzaSyDmeF8-pkGE-qrKPxuHwNubFPEnYPCx5iw",
    authDomain: "e-commerce-39299.firebaseapp.com",
    databaseURL: "https://e-commerce-39299-default-rtdb.firebaseio.com",
    projectId: "e-commerce-39299",
    storageBucket: "e-commerce-39299.appspot.com",
    messagingSenderId: "186993770570",
    appId: "1:186993770570:web:7f5fafe98a392be83f26b3",
    measurementId: "G-7HEGBY6TJ2"
  };

  // Initialize Firebase
   firebase.initializeApp(firebaseConfig);
  
  // reference your database
var contactFormDB = firebase.database().ref("e-commerce");

document.getElementById("e-commerce").addEventListener("submit", submitForm);

function submitForm(e) {
  e.preventDefault();

  var name = getElementVal("name");
  var emailid = getElementVal("emailid");
  var msgContent = getElementVal("msgContent");

  saveMessages(name, emailid, msgContent);

  //   enable alert
  document.querySelector(".alert").style.display = "block";

  //   remove the alert
  setTimeout(() => {
    document.querySelector(".alert").style.display = "none";
  }, 3000);

  //   reset the form
  document.getElementById("contactForm").reset();
}

const saveMessages = (name, emailid, msgContent) => {
  var newContactForm = contactFormDB.push();

  newContactForm.set({
    name: name,
    emailid: emailid,
    msgContent: msgContent,
  });
};

const getElementVal = (id) => {
  return document.getElementById(id).value;
};