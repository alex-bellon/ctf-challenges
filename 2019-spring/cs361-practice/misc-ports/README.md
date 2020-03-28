# Ports 
* **Event:** CS361 Practice
* **Problem Type:** Misc
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
You will notice that all of the things provided in the prompt are protocols. They also have ports associated with them which can be found [here](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers).

#### Step 2
If you convert all of the protocols to their common port number, you get 
```
a = 22 + 43 = 65
b = 88 + 80 = 168
c = 20 + 443 = 463
d = 79 + 25 = 104
```
You can then plug those variables into the formula to get the flag: `83647`.
