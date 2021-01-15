function JSONTable(input) {
    let result = '<table>\n'
    let employees = []

    input.forEach(element => {
        employees.push(JSON.parse(element))
    })

    employees.forEach(employee => {
        result += '\t<tr>\n'

        Object.values(employee).forEach(value => {
            result += `\t\t<td>${value}</td>\n`
        })

        result += '\t</tr>\n'
    })
    return result + '</table>'
}

// console.log(JSONTable(
//     [
//         '{"name":"Pesho","position":"Promenliva","salary":100000}',
//         '{"name":"Teo","position":"Lecturer","salary":1000}',
//         '{"name":"Georgi","position":"Lecturer","salary":1000}'
//     ]
// ))
