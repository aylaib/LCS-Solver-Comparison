# Longest Common Subsequence (LCS) Problem Solver
This project, carried out as part of the "Combinatorial Optimization Elements" module (Master 1 Bioinformatics, USTHB), explores and compares two algorithmic approaches to solve the Longest Common Subsequence (LCS) problem.
The objective is to analyze the performance of an **exact method (DFS)** compared to a **metaheuristic (Tabu Search)** in terms of execution time and solution quality.
## 📈 Implemented Algorithms
The `LSC.py` script contains the implementation of the following two methods:
### 1. Exact Method: Depth-First Search (DFS)
- **Principle:** Exhaustively explores all possible subsequences to guarantee the discovery of the optimal solution.
- **Advantages:** Provides a solution guaranteed to be the longest.
- **Disadvantages:** Temporal complexity is exponential, making it impractical for large sequences.
### 2. Metaheuristic: Tabu Search
- **Principle:** An advanced optimization method that intelligently navigates the solution space to find a high-quality solution in reasonable time.
- **Mechanisms:** Uses a "tabu list" to avoid returning to recently visited solutions, allowing it to escape local optima.
- **Advantages:** Much faster than the exact method, especially for large instances.
- **Disadvantages:** Does not guarantee finding the optimal solution, but aims for a quasi-optimal solution.
## 🚀 How to Use
The `LSC.py` script is an interactive command-line application.
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/LCS-Solver-Comparison.git
    cd LCS-Solver-Comparison
    ```
2.  **Run the script:**
    ```bash
    python LSC.py
    ```
3.  **Follow the instructions:**
    - Enter the alphabet to use (e.g., `ACGT` for DNA).
    - Specify the number of sequences and their respective lengths.
    - Choose the algorithm to test (DFS or Tabu Search).
    - Indicate the indices of the two sequences you want to compare.
4.  The program will display the LCS found, execution time, number of comparisons, and a summary table at the end.
## 📊 Results and Analysis
The comparative analysis shows that:
- **DFS** is very efficient for small sequences but its execution time explodes rapidly.
- **Tabu Search** maintains stable and much lower execution time, even for longer sequences, while providing high-quality solutions.
For a detailed analysis, comparative graphs and a discussion on complexity, please consult the complete report.

    ## 📌 Citation
If you use this project, please cite it as:

Ayoub Laib (2025), *Longest Common Subsequence (LCS) Problem Solver*, GitHub repository: https://github.com/aylaib/LCS-Solver-Comparison


## 📚 Reference Documents
- **[Complete Project Report](./Rapport_Projet_LCS.pdf)** : This document contains the introduction to the LCS problem, detailed description of algorithms, experimental results and their analysis.
