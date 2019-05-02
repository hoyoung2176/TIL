// 배열로 이루어진 숫자들을 모두 더하는 함수
// var numbers = [1, 2, 3, 4, 5,]
// const numbersAddEach = numbers => {
//     let sum = 0
//     for ( const number of numbers) {
//         sum += number
//     }
//     return sum

// }
// numbersAddEach(numbers)
// console.log(numbersAddEach(numbers))

// // 배열로 이루어진 숫자들을 모두 빼는 함수
// const numbersSubEach = numbers => {
//     let sub = 0
//     for (const number of numbers) {
//         sub -= number
//     }
//     return sub

// }

// console.log(numbersSubEach(numbers))
// // 배열로 이루어진 숫자들을 모두 곱하는 함수

// const numbersMulEach = numbers => {
//     let mul = 1
//     for (const number of numbers) {
//         mul *= number
//     }
//     return mul

// }
// console.log(numbersMulEach(numbers))

// // 숫자로 이루어진 배열의 요소들은 각각 [??] 한다. [??] 안에 쓸말은 알아서 해라
// const numbersEach = (numbers, callback) => {
//     let acc
//     for (const number of numbers) {
//         acc = callback(number, acc) // [??] 한다. == callback
//     }
//     return acc
// }

// //더한다.
// const addEach = (number, acc = 0) => {
//     return acc + number
// }
// numbersEach(numbers, addEach)
// console.log(numbersEach(numbers, addEach))
// //뺀다.
// const subEach = (number, acc = 0) => {
//     return acc - number
// }
// numbersEach(numbers, subEach)
// console.log(numbersEach(numbers, subEach))
// //곱한다.
// const mulEach = (number, acc = 1) => {
//     return acc * number
// }
// numbersEach(numbers, mulEach)
// console.log(numbersEach(numbers, mulEach))

// 변수를 정의할 때 일단 상수로 만든 후, 곰곰이 생각후 정말 재할당이 필요할 경우 변수(let)으로 바꾸어쓴다.

// numbersEach 이후의 제어들을 우리가 함수 정의 없이 매번 자유롭게 하려면?
const NUMBERS = [1, 2, 3, 4, 5,]
const numbersEach = (numbers, callback) => {
    let acc
    for (let i =0; i < numbers.length; i++) {
        number = numbers[i]
        acc = callback(number, acc)
    }
    return acc
}

// 이렇게 익명함수(1회용)를 쓴다!
console.log(numbersEach(NUMBERS, (number, acc = 0) => acc + number), numbersEach(NUMBERS, (number, acc = 0) => acc - number), numbersEach(NUMBERS, (number, acc = 1) => acc * number))

