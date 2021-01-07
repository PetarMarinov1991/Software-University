function sortArr(arr) {
    let sortByTwoCriteria = (x, y) => x.length - y.length || x.toLowerCase().localeCompare(y.toLowerCase())
    return arr.sort(sortByTwoCriteria).join('\n')
}

// console.log(sortArr(['alpha', 'beta', 'gamma']))
// console.log(sortArr(['Isacc', 'Theodor', 'Jack', 'Harrison', 'George']))
// console.log(sortArr(['test', 'Deny', 'omen', 'Default']))
