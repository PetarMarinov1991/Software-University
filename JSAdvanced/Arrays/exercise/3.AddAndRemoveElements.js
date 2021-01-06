function solve(arr) {
    let collection = []
    let num = 1
    for (const i in arr) {
        let command = arr[i]
        if (command == 'add') {
            collection.push(num)
        } else if (command == 'remove') {
            collection.pop()
        }
        num += 1
    }
    if (collection.length > 0) {
        return collection.join('\n')
    }
    return 'Empty'
}

// console.log(solve(['add', 'add', 'add', 'add']))
// console.log(solve(['add', 'add', 'remove', 'add', 'add']))
// console.log(solve(['remove', 'remove', 'remove']))
