function extractText() {
    const liElements = [...document.querySelectorAll('li')]
    const text = liElements.map(e => e.textContent)
    document.getElementById('result').value = text.join('\n')
}