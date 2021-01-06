function evenPositionElements(args) {
    let filtered = args.filter((x, i) => i % 2 == 0);
    return filtered.join(' ')
}

// console.log(evenPositionElements(['20', '30', '40']))
// console.log(evenPositionElements(['5', '10']))