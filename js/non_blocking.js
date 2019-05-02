// const nothing = () => {}

// console.log('start sleeping')
// setTimeout(nothing, 3000)   // non-block callback stack에서 3초동안 실행중이다.
// console.log('end of program')
// // non-blocking
// // 해당 함수의 시작이후 종료될때까지 기다리지 않고 바로 다음줄의 코드를 실행하는 것을 의미
// // 코드의 실행을 막지 않는다.


// // python code 처럼 동작하게 하려면
// const logEnd = () => {
//     console.log('end of program')
// }
// console.log('start sleeping')
// setTimeout(logEnd, 3000)


// function first() {
//     console.log('first')
// }
// function second() {
//     console.log('second')
// }
// function third() {
//     console.log('third')
// }
// first()
// setTimeout(second, 1000)
// third()

// 이벤트 루프
// 시간의 흐름에 따라 코드의 수행을 처리, 그 때마다 JS 엔진을 작동 시킴

// func1() 를 호출했을때 아래와 같이 콘솔에 출력
// func1
// func3
// func2
function func3() {
    console.log('func3')
}
function func2() {
    setTimeout(() => console.log('func2'), 0)
    func3()
}
function func1() {
    console.log('func1')
    func2()
}



func1()