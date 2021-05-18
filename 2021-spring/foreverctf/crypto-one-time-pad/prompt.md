# OTP

Two of my friends were arguing about which ice cream flavor is the best, but they encrypted it with the only information-theoretically secure cipher because they didn't want anyone to see. Lucky for us, they reused the same key; can you recover it?

Here are the ciphertexts:
```
213c234c232228234828371a49300d263324421928333728354927347f2c273723413a3b32363b2a2d3522
3b3b463829225b352d32207f20301a43313b271e2952272b263f21357f283d5924352b322a3731343e3846
```

_by balex_

## Hint

Try to read up on how the [One Time Pad](https://en.wikipedia.org/wiki/One-time_pad) works, and look into what happens when you reuse the same key twice and how you can use that to recover the key (which is the flag in this case).

## Hint 2

[This article](https://samwho.dev/blog/toying-with-cryptography-crib-dragging/) has a good explanation of how cribdragging works, and you can use [this online tool](https://toolbox.lotusfa.com/crib_drag/) to make it easier.

## Hint 3

The prompt says that they were arguing about which ice cream flavors are the best, so try messages that start with something like 'The best ice cream flavor is'.
