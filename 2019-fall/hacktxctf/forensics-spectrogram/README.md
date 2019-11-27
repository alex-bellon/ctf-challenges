# Beep Beep Boop
* **Event:** HackTXCTF 2019
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:** Sonic Visualizer or Audacity

## Steps​
#### Step 1
The prompt mentioned a message hidden in the audio file (as well as my talk from HackTXCTF Prep Day). Either of those clues should have pointed to you a form of audio steganography that hides information in spectrograms.

#### Step 2
The best tool to use to see spectrograms is [Sonic Visualizer](https://sonicvisualiser.org/). If you opened the audio file in Sonic Visualizer and then click `Pane` > `Add Spectrogram` in the menu bar, the spectrogram will pop up and you should be able to read the flag: `utflag{f33ling_wavy}`
