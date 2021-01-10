function numberSequence(len, k) {
    let seq = [1]

    for (i = 1; i < len; i++) {
        if (seq.length < k) {
            seq.push(seq.reduce((a, b) => a + b, 0))
        } else {
           seq.push(seq.slice(i - k, len).reduce((a, b) => a + b, 0))
        }
    }

    return seq
}

// console.log(numberSequence(6 , 3))
// console.log(numberSequence(8 , 2))