function solve(input) {
    let board = new Array(3).fill().map(() => new Array(3).fill(false));
    let player = 'X'

    for (line of input) {
        [row, col] = line.split(' ').map(Number)

        if (board[row][col] !== false) {
            console.log('This place is already taken. Please choose another!')
            continue
        }

        board[row][col] = player

        for (i=0; i < 3; i++) {
            if ((board[i][0] === player && board[i][1] === player && board[i][2] === player) ||
                (board[0][i] === player && board[1][i] === player && board[2][i] === player) ||
                (board[0][0] === player && board[1][1] === player && board[2][2] === player) ||
                (board[0][2] === player && board[1][1] === player && board[2][0] === player)) {
                    console.log(`Player ${player} wins!`)
                    return printMatrix()
            }
        }

        let includesFalse = false

        for (i=0; i < 3; i++) {
            if (board[i].includes(false)) {
                includesFalse = true
                break
            }
        }

        if (!includesFalse) {
            console.log('The game ended! Nobody wins :(')
            return printMatrix()
        }

        player = player === 'X' ? 'O' : 'X'
    }

    function printMatrix() {
        for (i=0; i < board.length; i++) {
            console.log(board[i].join('\t'))
        }
    }
}