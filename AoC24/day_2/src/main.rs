
use std::fs;

const INPUT_PATH: &str = "../../Input/2.txt";

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in fs::read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}

//return true if safe
fn check_dir(dir: i8, n: i32, p: i32) -> bool
{
    if (1 == dir) && (n > p)
    {
        true
    }
    else if (-1 == dir) && (n < p)
    {
        true
    }
    else
    {
        // not safe
        false
    }
}

//return true if safe
fn check_dist(dir: i8, n: i32, p: i32) -> bool
{
    if (1 == dir) && (n <= (p + 3))
    {
        true
    }
    else if (-1 == dir) && (n >= (p - 3))
    {
        true
    }
    else
    {
        false
    }
}

// return true if safe
// Skip the given index if not max
fn check_report(l: &str, skip_index: usize) -> bool
{
    let mut previous_n: i32 = 0;
    let mut dir: i8 = 0;
    let mut used_index = 0;
    for (i, n) in l.split_whitespace().enumerate()
    {
        // Convert string to int
        let n: i32 = n.trim().parse().expect("not a number!");

        println!("{:?}", n);

        if (skip_index != 65535) && (skip_index == i)
        {
            // skip this index
            println!("Skip this index {i}");
            continue;
        }

        if 0 == used_index
        {
            // First number -> initialize first number
        }
        else if 1 == used_index
        {
            // Second number -> init direction
            if n > previous_n
            {
                dir = 1;
            }
            else if n < previous_n
            {
                dir = -1
            }
            else
            {
                println!("same value!");
                return false;
            }

            // check the distance
            if !check_dist(dir, n, previous_n)
            {
                println!("{i} is not safe (dist)");
                return false;
            }

            //println!("n is {n} and p is {previous_n}, then dir is {:?}", dir);
        }
        else
        {
            // check the direction
            if !check_dir(dir, n, previous_n)
            {
                println!("{i} is not safe (dir)");
                return false;
            }

            // check the distance
            if !check_dist(dir, n, previous_n)
            {
                println!("{i} is not safe (dist)");
                return false;
            }
        }
        previous_n = n;
        used_index = used_index + 1;
    }

    if dir != 0
    {
        println!("it's safe!");
        true
    }
    else
    {
        false
    }
}


fn main() {
    println!("Input file: {INPUT_PATH}");

    let mut sum_part_1: u32 = 0;
    let mut sum_part_2: u32 = 0;

    let lines = read_lines( INPUT_PATH );
    for (l, this_line) in lines.iter().enumerate()
    {
        println!("Line {l} = {:?}", this_line);

        if check_report(this_line, 65535)
        {
            sum_part_1 = sum_part_1 + 1;
            sum_part_2 = sum_part_2 + 1;
        }
        else
        {
            // try to remove one element for part 2
            for (i, n) in this_line.split_whitespace().enumerate()
            {
                if check_report(this_line, i)
                {
                    sum_part_2 = sum_part_2 + 1;
                    break;
                }
            }

        }
    }

    println!("The result part 1 is: {:?}", sum_part_1);
    println!("The result part 2 is: {:?}", sum_part_2);
}

