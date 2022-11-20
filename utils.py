import numpy as np
def water_type(type):
    if type==1:
        bgr=[0.982,0.961,0.805]
    elif type==2:
        bgr=[0.975,0.955,0.804]
    elif type==3:
        bgr=[0.968,0.950,0.830]
    elif type==4:
        bgr=[0.940,0.925,0.800]
    elif type==5:
        bgr=[0.890,0.885,0.750]
    elif type==6:
        bgr=[0.875,0.885,0.750]
    elif type==7:
        bgr=[0.800,0.820,0.710]
    elif type==8:
        bgr=[0.670,0.730,0.670]
    elif type==9:
        bgr=[0.500,0.610,0.620]
    elif type==10:
        bgr=[0.290,0.460,0.550]
    return np.array(bgr)

def value_to_deep(x, min, max):
    y=(max-min)/255*x+min
    return y
