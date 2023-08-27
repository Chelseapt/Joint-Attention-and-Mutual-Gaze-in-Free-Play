#基于GT的headtracking的VFOA
#选用GT head的bounding box和VFOA算heatmap值#是否采用GT object的bounding box和VFOA算heatmap值（还是也用到DET object，对比使用GT object的结果看提高效果
## 选取GT object的bounding box
import pickle
import os
from pandas import DataFrame
#以妈妈视角为例
normmap_path="C://Users//li000167//Documents//project//gaze_attention//VFOA_basedonheadGT//normmap//mother//test//" #normmap存储位置 应该用label的
DET_objectpath="C://Users//li000167//Documents//project//gaze_attention//object label//test//" # object
GT_headpath="C://Users//li000167//Documents//Research//dataset//youth//test_data//annotation//CHECKED//PEITONG//test//" #如果是妈妈就是对应的小孩的头的位置
heatmap_all=DataFrame()
for filename in os.listdir(normmap_path):              #listdir的参数是存储norm_hm文件夹的路径 #./test2 是out3_all的测试路径，之后改成对应比如out3_B000167
    print (filename)
    for pklname in os.listdir(normmap_path+filename):       
        print (pklname)
        name=pklname.split('.')[0] #对应第几帧 比如 000025
        F_normmap=open(normmap_path+filename+'//'+pklname,'rb') #载入normmap
        content1=pickle.load(F_normmap)
        (height,width)=content1.shape# 得到原始图片的长宽
        #读取当前帧对应另一个人物的head的检测框
        F_headGT=open(GT_headpath+filename+'//'+name+'.txt')
        #找到headtxt对应帧的坐标值，没有的话就跳过这个循环，因为另一个head不存在统计当前帧没意义
        for line_head in F_headGT:#妈妈视角，所以是小孩的头对应的heatmap，id=13
            label_id =int(float(line_head.split(' ')[0])) # id 妈妈是12，小孩是13
            if label_id ==13: 
                x=float(line_head.split(' ')[2])*width
                y=float(line_head.split(' ')[3])*height
                w=float(line_head.split(' ')[4])*width
                h=float(line_head.split(' ')[5])*height
                x1_head=int(x-w/2)
                y1_head=int(y-h/2)
                x2_head=int(x+w/2)
                y2_head=int(y+h/2)
                heatmap_matrix=content1[max(0,y1_head):min(height,y2_head),max(0,x1_head):min(width,x2_head)]
                size=(y2_head-y1_head)*(x2_head-x1_head) #小孩/妈妈检测框的大小
                heatmap_value1=heatmap_matrix.sum()
                heatmap_value2=heatmap_matrix.sum()/size # 除以面积
                heatmap_value3=heatmap_matrix.max()
                heatmap={'filename': filename,'imagename': name, 'id':13 ,'point':1,'value1': heatmap_value1,'value2': heatmap_value2,'value3': heatmap_value3}
                heatmap_all=heatmap_all.append(heatmap,ignore_index=True)
        #读取txt内容，计算每个object的检测框的heatmap值
        #有些txt文件没有数据则跳过
        object_txtpath=DET_objectpath+filename+'//'+'labels'+'//'+name+'.txt'
        if not os.path.exists(object_txtpath): #有些txt文件没有数据则跳过
            pass
        else:
            F_objectDET=open(object_txtpath)#载入GT数据
            #读取每一行数据 计算每一行数据对应检测框的heatmap的value
            heatmap_object=DataFrame()
            for line in F_objectDET:
                label_id =int(float(line.split(' ')[0])) # id 先读取object的id
                point=float(line.split(' ')[5]) # 置信概率
                x=float(line.split(' ')[1])*width
                y=float(line.split(' ')[2])*height
                w=float(line.split(' ')[3])*width
                h=float(line.split(' ')[4])*height
                x1=int(x-w/2)
                y1=int(y-h/2)
                x2=int(x+w/2)
                y2=int(y+h/2)
                ##x1 y1 是左上角坐标，x2 y2 是右下角坐标
                heatmap_matrix=content1[max(0,y1):min(height,y2),max(0,x1):min(width,x2)]
                size=(y2-y1)*(x2-x1) #目标检测框的大小
                heatmap_value1=heatmap_matrix.sum()
                heatmap_value2=heatmap_matrix.sum()/size # 除以面积
                heatmap_value3=heatmap_matrix.max()
            ## 存成dataframe形式
               # heatmap={'imagename': '\t'+image, 'label': label,'value1': heatmap_value1,'value2': heatmap_value2,'value3': heatmap_value3}
                heatmap={'filename': filename,'imagename': name, 'id': label_id,'point':point,'value1': heatmap_value1,'value2': heatmap_value2,'value3': heatmap_value3}
                heatmap_object=heatmap_object.append(heatmap,ignore_index=True)
                del label_id,point,x1,y1,x2,y2 #防止用的是过去的数据，这样在新的不存在时会报错
            heatmap_object_new = heatmap_object.sort_values('point', ascending=False).drop_duplicates('id').sort_index()
            heatmap_all=heatmap_all.append(heatmap_object_new,ignore_index=True)
##将dataframe保存下来
#heatmap_df.to_csv('./heatmap_test_right.csv',index=None)
heatmap_all.to_csv('./heatmap_motherview_basedonGThead_DETobject.csv',index=None)
