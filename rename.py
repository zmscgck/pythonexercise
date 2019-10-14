#引入OS模块
import os
#1、获取指定路径下的所有文件名
allFileName=os.listdir('C:\CloudMusic\script')
print(allFileName)
#os.getcwd()
#2、循环的方式依次进行重命名
for name in allFileName:
    os.rename('C:\\CloudMusic\\script\\'+name,'C:\\CloudMusic\\script\\'+'my_'+name)
     
     