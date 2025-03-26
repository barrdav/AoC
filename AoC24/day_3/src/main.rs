
use std::fs;
use regex::Regex;


const INPUT_PATH: &str = "../Input/3.txt";

fn calc( c: regex::Captures) -> u32
{
    let n1 = u32::from_str_radix(&c[1],10).unwrap();
    let n2 = u32::from_str_radix(&c[2],10).unwrap();
    n1 * n2
}


fn check_valid_instruct( instruct: &str, re: &Regex ) -> u32
{
//    println!("Check this: {:?}", instruct);

    let caps = re.captures(instruct);
    let r;
    match caps {
        Some(c) => r = calc(c),
        None => r = 0,
    };

//    println!("added: {:?}", r);

    r
}


// return true if "don't" or *do* found
fn check_action( instruct: &str, re: &Regex ) -> bool
{
    println!("Check this: {:?}", instruct);

    let caps = re.captures(instruct);
    let ret = caps.is_some();

//    println!("Found action: {:?}", ret);

    ret
}


fn main() {

    let mut result_part_1: u32 = 0;
    let mut result_part_2: u32 = 0;

    let input: String = fs::read_to_string(INPUT_PATH).expect("Read input failed");

    let re_mul = Regex::new(r"^ul\((\d+),(\d+)\)").unwrap();

    let mut do_add = true;
    let re_dont = Regex::new(r"^(on't\(\))").unwrap();
    let re_do   = Regex::new(r"^(o\(\))"   ).unwrap();

    for (_i, instruct) in input.split('m').enumerate()    // start of "<m>ul"
    {
        for (_j, action) in instruct.split('d').enumerate()    // start of "<d>o/n't"
        {
            if check_action( action, &re_dont )
            {
                do_add = false;
            }
            else if check_action( action, &re_do)
            {
                do_add = true;
            }
            else
            {
                // no action found, do_add unchanged
            }

            let n = check_valid_instruct( action, &re_mul );
            result_part_1 += n;
            if do_add
            {
                println!("adding {:?}", n);
                result_part_2 += n;
            }
        }
    }

    println!("The result part 1 is: {:?}", result_part_1);
    println!("The result part 2 is: {:?}", result_part_2);
}

//159892596
