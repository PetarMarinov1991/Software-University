function calculateTimeToWalk(steps, footprint, speed) {
    let distance = steps * footprint;
    let restCount = Math.floor(distance / 500);
    let ms = speed * 0.277777778;

    let timeInSeconds = distance / ms;
    let seconds = timeInSeconds % (24 * 3600)
    let hours = Math.floor(seconds / 3600)
    let minutes = Math.floor(seconds / 60) + restCount
    seconds %= 60
    seconds = Math.round(seconds)

    if (seconds >= 60) {
        seconds -= 60
        minutes += 1
    }
    if (minutes >= 60) {
        minutes -= 60
        hours += 1
    }

    let result = `${hours}:${minutes}:${seconds}`;
    if (hours < 10) {
        result = '0' + result
    }
    if (seconds == 0) {
        result = result + '0'
    }
    return result
}

// console.log(calculateTimeToWalk(4000, 2, 5));
// console.log(calculateTimeToWalk(2564, 0.70, 5.5));
