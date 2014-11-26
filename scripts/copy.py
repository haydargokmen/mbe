import os
filePath = "/foo/bar/baz.py"
serverPath = "/blah/boo/boom.py"
os.system("scp "+filePath+" user@myserver.com:"+serverPath)
