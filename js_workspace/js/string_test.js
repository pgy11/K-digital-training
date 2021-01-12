let str = 'Hello JavaScript';
console.log(`${str}의 길이 : ${str.length}`);
console.log(`인덱스 2에 해당하는 ${str}의 문자 : ${str.charAt(2)}`);
console.log(`${str}의 l의 인덱스 ${str.indexOf('l')}`);
console.log(`${str}의 l의 인덱스를 오른쪽부터 찾습니다. 결과 : ${str.lastIndexOf('l')}`);

// includes()는 ECMA5부터 지원
console.log(`${str}은 Hello를 포함합니까? 결과 : ${str.includes('Hello')}`);
console.log(`${str}의 인덱스 2부터 인덱스7까지의 문자들은 ${str.substring(2,7)}`);
console.log(`인덱스 2부터 시작해서 5개의 문자 출력하기 : ${str.substr(2,5)}`);
