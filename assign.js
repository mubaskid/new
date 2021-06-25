let myForm = document.getElementById('myForm');

let age = document.getElementById('age');

let errorDiv = document.getElementById('error');


myForm.addEventListener('submit', (e) => {

    let messages = [];

    if (age.value < 18) {
        messages.push("You cannot enroll for this program");
    }

    if (age.value === '' || age.value === null) {
        messages.push("You cannot enroll for this program age is required");
    }

    if (messages.length > 0) {
        e.preventDefault();

        errorDiv.innerText = messages.join(' ');
        errorDiv.className = 'bg-warning';
    }
})



function myFunction() {
    var element = document.body;
    element.classList.toggle("dark-mode");
}

