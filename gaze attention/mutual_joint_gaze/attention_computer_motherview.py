import pandas as pd
mother_path='./heatmap_motherview_threshold.csv'
mother=pd.read_csv(mother_path)


data_list=[]
last_imagename=0
last_filename=0
X_motherview_score = [0] * 14
X_motherview_threshold = [-1] * 14

for i, row in mother.iterrows():
    filename = row['filename']
    imagename = row['imagename']
    print(filename,imagename)
    if (i!=0 and last_imagename!=imagename) or i==len(mother)-1:
       gaze_type={'filename': last_filename,'imagename':last_imagename,'X_motherview_score':X_motherview_score,'X_motherview_threshold':X_motherview_threshold}
       data_list.append(gaze_type)
       X_motherview_score = [0] * 14
       X_motherview_threshold= [-1] * 14

    id_ = row['id']
    X_motherview_score[id_]=row['value']
    X_motherview_threshold[id_]=row['threshold']
    X_motherview_threshold[12]=0 #  From a mother's perspective, a mother's head certainly exists, but it is definitely not gazing at itself, so its value is assigned as 0.
    last_imagename=imagename 
    last_filename=filename


df = pd.DataFrame(data_list)        
df.to_excel('./detect_motherview.xlsx',index=False)