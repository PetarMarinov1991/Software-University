function create(words) {
   const content = document.getElementById('content')

   Array.from(words).forEach(word => {
      const div = document.createElement('div')
      const paragraph = document.createElement('p')
      paragraph.textContent = word
      paragraph.style.display = 'none'
      div.appendChild(paragraph)
      content.appendChild(div)
   })

   content.addEventListener('click', onClick)

   function onClick(ev) {
      if (ev.target.tagName === 'DIV' || ev.target.tagName === 'P') {
         const p = ev.target.children[0] || e.target
         const isVisible = p.style.display === 'block'
         p.style.display = isVisible ? 'none' : 'block'
      }
   }
}
