# Binary Exploitation

These challenges focus on you figuring out how stuff works. They go from easy to not so easy. (Challenges 1 and 3 written by ExpertCactus, 2 and 4 written by NuclearFarmboy)

### BINARY1: Stacks On Stacks On Stacks (Phat Stacks)  
There's a flag somewhere in there. How do you see the stack?

**VALUE: 1 point||**
**FLAG: flag[flag]**

### BINARY2: FoRmAt StRiNgS

We take what you give us, and we evaluate it with printf().

**PLOT TWIST!**

The flag is already in there, and we try to print it using printf with the format string you give us and that format string IS THE REAL FLAG.


**VALUE: 2 points||**
**FLAG: the format string used to print the flag**


### BINARY3: Buffer? I hardly know'er!
So here's a binary. It has a non-executable stack (womp womp) but no stack protections. But there is a function that prints the flag. How do you get to that vulnerable function?

**VALUE: 3 points||**
**FLAG FORMAT: shellcode/exploit/address/etc. you used and a screenshot of printing the flag**

### BINARY4: Mario Style
Step 1. Turn aslr off.  

'''
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
'''

Step 2. Compiled with executable stack and no stack protections. 
Step 3. Smash.
Step 4. Spawn shell.
Step 5. ???
Step 6. Profit. 

**VALUE: 4 points||**
**FLAG: the shellcode you used and a screenshot you got a shell**

