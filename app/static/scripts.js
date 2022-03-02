const axios = require('axios').default;


const login_form = document.querySelector( "#login_form" );

login_form.addEventListener("submit", (e) => {
    const username = document.querySelector("#username").value;
    const password = document.querySelector("#password").value;
    e.preventDefault();
    console.log(username, password);

    function login() {
        axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/login',
            data: {
                username: username,
                password: username
            }
        })
        .then(function (response) {
            console.log(response.data);
            console.log(response.status);
            console.log(response.headers);
        });
    }

    login();
    // axios.post('/login', {
    //     username: username,
    //     password: password
    // })
    // .then(function (response) {

    // })
});


// const login_form = document.querySelector( "#login_form" );

// login_form.addEventListener("submit", (e) => {
//     const username = document.querySelector("#username").value;
//     const password = document.querySelector("#password").value;
//     e.preventDefault();
//     console.log(username, password);

//     fetch("http://127.0.0.1:8000/login", {
//         method: 'post',
//         headers: {
//             'Accept': 'application/json, text/plain, */*',
//             'Content-Type': 'application/json',
//             'Authorization': 'Bearer' 
//         },
//         body: {
//             "username": username,
//             "password": password
//         }
        
//     }).then(res => res.json())
//         .then(res => {
//             console.log(res);
//             let inMemoryToken = res.token;

//             localStorage.setItem('user', JSON.stringify(res));
//         })
// })
