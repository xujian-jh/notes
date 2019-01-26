阅读笔记：设计模式是软件设计中常见问题的可重用解决方案。推荐  [Learning JavaScript Design Patterns](https://addyosmani.com/resources/essentialjsdesignpatterns/book)。注意：示例基本基于 ES6 。

# 创建型模式（Creational patterns）：专注于优化新对象创建。

- 构造函数（Constructor pattern）
```
class Car { 
    constructor(model, year, miles){ 
        this.model = model; 
        this.year = year; 
        this.miles = miles 
    } 
    toString(){ 
        return this.model + " has done " + this.miles + " miles"; 
    } 
} 

// Usage
let civic = new Car( "Honda Civic", 2009, 20000 ); 
let mondeo = new Car( "Ford Mondeo", 2010, 5000 ); 
 
console.log( civic.toString() ); 
console.log( mondeo.toString() ); 
```
- 原型模式（Prototype pattern）
```
class Animal { 
    constructor(name) { 
        this.speed = 0; 
        this.name = name; 
    } 
    run(speed) { 
        this.speed += speed; 
        alert(`${this.name} runs with speed ${this.speed}.`); 
    } 
    stop() { 
        this.speed = 0; 
        alert(`${this.name} stopped.`); 
    } 
} 

// Inherit from Animal 
class Rabbit extends Animal { 
    hide() { 
        alert(`${this.name} hides!`); 
    } 
} 

// Usage
let rabbit = new Rabbit("White Rabbit"); 
rabbit.run(5); // White Rabbit runs with speed 5. 
rabbit.hide(); // White Rabbit hides!
```
- 模块模式（Module pattern）
```
// car.js 
class Car { 
    constructor(model, year, miles){ 
        this.model = model; 
        this.year = year; 
        this.miles = miles 
    } 
    toString(){ 
        return this.model + " has done " + this.miles + " miles"; 
    } 
} 
export default Car 

// main.js 
import Car from './car.js' 
let civic = new Car( "Honda Civic", 2009, 20000 ); 
let mondeo = new Car( "Ford Mondeo", 2010, 5000 ); 

console.log( civic.toString() ); 
console.log( mondeo.toString() );
```
- 单例模式（Singleton pattern）：用于将对象限制为单个实例的模式。如果该对象不存在，单例将创建对象的实例。如果存在，则返回现有实例。
```
class Car { 
    constructor(model, year, miles){ 
        if(Car.exists){ 
            return Car.instance 
        } 
        this.model = model; 
        this.year = year; 
        this.miles = miles; 
        Car.exists = true; 
        Car.instance = this; 
        return this 
    } 
    toString(){ 
        return this.model + " has done " + this.miles + " miles"; 
    } 
} 

// Usage: 
let civic = new Car( "Honda Civic", 2009, 20000 ); 
let mondeo = new Car( "Ford Mondeo", 2010, 5000 ); 

console.log( civic.toString() ); // Honda Civic has done 20000 miles 
console.log( mondeo.toString() ); // Honda Civic has done 20000 miles
```
- 工厂模式（Factory pattern）：通过提供接口来抽象对象，可以在其中指定要创建的工厂对象的类型。
```
// A class for defining new cars
class Car {
    constructor(doors, state, color) {
        this.doors = doors || 4;
        this.state = state || "brand new";
        this.color = color || "silver";
    }
    props(){
        return `I am a ${this.state} ${this.color} car and I have ${this.doors} doors`
    }
}

// A class for defining new trucks
class Truck {
    constructor(state, wheelSize, color) {
        this.state = state || "used";
        this.wheelSize = wheelSize || "large";
        this.color = color || "blue";
    }
    props(){
        return `I am a ${this.state} ${this.color} truck and I have a ${this.wheelSize} wheels`
    }
}

// Define a factory
class VehicleFactory {
    constructor(options) {
        let vehicle;
        switch (options.type) {
            case "car":
                vehicle = new Car(options.doors, options.state, options.color)
            break;
            case "truck":
                vehicle = new Truck(options.state, options.wheelSize, options.color);
            break;
        }
        return vehicle;
    }
}

// Usage
let options1 = {
    type: "car",
    color: "yellow",
    doors: 6
}
let options2 = {
    type: "truck",
    state: "like new",
    color: "red",
    wheelSize: "small"
}

let car = new VehicleFactory(options1);
let truck = new VehicleFactory(options2);

console.log(car.state) // brand new
console.log(car.color) // yellow
console.log(car.props()) // I am a brand new yellow car and I have 6 doors
console.log(truck.state) // used
console.log(truck.color)// red
console.log(truck.props())// I am a used red truck and I have a small wheels
```

# 结构型模式（Structural patterns）：涉及如何组成对象并简化不同对象之间的关系。

- 装饰模式（Decorator）：专注于向类添加新功能。
```
// The constructor to decorate
class MacBook {
    cost () {
        return 997;
    };
    screenSize () { 
        return 11.6; 
    };
}

// Decorator 1
function macbookDecorator1(macbook){
    macbook.discount = function(){
        return macbook.cost() * 0.1
    }
    return macbook;
}

// Decorator 2
function macbookDecorator2( macbook ) {
    var v = macbook.cost();
    macbook.cost = function() {
        return v + 75;
    };
    return macbook;
}

// usage
const decorator1 = macbookDecorator1(new MacBook());
console.log(decorator1.cost()); // 997
console.log(decorator1.discount()); // 99.7

const decorator2 = macbookDecorator2(new MacBook());
console.log(decorator2.cost()); 1072
```
- 外观模式（Facade）：简化界面，隐藏底层代码的复杂性。
```
class TaskService {
    constructor(data){
        this.name = data.name;
        this.priority = data.priority;
        this.project = data.project;
        this.user = data.user;
        this.completed = data.completed;
    }
    complete() {
        this.completed = true;
        console.log('completing task: ' + this.name);
    }
    setCompleteDate() {
        this.completedDate = new Date();
        console.log(this.name + ' completed on ' + this.completedDate);
    }
    notifyCompletion() {
        console.log('Notifying ' + this.user + ' of the completion of ' + this.name);
    }
    save () {
        console.log('saving Task: ' + this.name);
    }
}

class TaskServiceFacade extends TaskService{
    constructor(data){
        super(data)
    }
    completeAndNotify(){
        this.complete();
        this.setCompleteDate();
        this.notifyCompletion();
        this.save();
    }
}

let mytask = new TaskServiceFacade({
    name: 'MyTask',
    priority: 1,
    project: 'Courses',
    user: 'Jon',
    completed: false
})

console.log(mytask.completeAndNotify())
// completing task: MyTask
// MyTask completed on Sun Jan 06 2019 09:54:33 GMT+0100 (West Africa Standard Time)
// Notifying Jon of the completion of MyTask
// saving Task: MyTask
```
- 享元模式（Flyweight）

# 行为型模式（Behavioral patterns）：涉及对象之间的责任分配以及对象如何通信。

- 中间人模式（Mediator）
- 观察者模式（Observer）
- 命令模式（Command）