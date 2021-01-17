function cars(input) {
    let storage = {}

    input.forEach(line => {
      let [brand, model, produced] = line.split(' | ')
      
      if (!storage[brand]) {
          storage[brand] = {}
      }

      if (!storage[brand][model]) {
          storage[brand][model] = 0
      }
      
      storage[brand][model] += Number(produced)
    })
    for (const [brand, cars] of Object.entries(storage)) {
        console.log(brand)
        for (const [model, produced] of Object.entries(cars)) {
            console.log(`###${model} -> ${produced}`)
        }
    }
}
