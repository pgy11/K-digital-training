// 오름차순 정렬
let info = [45, 11, 7, 32, 20, 19];
info.sort(function(a, b){
    return a - b;
});

console.log(info);

// 내림차순 정렬
info.sort(function(a,b){
    return b - a;
});

console.log(info);

info = ['apple', 'banana', 'grape'];
console.log(info);

info.pop();
console.log(info);

info.push('tomato');
console.log(info);

info.shift();
console.log(info);

info.unshift('Snake');
console.log(info);

/**
 * splice()은 수정, 삭제
 * splice()는 배열 내부를 직접 바꾼다.
 * 
 */
info.splice(1,0,'f')
console.log(info);

info.splice(1,1);
console.log(info);

info.splice(0, 3, ['A', 1, true]);
console.log(info)

// filter은 조건에 맞는 아이템 추출
// filter 함수의 매개변수로 함수가 들어가서 
// filter 함수가 호출되면 매개변수에 있는 함수가 자동적으로 실행되는 이를 call back 메소드라고한다.
info = ['apple', 'banana', 'kiwi', 'tomato', 'cup'];
let k = info.filter(item => item.length > 5);
console.log(k);

// foreach -> 배열 아이템 조회

// map -> 배열 아이템을 조작 할 때 사용
const arr = [1,3,5,7];

const res = arr.map(x => x + '0');
console.log(res)

info = ['a', 'b', 'c', 'd', 'e'];
let removed = info.splice(0, 2, 'w', 'y', 'z');
console.log(removed);
console.log(info);

info = ['a', 'b', 'c', 'd', 'e'];
info.reverse();
console.log(info);

info = ['a', 'b', 'c', 'd', 'e'];
console.log(info.slice(2));
console.log(info.slice(0,3));

console.log(info.join(''));
console.log(info.join('-'));
console.log(info.toString());

// find vs filter
// find()은 단순 검색
// filter()은 조건에 맞는 아이템을 검색