let z=20;
console.log(typeof(z))
let name1="sai";
console.log(typeof(name1))
let b=true;
console.log(typeof(b))
     
x=10
y=20
console.log(x+y)

num1=20
num2=30
console.log(num1*num2)

a=40
b=20
console.log(a-b)

let num3=2
let num4=4
console.log(num3/num4)  


let age=2  

if (age>18){
  console.log(" eligible for vote")
}else if(age<17){
    console.log("not eligible for vote")
}else{
console.log("last chance for vote")  
}

//for loop
// initialize, condition, increment

for(let i=1;i<6;i++){
    console.log("hi",i)
}  

//do while loop

let num=0
 do{
    console.log(num);
    num++; 

}while(num<10);



let istrue=true;
let isfalse=false;

if(istrue!=isfalse){
    console.log("both condition is true")
}
else{
    console.log("one is false")
}


{
let a1=10
let b2=20
if(a1==b2)
    console.log('both are equal')
else
    console.log('both are not same')}
{
 let a1=10
let b2=20
if(a1!=b2)
    console.log('both are not equal')
else
    console.log('both are equal same')
 
}

//array

let array=[20,30,40,50,'sai','nani']

console.log(array)

console.log(array.length)

let myarray=[30,35,36,"bobby"]
let myarray1=[4, 3,5,36,"sumi"]

let newarray=myarray.concat(myarray1)

console.log(newarray)


//function

function namebro(){
   console.log("what is your name : sandeep")
}
namebro(); 



let array1=[20,30,40,50,60]
console.log(array1.length) //length

let array2=[11,12,13,14,15]
array2.pop() //pop
console.log(array2)

let array6=[23,24,25,26,27]
console.log(array6.indexOf(25)) //index

let array7=[240,41,42,43,230]
array7.shift() //shift
console.log(array7)

let array8=[240,250,260,270,280]
array8.unshift(400) //unshift
console.log(array8)

let array3=array1+array2
console.log(array3)

let array10=[380,340,235,456,123]
console.log(array10.slice(0,2)) //slice  

let arraysum=["sumi",10,20,30]
console.log(arraysum.reverse()) //reverse

let array40=[20,30,40,50]
array40.push("raju")
console.log(array40) //push
 
       //function

function person(name,age,role,greet){
    this.name=name
    this.age=age
    this.role=role
    this.greet=greet

    this.greet=function(){
        return("hello")
    }
}

const person1=new person("sai",23,"web developer")
const person2=new person("nani",24,"developer")

console.log(person1.name,person1.age,person1.role,person1.greet())
console.log(person2.name,person2.age,person2.role,person2.greet())






