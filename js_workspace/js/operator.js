// 연산자
// 1. 산술연산자 : +, -, *, /, %
let x = 10;
let y = 20;

console.log(x, '+', y, '=', x+y);
console.log(`${x} + ${y} = ${x+y}`);
console.log(`${x} - ${y} = ${x-y}`);
console.log(`${x} * ${y} = ${x*y}`);
console.log(`${x} / ${y} = ${x/y}`);
console.log(`${x} % ${y} = ${x%y}`);
console.log(`${x}`);

// 2. 대입연산자 : =
const z = x + y;
console.log(z);

// 3. 비교연산자 : >, <, >=, <=, ==, !=, ===
let w = x > y
console.log(`${x<y}`);
console.log(`${x!=y}`);
console.log(`ssno${10 === '10'}`); // ===은 숫자 문자 비교

// 4. 논리연산자 : &&, ||, !
console.log(`${x!=y && x==y}`);
console.log(`${x!=y || x==y}`);
console.log(`${!(x==y)}`);

// 5. 비트연산자 &, |, ^, ~, >>, <<
console.log(`${x&y}`);
console.log(`${x^y}`);

// 6. 삼항연산자 : 조건? 참 : 거짓
x == y? console.log(`${x} == ${y}`): console.log(`${x} != ${y}`);

// 7. type check
console.log('type ',typeof intV, typeof floatV, typeof booleanV, typeof stringV);

let p = 7;
let q = 5;
p < q? q = 3 : q = 10;
console.log(typeof p);
p = 's'
console.log(typeof p);
p = true;
console.log(typeof p);

var nn = 7;
console.log(nn);