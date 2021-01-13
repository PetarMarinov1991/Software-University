function replace(arr) {
    let result = []

    let sorted = arr.sort((a,b) => a - b)
    
    for (i=0; i < arr.length / 2; i++) {
        result.push(sorted[i])
        result.push(sorted[arr.length - i - 1])
    }
    return result.splice(0, arr.length)
}
  
// console.log(replace([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]))
