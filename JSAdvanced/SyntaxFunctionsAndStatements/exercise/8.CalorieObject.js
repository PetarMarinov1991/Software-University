function solve(args){
    let products = [];
    for (i=0; i < args.length; i+=2) {
            products.push(`${args[i]}: ${Number(args[i + 1])}`)
    }
    return '{' + products.join(', ') + '}'
}

console.log(solve(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']))
