function solve(start, ...rest) {
    let num = parseInt(start);
    let result = [];

    for (i=0; i < rest.length; i++) {
        let operation = rest[i];
        if (operation == 'chop') {
            num /= 2;
        } else if (operation == 'dice') {
            num = Math.sqrt(num)
        } else if (operation == 'spice') {
            num += 1
        } else if (operation == 'bake') {
            num *= 3
        } else if (operation == 'fillet') {
            num *= 0.8
        }
        result.push(num.toFixed(1));
    }
    return result.join('\n')
}

// console.log(solve(['32', 'chop', 'chop', 'chop', 'chop', 'chop']))
// console.log(solve(['9', 'dice', 'spice', 'chop', 'bake', 'fillet']))
