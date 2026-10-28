# Computer Architecture – Python Assignments

This repository contains two Python programs developed as part of my Computer Architecture assignment.

## Program 1: LRU Cache Replacement Algorithm

### Objective
To simulate the Least Recently Used (LRU) cache replacement algorithm for a cache with a capacity of 3 memory blocks.

### Input
- Cache capacity: 3 blocks
- Access sequence: `4, 2, 1, 4, 3, 2, 5, 4`

### Description
The program processes each memory block in the given access sequence and displays whether the access is a HIT or MISS, the current cache contents, and the block removed when replacement is required.

It also calculates the total number of hits, total misses, and hit ratio.

### Results
- Total accesses: 8
- Total hits: 1
- Total misses: 7
- Hit ratio: 12.50%

---

## Program 2: Effective Access Time (EAT) Using TLB

### Objective
To calculate the Effective Access Time (EAT) of a memory system using a Translation Lookaside Buffer (TLB) and compare the results for two different TLB hit ratios.

### Input Parameters
- TLB lookup time: 10 ns
- Main memory access time: 80 ns
- First TLB hit ratio: 0.90
- Second TLB hit ratio: 0.75

### Formula
EAT = h × (TLB lookup time + memory access time) + (1 − h) × (TLB lookup time + 2 × memory access time)

Where:
- `h` = TLB hit ratio
- TLB lookup time = time required to search the TLB
- Main memory access time = time required to access main memory

### Results

**For a TLB hit ratio of 0.90:**

EAT = 0.90 × (10 + 80) + 0.10 × (10 + 2 × 80)

EAT = 81 + 17 = 98 ns

**For a TLB hit ratio of 0.75:**

EAT = 0.75 × (10 + 80) + 0.25 × (10 + 2 × 80)

EAT = 67.5 + 42.5 = 110 ns

### Comparison
- EAT at a hit ratio of 0.90: 98 ns
- EAT at a hit ratio of 0.75: 110 ns
- Difference: 12 ns

A higher TLB hit ratio results in a lower effective access time because more memory accesses can be completed without requiring an additional main memory access.

---

## Technologies Used
- Python 3
- Visual Studio Code

## How to Run
Run either Python program from the terminal:

```bash
python filename.py
```

Replace `filename.py` with the actual name of the Python file you want to execute.

## Learning Outcomes
- Understanding cache replacement using the LRU algorithm.
- Understanding TLB hits and misses.
- Calculating effective memory access time.
- Comparing memory performance under different TLB hit ratios.
