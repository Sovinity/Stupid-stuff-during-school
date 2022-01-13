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

function chooseRandom(possibleReturn) {
    return possibleReturn[Math.floor(Math.random() * possibleReturn.length)];
}

functions = {
    
}

console.log("Hello World from Node JS!");

while (true) {
    x = input("", false).toLowerCase();

    if (x == "exit" || x == "quit") {
        process.exit(0);
    } else if (["snuggles", "snuggle", "cuddles", "cuddle"].some(v => x.includes(v))) {
        console.log(chooseRandom(["I'm sorry, I'm not in the mood for snuggles :/", "I'm nicer than python, I will give you snuggles!", "I want to cuddle too!"]));
    } else {
        console.log("I don't understand :/")
    }
}