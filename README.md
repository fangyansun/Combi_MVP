# Launch the back end
On a terminal open on the right folder
```sh
python main.py
```

# Launch the front end
by clicking on the html file

# NOTA
- the front end must be open after the server to start the websocket connexion
- Press Control Shift i to check the Javascript console of the front end and see the debug info.

# Files Tree
- back
	- log
- front
    - CSS
    - JS
    - IMAGES

# File transfer
## First, run a manual file transfer for test
scp log.csv name@address:/home/folder/log.csv

## Create a script to do so and launch it
```sh
#! /bin/bash

echo "beginning of the log transfer script"
scp log.csv name@address:/home/folder/log.csv
echo "transfer finished"
```

## Now, with a script which does not need the user to type the password
(here, we use a method which put the password in the server, but for safety reasons, it is better to use a public and private key as shown here : https://blog.csdn.net/zfjBIT/article/details/103362195)

send_log.sh
```sh
#! /bin/bash

echo "beginning of the log transfer script"
sshpass -p my_pass_word scp log.csv name@address:/home/folder/log.csv
echo "transfer finished"
```

## Test the cron

### We create another script to test the cron
vim create_new_files.sh
```sh
#! /bin/bash

# create a new file each minute
# the file name is the minute
touch /home/log_`date +"%M"`
```

### Check if it works without cron
source /path_to_script/create_new_files.sh

Change its authorizations so that it works without `source`

chmod +x /path_to_script/create_new_files.sh
chmod +x /path_to_script/send_log.sh

### Install the crons
crontab -e
*/1 * * * * /path_to_script/create_file.sh

If a new file was created on the right place after one minute, it worked !

If it did not, maybe cron was not started. So you can start it with :
`sudo /etc/init.d/cron start`

Then, we can install the log sending script so that it is executed each 20 minutes.

crontab -e
*/20 * * * * /path_to_script/send_log.sh











