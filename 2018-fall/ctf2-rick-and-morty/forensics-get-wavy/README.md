# Get Schwifty
* **Event:** RickAndMortyCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
If you try to play the audio, at the end it starts to sound all garbled, because there is [information hidden in the spectrogram](https://solusipse.net/blog/post/basic-methods-of-audio-steganography-spectrograms/). 

#### Step 2
If you open the song in [Sonic Visualizer](https://sonicvisualiser.org/) (Audacity also works but I prefer Sonic), and add the spectrogram pane, you will be able to see the flag: `utctf{i_h@t3_this_s0ng_s0_much}`.
