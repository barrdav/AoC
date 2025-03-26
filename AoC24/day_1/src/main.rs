
use std::fs;

//const INPUT_PATH: &str = "../../Input/test.txt";
const INPUT_PATH: &str = "../../Input/1.txt";

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in fs::read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}

fn searchNumber(n_to_find: u32, list: &Vec<u32>) -> u32
{
    let mut num_of: u32 = 0;

    for (i, n) in list.iter().enumerate()
    {
        if *n == n_to_find
        {
            println!("Found {n_to_find}");
            num_of = num_of + 1;
        }
    }
    num_of
}


fn main() {
    println!("Input file: {INPUT_PATH}");

    let mut col_A: Vec<u32> = vec![];
    let mut col_B: Vec<u32> = vec![];
    let mut sum: u32 = 0;

    let lines = read_lines( INPUT_PATH );
    for (_i, this_line) in lines.iter().enumerate()
    {
        // Create a vector for each column
        let mut i = 0;
        // Separate each line in 2 parts separated by space
        for n in this_line.split_whitespace()
        {
            // Convert string to int
            let n: u32 = n.trim().parse().expect("not a number!");
            if i == 0
            {
                col_A.push(n);
            }
            else
            {
                col_B.push(n);
            }
            i += 1;
        }
    }

    // search each number from the first column in the second column
    for n in col_A.iter()
    {
        println!("Search for {n}");
        sum = sum + (n * searchNumber(*n, &col_B));
    }

    println!("The result is: {:?}", sum);
}

