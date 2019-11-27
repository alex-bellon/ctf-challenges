# Packet Hacker
* **Event:** HackTXCTF 2019
* **Problem Type:** Networking
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:** Wireshark, Bless

## Steps​
#### Step 1
If you open the `.pcap` in Wireshark, you will see that it's full of a bunch of USB traffic. There are a lot of frames where thousands of bytes are being transferred - these are where files were being moved back and forth from the USB drive.

#### Step 2
If you look at all of the large transfers of data, you will see that most of them are transferring text files containing different books. But one of the specific frames has a PNG header in the data:

```
0000   80 54 b2 96 5e 9f ff ff 43 03 81 02 03 00 2d 00   .T..^...C.....-.
0010   8f 0c 9e 5d 00 00 00 00 4c de 09 00 00 00 00 00   ...]....L.......
0020   00 e0 01 00 00 f0 00 00 00 00 00 00 00 00 00 00   ................
0030   00 00 00 00 00 00 00 00 01 02 00 00 00 00 00 00   ................
0040   89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52   .PNG........IHDR
0050   00 00 02 bc 00 00 01 d3 08 06 00 00 00 c5 f0 cb   ................
0060   51 00 00 18 2a 7a 54 58 74 52 61 77 20 70 72 6f   Q...*zTXtRaw pro
0070   66 69 6c 65 20 74 79 70 65 20 65 78 69 66 00 00   file type exif..
0080   78 da ad 9a 69 92 1b 39 92 85 ff c7 29 e6 08 d8   x...i..9....)...
0090   1d 38 0e e0 00 cc e6 06 73 fc f9 5e 90 a5 92 54   .8......s..^...T
00a0   d5 dd d6 d3 93 29 25 c9 60 10 01 f8 f2 16 04 9f   .....)%.`.......
00b0   f3 3f ff 7d 9f ff e2 a7 5a 08 4f a9 d6 db 68 2d   .?.}....Z.O...h-
00c0   f0 53 46 19 69 f2 a4 87 cf cf e7 31 86 f2 fe 7d   .SF.i......1...}
00d0   7f 96 87 f4 3d fa cb f1 67 e7 ef d3 c4 63 e6 31   ....=...g....c.1
.
.
.
```

#### Step 3
If you copy that data as a hex stream, and then use Bless to create a new file from that hex, you should have enough data to create the top half of an image that reads: `utflag{lemme_capture_ur_packets}`.
