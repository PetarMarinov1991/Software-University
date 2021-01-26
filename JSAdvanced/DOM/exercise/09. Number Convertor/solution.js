function solve() {
    let selectElement = document.querySelector('#selectMenuTo')
    let binary = document.createElement('option')
    let hexadecimal = document.createElement('option')

    binary.value = 'binary'
    binary.text = 'Binary'
    hexadecimal.value = 'hexadecimal'
    hexadecimal.text = 'Hexadecimal'

    selectElement.add(binary)
    selectElement.add(hexadecimal)

    document.querySelector('button').addEventListener('click', clickEvent)

    function clickEvent() {
        let decimalNumber = +document.querySelector('#input').value
        let convertTo = selectElement.options[selectElement.selectedIndex].text

        let result = undefined

        switch (convertTo) {
            case 'Binary':
                result = decimalNumber.toString(2)
                break
            case 'Hexadecimal':
                result = decimalNumber.toString(16).toUpperCase()
                break
        }

        document.querySelector('#result').value = result
    }
}
