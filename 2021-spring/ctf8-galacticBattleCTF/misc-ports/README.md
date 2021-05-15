# Following Protocol
* **Event:**
* **Problem Type:**
* **Point Value / Difficulty:**
* **(Optional) Tools Required / Used:**


## Steps
#### Step 1
All of these acronyms are different protocols, and since it looks like we're doing math with them, we're going to need to get them in number form somehow. Luckily, each protocol usually operates on a specific port on your computer, which are handily listed on [this Wikipedia article](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers).

#### Step 2
After converting all of the protocols to their respective port numbers, here is what the math should look like:

```
a = SSH + HTTP = 22 + 80 = 102
b = RDP - NTP = 3389 - 123 = 3266
c = (Telnet + FTP) * SMTP = (23 + 21) * 25 = 1100
d = STUN * Echo = 3478 * 7 = 24346

flag = c(a + b) - d = 1100 (102 + 3266) - 24346 = 3680454
```
