function sumByTown(arr) {
    let obj = {}

    for (i=0; i < arr.length; i+=2) {
        obj[arr[i]] = 0
    }
    for (i=1; i < arr.length; i+=2) {
        obj[arr[i - 1]] = obj[arr[i - 1]] + Number(arr[i])
    }

    return obj
}

// console.log(sumByTown(['Sofia','20','Varna','3','Sofia','5','Varna','4']))
// console.log(sumByTown(['Sofia','20','Varna','3','sofia','5','varna','4']))