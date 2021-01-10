function rotate(arr) {
    let rotations = Number(arr[arr.length - 1])
    let rest = arr.splice(0, arr.length - 1)

    for (i=0; i < rotations; i++) {
        rest.unshift(rest.pop())
    }
    return rest.join(' ')
}

// console.log(rotate(['1', '2', '3', '4', '2']))
// console.log(rotate(['Banana', 'Orange', 'Coconut', 'Apple', '15']))
