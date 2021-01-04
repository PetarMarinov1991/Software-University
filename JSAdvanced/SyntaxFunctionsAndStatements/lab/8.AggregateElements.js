function solve(args) {
    let sumOfArray = 0;
    let invertedValues = 0;
    let concatenatedValues = '';

    for (i=0; i < args.length; i++) {
        sumOfArray += args[i]
        invertedValues += (1 / args[i] * -1) * -1;
        concatenatedValues += args[i].toString();
    }

    return [sumOfArray, invertedValues, concatenatedValues].join("\n");
}

// console.log(solve([1, 2, 3]));
// console.log('')
// console.log(solve([2, 4, 8, 16]));
