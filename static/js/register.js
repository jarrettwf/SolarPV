var myInput = document.getElementById("password");
var letter = document.getElementById("lett");
var capital = document.getElementById("cap");
var number = document.getElementById("num");
var length = document.getElementById("len");

/** The function below is doing 2 things...
    When the user begeins to type in the password box, the warning display will become block
    Second, there are multiple If/Else statements used to verify the password complexity!
**/
myInput.onkeyup = function () {
    document.getElementById("warning").style.display = "block";
    
    var lowerCase = /[a-z]/g;
    if (myInput.value.match(lowerCase)) {
        letter.classList.remove("invalid");
        letter.classList.add("valid");
    } else {
        letter.classList.remove("valid");
        letter.classList.add("invalid");
    }

    var upperCase = /[A-Z]/g;
    if (myInput.value.match(upperCase)) {
        capital.classList.remove("invalid");
        capital.classList.add("valid");
    } else {
        capital.classList.remove("valid");
        capital.classList.add("invalid");
    }

    var numbers = /[0-9]/g;
    if (myInput.value.match(numbers)) {
        number.classList.remove("invalid");
        number.classList.add("valid");
    } else {
        number.classList.remove("valid");
        number.classList.add("invalid");
    }

    if (myInput.value.length <= 8) {
        length.classList.remove("invalid");
        length.classList.add("valid");
    } else {
        length.classList.remove("valid");
        length.classList.add("invalid");
    }
}

//sets display to none when clicked out of password window
myInput.onblur = function () {
    document.getElementById("warning").style.display = "none";
}
