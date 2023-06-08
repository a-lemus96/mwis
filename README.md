# Maximum Weighted Independent Set (MWIS)

This repository contains a divide and conquer (D&C) solution to the maximum weighted independent set (MWIS) for path graphs. It also contains a dynamic programming solution (DP) to verify algorithm correctness. Both D&C and DP solutions are coded as methods inside `mwis.py`. Script `test.py` runs both methods over one of the files stored in `data/` folder and displays the total weight for each solution.

### Data format
`data/` folder contains the following files: `wis1.txt`, `wis2.txt` and `wis3.txt`. The format for each text file is
```
N -> Length of the array
A1 -> Element 1
A2 -> Element 2 
.
.
.
AN -> Element N
```

### Running the test
In order to solve the problem using both approaches and compare the total weight for each solution (this is done because there is no guarantee for the existence of a unique solution, especially for arbitrary large arrays), simply run `python test.py -file FILE` where `FILE` is one of the text files inside `data/` folder. The output should look like this:

![image](https://github.com/a-lemus96/mwis/assets/95151624/ba49e07f-4418-4cb5-9154-b613f22bb9e6)
