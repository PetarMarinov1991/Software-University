function carFactory(params) {
    const engines = {
        90:  1800,
        120: 2400,
        200: 3500
    }

    let model = params['model']
    let power = Number(Object.keys(engines).reduce(function(prev, curr) {
        return (Math.abs(curr - params['power']) < Math.abs(prev - params['power']) ? curr : prev)}))
    let color = params['color']
    let carriage = params['carriage']
    let wheelsize = params['wheelsize'] % 2 == 0 ? 2 * Math.floor(params['wheelsize'] / 2) - 1 : params['wheelsize']
    
    let car = {
        model: model,
        engine: {
            power: power,
            volume: engines[power]
        },
        carriage: {
            type: carriage,
            color: color
        },
        wheels: Array.from({length: 4}, () => wheelsize)
    }

    return car
}
