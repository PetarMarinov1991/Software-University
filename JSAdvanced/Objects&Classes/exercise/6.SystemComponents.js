function systemComponents(input) {
    let components = {}

    input.forEach(line => {
        let [systemName, componentName, subcomponentName] = line.split(' | ')

        if (!components[systemName]) {
            components[systemName] = {}
        }

        if (!components[systemName][componentName]) {
            components[systemName][componentName] = []
        } 

        components[systemName][componentName].push(subcomponentName)
    })

    Object.entries(components)
        .sort((x, y) => Object.entries(y[1]).length - Object.entries(x[1]).length || x[0].localeCompare(y[0]))
        .forEach(system => { console.log(system[0])
        Object.entries(system[1])
            .sort((x, y) => x.length - y.length)
            .forEach(component => { console.log(`|||${component[0]}`)
                for (const subCompoment of component[1]) {
                    console.log(`||||||${subCompoment}`)
                }
            })
    })
}
