function magicMatrix(matrix) {
    numbers = []
    for (i=0; i < matrix.length; i++) {
        let sumRow = 0
        let sumCol = 0
        for (j=0; j < matrix.length; j++) {
            sumRow += matrix[i][j]
            sumCol += matrix[j][i]
        }
        numbers.push(sumRow)
        numbers.push(sumCol)
    }
    return numbers.every( x => x === numbers[0])
}

// console.log(magicMatrix([[4, 5, 6], [6, 5, 4], [5, 5, 5]]))
// console.log(magicMatrix([[11, 32, 45], [21, 0, 1], [21, 1, 1]]))
// console.log(magicMatrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]]))
