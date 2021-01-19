function population(arr) {
    let cities = {}
    
    arr.forEach(element => {
        let [town, people] = element.split(' <-> ')
        if (cities[town] == null) cities[town] = 0
        cities[town] += Number(people)
    })
    
    Object.entries(cities).forEach(town => console.log(`${town[0]} : ${town[1]}`))
}

// population(
//     [
//         'Sofia <-> 1200000',
//         'Montana <-> 20000',
//         'New York <-> 10000000',
//         'Washington <-> 2345000',
//         'Las Vegas <-> 1000000'
//     ]
// )

// population(
//     [
//         'Istanbul <-> 100000',
//         'Honk Kong <-> 2100004',
//         'Jerusalem <-> 2352344',
//         'Mexico City <-> 23401925',
//         'Istanbul <-> 1000'
//     ]
// )
