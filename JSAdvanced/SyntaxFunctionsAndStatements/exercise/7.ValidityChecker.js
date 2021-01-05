function solve(points) {
    let x1 = points[0];
    let y1 = points[1];
    let x2 = points[2];
    let y2 = points[3];

    function distance(x1, y1, x2, y2) {
        let distanceX = x1 - x2;
        let distanceY = y1 - y2;
        return Math.sqrt(distanceX ** 2 + distanceY ** 2);
    }

    let result = [
        `{${x1}, ${y1}} to {0, 0} is invalid`, 
        `{${x2}, ${y2}} to {0, 0} is invalid`, 
        `{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`
    ];

    if (Number.isInteger(distance(x1, y1, 0, 0))) {
        result[0] = `{${x1}, ${y1}} to {0, 0} is valid`;
    } 
    if (Number.isInteger(distance(x2, y2, 0, 0))) {
        result[1] = `{${x2}, ${y2}} to {0, 0} is valid`;
    } 
    if (Number.isInteger(distance(x1, y1, x2, y2))) {
        result[2] = `{${x1}, ${y1}} to {${x2}, ${y2}} is valid`;
    }

    return result.join('\n')
}
