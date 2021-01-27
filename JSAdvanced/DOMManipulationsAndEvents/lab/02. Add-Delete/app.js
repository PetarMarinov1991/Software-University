function addItem() {
    const input = document.getElementById('newText').value
    const newItem = createElement('li', input)

    const deleteBtn = createElement('a', '[Delete]')
    deleteBtn.href = '#'
    newItem.appendChild(deleteBtn)

    deleteBtn.addEventListener('click', ev => {
        ev.target.parentNode.remove()
    })

    document.getElementById('items').appendChild(newItem)
    document.getElementById('newText').value = null

    function createElement(type, content) {
        const element = document.createElement(type)
        element.textContent = content
        return element
    }
}
