function cappyJuice(input) {
    let juices = {}
    let bottles = {}

    for (data of input) {
        let [fruit, quantity] = data.split(' => ')

        if (!juices[fruit]) {
            juices[fruit] = 0
        }
    
        juices[fruit] += Number(quantity)

        if (juices[fruit] >= 1000) {
            if (!bottles[fruit]) {
                bottles[fruit] = 0
            } 

            bottles[fruit] += Math.floor(juices[fruit] / 1000)
            juices[fruit] %= 1000
        }
    }

    for (const [fruit, bottlesCount] of Object.entries(bottles)) {
        console.log(`${fruit} => ${Math.floor(bottlesCount)}`)
    }
}
