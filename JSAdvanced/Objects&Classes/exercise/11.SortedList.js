function createSortedList() {
    let sortedList = {
        list: [],
        add: function(num) {
            this.list.push(num)
            this.list.sort((a, b) => a - b)
        },
        push: function(num) {
            return add(num) // needed?
        },
        remove: function(index) {
            if (index >= 0 && index < this.list.length) {
                this.list.splice(index, 1)
            } 
            return 'IndexError'
        },
        get: function(index) {
            if (index >= 0 && index < this.list.length) {
                return this.list[index]
            }
            return 'IndexError'
        },
        size: this.list.length // ... error?
    }
    return sortedList
}
