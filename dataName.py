import os

root_dir = ["./datasets2/down/", "./datasets2/up/","./datasets2/Left/","./datasets2/Right/", 
        "./datasets2/Right up/", "./datasets2/Right down/","./datasets2/Left up/","./datasets2/Left down/"]

for i in range(0,8):
    temp_record=[]
    l = 0
    for k in range (0, 2):
        for j in range(0,4000):
            try:
                os.rename(os.path.join(root_dir[i] + str(k) + '/' + str(j) + '.jpg'), os.path.join(root_dir[i]+str(l)+'.jpg'))
                l = l + 1
            except:
                continue