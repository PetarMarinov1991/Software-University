function biggestElement(args) {
    numbers = []
    for (const i in args) {
        numbers.push(Math.max.apply(null, args[i]))
    }
    return Math.max.apply(null, numbers)
}

// console.log(biggestElement(
//     [
//         [20, 50, 10], 
//         [8, 33, 145]
//     ]
//     ))
// console.log(biggestElement(
//     [
//         [3, 5, 7, 12],
//         [-1, 4, 33, 2],
//         [8, 3, 0, 4]
//     ]
//    ))
