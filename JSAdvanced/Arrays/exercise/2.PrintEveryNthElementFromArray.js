function solve(arr) {
    let step = Number(arr[arr.length - 1])
    let rest = arr.splice(0, arr.length - 1)

    for (i=0; i < rest.length; i+= step) {
        console.log(rest[i])
    }
}

// solve(['5', '20', '31', '4', '20', '2'])
// solve(['dsa','asd', 'test', 'tset', '2'])
// solve(['1', '2', '3', '4', '5', '6'])
