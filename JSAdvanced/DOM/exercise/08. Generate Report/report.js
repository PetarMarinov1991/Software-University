function generateReport() {
    const output = document.getElementById('output')
    const checkboxes = [...document.querySelectorAll('thead th input')]

    let checkedBoxesIndexes = []

    checkboxes.forEach((box, idx) => {
        if (box.checked === true) {
            checkedBoxesIndexes.push(idx)
        }
    })

    let result = []

    const th = document.querySelectorAll('thead th')
    const tr = [...document.querySelectorAll('tbody tr')]

    for (const row of tr) {

        let obj = {}
    
        for (const idx of checkedBoxesIndexes) {
            let currRowArr = row.children[idx].textContent
            let currThName = th[idx].textContent.toLowerCase().trim()
            obj[currThName] = currRowArr
        }

        result.push(obj)
    }

    output.value = JSON.stringify(result, null, 2)
}
