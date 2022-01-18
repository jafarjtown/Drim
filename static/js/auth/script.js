$("#verify_email").on("click", async function () {
	let em = formValidate({ type: "email", id: "email", length: 5 });
	if (em.pass === true) {
		hideForm();
		let rt = await verifyEmail($("#email")[0].value);
		if (rt.code === 200) {
			$("#emailV").setDisplay("none");
			$("#st").textContent("Login");
			$("#message").innerHTML(`<div class='user'>
                    <img src='${rt.avatar}'/>
                    <span>${email.value}</span>
                </div>`);
			$("#message").setDisplay("block");
			$("#passwordView").setDisplay("flex");
			$("#form").addClass("tr_log");
			$("#verify_email").setDisplay("none");
			$("#login").setDisplay("block");
		} else {
			$("#emailV").setDisplay("none");
			$("#st").textContent("Sign up");
			$("#message").textContent("");
			$("#message").innerHTML(
				`looks like you dont have an account <br/> Lets create an account for <b id='email1'>${$("#email")[0].value
				}</b>`
			);
			$("#message").setDisplay("block");
			$("#new").setDisplay("block");
			$("#passwordView").setDisplay("none");
			$("#form").addClass("tr_sign");

			$("#verify_email").setDisplay("none");
			$("#register").setDisplay("block");
		}
		$("#socials").setDisplay("none");
		showForm();
	} else {
		$("#eerror").textContent(em.ms);
		$("#eerror").setDisplay("block");
		setTimeout(() => $("#eerror").setDisplay("none"), 5000);
	}
});
$("#login").on("click", async function () {
	let ep = formValidate({
		type: "password",
		id: "password",
		length: 8,
		message: "password must be greater or equal to 8",
	});
	if (ep.pass) {
		hideForm();
		const res = await loginUser($("#email")[0].value, $("#password")[0].value);
		if (parseInt(res.code) === 200) {
			$("#message").textContent("Login successfully");
			location.reload();
		} else {
			$("#message").textContent("Wrong password! try again");
			showForm();
		}
	} else {
		$("#perror").textContent(ep.ms);
		$("#perror").setDisplay("block");
		setTimeout(() => $("#perror").setDisplay("none"), 3000);
	}
});
$("#register").on("click", async function () {
	let p = formValidate({
		type: "password",
		id: "password1",
		length: 8,
		message: "password must be greater or equal to 8",
	});
	let t = formValidate({ type: "text", id: "full_name", length: 8 });
	let t1 = formValidate({ type: "text", id: "username", length: 5 });
	if (p.pass && t.pass && t1.pass) {
		const [first_name, last_name] = $("#full_name")[0].value.split(" ");
		hideForm();
		const res = await registerUser(
			$("#email")[0].value,
			first_name,
			last_name,
			$("#username")[0].value,
			$("#password1")[0].value
		);

		if (res === 200) {
			location.reload();
		}
		showForm();
	} else {
		if (p.ms) $("#p1error").textContent(p.ms);
		if (t.ms) $("#ferror").textContent(t.ms);
		if (t1.ms) $("#uerror").textContent(t1.ms);

		if (p.ms) $("#p1error").setDisplay("block");
		if (t.ms) $("#ferror").setDisplay("block");
		if (t1.ms) $("#uerror").setDisplay("block");

		setTimeout(() => {
			$("#p1error").setDisplay("none");
			$("#uerror").setDisplay("none");
			$("#ferror").setDisplay("none");
		}, 3000);
	}
});

async function verifyEmail(email) {
	const res = await fetch("http://127.0.0.1:8000/account/auth/verify", {
		method: "POST",
		body: JSON.stringify({
			email,
		}),
	});
	let r = await res.json();
	return r;
}
async function loginUser(email, password) {
	const res = await fetch("http://localhost:8000/account/auth/login/", {
		method: "POST",
		body: JSON.stringify({
			email,
			password,
		}),
	});
	let r = await res.json();
	return r;
}
async function registerUser(email, first_name, last_name, username, password) {
	let f = {
		email,
		first_name,
		last_name,
		username,
		password,
	};
	const res = await fetch("http://127.0.0.1:8000/account/auth/register", {
		method: "POST",
		body: JSON.stringify(f),
	});
	let r = await res.json();
	if (r.message) {
		$("#uerror").setDisplay("block");
		$("#uerror").textContent(r.message);
		setTimeout(() => {
			$("#uerror").setDisplay("none");
		}, 3000);
	}
	return r.code;
}
function hideForm() {
	$(".loading_div").setDisplay("flex");
}
function showForm() {
	$(".loading_div").setDisplay("none");
}

$('#fgp').setStyle(
	'width 100%',
	'background-color inherit',
	'border none',
	'box-shadow none',
	'display flex',
	'justify-content flex-end'
)
$('#fgpl').setStyle(
	'text-decoration none',
	'color #0064e5',
)