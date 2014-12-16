#!/bin/bash

echo "construction des arborescences"

sudo chown fmr /discotheque
cd /discotheque
mkdir Albums Jingles Publicites

echo "installation des packages"

apt-get install mc links tree wget ntp mudita24