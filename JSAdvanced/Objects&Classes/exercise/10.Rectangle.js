function rectangle(width, height, color) {
    let rect = {
        width: width,
        height: height,
        color: color,
        calcArea: function() {
           return width * height
        }
    }

    return rect
}
