import pandas as pd
#妈妈路径
#path='C://Users//li000167//Documents//project//gaze_attention//heatmap_childrenview_basedonGT.csv'
#小孩路径
path='C://Users//li000167//Documents//project//gaze_attention//GThead_DETobject//heatmap_motherview_basedonGThead_DETobject.csv'
data = pd.read_csv(path)

threshold2 = []
threshold3 = []

for i in range(len(data)):
    if data.loc[i, 'value2'] >= 80:
        threshold2.append(1)
    else:
        threshold2.append(0)

    if data.loc[i, 'value3'] >= 190:
        threshold3.append(1)
    else:
        threshold3.append(0)

data['threshold2'] = threshold2
data['threshold3'] = threshold3
out_path='C://Users//li000167//Documents//project//gaze_attention//GThead_DETobject//heatmap_motherview_basedonGThead_DETobject_threshold.csv'
data.to_csv(out_path, index=False)

