function createSortedList() {
    let sortedList = {
        list: [],
        add: function(num) {
            this.list.push(num)
            this.list.sort((a, b) => a - b)
        },
        remove: function(index) {
            this.list.splice(index, 1)
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
