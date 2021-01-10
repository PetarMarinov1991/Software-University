function extractWords(input) {
    return input.match(/(\w+)/g).join(", ").toUpperCase()
}

// console.log(extractWords('Hi, how are you?'))
// console.log(extractWords('hello'))
