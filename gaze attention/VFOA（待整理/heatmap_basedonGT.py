#基于GT的headtracking的VFOA
#选用GT head的bounding box和VFOA算heatmap值#是否采用GT object的bounding box和VFOA算heatmap值（还是也用到DET object，对比使用GT object的结果看提高效果
## 选取GT object的bounding box
import pickle
import os
from pandas import DataFrame
#以妈妈视角为例
normmap_path="./VFOA_basedonheadGT/normmap/children/"
GT_path="C://Users//li000167//Documents//Research//dataset//youth//test_data//annotation//CHECKED//PEITONG//"
heatmap_all=DataFrame()
for filename in os.listdir(normmap_path):              #listdir的参数是存储norm_hm文件夹的路径 #./test2 是out3_all的测试路径，之后改成对应比如out3_B000167
    print (filename)
    for txtname in os.listdir(normmap_path+filename):       
        print (txtname)
        name=txtname.split('.')[0]
        F_normmap=open(normmap_path+filename+'//'+txtname,'rb') #载入normmap
        content1=pickle.load(F_normmap)
        (height,width)=content1.shape# 得到原始图片的长宽
        #读取txt内容，计算每个object的检测框的heatmap值
        F_GT=open(GT_path+filename+'//'+name+'.txt')#载入GT数据
        #读取每一行数据 计算每一行数据对应检测框的heatmap的value
        for line in F_GT:
            label_id =int(float(line.split(' ')[0])) # id 妈妈是12，小孩是13
            if label_id !=13: #因为从妈妈/小孩视角出发，所以不统计id=12（妈妈）/id=13（小孩）的bb与VFOA重叠的heatmap。
                x=float(line.split(' ')[2])*width
                y=float(line.split(' ')[3])*height
                w=float(line.split(' ')[4])*width
                h=float(line.split(' ')[5])*height
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
                heatmap={'filename': filename,'imagename': name, 'id': label_id,'point':1,'value1': heatmap_value1,'value2': heatmap_value2,'value3': heatmap_value3}
                heatmap_all=heatmap_all.append(heatmap,ignore_index=True)
                del label_id,x1,y1,x2,y2 #防止用的是过去的数据，这样在新的不存在时会报错
##将dataframe保存下来
#heatmap_df.to_csv('./heatmap_test_right.csv',index=None)
heatmap_all.to_csv('./heatmap_childrenview_basedonGT.csv',index=None)
