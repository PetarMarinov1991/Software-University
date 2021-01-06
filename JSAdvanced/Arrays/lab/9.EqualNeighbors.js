function equalNeighbors(matrix) {
    let pairs = 0
    for (i=0; i < matrix.length - 1; i++) {
       for (j=0; j < matrix[i].length - 1; j++) {
            if (matrix[i][j] == matrix[i + 1][j] || matrix[i][j] == matrix[i][j + 1]) {
                pairs += 1
            }
        }
    }
    return pairs
}

// console.log(equalNeighbors(
//     [
//         ['2', '3', '4', '7', '0'],
//         ['4', '0', '5', '3', '4'],
//         ['2', '3', '5', '4', '2'],
//         ['9', '8', '7', '5', '4']
//     ]
// ))
// console.log(equalNeighbors(
//     [
//         ['test', 'yes', 'yo', 'ho'],
//         ['well', 'done', 'yo', '6'],
//         ['not', 'done', 'yet', '5']
//     ]
// ))
