var MongoClient = require('mongodb').MongoClient;
const dbpassword = process.env.DB_PASSWORD;
const uri = "mongodb+srv://bmb4:"+dbpassword+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority";



 function CreateAcc(){
     console.log("creating account..")
    var user = document.getElementById("myform").elements.namedItem("username").value;
    var pass = document.getElementById("myform").elements.namedItem("password").value;
    var conpass = document.getElementById("myform").elements.namedItem("password_confirm").value;
   /*   if(user == ""){
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
    } */
     MongoClient.connect(uri, function(err, DB) {
        if (err) throw err;
        // db pointing to newdb
        
        // document to be inserted
        var doc = { name: "josh", password: "josh" };
            
        // insert document to 'users' collection using insertOne
        DB.collection("Test").insertOne(doc, function(err, res) {
            if (err) throw err;
            console.log("Document inserted");
            // close the connection to db when you are done with it
            DB.close();
        });
    });

} 


