function biggerHalf(arr) {
    let sorted = function(arr) {
        return arr.sort((a, b) => a - b)
    }
    return sorted(arr).splice(arr.length / 2, arr.length - 1)
}

// console.log(biggerHalf([4, 7, 2, 5]))
// console.log(biggerHalf([3, 19, 14, 7, 2, 19, 6]))
