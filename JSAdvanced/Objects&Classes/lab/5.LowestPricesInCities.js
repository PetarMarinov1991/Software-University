function lowestPrices(arr) {
    let result = {}

    arr.forEach(row => {
        let data = row.split(' | ')
        let town = data[0]
        let product = data[1]
        let price = Number(data[2])

        if (result[product]){
            if (result[product][0] <= price) {
                return
            }
        }   

        result[product] = [price, town]      
    })

    for (const [product, value] of Object.entries(result)) {
        console.log(`${product} -> ${value[0]} (${value[1]})`)
    }
}
