function printAndSum(a, b) {


    let start = Number(a);
    let end = Number(b);

    let total = 0;
    let save = "";

    for (let i = start; i <= end; i++) {
        save += (`${i}` + " ");
        total += i;

    }

    console.log(save);
    console.log(`Sum: ${total}`)

}
