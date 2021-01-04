function solve(num) {
    let numToString = num.toString();
    let current = numToString[0];
    let result = true;
    let sumOfAllDigits = 0;

    for (i=0; i < numToString.length; i++) {
        sumOfAllDigits += Number(numToString[i])
        if (current !== numToString[i]) {
            result = false;
        }
    }
    return [result, sumOfAllDigits].join('\n')
}

// console.log(solve(2222222))
// console.log(solve(1234))
