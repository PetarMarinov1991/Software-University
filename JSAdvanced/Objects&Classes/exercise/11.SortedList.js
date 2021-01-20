function createSortedList() {
    let sortedList = {
        list: [],
        add: function(element) {
            this.list.push(element)
            this.list.sort((a, b) => a - b)
        },
        remove: function(element) {
            this.list.splice(element, 1)
        },
        get: function(index) {
            return this.list[index]
        },
        size: function() {
            return this.list.length
        }
    }

    return sortedList
}
