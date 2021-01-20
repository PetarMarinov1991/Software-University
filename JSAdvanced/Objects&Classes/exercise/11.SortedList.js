function createSortedList() {
    let sortedList = {
        list: [],
        add: function(num) {
            this.list.push(num)
            this.list.sort((a, b) => a - b)
        },
        remove: function(num) {
            this.list.splice(num, 1)
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
