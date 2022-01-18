class ElementCollection extends Array {
    ready(cb) {
        const isReady =
            document.readyState !== "loading" || document.readyState !== null;
        if (isReady) {
            cb();
        } else {
            this.on("DOMContentLoaded", cb);
        }
    }
    on(event, cbOrSelector, cb) {
        if (typeof cbOrSelector === "function") {
            this.forEach((e) => e.addEventListener(event, cbOrSelector));
        } else {
            this.forEach((elem) => {
                elem.addEventListener(event, (e) => {
                    if (e.target.matches(cbOrSelector)) cb(e);
                });
            });
        }
    }
    next() {
        return this.map((e) => e.nextElementSibling).filter((e) => e !== null);
    }
    prev() {
        return this.map((e) => e.previousElementSibling).filter((e) => e !== null);
    }
    removeClass(className) {
        this.forEach((e) => e.classList.remove(className));
    }
    addClass(className) {
        this.forEach((e) => e.classList.add(className));
    }
    play() {
        return this.forEach((e) => e.play());
    }
    pause() {
        return this.forEach((e) => e.pause());
    }
    append(el) {
        return this.forEach((elem) => elem.append(el));
    }
    prepend(el) {
        return this.forEach((elem) => elem.prepend(el));
    }
    innerHTML(html) {
        return this.forEach((elem) => (elem.innerHTML = html));
    }
    textContent(txt) {
        return this.forEach((elem) => (elem.textContent = txt));
    }
    setId(id) {
        return this.forEach((elem) => (elem.id = id));
    }
    setAttribute(name, value) {
        return this.forEach((elem) => elem.setAttribute(name, value));
    }
    setAttributes(...atr) {
        atr.forEach((at) => {
            let [name, value] = at.split(" ");
            return this.forEach((elem) => elem.setAttribute(name, value));
        });
    }
    setStyle(...atr) {
        atr.forEach((at) => {
            return this.forEach((elem) => {
                let [name, value] = at.split(" ");
                if (name.includes("-")) {
                    name.replace("-", (e, i) => {
                        let newName =
                            name.slice(0, i) + name[i + 1].toUpperCase() + name.slice(i + 2);
                        elem.style[newName] = value;
                    });
                } else {
                    elem.style[name] = value;
                }
            });
        });
    }
    setDisplay(txt) {
        this.forEach((elem) => (elem.style.display = txt));
    }
    randomChild(n = 1) {
        let children = ["p", "b", "i"];
        return this.forEach((elem) => {
            for (let i = 0; i < n; i++) {
                let n = Math.floor(Math.random() * children.length);
                let child = document.createElement(children[n]);
                child.textContent = "from random child generator";
                elem.appendChild(child);
            }
        });
    }
    createChild(tag, text, styles) {
        return this.forEach((elem) => {
            let child = document.createElement(tag);
            let txt = document.createTextNode(text);
            styles.forEach((st) => {
                let [name, value] = st.split(" ");
                if (name.includes("-")) {
                    name.replace("-", (e, i) => {
                        let newName =
                            name.slice(0, i) + name[i + 1].toUpperCase() + name.slice(i + 2);
                        child.style[newName] = value;
                    });
                } else {
                    child.style[name] = value;
                }
            });
            child.append(txt);
            elem.appendChild(child);
        });
    }
    parent() {
        return this.map((elem) => elem.parentElement);
    }
    children() {
        return this.map((elem) => elem.children);
    }
    toggleClass(cl1,cl2) {
        return this.forEach(elem => {
            if (elem.classList.contains(cl1)) {
                elem.classList.toggle(cl1)
                elem.classList.toggle(cl2)
            }
            else {
                elem.classList.toggle(cl1)
                elem.classList.toggle(cl2)
            }
        })
    }
}
class Component extends HTMLElement {
	constructor() {
		super();
        this.shadow = this.attachShadow({ mode: "open" });
    }
    get observedAttributes() {
        return this.attributes
    }
    attributeChangedCallback(prop, oldV, newV) {
        console.log(this.observedAttributes)
        if (this.observedAttributes[prop]) this.render()
    }
	connectedCallback() {
		this.render();
	}
}
function $(params) {
    if (typeof params === "string" || params instanceof String) {
        return new ElementCollection(...document.querySelectorAll(params));
    } else {
        return new ElementCollection([params]);
    }
}
function formValidate({ type, length, id, className, message }) {
    let ms = "";
    let input = id ? $(`#${id}`)[0] : $(`.${className}`)[0];
    const TextValidotor = () => {
        let text = input.value;
        if (length) {
            if (text.length < length) {
                ms = message ? message : `Text must be ${length} length`;
                return {
                    ms,
                    error: true,
                };
            }
        }
        return {
            pass: true,
            error: false,
        };
    };
    const PasswordValidotor = () => {
        let text = input.value;
        if (length) {
            if (text.length < length) {
                ms =
                    message !== undefined ? message : `Password must be ${length} length`;
                return {
                    ms,
                    error: true,
                };
            }
        }

        return {
            pass: true,
            error: false,
        };
    };
    const EmailValidotor = () => {
        let text = input.value;
        if (length) {
            if (text.length < length) {
                ms = message ? message : `Email must be ${length} length`;
                return {
                    ms,
                    error: true,
                    pass: false,
                };
            }
        }
        if (!/\S+@\S+\.\S+/.test(text)) {
            ms = message !== undefined ? message : "Email is invalid";
            return {
                error: true,
                pass: false,
                ms,
            };
        }
        return {
            pass: true,
            error: false,
        };
    };

    switch (type) {
        case "email":
            return EmailValidotor();
            break;
        case "password":
            return PasswordValidotor();
            break;
        default:
            return TextValidotor();
            break;
    }
}
