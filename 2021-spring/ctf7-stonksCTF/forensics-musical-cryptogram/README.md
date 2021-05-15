# Song of Flags
* **Event:** stonksCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
Since this sheet music doesn't exactly look like a real piece of music (certainly not a *good* piece of music), you can probably assume the flag is somehow encoded in the music. If you look up ways you can hide data/strings in sheet music, you should find information about [musical cryptograms](https://en.wikipedia.org/wiki/Musical_cryptogram). 

#### Step 2
If you look at the "French" method of encoding data, that is how the flag is encoded here. The following table shows how each letter of the flag is encoded as a note:

|   | **A** | **B** | **C** | **D** | **E** | **F** | **G**|
|---|---|---|---|---|---|---|---|
| ♯ | H | I | J | K | L | M | N |
| ♮ | O | P | Q | R | S | T | U |
| ♭ | V | W | X | Y | Z |   |   |

Using this table, you can decode the flag: `utflag{lolidkhowmusicworks}`.

**NOTE: In this specific problem I accidentally inccorrectly encoded 'O's as 'H's, so if you see an H in a weird spot, it should actually be an O.**
