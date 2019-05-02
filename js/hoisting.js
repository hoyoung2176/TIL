// let 블록 스코프 예제
// {
//     let x = '정운지'
//     console.log(x)  // 정운지
//     {
//         let x = 1
//         console.log(x)  // 1
//     }
//     console.log(x)  // 정운지
// }
// console.log(typeof x)  // undefined

// var로 선언하면 현재 스코프(유효범위) 안이라면 어디서든 사용할 수 있으며, 심지어 선언하기도 전에 사용할 수있다.
// 전역 변수의 오염
// let 으로 선언하면 그 변수는 선언하기 전에는 존재하지 않는다.
// 선언되지 않은 변수(에러O) !== undefined 변수(에러X)

// let foo
// let bar = undefined

// foo // undefined
// bar // undefined

// baz // ReferenceError baz is not defined

// // ReferenceError x is not defined
// x
// let x = 1

// // 변수를 선언하지도 않았는데 그 변수에 접근할 수 있다는 특이한 현상이 발생
// y
// var y = 1
// y

// // JS 가 이해한 코드
// var y
// y   // undefined
// y = 1   // 1
// y   // 1

if (x !== 1) {
    console.log(y)  //undefined
    var y = 3
    if (y === 3) {
        var x = 1   
    }
    console.log(y)  // 3
}
if (x === 1) {
    console.log(y)  // 3
}

// var 로 변수를 선언하면 JS는 같은 변수를 여러번 정의하더라도 무시한다.
var x = 1
if (x===1) {
    var x = 2
    console.log(x)  // 2
}
console.log(x)  // 2
// JS가 이해한것
var x
x = 1
if (x === 1) {
    x = 2
    console.log(x)
}
console.log(x)

// 함수 호이스팅
// ssafy 함수가 선언되기 전에 ssafy() 로 호출된 형태
ssafy()
function ssafy() {
    console.log('hoisting!!')
}

// 변수에 할당한 함수는 호이스팅 되지 않는다.
ssafy() // 명시적 호출
let ssafy = function () {
    console.log('hoisting!!')
}

