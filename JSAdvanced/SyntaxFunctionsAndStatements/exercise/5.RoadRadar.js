function roadRadar([speed, location]) {
    let restrictionsDict = {
        'motorway': 130,
        'interstate': 90,
        'city': 50,
        'residential': 20
    }
    if (speed > restrictionsDict[location]) {
        let diff = speed - restrictionsDict[location];
        if (diff > 40) {
            return 'reckless driving'
        } else if (diff > 20) {
            return 'excessive speeding'
        } else {
            return 'speeding'
        }
    }
}

// console.log(roadRadar(40, 'city'))
// console.log(roadRadar(21, 'residential'))
// console.log(roadRadar(120, 'interstate'))
// console.log(roadRadar(200, 'motorway'))
