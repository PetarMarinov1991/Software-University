function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const searchedWord = document.getElementById('searchField').value
      const table = [...document.querySelectorAll('tbody tr')]
      
      table.forEach(row => {
         if (row.textContent.includes(searchedWord)) {
            row.classList.add('select')
         } else {
            row.classList.remove('select')
         }
      })
   }
}