function diagonalSums(matrix) {
    firstDiagonal = 0
    secondDiagonal = 0

    for (i=0; i < matrix.length; i++) {
        firstDiagonal += matrix[i][i]
        secondDiagonal += matrix[i][matrix.length - i - 1]
    }

    return `${firstDiagonal} ${secondDiagonal}`
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
