function storeCatalogue(input) {
    let letters = []
    let products = {}

    for (const data of input) {
        let [product, price] = data.split(' : ')
        let initialLetter = product[0]

        if (!letters.includes(initialLetter)) {
            letters.push(initialLetter)
        } 

        products[product] = price
    }

    for (const letter of letters.sort()) {
        console.log(letter)
        for (const product of Object.keys(products).sort()) {
            if (product[0] == letter) {
                console.log(`${product}: ${products[product]}`)
            }
        }
    }
}
