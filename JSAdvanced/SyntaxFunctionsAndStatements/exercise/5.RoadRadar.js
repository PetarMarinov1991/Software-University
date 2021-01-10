function roadRadar(speed, location) {
    let restrictionsDict = {
        'motorway': 130,
        'interstate': 90,
        'city': 50,
        'residential': 20
    }
    if (speed > restrictionsDict[location]) {
        let diff = speed - restrictionsDict[location];
        let result = `The speed is ${diff} km/h faster than the allowed speed of ${restrictionsDict[location]}`
        if (diff > 40) {
            return `${result} - reckless driving`
        } else if (diff > 20) {
            return `${result} - excessive speeding`
        } else {
            return `${result} - speeding`
        }
    }
    return `Driving ${speed} km/h in a ${restrictionsDict[location]} zone`
}

// console.log(roadRadar(40, 'city'))
// console.log(roadRadar(21, 'residential'))
// console.log(roadRadar(120, 'interstate'))
// console.log(roadRadar(200, 'motorway'))
