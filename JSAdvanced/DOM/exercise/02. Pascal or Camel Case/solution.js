function solve() {
  const input = (document.getElementById('text').value).split(' ')
  const convertCase = document.getElementById('naming-convention').value

  let wordsToLowerCase = []

  input.forEach(word => wordsToLowerCase.push(word.toLowerCase()))
  
  let result = ''

  wordsToLowerCase.forEach(word => {
    let firstLetter = word[0].toUpperCase()
    let rest = word.slice(1, word.length)
    result += firstLetter + rest

    if (convertCase == 'Pascal Case') result 
    else if (convertCase == 'Camel Case') result = result[0].toLowerCase() + result.slice(1, result.length) 
    else result = 'Error!'
  })
  document.getElementById('result').textContent = result
}