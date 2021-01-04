function squareOfStars(a) {
    if (typeof(a) === 'undefined'){
        a = 5;
    }

    let result = '';

    for (let i=0; i < a; i++) {
        result += '* '.repeat(a) + '\n'
    }

    return result;
}

// console.log(squareOfStars());
// console.log(squareOfStars(2));
// console.log(squareOfStars(3));
// console.log(squareOfStars(5));
