import time

readsize = 1024
#filelist = ['bz4w01x006y010_1_1.dat','bz4w01x006y010_1_2.dat','bz4w01x006y010_1_3.dat',
#            'bz4w01x006y010_1_4.dat','bz4w01x006y010_1_5.dat','bz4w01x006y010_1_6.dat',
#           'bz4w01x006y010_1_7.dat','bz4w01x006y010_1_8.dat']
#tofile = 'all.dat'
def join(filelist,tofile):
    localtime = time.asctime(time.localtime(time.time()))
    print 'file merge start time :',localtime
    with open(tofile,'wb') as output:
        for filename in filelist:
            with open(filename,'rb') as fileobj:
                while True:
                    filebytes = fileobj.read(readsize)
                    if not filebytes:break
                    output.write(filebytes)
    localtime = time.asctime(time.localtime(time.time()))
    print 'file merge end time :',localtime

