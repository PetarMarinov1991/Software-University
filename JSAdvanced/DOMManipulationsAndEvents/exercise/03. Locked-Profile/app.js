function lockedProfile() {
    document.getElementById('main').addEventListener('click', ev => {
        if (ev.target.tagName === 'BUTTON') {
            const profile = ev.target.parentNode
            let locked = profile.querySelector('input[type=radio]:checked').value

            if (locked === 'unlock') {
                let div = profile.querySelector('div')
                let visible = div.style.display === 'block'
                div.style.display = visible ? 'none' : 'block'
                ev.target.textContent = visible ? 'Show more' : 'Hide it'
            }
        }
    })
}
