#! /bin/bash

echo "start the back"
python3 /path_to_src/back/main.py &
sleep 5
echo "start the front"
firefox /path_to_scr/front/tableau_de_bord.html &
echo "*******  close this window to quit the back and front ************"
wait