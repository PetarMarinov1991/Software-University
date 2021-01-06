function solve(arr) {
    return arr.splice(0, arr.length - 1).join(arr[arr.length - 1])
}

// console.log(solve(['One', 'Two', 'Three', 'Four', 'Five', '-']))
// console.log(solve(['How about no?', 'I', 'will', 'not', 'do', 'it!', '_']))
