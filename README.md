# Automated-Detection-of-Joint-Attention-and-Mutual-Gaze-in-Free-Play-Parent-Child-Interactions
## face tracking
### face detection
采用了[LAEO-Net++](https://github.com/AVAuco/laeonetplus)中的head detection。
### fae tracking
### interpolate
## objet detection
## VFOA
### gaze attention
### VFOA 
1. object/mother/children heatmap
2. threshold, setting=80
### mutual/joint attention
1. motherview/childview 
将threshold变成14维向量
2. combineview 
13维向量
前12维joint attention ，第13维joint attention
## evaluation
cohen-kappa
