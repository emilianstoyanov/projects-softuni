function triangleOfNumbers(input) {
    let num = Number(input);

    let dynamically = 1;

    let save = "";
    for (let i = 1; i <= num; i++){
        for (let j = 1; j <= i; j++){
            save += dynamically + " "
            
        }
        console.log(save)
        dynamically++;
        save = "";
    }


}
