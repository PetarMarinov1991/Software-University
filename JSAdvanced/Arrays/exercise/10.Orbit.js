function orbit([width, height, x, y]) {
    let matrix = new Array(width).fill().map(() => new Array(height).fill(0))

    for (row=0; row < width; row++) {
        for (col=0; col < height; col++) {
            matrix[row][col] = Math.max(Math.abs(row - x), Math.abs(col - y)) + 1
        }
    }
    console.log(matrix.map(row => row.join(" ")).join("\n"));
}

// orbit([4, 4, 0, 0])
// orbit([5, 5, 2, 2])
// orbit([3, 3, 2, 2])