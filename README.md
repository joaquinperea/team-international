
# Team International Trial

This is a solution to the evaluation presented 
by Team International in its hiring process.

Author: Eng. Joaquin Perea



## SetUp

This project only use "pytest" library for testing tasks.
To set up this solution, create a virtual environment and activate it:

```bash
  python3 -m pip install --user virtualenv
  python3 -m venv /path/to/new/virtual/environment
  source venv/bin/activate
```

After you activate the virtual environment, install "pytest":

```bash
  python3 -m pip install --user pytest
```
## Testing
To run project tests after installing "pytest", execute in console:

```bash
  pytest
```

## Process and Decisions
The requirements for the methods of the "DataCapture" class defined that the "add" method must have a time complexity 
of O(1), while the "build_stats" method, of O(n) at most.
Due to this, I decided to include in the "build_stats" method the generation of a dictionary based on the elements 
that were added to the list throughout the execution time. This means that each element of the dictionary has 
information about how many minor and major elements it has in the array, contemplating the cases of repeated numbers.
This allows that when executing the methods of the "Stats" class, they are kept in a time complexity of O(1).