function generateReport() {
    const output = document.getElementById('output')
    const checkboxes = [...document.querySelectorAll('thead th input')]

    let checkedBoxesIndexes = []

    checkboxes.forEach((box, idx) => {
        if (box.checked) checkedBoxesIndexes.push(idx)
    })

    let result = []

    const th = document.querySelectorAll('thead th')
    const tr = [...document.querySelectorAll('tbody tr')]

    for (const row of tr) {

        let report = {}
    
        for (const idx of checkedBoxesIndexes) {
            let rowInfo = row.children[idx].textContent
            let thName = th[idx].textContent.toLowerCase().trim()
            report[thName] = rowInfo
        }

        result.push(report)
    }

    output.value = JSON.stringify(result, null, 2)
}
