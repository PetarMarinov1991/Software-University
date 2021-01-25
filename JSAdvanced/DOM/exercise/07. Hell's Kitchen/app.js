function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      const input = document.querySelector('#inputs>textarea').value
         .replace(new RegExp(/[\[\]']/g), null)
         .split('"')

      let restaurantsData = {}
      
      input.forEach(row => {
         let [restourantName, workers] = row.split('-')
         restourantName = restourantName.trim()
         
         if (workers !== undefined) {
            let workersInRestaurant = workers.split(',')
            workersInRestaurant.forEach(worker => {
               let [_, workerName, workerSalarvalue] = worker.split(' ')
               if (!restaurantsData[restourantName]) {
                  restaurantsData[restourantName] = {}
               }
               if (!restaurantsData[restourantName][workerName]) {
                  restaurantsData[restourantName][workerName] = Number(workerSalarvalue)
               }
            })
         }
      })
      let sorted = {}
      Object.entries(restaurantsData).forEach(element => {
         let restourantName = element[0]
         sorted[restourantName] = {}
         sorted[restourantName]['averageSalary'] = 0
         Object.entries(element[1])
            .sort((x, value) => value[1] - x[1])
            .forEach(element => { 
               sorted[restourantName][element[0]] = element[1]
               sorted[restourantName]['averageSalary'] += element[1]
            })
            sorted[restourantName]['averageSalary'] /= Object.values(sorted[restourantName]).length - 1
      })
      
      let bestAverage = 0
      let bestPlace = []
      let result = ''

      for (const [placeName, info] of Object.entries(sorted)) {
         for (const [key, value] of Object.entries(info)) {
            if (key === 'averageSalary' && value > bestAverage) {
               bestPlace = [placeName, Object.entries(info)]
            }
         }
      }
      
      for (let i=1; i < bestPlace[1].length; i++) {
         result += `Name: ${bestPlace[1][i][0]} With Salary: ${bestPlace[1][i][1]} `
      }

      document.querySelector('#bestRestaurant>p').textContent =
         `Name: ${bestPlace[0]} Average Salary: ${bestPlace[1][0][1].toFixed(2)} Best Salary: ${bestPlace[1][1][1].toFixed(2)}`
      document.querySelector('#workers>p').textContent = result
   }
}
