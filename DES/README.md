# Data Encryption Standard
The DES (Data Encryption Standard) algorithm is a symmetric-key block cipher created in the early 1970s by an IBM team and adopted by the National Institute of Standards and Technology (NIST). The algorithm takes the plain text in 64-bit blocks and converts them into ciphertext using 48-bit keys.

To have a better understanding, don't forget to have a look at [Simpler version of DES.](https://github.com/SyedSahil80328/information-security/tree/main/SDES)

# Directory Structure
This directory consists of two python programs for execution.
1. `DESUtils.py`: For providing utility functions.
2. `DES.py`: Driver Program to be run.

It also consists of three files for required data. All contains numbers separated by commas.
1. `Credentials.txt`: Provides plain text and key.
  - First line is the 64 bit plain text.
  - Second line is the 64 bit key.
2. `Permutations.txt`: Provides permutation data for re-ordering.
  - First line is the Permutation Choice One for key (64-56).
  - Second line is the Permutation Choice Two for key (56-48).
  - Third line is the Initial Permutation (64-64).
  - Fourth line is the Expansion Permutation (32-48).
  - Fifth line is the Straight Permutation (16-16).
  - Sixth line is the Inverse Permutation (64-64).
3. `SubstitutionBoxes.txt`: Contains 8 contracting 8-6 substitution boxes (Each are 4x16 matrix). So, 32 lines of this file makes 8 S Boxes. 

Note: Editing `Credentials.txt` has some constraints.
1. Both lines must be binary.
2. Both lines must have exactly 64 bits.
3. No more or less lines than two is considered.

# Sample Input and Output
Here, I have pasted the sample output for it's better usage.

## Gathering Input from the file
![Input/Output Process](IO%20process.png)

## Encryption Process
![Encryption Process](Encryption.png)

## Decryption Process
![Decryption Process](Decryption.png)
