function solve() {
  const input = document.getElementById('input').value
  const output = document.getElementById('output')

  input
    .match(/[^\.!\?]+[\.!\?]+/g)
    .reduce((acc, sentence, index) => {
      if (index % 3 === 0) acc.push([sentence]) 
      else acc[acc.length - 1].push(sentence) 
      return acc
    }, [])
    .forEach(p => {
      let paragraph = document.createElement('p')
      paragraph.textContent = p
      output.appendChild(paragraph)
    })
}
