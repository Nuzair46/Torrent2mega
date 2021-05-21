# Torrent2mega
--------------
* A simple docker to transfer torrents to your Mega drive. Can be run on Heroku.

## Purpose?
-----------
* This tool is aimed to utilize the high speed of a VPS to download really slow torrents to you Mega drive.

## Setup
---------
* Fork this repo.
* Need to set Env variables:
	* EMAIL: "your_mega_email_id"
	* PASS: "your_mega_password"
	* MAGNET: "magnet_uri"

* Above variable can be set in heroku `config vars`. Don't use "quotes".
* To run the docker on a VPS:
	* Fill the `.env` given. Don't use "quotes".
	* `sudo docker build --no-cache -t torrent2mega .`
	* `sudo docker run --env-file .env -it torrent2mega`

* On Heroku, make sure to kill the Dyno after the download is complete, because Heroku will relaunch the code and may lead to overwriting in Mega.
* When using on Heroku, Make sure to deploy the repo everytime rather than just starting the Dyno, this will delete any previously downloaded cache.
* When on a VPS, rebulding from the above command is the best option as it will clear previous caches.

### Notes and ToDo.
-------------------
* On Heroku, the tool may look like its not doing anything. Please wait until the download completes and then you will see all the logs.  

* I wanted the code to directly save contents to the mega drive rather than download and upload, But due to the limitations of finding something for Mega to mount the drives, I could not do it.
	* You're most welcome if you can add this feature.

* I tried Alpine image but it creates some issue with pip, so I discarded it.

* This is like in a beta stage for now. It may have issues. If you find any, submit an issue.
