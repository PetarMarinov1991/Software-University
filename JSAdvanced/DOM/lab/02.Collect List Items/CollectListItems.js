function extractText() {
    const liElements = [...document.querySelectorAll('li')]
    const text = liElements.map(el => el.textContent)
    document.getElementById('result').value = text.join('\n')
}