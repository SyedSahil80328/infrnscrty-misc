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
3. Needs exactly two lines.
4. Misordering of inputs will result in unexpected encryption (Plain text will become key and vice-versa).

It is recommended not to edit `Permutations.txt` and `SubstitutionBoxes.txt`. If it is required, then handle the modification carefully.
1. `SubstitutionBoxes.txt` must have 32 lines with 16 unique values each ranging from 0 to 15 in random order separated by commas.
2. Inclusion of whitespaces between values in both files will result in errors.
3. `Permutations.txt` must have 6 lines with following specifications:
     - First line must have 56 unique values from 1 to 64.
     - Second line must have 48 unique values from 1 to 56.
     - Third line must have 64 unique values from 1 to 64.
     - Fourth line must have 48 values from 1 to 32.
     - Fifth line must have 16 unique values from 1 to 16.
     - Sixth line must have 64 unique values from 1 to 64.
     - All lines must have values separated by commas without whitespaces.

# Sample Input and Output
Here, I have pasted the sample output for it's better usage.

## Gathering Input from the file
![Input Process](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/InputReading.png)

## Permutations and key generation
![Round Keys and Permutations](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/RoundKeysAndPermutations.png)

## Encryption Process
![Iteration 1-2](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/EncryptionOne.png)
![Iteration 3-4](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/EncryptionTwo.png)
![Iteration 5-6](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/EncryptionThree.png)
![Iteration 7-8](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/EncryptionFour.png)
![Iteration 9-10](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/EncryptionFive.png)
![Iteration 11-12](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/EncryptionSix.png)
![Iteration 13-14](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/EncryptionSeven.png)
![Iteration 15-16](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/EncryptionEight.png)
![Final Output](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/FinalEncryption.png)

## Decryption Process
![Iteration 1-2](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/DecryptionOne.png)
![Iteration 3-4](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/DecryptionTwo.png)
![Iteration 5-6](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/DecryptionThree.png)
![Iteration 7-8](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/DecryptionFour.png)
![Iteration 9-10](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/DecryptionFive.png)
![Iteration 11-12](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/DecryptionSix.png)
![Iteration 13-14](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/DecryptionSeven.png)
![Iteration 15-16](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/DecryptionEight.png)
![Final Output](https://github.com/SyedSahil80328/information-security/blob/main/DES/DESOutput/FinalDecryption.png)
