# Garbage
* **Event:** TetrisCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:** [strings](https://linux.die.net/man/1/strings)

## Steps
#### Step 1
You can use the tool `strings` (hinted at in the prompt) to look for strings in the file. You can also use `grep` to search through those strings for the word "flag", or you can just look manually. 

```
$ strings tetris.png | grep "flag"
utflag{tetris_for_jeff}
```

