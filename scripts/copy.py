import os
filePath = "/home/admin/mbe/scripts/copy.py"
serverPath = "/data/backup/"
os.system("scp "+filePath+" admin@58.162.142.237:"+serverPath)
