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
