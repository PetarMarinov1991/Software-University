function townsToJSON(input) {
    let data = input
        .map(row => row.split('|')
        .filter(x => x != '')
        .map(x => x.trim()))

    let keys = data.shift()
    let result = []

    data.forEach(row => {
        let currentObj = {
            [keys[0]]: row[0],
            [keys[1]]: Number(Number(row[1]).toFixed(2)),
            [keys[2]]: Number(Number(row[2]).toFixed(2))
        }
        result.push(currentObj)  
    })
    return result
}

// console.log(townsToJSON(
//     [
//         '| Town | Latitude | Longitude |',
//         '| Sofia | 42.696552 | 23.32601 |',
//         '| Beijing | 39.913818 | 116.363625 |'
//     ]
// ))
