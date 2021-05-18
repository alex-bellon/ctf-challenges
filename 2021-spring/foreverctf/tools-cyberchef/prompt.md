# Intro to CyberChef

CyberChef is a super powerful tool developed by GCHQ (basically the British version of NSA) that has a ton of encoding/decoding, encrypting/decrypting and enciphering/deciphering tools that you can chain together into one larger program. As you can imagine, this makes CyberChef a very useful and powerful tool for cryptography (and sometimes forensics or miscellaneous) CTF problems. It gives you so many powerful tools in one place that it's indispensable tool for competing in CTFs.

You can access it online at [CyberChef](https://gchq.github.io/CyberChef/), or if you don't feel comfortable sending super secret CTF data to the British government, you can run it locally using their code on [GitHub](https://github.com/gchq/CyberChef).

There are four main panels on CyberChef: Operations, Recipe, Input and Output.
- **Operations**: This pane contains all possible "ingredients" you can add to your recipe, like "From Bas64" which decodes from Base64, or 'To Binary", which encodes to binary. The pane is divided into different sections to help you find relevant operations, and there's also a search bar if you already know what operation you're looking for.
- **Recipe**: This is the current overall "program" you are running, made up of all the different operations you added. This is what gets run on the input. You can drag operations from the Operations pane into the Recipe pane to build your "program", and drag to rearrange which operations happen in which order. To delete an operation from the recipe, just drag it out of the recipe pane and it should disappear, or, clear the whoel recipe with the Trash icon at the top. Each operation in the recipe allows you to change different settings for the operation with different drop down menus and checkboxes, and you can also disable individual operation or set breakpoints after they finish using the two gray icons in the top right of the operation box.
- **Input**: This one is pretty straightforward, this is where you put your input text that you want the recipe to run on. You can also open multiple tabs for multiple streams of input, as well as import files and folders to use as input.
- **Output**: Another straightforward panel, this is where you will see the output of your program. You can copy or export the output, as well as quickly move the current output to the input panel.

The last big part of CyberChef is the **Bake** button: this actually runs your recipe. If you have **Auto Bake** checked, CyberChef will automatically run the recipe for you and update the output as you change the recipe or input. You can also use the **Step** button to step through individual operations in your recipe instead of the whole thing.

Now that you're familiar with CyberChef, see if you can use it to decode the following message. You can use the hints below if you're stuck at a step.

```
01011010 01010111 01010010 01110111 01100100 01101101 01110100 01111000 01100101 00110011 01101000 00110101 01011010 00110001 00111001 01110000 01100101 01010111 01010110 01101001 01100010 00110001 00111001 01110100 01100101 01011000 01101100 00110001 01100011 00110011 01101000 01111000 01011000 00110010 01100100 01111010 01011010 01001000 01001010 01100110 01100010 01010111 01101100 01110011 01100010 00110010 01001010 01110100 01100011 01101101 00111001 01110111 01100110 01010001 00111101 00111101
```

_by balex_

## Hint 1

This encoding only uses 0s and 1s, and it pretty common in computer science.

## Hint 2

Uh-oh, looks like we have another block of text, with some sort of special encoding. Can you figure out what this encoding is? (hint: if you look carefully, you\'ll notice that there only characters present are A-Z, a-z, 0-9, and sometimes / and +, so 64 characters in total. See if you can find an encoding that looks like this one.)

## Hint 3

New challenge! Can you figure out what\'s going on here? It looks like the letters are shifted by some constant. (hint: you might want to start looking up Roman people).
