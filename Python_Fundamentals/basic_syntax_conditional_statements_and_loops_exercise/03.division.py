function division(input) {
    let num = Number(input);

    let flagTwo = false;
    let flagThree = false;
    let flagSix = false;
    let flagSeven = false;
    let flagTeen = false;


    if (num % 2 === 0) {
        flagTwo = true;
    }
    if (num % 3 === 0) {
        flagThree = true;
    }
    if (num % 6 === 0) {
        flagSix = true;
    }
    if (num % 7 === 0) {
        flagSeven = true;
    }
    if (num % 10 === 0) {
        flagTeen = true;


    }
    if (flagTeen) {
        console.log(`The number is divisible by 10`)
    } else if (flagSeven) {
        console.log(`The number is divisible by 7`)
    } else if (flagSix) {
        console.log(`The number is divisible by 6`)
    } else if (flagThree) {
        console.log(`The number is divisible by 3`)
    } else if (flagTwo) {
        console.log(`The number is divisible by 2`)
    } else {
        console.log(`Not divisible`)
    }


}
