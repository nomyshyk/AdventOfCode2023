use std::collections::{HashMap};
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

// Task - 2
fn main() {
    // File must exist in the current path
    if let Ok(lines) = read_lines("./input4_2.txt") {
        println!();
    
        let mut result_map: HashMap<i32, i32> = HashMap::new();
        let mut result_list: Vec<i32> = Vec::new();
       
        // Consumes the iterator, returns an (Optional) String
        for (idx, line) in lines.flatten().enumerate() {
            let score = save_input_upd_2(&line);
            let idx32 = idx as i32;

            match result_map.get(&idx32) {
                Some(count) => { 
                    result_map.insert(idx32, count + score); 
                }
                None => { 
                    result_map.insert(idx32, score);
                    result_list.push(score);
                }
            };
        }

        let mut cards : Vec<i128> = Vec::with_capacity(result_map.len());

        for (_key, _val) in &result_map {
            cards.push(1);
        }

        let mut idx_s = 0;
        for val in result_list {
            for it in 1..val+1 {
                println!("iter val={}, it={}", val, it);
                cards[(idx_s + it) as usize] += cards[idx_s as usize]
            }
            idx_s +=1;
        }

        let zis = cards.iter().sum::<i128>();
        
        println!("final result is = {}", zis);
    }

}


//Task - 1 
// fn main() {
//     // File must exist in the current path
//     if let Ok(lines) = read_lines("./input4_1.txt") {
//         println!();
//         let mut summa = 0;
//         let mut result_map: HashMap<i32, i32> = HashMap::new();
//         // Consumes the iterator, returns an (Optional) String
//         for (idx, line) in lines.flatten().enumerate() {
//             summa += save_input_upd(&line);
//         }
//         println!("final result is = {}", summa);
//     }
// }

// The output is wrapped in a Result to allow matching on errors.
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

// task 1
// fn save_input_upd(text_line: &str) -> i32 {
    
//     let pos_start_win = text_line.find(":").unwrap() + 1;
    
//     let mut num_beg : i32 = -1;
//     let mut number_build: String = "".to_string();
//     let mut map_numbers: HashMap<i32, i32> = HashMap::new();
//     let mut is_win = 1;

//     let substr = text_line[pos_start_win..text_line.len()].to_string();
//     for (idx, symb) in substr.chars().enumerate() {
//         if symb == '|' {
//             is_win = -1;
//             continue;
//         } 

//         if symb == ' ' {
//             if num_beg == -1 {
//                 number_build.clear();
//                 num_beg = -1; 
//             } else {
//                 match number_build.parse::<i32>() {
//                     Ok(n) => {
//                         match map_numbers.get(&n) {
//                             Some(count) => { map_numbers.insert(n, count + is_win); }
//                             None => { map_numbers.insert(n, is_win); }
//                         } 
//                         },
//                     Err(e) =>
//                         panic!("this is a terrible mistake {}!", e),
//                   }
//                 num_beg = -1; 
//                 number_build.clear();
//             }
//         } else {
//             if num_beg == -1 {
//                 num_beg = idx as i32
//             } 
//             number_build.push(symb);
            
//             // For last char in line
//             if idx == substr.len()-1 {
//                 match number_build.parse::<i32>() {
//                     Ok(n) => {
//                         match map_numbers.get(&n) {
//                             Some(count) => { map_numbers.insert(n, count + is_win); }
//                             None => { map_numbers.insert(n, is_win); }
//                         } 
//                         },
//                     Err(e) =>
//                         panic!("this is a terrible mistake {}!", e),
//                   }
//                 num_beg = -1;
//                 number_build.clear();
//             }
//         }
//     }

//     let mut cnt = 0;
//     for (key, val) in map_numbers {
        
//         if val == 0 {
//             cnt += 1;
//         }    }

//     match cnt {
//         0 => return 0, 
//         _ => return (2 as i32).pow(cnt-1)
//     } 
    
// }

// task 2
fn save_input_upd_2(text_line: &str) -> i32 {
    
    let pos_start_win = text_line.find(":").unwrap() + 1;
    
    let mut num_beg : i32 = -1;
    let mut number_build: String = "".to_string();
    let mut map_numbers: HashMap<i32, i32> = HashMap::new();
    let mut is_win = 1;

    let substr = text_line[pos_start_win..text_line.len()].to_string();
    for (idx, symb) in substr.chars().enumerate() {
        //print!("symb = {}", symb);
        if symb == '|' {
            is_win = -1;
            continue;
        } 

        if symb == ' ' {
            if num_beg == -1 {
                number_build.clear();
                num_beg = -1;
            } else {
                match number_build.parse::<i32>() {
                    Ok(n) => {
                        match map_numbers.get(&n) {
                            Some(count) => { map_numbers.insert(n, count + is_win); }
                            None => { map_numbers.insert(n, is_win); }
                        } 
                        },
                    Err(e) =>
                        panic!("this is a terrible mistake {}!", e),
                  }
                num_beg = -1;
                number_build.clear();
            }
        } else {
            if num_beg == -1 {
                num_beg = idx as i32
            } 
            number_build.push(symb);
            
            // For last char in line
            if idx == substr.len()-1 {
                match number_build.parse::<i32>() {
                    Ok(n) => {
                        match map_numbers.get(&n) {
                            Some(count) => { map_numbers.insert(n, count + is_win); }
                            None => { map_numbers.insert(n, is_win); }
                        } 
                        },
                    Err(e) =>
                        panic!("this is a terrible mistake {}!", e),
                  }
                num_beg = -1;
                number_build.clear();
            }
        }
    }

    println!("{}", "");
    let mut cnt = 0;
    for (key, val) in map_numbers {
        
        if val == 0 {
            cnt += 1;
        }
    }

    return cnt;
    
}