const display = document.getElementById("display");

function appendToDisplay(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = "";
}

function deleteLast() {
    display.value = display.value.slice(0, -1);
}

function toggleSign() {
    if (display.value) {
        display.value = String(-parseFloat(display.value));
    }
}

function calculate() {
    try {
        display.value = eval(display.value);
    } catch (e) {
        display.value = "Error";
    }
}

// ✅ Handle keyboard input
document.addEventListener("keydown", (event) => {
    const key = event.key;

    if (!isNaN(key)) {
        appendToDisplay(key); // 0–9
    } else if (["+", "-", "*", "/"].includes(key)) {
        appendToDisplay(key);
    } else if (key === "Enter" || key === "=") {
        calculate();
    } else if (key === "Backspace") {
        deleteLast();
    } else if (key === "Escape") {
        clearDisplay();
    } else if (key === ".") {
        appendToDisplay(".");
    } else if (key === "%") {
        appendToDisplay("%");
    }
});
