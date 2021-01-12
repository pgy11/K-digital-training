// 1. var, let(ECMA6, 권장), const
// var x;
// 값을 할당하는 시점에 변수의 타입을 결정
// 아래는 문자 x는 '6'을 저장
// 이 방법은 규모가 커질 수록 좋지 않음
// var은 변수의 유효범위 구분이 안된다. 따라서 let을 사용.
// const는 상수고 변경이 불가 (e.g. 서버로부터 받은 데이터) - read only

const constVariable = 10;

x = 6;
x = '6';
let globalVariable = 5;
{
    let localVariable = 5;
    var y = 5;
    console.log('localVariable ', localVariable);
    console.log('globalVariable', globalVariable);
    console.log('var x ', x);
    console.log('var y ', y);
    console.log('const ', constVariable);

}

constVariable = 7; // error
console.log("const", constVariable);

// console.log('localVariable ', localVariable); // error
console.log('globalVariable', globalVariable);
console.log('var x ', x);
console.log('var y ', y);

document.getElementById("data").innerHTML = "<h3>variable x = " + x + "</h3>";


// 2. DataType - primitive(int, float, string, boolean), Reference(Class, Array)
// string + 숫자를 값에 할당하면, string + string(숫자)가 되어 문자열 이어 붙이기가 된다.
// string / 숫자를 하면 몫을 리턴한다.
let intV = 10;
let floatV = 10.5;
let stringV = '10';
let booleanV = true;
console.log('data type ', intV, floatV, stringV, booleanV);

// 3.