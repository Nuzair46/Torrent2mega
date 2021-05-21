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
* This works on Heroku too. but it doesn't give any log. but you can see the output in your mega drive. But this is a bit slow.  

* I also wanted it to directly save contents to the drive rather than download and upload, But due to the limitations of finding something for Mega, I could not do it.
	* You're most welcome if you can add this feature.
