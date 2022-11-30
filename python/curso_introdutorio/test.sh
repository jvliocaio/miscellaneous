#!/usr/bin/env bash

# sudo apt update 

# sudo apt upgrade -y

#ARRAY=$(apt list --upgradable | cut -f1 -d '/')

ARRAY=('A' 'B' 'C' 'D' 'E' 'F' 'G' 'H')

PACKAGES=$($ARRAY[0]=''; echo ${ARRAY[@]})

for pkg in ${packages[@]}; do
echo $pkg
#  if [[ "$pkg" != "Listing..." ]]; then
# 	sudo apt install -y $pkg
#  fi
done

# sudo apt autoremove -y  && sudo apt autoclean -y