import os
import math

last_position=[0.0,0.0]
my_dict=dict()
last_frame=0
count=0
# children for example
for filename in os.listdir(r"./result/before_interpolate/children/"):              
    print (filename) 
    f=open(r"./result/before_interpolate/children/"+filename)
    with open('./result/interpolate/txt/children/'+filename,"w") as f1:
        for line in f:
            A=line.split(',')
            frame=int((A[0].split('.'))[0]) #提取出帧数
            gap=frame-last_frame 
            x1=float(A[1])
            y1=float(A[2])
            x2=float(A[3])
            y2=float(A[4])
            w=x2-x1
            h=y1-y2
            position=[(x1+x2)/2,(y1+y2)/2]
            position_shift=math.sqrt(math.pow(position[0]-last_position[0],2)+math.pow(position[1]-last_position[1],2))
            position_interval=position_shift//5 #5个为1区间
            if gap>1 and gap<=50 and last_frame!=0: 
                if position_interval<=9 : #
                    for i in range(1,gap):
                        interpolate_position=[(last_position[0]+(position[0]-last_position[0])*i/(gap-1)),(last_position[1]+(position[1]-last_position[1])*i/(gap-1))]
                        interpolate_x1=interpolate_position[0]-w/2
                        interpolate_y1=interpolate_position[1]+h/2
                        interpolate_x2=interpolate_position[0]+w/2
                        interpolate_y2=interpolate_position[1]-h/2
                        interframe=last_frame+i
                        content='{:06d}.jpg, {:.2f}, {:.2f}, {:.2f}, {:.2f}'.format(interframe,interpolate_x1,interpolate_y1,interpolate_x2,interpolate_y2)                    
                        f1.write(content+'\n')
            last_position=position
            last_frame=frame   
            last_w=w
            last_h=h  
      
                    