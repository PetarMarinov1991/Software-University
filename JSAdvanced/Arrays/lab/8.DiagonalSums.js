function diagonalSums(matrix) {
    firstDiagonalSum = 0
    secondDiagonalSum = 0

    for (i=0; i < matrix.length; i++) {
        firstDiagonalSum += matrix[i][i]
        secondDiagonalSum += matrix[i][matrix.length - i - 1]
    }

    return `${firstDiagonalSum} ${secondDiagonalSum}`
}

// console.log(diagonalSums(
//     [
//         [20, 40],
//         [10, 60]
//     ]
//    ))
// console.log(diagonalSums(
//     [
//         [3, 5, 17],
//         [-1, 7, 14],
//         [1, -8, 89]
//     ]
//    ))
