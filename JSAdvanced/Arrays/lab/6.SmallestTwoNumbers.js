function smallestTwoNumbers(args) {
    let min = Math.min.apply(null, args)
    let secondMin = Math.min.apply(null, args.filter(n => n != min))

    if (secondMin === Infinity) {
        secondMin = min
    }
    if (args.length == 1) {
        return `${min}`
    }
    
    return `${min} ${secondMin}`
}

// console.log(smallestTwoNumbers([30, 15, 50, 5]))
// console.log(smallestTwoNumbers([3, 0, 10, 4, 7, 3]))
// console.log(smallestTwoNumbers([3]))