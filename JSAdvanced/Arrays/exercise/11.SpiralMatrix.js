function generateMatrix(n) {
    let matrix = new Array(n).fill().map(() => new Array(n).fill(0))
    let x = 0
    let y = 0
    let step = 0

    for (i=0; i < n ** 2;) {
        while (y + step < n) {
            i += 1
            matrix[x][y] = i
            y += 1
        }

        y -= 1
        x += 1  

        while (x + step < n) {
            i += 1
            matrix[x][y] = i
            x += 1
        }

        x -= 1
        y -= 1  

        while (y >= step) {
            i += 1
            matrix[x][y] = i
            y -= 1
        }

        y += 1
        x -= 1
        step += 1

        while (x >= step) {
            i += 1
            matrix[x][y] = i
            x -= 1
        }

        x += 1
        y += 1
    }
    for (row of matrix) {
        console.log(row.join(' '))     
    }
}

// generateMatrix(5, 5)
// generateMatrix(3, 3)