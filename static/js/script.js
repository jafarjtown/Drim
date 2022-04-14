// validate form logic
function checkPasswordMatch() {
    let p1 = document.querySelector('[name="password1"]')
    let p2 = document.querySelector('[name="password2"]')
    if (p1.value === p2.value) {
        return true
    }
    return false
}
function checkValidEmail() {
    let e = document.querySelector('[name="email"]').value
    let reg = /[a-zA-Z0-9]@[a-z].[a-z]/g
    return e.match(reg)
}
function checkPasswordLength() {
    let p1 = document.querySelector('[name="password1"]')
    return p1.value.length > 6
}
function runCheck() {
    let error = false
    let cp = checkPasswordMatch()
    let ce = checkValidEmail()
    let pl = checkPasswordLength()
    if (cp) {
        document.querySelector('#p2error').style.display = 'none'
    } else {
        document.querySelector('#p2error').style.color = 'red'
        document.querySelector('#p2error').style.display = 'block'

        
    }
    if (ce) {
        document.getElementById('eerror').style.display = 'none'
    } else {
        document.getElementById('eerror').style.color= 'red'
        document.getElementById('eerror').style.display = 'block'
    }
    if (pl) {
        document.getElementById('p1error').style.display = 'none'
    } else {
        document.getElementById('p1error').style.color = 'red'
        document.getElementById('p1error').style.display = 'block'
        
    }
    error = cp && ce && pl
    if (!error) {
        let btn = document.querySelector('#submit')
        btn.disabled = true
    } else {
        let btn = document.querySelector('#submit')
        btn.disabled = false
    }
}
document.querySelectorAll('input')?.forEach(input => {
    input.addEventListener('input', ()=>{
        runCheck()
        
    })
    
})

