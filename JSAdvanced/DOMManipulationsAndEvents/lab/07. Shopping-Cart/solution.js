function solve() {
   const output = document.querySelector('textarea')
   const addCartBtn = document.querySelector('.shopping-cart')
   const checkOutBtn = document.querySelector('.checkout')

   const cart = {}

   addCartBtn.addEventListener('click', ev => {
      if (ev.target.tagName == 'BUTTON' && ev.target.className == 'add-product') {
         if (checkOutBtn.disabled) {
            ev.target.disabled = true
         } else {
            const product = ev.target.parentNode.parentNode
            const title = product.querySelector('.product-title').textContent
            const price = Number(product.querySelector('.product-line-price').textContent)
   
            output.value += `Added ${title} for ${price.toFixed(2)} to the cart.\n`
   
            if (!cart[title]) {
               cart[title] = price
            } else {
               cart[title] += price
            }
         }
      }
   })

   let products = []
   let sum = 0

   checkOutBtn.addEventListener('click', () => {
      for (const [product, price] of Object.entries(cart)) {
         products.push(product)
         sum += price
      }

      output.value += `You bought ${products.join(', ')} for ${sum.toFixed(2)}.`
      checkOutBtn.disabled = true
   })
}
