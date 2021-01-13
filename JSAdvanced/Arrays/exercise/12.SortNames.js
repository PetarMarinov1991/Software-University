function sortNames(arr) {
    for (const [idx, name] of arr.sort().entries()) {
        console.log(`${idx + 1}.${name}`)
    }
}

// sortNames(["John", "Bob", "Christina", "Ema"])