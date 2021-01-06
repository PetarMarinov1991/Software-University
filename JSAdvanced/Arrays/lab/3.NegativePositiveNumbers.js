function negativePositiveNumbers(args) {
    let result = []
    for (i=0; i < args.length; i++) {
        let num = args[i]
        if (num >= 0) {
            result.push(num)
        } else {
            result.unshift(num)
        }
    }
    return result.join('\n')
}

// console.log(negativePositiveNumbers([7, -2, 8, 9]))
// console.log(negativePositiveNumbers([3, -2, 0, -1]))