const loginForm = document.querySelector( "#login_form" );
const username = document.querySelector("#username").value;
const password = document.querySelector("#password").value;


let formdata = new FormData();
formdata.append("username", username);
formdata.append("password", password);

let requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
//   headers : {
//       'Content-Type': 'application/json'
//   }
};


loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    fetch("http://127.0.0.1:8000/login", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

});



// fetch("http://127.0.0.1:8000/login", {
//     method: 'post',
//     headers: {
//         'Content-Type': 'application/x-www-form-urlencoded'
//     },
//     body: {
//         "username": username,
//         "password": password
//     }            
// })
// .then((res) => {
//     console.log(res);
// });    




// fetch("http://127.0.0.1:8000/login", {
//     method: 'get',
//     headers: {
//         'Authorization': 'Bearer '  
//     },
//     body: {
//         "username": username,
//         "password": password
//     }
    
// })




// function makeTwoRequests() {

//     fetch("http://127.0.0.1:8000/login", {
//         method: 'post',
//         headers: {
//             'Content-Type': 'application/x-www-form-urlencoded'
//         },
//         body: {
//             "username": username,
//             "password": password
//         }            
//     })
//     .then((res) => {
//         console.log(res);
//     });    
    
// };