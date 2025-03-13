# Launch the back end manually
On a terminal open on the right folder
```sh
cd /home/combi/Desktop/Combi_MVP/
source ./env/env/bin/activate
cd ../back
python main.py
```

# Launch a front server
```sh
cd /home/combi/Desktop/Combi_MVP/
cd front
python server.py
```

# Install the launcher
- Put the file combi.service in /etc/systemd/system/
- Give it execution right with `chmod +x /etc/systemd/system/combi.service`
- Enable it with `sudo systemctl enable ./combi.service`
- Launch it with `sudo systemctl start combi.service`
- Check that it is working with `sudo systemctl status combi.service`

Now, it will restart at boot and whenever it crashes.
