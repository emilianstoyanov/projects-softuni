function leapYear(input) {

    let num = Number(input);

    if ((num % 100 === 0) ? (num % 400 === 0) : (num % 4 === 0)) {
        console.log(`yes`);
    } else {
        console.log(`no`);
    }


}
