function population(arr) {
    let obj = {}
    
    arr.forEach(element => {
        let [town, people] = element.split('<->').map(x => x.trim())
        if (obj[town] == null) obj[town] = 0
        obj[town] = obj[town] + Number(people)
    })
    
    console.log(obj)
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
