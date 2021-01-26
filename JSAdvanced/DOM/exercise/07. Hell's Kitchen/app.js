function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      const input = JSON.parse(document.querySelector('#inputs>textarea').value)

      let restaurants = {}
      
      input.forEach(row => {
         let args = row.split(' - ')
         let name = args[0]
         let workersArr = args[1].split(', ')
         let workers = []

         workersArr.forEach(worker => {
            let args = worker.split(' ')
            let workerName = args[0]
            let salary = Number(args[1])
            
            workers.push({ name: workerName, salary })
         })

         if (restaurants[name]) {
            workers = workers.concat(restaurants[name].workers)
         }

         workers.sort((worker1, worker2) => worker2.salary - worker1.salary)
         const bestSalary = workers[0].salary
         const averageSalary = workers.reduce((sum, worker) => sum + worker.salary, 0) / workers.length

         restaurants[name] = {
            workers,
            averageSalary,
            bestSalary
         }
      })
      
      let bestRestaurantSalary = 0
      let best = {}

      for (const name in restaurants) {
         if (restaurants[name].averageSalary > bestRestaurantSalary)
            best = {
               name, 
               workers: restaurants[name].workers,
               bestSalary: restaurants[name].bestSalary,
               averageSalary: restaurants[name].averageSalary
            }

            bestRestaurantSalary = restaurants[name].averageSalary
      }

      let result = ''

      best.workers.forEach(worker => result += `Name: ${worker.name} With Salary: ${worker.salary} `)

      document.querySelector('#bestRestaurant>p').textContent = `Name: ${best.name} Average Salary: ${best.averageSalary.toFixed(2)} Best Salary: ${best.bestSalary.toFixed(2)}`
      document.querySelector('#workers>p').textContent = result
   }
}
