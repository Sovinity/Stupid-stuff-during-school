// Hello World!

const prompt = require("prompt-sync")();

// Functions

function input(text, isNumber) {
    if (text != "") {
        text += "\n";
    }
    text += ">>> ";
    while (true) {
        answer = prompt(text)

        if (isNumber && Number(answer) != NaN) {
            return answer;
        } else if (isNumber && Number(answer) == NaN) {
            console.log("That was not a Number");
        } else {
            return answer;
        }
    }
}

console.log("Hello World from Node JS!");

while (true) {
    x = input("", false);

    if (x == "exit" || x == "quit") {
        process.exit(0);
    } else if (x.includes("snuggles") || x.includes("snuggle") || x.includes("cuddle") || x.includes("cuddles")) {
        console.log("I'm nicer than python, I'll give you cuddles!");
    } else {
        console.log("I don't understand :/")
    }
}