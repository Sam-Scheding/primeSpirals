# primeSpirals

A coded implementation of the Ulam Spiral: https://en.wikipedia.org/wiki/Ulam_spiral

## Basic Premise

On a peice of paper, divided into a grid, start at the center square and write the number 1, then move outwards in an anti clockwise spiral, filling in the numbers as you go, like so:
```
  5 4 3
  6 1 2
  7 8 9
```

If you circle the primes as you go, a pattern will emerge as the spiral gets large; the primes will appear as if they streak off in diagonals:

![image](https://user-images.githubusercontent.com/4335944/145282752-d79a2cd7-b1bc-494e-89db-ff3b802a6829.png)

This program implements a way to see this phenomenon. 

## Usage

```bash
$ python primeSpirals.py <radius>

```

### Arguments

#### radius 

Must be an odd number so the spiral can be constructed evenly.

# Example Output

![image](https://user-images.githubusercontent.com/4335944/145281941-bee9b647-8a37-496b-bd62-c6d926b1b430.png)
