function processOddNumbers(args) {
    let result = []
    for (i=1; i < args.length; i+=2) {
        result.push(args[i] * 2)
    }
    return result.reverse().join(' ')
}

// console.log(processOddNumbers([10, 15, 20, 25]))
// console.log(processOddNumbers([3, 0, 10, 4, 7, 3]))