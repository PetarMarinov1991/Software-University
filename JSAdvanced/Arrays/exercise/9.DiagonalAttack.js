function solve(input) {
    let matrix = input.map(row => row.split(' ').map(Number))
    let sumFirstDiagonal = 0
    let sumSecondDiagonal = 0

    for (i=0; i < matrix.length; i++) {
        sumFirstDiagonal += matrix[i][i];
        sumSecondDiagonal += matrix[i][matrix.length - i - 1];
    }

    if (sumFirstDiagonal == sumSecondDiagonal) {
        for (i=0; i < matrix.length; i++) {
            for (j=0; j < matrix.length; j++) {
                if(i != j && i != matrix.length - j - 1)  {
                    matrix[i][j] = sumFirstDiagonal
                }
            }
        }
    }
    
    let result = []
    for (i=0; i < matrix.length; i++) {
        result.push(matrix[i].join(' '))
    }
    
    return result.join('\n')
}

// console.log(solve(
//     [
//         '5 3 12 3 1', 
//         '11 4 23 2 5', 
//         '101 12 3 21 10', 
//         '1 4 5 2 2', 
//         '5 22 33 11 1'
//     ]
// ))
