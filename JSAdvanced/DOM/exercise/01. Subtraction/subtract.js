function subtract() {
    const num1 = Number(document.getElementById('firstNumber').value)
    const num2 = Number(document.getElementById('secondNumber').value)
    const diff = num1 - num2
    document.getElementById('result').textContent = diff
}