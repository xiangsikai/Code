

import subprocess

res=subprocess.Popen("dir",
                     shell=True,
                     stderr=subprocess.PIPE,
                     stdout=subprocess.PIPE)


print(res.stdout.read().decode("gbk"))




