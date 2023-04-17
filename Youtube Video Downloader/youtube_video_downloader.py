import pytube
DOWNLOAD_PATH = "/home/testi/Downloads/FILE"   
link = input('Enter The Youtube Video URL')
dn = pytube.YouTube(link)
dn.streams.first().download(DOWNLOAD_PATH)
print('Your Video Has Been Downloaded', link)