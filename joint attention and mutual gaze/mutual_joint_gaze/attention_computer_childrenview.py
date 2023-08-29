import pandas as pd
children_path='.//heatmap_childrenview_threshold.csv'
children= pd.read_csv(children_path)


data_list=[]
last_imagename=0
last_filename=0


X_childrenview_score = [0] * 14
X_childrenview_threshold = [-1] * 14

for i, row in children.iterrows():
    filename = row['filename']
    imagename = row['imagename']
    print(filename,imagename)
    if (i!=0 and last_imagename!=imagename) or i==len(children)-1:
       gaze_type={'filename': last_filename,'imagename':last_imagename,'X_childrenview_score':X_childrenview_score,'X_childrenview_threshold':X_childrenview_threshold}
       data_list.append(gaze_type)
       X_childrenview_score = [0] * 14
       X_childrenview_threshold = [-1] * 14
    id_ = row['id']
    X_childrenview_score[id_]=row['value']
    X_childrenview_threshold[id_]=row['threshold']
    X_childrenview_threshold[13]=0 # From a child's perspective, a child's head certainly exists, but it is definitely not gazing at itself, so its value is assigned as 0.
    last_imagename=imagename 
    last_filename=filename


df = pd.DataFrame(data_list)        
df.to_excel('./detect_childrenview.xlsx',index=False)
