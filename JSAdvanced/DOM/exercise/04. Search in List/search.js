function search() {
   const towns = [...document.getElementsByTagName('li')]
   const searchedWord = document.getElementById('searchText').value

   let matchesCount = 0

   towns.forEach(element => {
      if (element.textContent.includes(searchedWord)) {
         element.style.textDecoration = 'underline'
         element.style.fontWeight = 'bold'
         matchesCount++
      }
   })
   
   document.getElementById('result').textContent = `${matchesCount} matches found`
}
