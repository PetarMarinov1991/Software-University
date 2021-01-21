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
            if (validIndex(index)) {
                this.list.splice(index, 1)
            }
            return 'IndexError'
        },
        get: function(index) {
            if (validIndex(index)) {
                return this.list[index]
            }
            return 'IndexError'
        },
        size: 0,
        // size: this.list.length ...error?
        // size: sortedList['list'].length ...error?
    }
    let validIndex = index => index >= 0 && index < sortedList['list'].length
    sortedList['size'] = sortedList['list'].length // still 0 ? the list is not saved?
    return sortedList
}
