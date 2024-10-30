## Uzo_Uwaz-MiniProject8
 IDS 706 Week 8 : This is a recreation Week 2 Mini Project of Reading and Describing a Dataset. It establishes an environment on codespaces and uses Github Actinos to run a Makefile for : make install, make test, make format, and make lint. It loads the Top Wealthiest data set from Kaggler and runs a function to generate a pie chart as well as some summary statistics about the data. We utilized Rust to convert this code to a much faster format ! 

The data we will be analyzing will be from Kaggle.com. We will be analyzing the top 1000 wealthiest people in the world. (https://www.kaggle.com/datasets/muhammadehsan02/top-1000-wealthiest-people-in-the-world)

## Rust Implementation:

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

## Speed and Resource Usage:
[Link to Rust runtime Markdown File](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week8/blob/main/rust_times.md)
[Link to Python runtime Markdown File](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week8/blob/main/python_times.md)

You can view how long it takes to encrypt and decrypt the same messages above. Based on the speed, it's obvious Rust run on average 400 times faster than Python and we can infer why the resource usage is vastly smaller than Python. Rust outperforms Python in speed primarily due to its static typing, zero-cost abstractions, and absence of a Global Interpreter Lock (GIL). Rust's strict typing allows for more efficient compilation, while its ownership system enables high-performance abstractions without sacrificing safety. Additionally, Rust manages memory directly, avoiding the overhead of Python's garbage collector. The language also offers fine-grained control over memory, enabling low-level optimizations. These factors, combined with an optimized compiler and a performance-centric standard library, contribute to Rust's reputation for speed.

I also track the memory used in Rust and Python in the markdown files above. We can see that Rust barely uses memory whereas Python requires mb of memory for the same encryption and decryption to run.

## FINDINGS

See the sample chart below  of percentages of wealth per each industry described in the dataset 
![Alt Text](Piechart%20Image.png)

### From here we can see that Technology is the most lucrative of indsutries to immerse oneself in... I guess it's a lucky thing that we're studying Data Science! 

### The summary Statistics are as follows 
mean = 102 billion in networth 
std = 56 billion from mean 
min networth = 1.57 billion
max networth = 199 billion 






