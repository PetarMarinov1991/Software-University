function rectangle(width, height, color) {
    let capitalize = color => color[0].toUpperCase() + color.slice(1)
    let calcArea = () => width * height

    let rect = {
        width,
        height,
        color: capitalize(color),
        calcArea
    }

    return rect
}
