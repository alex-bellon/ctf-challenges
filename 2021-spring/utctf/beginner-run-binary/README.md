# Run-ELF
* **Event:** UTCTF 2021
* **Problem Type:** Beginner
* **Point Value / Difficulty:**
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
This challenge is pretty straightforward: you're given an ELF file, and the prompt mentions that you have to figure out how to run it. If you look up what an [ELF file](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) is, you'll see that it's an executable file format used in UNIX-like systems (basically the equivalent of an `.exe` in Windows).

#### Step 2
In order to run it, you'll need access to an UNIX terminal. On Mac and Linux you have these built in, and on Windows you might have to use something like [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux). In order to run the executable you can just use the command

```shell
./run
```

and it will spit out the flag `utflag{run_run_binary_9312854}`.
