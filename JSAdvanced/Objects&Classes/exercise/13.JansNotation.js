function solve(input) {
    let arr = []
    
    input.forEach(element => {
        if (typeof element === 'number') arr.push(Number(element)) 
        else doMath(arr, element)
    })

    return arr.length >= 2 ? 'Error: too many operands!' : arr.toString()

    function doMath(numbers, operator) {
        let idx1 = numbers.length - 2
        let idx2 = numbers.length - 1

        if (numbers.length < 2) console.log('Error: not enough operands!')
        else if (operator === '+') numbers[idx1] += numbers[idx2]
        else if (operator === '-') numbers[idx1] -= numbers[idx2]
        else if (operator === '*') numbers[idx1] *= numbers[idx2]
        else if (operator === '/') numbers[idx1] /= numbers[idx2]
        numbers.splice(-1, 1)
    }
}
