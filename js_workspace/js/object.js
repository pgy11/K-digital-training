// class : object를 생성하기 위한 template, type(요구사항을 추상화해서 속성과 기능을 표현한 템플릿)
// object : class type으로 생성된 변수(클래스를 예약어 new, 생성자를 객체를 만든다.)
// 간단한 설명
// 관례는 첫문자는 대문자로 쓴다.
// 현실세계 -> 프로그래밍 세계
// 복잡한 현실세계를 프로그래밍 세계로 변환할 때 요구사항을 단순화한다.(추상화)
/* 
ex) 
현실세계              -------->      프로그래밍 세계
자동차의 속성, 기능     추상화          Car(class)
                                      속성 : name, color, cc (attribute)
                                      기능 : run(), stop() (operation)

class를 메모리에 띄우는 것을 instance화, 
{사용방법}
// myCar은 객체
Car myCar = new Car(); // 생성자를 통해 속성 값 초기화
myCar.name = 'Hyundai';
myCar.color = 'black';
myCar.cc = 3000;

myCar.run();
*/


// 1. class 선언(ECMA6 - 예약어 class 사용가능)
/**
 * class 클래스명{
 *  변수;
 *  메소드; 
 * }
 * 
 */

/**
 * 접근제한자는 ECMA7부터 지원하지만 브라우저에서 지원을 안 할 수도있다.
 * 따라서 set, get을 이용해 캡슐화를 시도하는 방법이있다.(e.g. 멤버변수 조작)  
 */
class Person{
    name = '';
    age = 0;

    constructor(name, age){
        this.name = name;
        this.age = age;
    }

    print(){
        console.log(`이름 : ${this.name}, 나이 : ${this.age}`);
    }

    // computed 
    get birthYear(){
        return 2021 - this.age + 1;
    }

    // action
    set birthYear(year){
        this.age = 2021 - year + 1;
    }
}

let p = new Person('Gil-dong', 26);
p.print();
//p.birthYear(1997) // error, not a function - Type error
p.birthYear = 1997; // set을 이용해 값을 줄 때는 대입연산자를 이용한다.
console.log(`${p.name}는 ${p.birthYear} 출생`);


// 2. function 객체로 선언
function Student(name, age, major){
    this.name = name;
    this.age = age;
    this.major = major;

    this.print = function(){
        console.log(`이름 : ${this.name}, 나이 : ${this.age}, 전공 : ${this.major}`); 
    }
}

// 이렇게 사용하기도 한다.
// 이전에는 JS는 구조적으로 프로그래밍 하였음
// Student.prototype.print : function(){
//
//}

let s = new Student('John', 22, 'CS');
s.print();

// 3. JSON(JavaScript Obejct Notation)
// JSON은 데이터 교환 할 때 사용한다.
let e = {
    name : 'Mike',
    age : 28,
    department : 'Lab'
};

// JSON의 value 값은 다양한 자료형(object, array, number, string, boolean)이 올 수 있다.
let w = {
    person : {name : 'Gil-dong', age : 22},
    department : 'Lab',
    items : [1,2,3,4],
    male : true
};
console.log(e);

// 참고
// 배열안에 있는 다양한 자료형이 올 수 있다.
let array = [{name : 'Min-soo', age :28}, 1, 'js', false];