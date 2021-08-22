var name = 'Abdi'

function changeName(){
    name ='Ahmed'
}
changeName()
console.log(name) //Abdi

{
    let name = 'Abdi'
}
function changeName(){
    var name = 'Ahmed'
}
changeName()
console.log(name) //undefined


const name // Syntax Error
const name = 'Abdi';

const person ={}
pesrson.name = 'Abdi';
console.log(person); // { name: 'Abdi' }

const person = Object.freeze({});
person.name = 'Abdi';
console.log(person); // {}

"use strict"
const person = Object.freeze({});
person.name = 'Abdi';
console.log(person); // TypeError: Cannot add property name, object is not extensible

function asycTask(){
    var promises = new Promise ((resolve, reject)=>{
        setTimeout(()=>{
            console.log("Action complete");
            resolve();
        },1000);
    });
    return promises;
}

function asycTask(){
    var promise = new Promise((resolve,reject)=>{
        setTimeout(()=>{
            try{
             console.log("Action complete");
             resolve();
            }catch(err){
              reject();
            }
        },1000);
    });
    return promise;
}
asycTask().then(()=>{console.log('Event was successful')},()=>{console.log('Event failed')},)


