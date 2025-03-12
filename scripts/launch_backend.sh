#! /bin/bash

echo "start the back"
cd /home/combi/Desktop/Combi_MVP/
source ./env/bin/activate
cd ./back
python main.py
echo "*******  close this window to quit the back and front ************"
wait
