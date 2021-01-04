function circleArea(arg) {
    let type = typeof(arg);

    if (type !== 'number') {
        return `We can not calculate the circle area, because we receive a ${type}.`
    }

    return (Math.pow(arg, 2) * Math.PI).toFixed(2);
}

// console.log(circleArea(5));
// console.log(circleArea('name'));
