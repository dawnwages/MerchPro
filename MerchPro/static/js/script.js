document.documentElement.classList.remove("no-js");
document.documentElement.classList.add("js");


// Four images side by side
function four() {
    var elements = document.getElementsByClassName("column");
    var i;
    for (i = 0; i < elements.length; i++) {
        elements[i].style.width = "25%";
    }
}

// Two images side by side
function two() {
    var elements = document.getElementsByClassName("column");
    var i;
    for (i = 0; i < elements.length; i++) {
        elements[i].style.width = "50%";
    }
}

// Full-width images
function one() {
    var elements = document.getElementsByClassName("column");
    var i;
    for (i = 0; i < elements.length; i++) {
        elements[i].style.width = "100%";
    }
}