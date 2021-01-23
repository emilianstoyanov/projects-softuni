function login(input) {
    let username = String(input.shift());

    let length = input.length;
    let stopCount = 0;

    while (stopCount < length) {
        stopCount++;
        let searchPassword = String(input.shift());
        let reversedPassword = searchPassword.split("").reverse().join("");

        if (username === reversedPassword) {
            console.log(`User ${username} logged in.`);
        } else {
            if (stopCount === 4) {
                console.log(`User ${username} blocked!`);
                break;
            } else {
                console.log(`Incorrect password. Try again.`);
            }

        }


    }


}
