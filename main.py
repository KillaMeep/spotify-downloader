import time
import os
from utils.helper import *
fn = time.strftime("%Y%m%d-%H%M%S")

os.system('cls')

inp = input('Input spotify url: ')
num = int(input('Download on how many threads (1-5): '))
temp = searcher.search_sp(inp)

urls = searcher.search_yt(temp)


misc.create_folder(fn)
downloader.download_fast(urls,num,fn)
