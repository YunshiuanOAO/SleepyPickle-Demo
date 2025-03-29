import pickle
import pickletools

with open('evil.pkl', 'rb') as f:
    #pickletools.dis(f)
    pickle.load(f)