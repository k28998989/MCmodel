import os
old_file_path = './datasets/test'
j=0

    
for k in range(0,100):
    try: 
        os.rename(old_file_path+'/'+str(k)+'.jpg', old_file_path+'/'+str(j)+'.jpg')
        j = j + 1
    except: 
        pass