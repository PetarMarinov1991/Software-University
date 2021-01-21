function createSortedList() {
    let list = []

    function add(num) {
        list.push(num), list.sort((a, b) => a - b), this.size++
    }
    function remove(index) {
        if (index >= 0 && index < list.length) list.splice(index, 1), this.size--
    }
    function get(index) {
        if (index >= 0 && index < list.length) return list[index]
    }
    
    let listAsObject = {
        add, 
        remove, 
        get, 
        size: 0
    }
    return listAsObject
}
