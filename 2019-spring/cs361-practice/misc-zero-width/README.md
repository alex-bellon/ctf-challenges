# Zero Width
* **Event:** CS361 Practice
* **Problem Type:** Misc
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
If you try to copy the flag and submit it, it won't work. But, if you copy the flag into something like `vim`, you will see that there are extra characters in there: `utflag{this<200b>_is<200b>_literally<200b>_the<200b>_flag}`;

#### Step 2
Those characters are [zero width characters](https://en.wikipedia.org/wiki/Zero-width_space) that cannot be seen when printed. If you remove them (or copy the flag by hand), the flag will work: `utflag{this_is_literally_the_flag}`.
