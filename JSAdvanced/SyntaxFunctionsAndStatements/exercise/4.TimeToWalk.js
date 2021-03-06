function calculateTimeToWalk(steps, footprint, speed) {
    let distance = steps * footprint;
    let rest = Math.floor(distance / 500);
    let ms = speed * 0.277777778;

    let seconds = (distance / ms) + rest * 60;
    let h = Math.floor(seconds % (3600 * 24) / 3600);
    let m = Math.floor(seconds % 3600 / 60);
    let s = Math.round(seconds % 60);

    if (s == 60) {
        s -= 60
        m += 1
    }

    function pad(num, size=2) {
        num = num.toString();
        while (num.length < size) num = "0" + num;
        return num
    }

    return `${pad(h)}:${pad(m)}:${pad(s)}`
}

// console.log(calculateTimeToWalk(4000, 0.6, 5));
// console.log(calculateTimeToWalk(2564, 0.70, 5.5));
