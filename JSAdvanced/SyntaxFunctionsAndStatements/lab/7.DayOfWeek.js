function dayOfWeek(day) {
    weekDict = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7
    }

    if (day in weekDict) {
        return weekDict[day]
    }

    return 'error'
}

// console.log(dayOfWeek('Monday'));
// console.log(dayOfWeek('Friday'));
// console.log(dayOfWeek('Invalid'));
