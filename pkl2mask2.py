import os
g = os.walk(".\\train_images")
count=0

filename_fullpath_tb=dict()
for path,d,filelist in g:
    #print d;
    for filename in filelist:
        fullpath=os.path.join(path, filename)
        filename_fullpath_tb[filename]=fullpath
        #print(filename)

import pickle
with open('new_polygons.pkl','rb') as f:
    imgpoly_dict = pickle.load(f)
    print(type(imgpoly_dict))
    for key,value in imgpoly_dict.items():
        img_class=value[0]
        points=value[1:]
        if key in filename_fullpath_tb.keys():
            keytrans=filename_fullpath_tb[key]
            #print(keytrans,points,img_class)
            
            maxx=0
            maxy=0
            minx=9999999
            miny=9999999
            for p in points:
                x=int(p[0])
                y=int(p[1])
                #print(x,y)
                if x>maxx:
                    maxx=x
                if y>maxy:
                    maxy=y
                if x<minx:
                    minx=x
                if y<miny:
                    miny=y
            #count = count +1
            content = keytrans + ',' +  str(minx) + ',' +  str(miny) + ',' + str(maxx) + ','  + str(maxy) + ',' +  'disease'       
            #print(keytrans,minx,miny,maxx,maxy,img_class)
            print(content)
        #print(count)
    #k='Colonoscopy 3068 Photo (3).BMP'
    #v=imgpoly_dict[k]
    #print(type(v))
    #print(v)
    