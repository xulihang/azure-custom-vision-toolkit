import os
for filename in os.listdir("./yolo/"):
    if filename.endswith(".txt"):
        f=open("./yolo/" + filename,"r")
        fw=open("./out/" + filename,"w")
        for line in f.readlines():
            line=line.replace("\n","")
            x_center=line.split(" ")[1]
            y_center=line.split(" ")[2]
            w=line.split(" ")[3]
            h=line.split(" ")[4]
            x=float(x_center)-float(w)/2
            y=float(y_center)-float(h)/2
            fw.write(" ".join([str(x),str(y),str(w),str(h)])+"\n")
        f.close()
        fw.close()