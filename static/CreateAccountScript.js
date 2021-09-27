
function CreateAcc(){ 
    var user = document.getElementById("myform").elements.namedItem("username").value;
    var pass = document.getElementById("myform").elements.namedItem("password").value;
    var conpass = document.getElementById("myform").elements.namedItem("password_confirm").value;
     if(user == ""){
         alert("Please Enter Username");
         return false;
    }
    if(pass == ""){
        alert("Please Enter Password");
        return false;
   }
   if(pass != conpass){
    alert("Passwords do not match");
    return false;
}
    else{ 
  document.writeln("Account has been created <br>");
  document.writeln("Your Username is:" + user);
  document.writeln("<br>Your Password is:" + pass);
    }
    

}
   

