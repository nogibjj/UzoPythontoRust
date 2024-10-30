## Uzo_Uwaz-MiniProject8
 IDS 706 Week 8 : This is a recreation Week 2 Mini Project of Reading and Describing a Dataset. It establishes an environment on codespaces and uses Github Actinos to run a Makefile for : make install, make test, make format, and make lint. It loads the Top Wealthiest data set from Kaggler and runs a function to generate a pie chart as well as some summary statistics about the data. We utilized Rust to convert this code to a much faster format ! 

The data we will be analyzing will be from Kaggle.com. We will be analyzing the top 1000 wealthiest people in the world. (https://www.kaggle.com/datasets/muhammadehsan02/top-1000-wealthiest-people-in-the-world)

## Rust Implementation :ballot_box_with_check: 

### Preparation and Dependency Installation: 
1. Install Rust : in bash : `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
2. open codespaces 
3. wait for codespaces to be built 
4. build: `cargo build` for dependencies installation
5. run: `cargo run --  --message "Off to the bunker. Every person for themselves" --encrypt` or use your own string

### Check Format and Test Erros: 
1. Format code `make format`
2. Lint code `make lint`
3. Test coce `make test`

## Python Implementation:
This python version uses libraries like pandas to read a csv and matplotlib for plotting relevant data.


### Preparation: 
1. git clone the repo
2. install: `make python_install`
3. install:   

### Check Format and Test Errors: 
1. Format code `make python_format`
2. Lint code `make python_lint`
3. Test coce `make python_test`

## FINDINGS

See the sample chart below  of percentages of wealth per each industry described in the dataset 
![Alt Text](Piechart%20Image.png)

### From here we can see that Technology is the most lucrative of indsutries to immerse oneself in... I guess it's a lucky thing that we're studying Data Science! 

## :ballot_box_with_check: The summary Statistics are as follows 
mean = 102 billion in networth 
std = 56 billion from mean 
min networth = 1.57 billion
max networth = 199 billion 

## Takeaways
We see that Rust is much faster than python. However due to a rather strict compiler Rust is much more limited in its capabilities for now. In this project I was unable to create a piechart due to a rather complicated Plotter library that I would rather not deal with. Rust is so powerful though because with a package as powerful as Cargo. You can ensure `build` , `run` and `test` all work directly from the command line. 


## Speed and Resource Usage:

| Metric           | Rust                          | Python                        |
|------------------|-------------------------------|-------------------------------|
| **Memory Usage** | 5476352 kilobytes                  | 232.00 Kilobytes           |
| **Runtime**      | 1.5631420 seconds        | 0.0370762 seconds          |


- **Memory Efficiency**: Python uses ~98% less memory, making it more suitable for small-scale tasks. Python’s garbage collector automatically     reclaims memory, which can sometimes appear more efficient if the Rust code is not optimized for memory management.
- **Execution Speed**: Python is faster due to lower overhead, while Rust's extra time comes from system-level operations. Python can also be more optimized for execution speed using native libraries. 
- **Use Case**: Python is ideal for small tasks, while Rust shines in larger, more complex, or resource-heavy scenarios. Ultimately, Python libraries offer high-level abstractions and efficient algorithms for common tasks (e.g., matrix multiplication in NumPy), which can make the Python script appear faster and more memory-efficient.





