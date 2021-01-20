function objectComposer(arr) {
    let obj = {}
    for (let i=0; i < arr.length - 1; i++) {
        obj[arr[i]] = Number(arr[i + 1])
        i++
    }
    return obj
}
