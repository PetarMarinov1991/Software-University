function solve(arr) {
    let currentBiggest = Number.MIN_SAFE_INTEGER
    for (const i in arr) {
        if (arr[i] >= currentBiggest) {
            console.log(arr[i])
            currentBiggest = arr[i]
        }
    }
}

// solve([1, 3, 8, 4, 10, 12, 3, 2, 24])
// solve([1, 2, 3, 4])
// solve([20, 3, 2, 15, 6, 1])
