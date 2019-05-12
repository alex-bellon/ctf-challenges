#!/bin/bash

printf "\n"
echo -n "Flag: "
read flag

mkdir secret
cd secret
echo "text 15,15 "$flag"" > flag.txt

convert -size 300x300 xc:white -font "Noto-Sans-Regular" -pointsize 12 -fill black -draw @flag.txt flag.png
rm -f flag.txt

cd ..
zip -r secret.zip secret/ &> /dev/null

echo -n "File to hide in: "
read cover

echo -n "Name for new file (must be different: "
read result

cat $cover secret.zip > $result

rm -rf secret
rm -f secret.zip

printf "\n\t  ;    +---------------------+\n\t [\"] - | your file is ready! |\n\t/[_]\\  +---------------------+\n\t ] [  \n"
