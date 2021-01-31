function deleteByEmail() {
    let table = [...document.querySelectorAll('tbody tr')]
    const input = document.querySelector('input[name="email"]')
    let result = document.getElementById('result')

    table.forEach(row => {
        if (row.children[1].textContent == input.value) {
            row.remove()
            result.textContent = 'Deleted.'
        } else {
            result.textContent = 'Not found.'
        }
    })
}
