function vacation(a, b, c) {
    let groupOfPeople = Number(a);
    let typeTheGroup = String(b);
    let dayTheWeek = String(c);

    let total = 0;

    if (typeTheGroup === "Students") {

        if (dayTheWeek === "Friday") {
            total = groupOfPeople * 8.45;
        } else if (dayTheWeek === "Saturday") {
            total = groupOfPeople * 9.80;
        } else if (dayTheWeek === "Sunday") {
            total = groupOfPeople * 10.46;
        }
    } else if (typeTheGroup === "Business") {

        if (dayTheWeek === "Friday") {
            total = groupOfPeople * 10.90;
        } else if (dayTheWeek === "Saturday") {
            total = groupOfPeople * 15.60;
        } else if (dayTheWeek === "Sunday") {
            total = groupOfPeople * 16;
        }
    } else if (typeTheGroup === "Regular") {

        if (dayTheWeek === "Friday") {
            total = groupOfPeople * 15;
        } else if (dayTheWeek === "Saturday") {
            total = groupOfPeople * 20;
        } else if (dayTheWeek === "Sunday") {
            total = groupOfPeople * 22.50;
        }
    }

    if (typeTheGroup === "Students" && groupOfPeople >= 30) {
        total -= total * 0.15;
    } else if (typeTheGroup === "Business" && groupOfPeople >= 100) {
        if (dayTheWeek === "Friday") {
            total -= 10 * 10.90;
        } else if (dayTheWeek === "Saturday") {
            total -= 10 * 15.60;
        } else if (dayTheWeek === "Sunday") {
            total -= 10 * 16;
        }
    } else  if (typeTheGroup === "Regular" && groupOfPeople >= 10 && groupOfPeople <= 20) {
        total -= total * 0.05;
    }

    console.log(`Total price: ${total.toFixed(2)}`);


}
