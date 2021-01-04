function solve(str1, str2, str3) {
    let totalStrLen = (str1 + str2 + str3).length;
    let averageStrLen = Math.floor(totalStrLen / 3);
    
    console.log(totalStrLen);
    console.log(averageStrLen);
}

// solve('chocolate', 'ice cream', 'cake');
// solve('pasta', '5', '22.3');
