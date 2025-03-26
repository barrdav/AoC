use std::fs;

const INPUT_PATH: &str = "../Input/4.txt";

fn read_lines(filename: &str) -> Vec<String> {
    let mut lines_read = Vec::new();

    for line in fs::read_to_string(filename).unwrap().lines()
    {
        lines_read.push(line.to_string())
    }

    lines_read
}

fn check_char(c1: &str, c2: &str, c3: &str, c4: &str) -> bool
{
    let mut found = false;

    if c1.starts_with("X") &&
       c2.starts_with("M") &&
       c3.starts_with("A") &&
       c4.starts_with("S") {
        found = true;
    }
    else if c1.starts_with("S") &&
            c2.starts_with("A") &&
            c3.starts_with("M") &&
            c4.starts_with("X") {
        found = true;
    }
    else {
//        println!("Not found in {:?}", s);
    }
    found
}


// Check X.M.A.S or S.A.M.X
fn check_horizon(lines: &Vec<String>, l: usize, x_pos: usize) -> bool
{
    let mut found = false;
    let this_line = &lines[l];
    let s = &this_line[x_pos..(x_pos+4)];

    if s.starts_with("XMAS") {
        found = true;
//        println!("FOUND horiz at {l} {x_pos}");
    }
    else if s.starts_with("SAMX") {
        found = true;
//        println!("FOUND horiz at {l} {x_pos}");
    }
    else {
//        println!("Not found in {:?}", s);
    }
    found
}

// Check X S
//       M A
//       A M
//       S X
fn check_vertical(lines: &Vec<String>, l: usize, x_pos: usize) -> bool
{
    let c1 = &lines[l][x_pos..x_pos+1];
    let c2 = &lines[l+1][x_pos..x_pos+1];
    let c3 = &lines[l+2][x_pos..x_pos+1];
    let c4 = &lines[l+3][x_pos..x_pos+1];

    check_char(c1, c2, c3, c4)
}

// Check X S
//        M A
//         A M
//          S X
fn check_diag_fwd(lines: &Vec<String>, l: usize, x_pos: usize) -> bool
{
    let c1 = &lines[l][x_pos..x_pos+1];
    let c2 = &lines[l+1][x_pos+1..x_pos+2];
    let c3 = &lines[l+2][x_pos+2..x_pos+3];
    let c4 = &lines[l+3][x_pos+3..x_pos+4];

    if check_char(c1, c2, c3, c4)
    {
//        println!("found diag fwd {l} {x_pos}", );
        return true
    }
    return false
}

// Check X S
//      M A
//     A M
//    S X
fn check_diag_back(lines: &Vec<String>, l: usize, x_pos: usize) -> bool
{
    let c1 = &lines[l][x_pos..x_pos+1];
    let c2 = &lines[l+1][x_pos-1..x_pos];
    let c3 = &lines[l+2][x_pos-2..x_pos-1];
    let c4 = &lines[l+3][x_pos-3..x_pos-2];

    if check_char(c1, c2, c3, c4)
    {
//        println!("found diag back {l} {x_pos}", );
        return true
    }
    return false
}

// M M  S M  M S  S S
//  A    A    A    A
// S S  S M  M S  M M
fn check_x_mas(lines: &Vec<String>, l: usize, x_pos: usize) -> bool
{
    let a  = &lines[l][  x_pos  ..x_pos+1];
    let c1 = &lines[l-1][x_pos-1..x_pos];
    let c2 = &lines[l-1][x_pos+1..x_pos+2];
    let c3 = &lines[l+1][x_pos-1..x_pos];
    let c4 = &lines[l+1][x_pos+1..x_pos+2];

    if !a.contains('A')
    {
        return false;
    }

    if c1.starts_with("M") &&
       c4.starts_with("S") {
    }
    else if c1.starts_with("S") &&
            c4.starts_with("M") {
    }
    else {
        return false;
    }

    if c2.starts_with("M") &&
       c3.starts_with("S") {
    }
    else if c2.starts_with("S") &&
            c3.starts_with("M") {
    }
    else {
        return false;
    }

    true
}

fn main() {
    let mut result_part_1: u32 = 0;
    let mut result_part_2: u32 = 0;

    let lines = read_lines( INPUT_PATH );

    let nb_lines = 140;   //TODO

    for (l, this_line) in lines.iter().enumerate()
    {
        println!("line {l} = {:?}", &lines[l]);

        let count = this_line.chars().count();
        for i in 0..count
        {
            if i <= count - 4
            {
                if check_horizon(&lines, l, i)
                {
                    result_part_1 += 1;
                }
                if l <= nb_lines - 4
                {
                    if check_diag_fwd(&lines, l, i)
                    {
                        result_part_1 += 1;
                    }
                }
            }
            if l <= nb_lines - 4
            {
                if check_vertical(&lines, l, i)
                {
                    result_part_1 += 1;
                }
            }
            if i >= 3 && l <= nb_lines - 4
            {
                if check_diag_back(&lines, l, i)
                {
                    result_part_1 += 1;
                }
            }

            if l > 0 && l < nb_lines - 1 && i > 0 && i < count - 1
            {
                if check_x_mas(&lines, l, i)
                {
                    result_part_2 += 1;
                }
            }
        }
    }


    println!("The result part 1 is: {:?}", result_part_1);
    println!("The result part 2 is: {:?}", result_part_2);
}

