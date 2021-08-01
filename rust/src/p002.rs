pub fn solution(){
    let mut fibs: [i32; 1000] = [0; 1000];
    let mut index = 2;
    let mut sum = 2;
    fibs[0] = 1;
    fibs[1] = 2;

    loop {
        fibs[index] = fibs[index-1] + fibs[index-2];
        if fibs[index] >= 4000000 {
            break;
        }
        else if fibs[index] % 2 == 0 {
            sum += fibs[index];
        }
        index+=1;
    }
    println!("{}", sum); 
}