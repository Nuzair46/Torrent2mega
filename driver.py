import libtorrent as lt 
import time
import os

from os import walk
from mega import Mega
from datetime import datetime

email = os.environ['EMAIL']
password = os.environ['PASS']
magnet = os.environ['MAGNET']

class Driver():
	def run():
		mega = Mega()
		try:
			mClient = mega.login(email, password)
		except Exception:
			print("If running locally, try if you can ping 'www.mega.co.nz'. if not, use cloudflare dns 1.1.1.1 or any vpn. Else, check your login credentials.")
			return
		print(f"Transfer Quota: {mClient.get_quota()} KB")
		storage = mClient.get_storage_space()
		storage_left = int(storage['total']) - int(storage['used'])
		storage_left = storage_left / (1073741824)
		print(f"Storage Left: {storage_left}GB")

		client = lt.session({'listen_interfaces': '0.0.0.0:6881'})
		minfo = lt.parse_magnet_uri(magnet)
		handle = client.add_torrent(minfo)
		begin = time.time()
		print(datetime.now())
		print("Downloading Metadata...")
		while not handle.has_metadata():
			time.sleep(1)
		print("Metadata downloaded. Starting Torrent Downloading...")
		
		mClient.create_folder(f'{handle.name()}')
		
		print(f"Starting {handle.name()}.")
		s = handle.status()
		while not s.is_seeding:
			s = handle.status()
			state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 'finished', 'seeding', 'allocating']
			try:
				print ('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s ' % \
						(s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
						s.num_peers, state_str[s.state]))
			except IndexError:
				pass
			time.sleep(5)

		end = time.time()
		print(f"{handle.name()} completed...")
		print("Elapsed Time: ",int((end-begin)//60),"min :", int((end-begin)%60), "sec")

		print(datetime.now())
		f = []
		for (dirpath, dirnames, filenames) in walk(f'{handle.name()}'):
			f.extend(filenames)
			break
		folder = mClient.find(f'{handle.name()}')
		print("Uploading to Mega...")
		for file in f:
			mClient.upload(f'{handle.name()}/{file}', folder[0])
		print("Upload Completed...\n Happy Torrenting...")
		exit()
if __name__ == '__main__':
	Driver.run()