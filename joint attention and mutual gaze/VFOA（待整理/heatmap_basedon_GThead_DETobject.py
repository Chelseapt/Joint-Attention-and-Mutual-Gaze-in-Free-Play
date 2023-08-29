import pickle
import os
from pandas import DataFrame
# motherview for example
normmap_path="./gaze_attention//VFOA_basedonheadGT/normmap//mother/test/" #normmap is the result from attention-target-detection project
DET_objectpath="./gaze_attention/object label//test/" # object detection result
GT_headpath="./annotation/test/" # head location GT,  for children (motherview) 
heatmap_all=DataFrame()
for filename in os.listdir(normmap_path):              
    print (filename)
    for pklname in os.listdir(normmap_path+filename):       
        print (pklname)
        name=pklname.split('.')[0] 
        F_normmap=open(normmap_path+filename+'//'+pklname,'rb') 
        content1=pickle.load(F_normmap)
        (height,width)=content1.shape
        # Retrieve the bounding box of the head for another character in the current frame.
        F_headGT=open(GT_headpath+filename+'//'+name+'.txt')
        for line_head in F_headGT:
            label_id =int(float(line_head.split(' ')[0])) # id mother_id=12，children_id=13
            if label_id ==13:  # Motherview, so it's the heatmap corresponding to the child's head, ID =13.
                x=float(line_head.split(' ')[2])*width
                y=float(line_head.split(' ')[3])*height
                w=float(line_head.split(' ')[4])*width
                h=float(line_head.split(' ')[5])*height
                x1_head=int(x-w/2)
                y1_head=int(y-h/2)
                x2_head=int(x+w/2)
                y2_head=int(y+h/2)
                heatmap_matrix=content1[max(0,y1_head):min(height,y2_head),max(0,x1_head):min(width,x2_head)]
                size=(y2_head-y1_head)*(x2_head-x1_head) #The size of the bounding box.
                heatmap_value=heatmap_matrix.sum()/size # average the heatmap
                heatmap={'filename': filename,'imagename': name, 'id':13 ,'point':1,'value': heatmap_value}
                heatmap_all=heatmap_all.append(heatmap,ignore_index=True)
        #calculate the heatmap value of each object's bounding box.
        object_txtpath=DET_objectpath+filename+'//'+'labels'+'//'+name+'.txt'
        if not os.path.exists(object_txtpath): 
            pass
        else:
            F_objectDET=open(object_txtpath)
            heatmap_object=DataFrame()
            for line in F_objectDET:
                label_id =int(float(line.split(' ')[0])) 
                point=float(line.split(' ')[5]) # Confidence probability.
                x=float(line.split(' ')[1])*width
                y=float(line.split(' ')[2])*height
                w=float(line.split(' ')[3])*width
                h=float(line.split(' ')[4])*height
                x1=int(x-w/2)
                y1=int(y-h/2)
                x2=int(x+w/2)
                y2=int(y+h/2)
                heatmap_matrix=content1[max(0,y1):min(height,y2),max(0,x1):min(width,x2)]
                size=(y2-y1)*(x2-x1) # x1 and y1 are the coordinates of the top-left corner, while x2 and y2 are the coordinates of the bottom-right corner.
                heatmap_value=heatmap_matrix.sum()/size # average the heatmap
                heatmap={'filename': filename,'imagename': name, 'id': label_id,'point':point,'value': heatmap_value}
                heatmap_object=heatmap_object.append(heatmap,ignore_index=True)
                del label_id,point,x1,y1,x2,y2 
            heatmap_object_new = heatmap_object.sort_values('point', ascending=False).drop_duplicates('id').sort_index()
            heatmap_all=heatmap_all.append(heatmap_object_new,ignore_index=True)
##save the dataframe
heatmap_all.to_csv('./heatmap_motherview_basedonGThead_DETobject.csv',index=None)
