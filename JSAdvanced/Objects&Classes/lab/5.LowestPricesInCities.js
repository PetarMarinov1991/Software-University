function lowestPrices(arr) {
    let data = arr
        .map(row => row.split('|')
        .map(x => x.trim()))

    let result = {}

    data.forEach(row => {
        let town = row[0]
        let product = row[1]
        let price = Number(row[2])

        if (result.hasOwnProperty(product)){
            if (result[product][0] < price) {
                return
            }
        }   

        result[product] = [price, town]
        
    });

    for (key in result) {
        console.log(`${key} -> ${result[key][0]} (${result[key][1]})`)
    }
}

// lowestPrices(
//     [
//         'Sample Town | Sample Product | 1000',
//         'Sample Town | Orange | 2',
//         'Sample Town | Peach | 1',
//         'Sofia | Orange | 3',
//         'Sofia | Peach | 2',
//         'New York | Sample Product | 1000.1',
//         'New York | Burger | 10'
//     ]
// )
