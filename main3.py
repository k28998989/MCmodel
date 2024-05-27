import os

root_dir = ["./datasets/down/", "./datasets/up/","./datasets/Left/","./datasets/Right/", 
        "./datasets2/Right up/", "./datasets2/Right down/","./datasets2/Left up/","./datasets2/Left down/"]
N_Pic = [2737, 2686, 3746 ,2947]
for i in range(0,8):
    temp_record=[]
    for j in range(0,4000):
        if os.path.exists(os.path.join(root_dir[i]+str(j)+'.jpg')):
            print (root_dir[i]+str(j)+'.jpg')