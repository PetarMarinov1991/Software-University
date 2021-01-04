function calculateFruitPrice(fruit, weightInGrams, kgPrice) {
    weightInKg = weightInGrams / 1000;
    fruitPrice = weightInKg * kgPrice;

    return `I need $${fruitPrice.toFixed(2)} to buy ${weightInKg.toFixed(2)} kilograms ${fruit}.`
}

// console.log(calculateFruitPrice('orange', 2500, 1.80));
// console.log(calculateFruitPrice('apple', 1563, 2.35));
