function addItem() {
    const items = document.getElementById('items')  
    const newItem = document.getElementById('newItemText').value

    items.appendChild(document.createElement("li")).textContent = newItem
    document.getElementById('newItemText').value = null
}
