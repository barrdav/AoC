use std::fs;

const INPUT_PATH: &str = "../Input/test.txt";


struct Rule {
    before: u32,
    after: u32
}

fn read_lines(filename: &str) -> Vec<String> {
    let mut lines_read = Vec::new();

    for line in fs::read_to_string(filename).unwrap().lines()
    {
        lines_read.push(line.to_string())
    }

    lines_read
}

// Get one order rule from one line
// Return true if not a rule (last rule found)
fn get_rule(this_line: &str, rule_list: &mut Vec<Rule>) -> bool
{
    let this_rule_line = this_line.split('|');      // one line with the order of 2 numbers
    if this_rule_line.clone().count() != 2
    {
        println!("End of Rules.");
        return true
    }

    let mut n_before: u32 = 0;
    for rule_part in this_rule_line.enumerate()
    {
        // Convert string to int
        let n: u32 = rule_part.1.parse().unwrap();

        if rule_part.0 == 0     // firt number "before"
        {
            n_before = n;

        }
        else            // Second number "after"
        {
            let this_rule = Rule {
                before: n_before,
                after:  n
            };
            rule_list.push(this_rule);
        }
    }
    return false
}

// Check all rules on one manual and return true if OK
fn check_manual(safety_manual: &Vec<u32>, rule_list: &Vec<Rule>) -> bool
{
    for this_rule in rule_list
    {
        let pos_before  = safety_manual.iter().position(|&x| x == this_rule.before);
        if  pos_before != None
        {
            // Found first number of the rule
            let pos_after  = safety_manual.iter().position(|&x| x == this_rule.after);
            if  pos_after != None && pos_before > pos_after
            {
                // Found second number and rule fails, abort this manual
                println!("Rule failed at index {:?}", pos_before);
                return false
            }
        }
    }

    return true
}


fn swap_page(report: &mut Vec<u32>, i1: usize, i2: usize)
{
    let swap   = report[i1];
    report[i1] = report[i2];
    report[i2] = swap;
}

fn main() {

    let mut result_part_1: u32 = 0;
    let mut result_part_2: u32 = 0;

    let mut rule_list: Vec<Rule> = vec![];
    let mut end_build_rules = false;

    let lines = read_lines( INPUT_PATH );
    for (_l, this_line) in lines.iter().enumerate()
    {
        if false == end_build_rules
        {
            // Step 1: Build the rules
            end_build_rules = get_rule( this_line, &mut rule_list );
        }
        else
        {
            // Step 2: Check the rules for each manual,

            // Create a vector of the safety_manual
            let mut safety_manual: Vec<u32> = vec![];
            let this_manual_line = this_line.split(',');
            for manual_page in this_manual_line.enumerate()
            {
                let page_to_add: u32 = manual_page.1.parse().unwrap();
                safety_manual.push(page_to_add);
            }

            // For each line of safety_manual, verify each rule.
            // Search first and second number in the safety_manual,
            // and verify in which this_rule_line they are found
            // If only one found -> OK
            println!("\nProcessing {:?}", safety_manual);

            let is_manual_ok = check_manual( &safety_manual, &rule_list );

            // Get the middle value for manual without error
            if is_manual_ok
            {
                let n: usize = (safety_manual.len() / 2).try_into().unwrap();
                println!("Middle page = {:?}", safety_manual[n]);
                result_part_1 += safety_manual[n];
            }
            else
            {
            //    unimplemented!();
            }
        }
    }

    // TEST SWAP
    let mut test_swap = vec![1, 2, 3];
    println!("{:?}", test_swap);
    swap_page(&mut test_swap, 0, 2);
    println!("{:?}", test_swap);

    // Part 2: repeat rule check until no error found
    // swap value on error
    // Take middle value of manual with reorder only
    // use a flag: re-ordered
    result_part_2 += 1;

    println!("The result part 1 is: {:?}", result_part_1);
    println!("The result part 2 is: {:?}", result_part_2);
}

// crate IndexList  swap_index( index_a, index_b )