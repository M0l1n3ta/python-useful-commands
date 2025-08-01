# Python Downloader
# pip install internetdownloadmanager
import internetdownloadmanager as idm

def Downloader(url, output):
    pydownloader = idm.Downloader(worker=20,
                                part_size=1024*1024*10,
                                resumable=True,)

    pydownloader .download(url, output)




Downloader("https://www.youtube.com/watch?v=GBTI6ZwqA8w", "D:\\Datos\\Videos\\video.mp4")