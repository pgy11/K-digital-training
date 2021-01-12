// 1. 조건문

// 1.1 if, else if, else
let month = prompt('월 입력', '');

if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) console.log(`${month}월은 31일까지 있습니다.`);
else if(month == 4 || month == 6 || month == 9 || month == 11) console.log(`${month}월은 30일까지 있습니다.`);
else if(month == 2) console.log(`${month}월은 28일까지 있습니다.`);
else console.log('입력 오류');

// 1.2 switch
month = prompt('월 입력', '');

switch(month){
    case '1':
    case '3':
    case '5':
    case '7':
    case '8':
    case '10':
    case '12':
        console.log(`${month}월은 31일까지 있습니다.`);
        break;
    
    case '2':
        console.log(`${month}월은 28일까지 있습니다.`);
        break;
    
    case '4':
    case '6':
    case '9':
    case '11':
        console.log(`${month}월은 30일까지 있습니다.`);
        break;
    
    default:
        console.log('입력 오류');
}

// 2. 반복문
// 2.1 while
// 초기값이 필요하다.
// 반복문을 중간에 벗어나고 싶으면, 조건식을 넣고 만족하면 break문을 사용한다.
/* 
초기값;
while(조건식){
    실행내용;
    증감식;
}
*/

let index = 1;
let sum = 0;

while(index < 11){
    sum += index; // sum = sum + index;
    index++; //index = index + 1;
    /*
    먼저 변수를 증가시키고 연산하려면 ++index;
    연산을 하고나서 변수를 증가시키려면 index++;
    * */
}

console.log(`1~10의 합 : ${sum}`);


// 2.2 do-while
/*
초기값;
do{
    실행내용;
    증감식;
}while(조건식)
* */

index = 0;
sum = 0;

do{
    sum += index;
    index += 1;
}while(index < 11);

console.log(`1~10의 합 : ${sum}`);

// 2.3 for
/*
for(초기값; 조건식; 증감식){
    실행문;
}

for(데이터 in|of 리스트데이터){
    실행문;
}
* */

sum = 0

for(index = 1; index <11; index++){
    sum += index;
}

console.log(`1~10의 합 : ${sum}`);

// 2.4 return, break, continue
// 2.4.1 return
// return은 함수를 종료 할 때 사용 - 나중에 배움
// 2.4.2 break
// 반복문을 중간에 벗어나고 싶을 때 조건식을 이용하여 사용
sum = 0

for(index = 1; index < 11; index++){
    if(index == 5) break;
    sum += index;
}
console.log(`결과 : ${sum}`);

// 2.4.3 continue
// 반복문의 일부분만을 실행하고 싶을 때 조건식을 이용하여 사용
sum = 0;
for(index = 1; index < 11; index++){
    if(index % 2 == 0) continue;
    sum += index;
}

console.log(`결과 : ${sum}`);

// 반복문을 중첩하여 구구단 만들기
for(num = 2; num < 10; num++){
    for(k = 1; k < 10; k++){
        console.log(`${num} x ${k} = ${num * k}`);
    }
    console.log('\n');
}
