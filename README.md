# Torrent2mega
--------------
* A simple docker to torrent within Heroku to transfer the files to your Mega drive.

## Purpose?
-----------
* This tool is aimed to utilize the high speed of a VPS to download really slow torrents to you drive.

## Setup
---------
* You can run the docker after building. Or you can use docker-compose.
* Need to set Env varibales, mega: email, password and torrent magnet.

### Notes and ToDo.
-------------------
* Although I wanted this to be hosted on Heroku, It is not working beyond `State changed from starting to up` .
	* You are free to look into this. heroku.yml is already setup, you can edit it with your needs if you can make it work.

* I also wanted it to directly save contents to the drive rather than download and upload, But due to the limitations of finding something for Mega, I could not do it.
	* You're most welcome if you can add this feature.
