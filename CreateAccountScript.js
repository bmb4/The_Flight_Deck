var MongoClient = require('mongodb').MongoClient;


const dbpassword = process.env.DB_PASSWORD;
const url = "mongodb+srv://bmb4:"+dbpassword+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority";
var client = new MongoClient(url);

async function AddAccount(){ 
/* var user = document.getElementById("myform").elements.namedItem("username").value;
 var pass = document.getElementById("myform").elements.namedItem("password").value;
 var conpass = document.getElementById("myform").elements.namedItem("password_confirm").value;*/
 var user = "test2" 
 var pass = "test"
 var conpass = "test"
  try {
    await client.connect();
    
    const database = client.db("DB");
    const db = database.collection("Test");
    console.log("creating account..")
    // create a document to insert
    const doc = {
      Username: user,
      Password: pass,
    }
    const find =  await db.find({"Username":user}).count()
    if(find == 0){
    var v = CheckAcc(user,pass,conpass);
    if(v == true){
    const result = await db.insertOne(doc);
    console.log(`A document was inserted with the _id: ${result.insertedId}`);
    }
  }
  else{
    
    console.log("Account Already exists");
  }
  } finally {
    await client.close();
  }
}

async function FindAccount(username){ 

    try {
      await client.connect();
      
      const database = client.db("DB");
      const db = database.collection("Test");
      console.log("looking for account..")
      // create a document to insert
      const doc = {
        Username: username,
      }
      const result = await db.findOne(doc);
      console.log(result);
    } finally {
      await client.close();
    }
  }

AddAccount().catch(console.dir);

/*  function CreateAcc(){
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
   
}  */

function CheckAcc(username,password,password2){
  var x = true;
   if(username == ""){
      alert("Please Enter Username");
      x = false;
 }
 if(password == ""){
     alert("Please Enter Password");
     x = false;
}
if(password != password2){
 alert("Passwords do not match");
 x =  false;
}
 return x
} 