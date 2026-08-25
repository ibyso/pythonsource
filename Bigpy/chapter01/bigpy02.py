import pickle

f=open('setting1.txt','rb')
setting = pickle.load(f,encoding='utf-8')
f.close()

print(setting)