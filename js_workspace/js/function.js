// 1. 함수
// javascript은 1급 함수; 함수를 객체 취급함
/* 
[]은 생략가능
정의 : function 함수명([parameter1, parameter2, ...]){
    실행내용;
    [return data;]
}
호출 : let data = 함수명([parameter1, parameter2, ...])
// paramter, return 값으로 함수를 사용 할 수 있다.
//====

let functionV = function([parameter1, parameter2, ...]){
    실행내용;
    [return data;]
}
위에서 functionV는 함수객체가 된다.
*/
// arrow function : ([parameter1, parameter2, ...]) =>{실행내용; [return data;]}


// 함수 정의
function add(x, y){
    return x + y;
}

// 함수 호출
let sum = add(10, 20);
console.log(`add(10, 20) = ${sum}`);
sum = add(10, '30');
console.log(sum);

// 익명 함수 함수를 객체에 할당
// subtract은 객체 타입(타입 명은 function)
let subtract = function(x,y){
    return x-y;
}

console.log(`subtract(10, 20) : ${subtract(10, 20)}`);
console.log(typeof subtract);
console.log(subtract)

// arrow function, 람다식
subtract = (x,y) => {return x- y};
console.log(subtract(5,5))
let division = (x, y) => console.log(`divide(${x}, ${y}) : ${x/y}`);
division(10,20);
division(30, 10);


// 함수선언 및 실행
// 선언을 하고나서 필요할 때 사용하는 것이 아닌 선언 직후 바로 호출된다.
// 이후 다른 곳에서 사용 할 수 없다. -> 한번 만 사용 할 수 있음
let multiply = ((x,y) => {console.log(`${x} x ${y} = ${x*y}`)})(20,10);

// 클로저
// 함수에서 다른 함수를 리턴
function makeAdder(x){
    let y = 1; // makeAdder 함수의 지역 변수
    return function(z){ // 반환되는 함수는 클로저 함수가 된다.
        y = 100; // 외부 함수에 있는 지역변수 사용(x, y)
        return x + y + z;
    }
}

let add5 = makeAdder(5);
let add10 = makeAdder(10);
console.log(add5);
console.log(add5(2));
console.log(add10(2));

function multi(n){
    return function(){
        return n *= n; 
    }
}

let multi5 = multi(5);
let multi10 = multi(10);
console.log(typeof multi5);
console.log(typeof multi10);
console.log(`multi5() : ${multi5()}`);
console.log(`multi10() : ${multi10()}`);

// 클로저 사용 시 주의 사항
// 클로저 함수에서 변수를 만들 때, 함수 밖의 변수명을 고려해야한다. 

// 재귀함수
// 함수가 자기자신을 호출
// 종료점이 필요하다.

function fact(n){
    if(n == 1){
        return 1;
    }
    return n * fact(n-1);
}

let k = fact(4);
console.log(k);

function add(x, y=7){
	return x + y;
}

console.log(add(4)); // 11

function displayInfo(name, food, eat = name + ' eats ' + food){
	console.log(eat);
}

displayInfo('Gil-dong', 'apple');

function subtract_(x, y){
	return x - y;
}

function callSubFunc(f){
	return f;
}

console.log(callSubFunc(subtract_(7,6)));


function getNumPlusOne(yy){
    return yy;
}

let tt;
console.log(getNumPlusOne(tt));


console.log(
	function(){
		return 'hello js';
	}()
);

res = function(x, y){
    return x + y;
}(7, 8);

console.log(res); // res === 15

// 익명 함수
let res1 = function(x, y){
    return x + y;    
}(4, 8);

// 람다식
let res2 = ((x, y) => {
    return x + y;	
})(4,4);

console.log(res1);
console.log(res2);

(function(){
    console.log('hello js');
})();

let total;
(function(x, y){
    total = x * y;
})(4,2);

console.log(total);

(function(x, y){
    console.log(x + y);
    return x + y;
})(4,2);


total = ((x,y,z) =>{
    return x + y + z;
})(1,2,3);

console.log(total);

(function(){
    console.log('hello js');
})();

(()=>{
    console.log('hello js');
})();

((x,y,z) => {
    k = 56
    console.log(k);    
})(1,2,3);

(()=>{
    console.log('ss');
})();

z = ((x)=>{
    return x+1;
})(1);

console.log(z);

k = ((x) => {
    return x + 1;
})(5);

console.log(k); // k === 6

(() => {
    console.log('Hello js');    
})();