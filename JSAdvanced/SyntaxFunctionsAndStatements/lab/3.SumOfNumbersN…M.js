function sumOfNumbers(str1, str2) {
    let num1 = Number(str1);
    let num2 = Number(str2);

    let result = 0;

    for (i = num1; i <= num2; i++) {
        result += i;
    }

    return result
}

// console.log(sumOfNumbers('1', '5' ));
// console.log(sumOfNumbers('-8', '20'));
