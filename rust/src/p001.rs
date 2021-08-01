pub fn solution() {
    let mut sum: i32 = 0;
    for i in 1..1001 {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i;
        }
    }

    println!("{}", sum);
}

