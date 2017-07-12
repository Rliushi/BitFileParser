# -*- coding:utf-8 -*-
class GZipTool:
    def __init__(self):
        bufSize=1024*8
        self.bufSize = bufSize
        self.fin = None
        self.fout = None
 
    def compress(self, src, dst):
        self.fin = open(src, 'rb')
        self.fout = gzip.open(dst, 'wb')
         
        self.__in2out()
         
    def decompress(self, gzFile, dst):
        self.fin = gzip.open(gzFile, 'rb')
        self.fout = open(dst, 'wb')
         
        self.__in2out()
         
    def __in2out(self,):
        while True:
            buf = self.fin.read(self.bufSize)
            if len(buf) < 1:
                break
            self.fout.write(buf)
             
        self.fin.close()
        self.fout.close()



from bitarray import bitarray;
import gzip
import zipfile  
import numpy
import time



def test_Logical_file():
    seperate_bit_data1('bz4w01x006y006_func.dat')
    
    t1=GZipTool()
    localtime = time.asctime( time.localtime(time.time()) )
    print "unGzip start time :", localtime
    t1.decompress('test.dat.gz','test.dat')
    localtime = time.asctime( time.localtime(time.time()) )
    print "unGzip end time :", localtime
    
    #4bits-run-length
    unPack_4bit_run_length('test.dat')
    
def test_load_xml(ChipData):
    
    # file1=['bz4w01x006y006_phy.dat','0xD0','0x87A8','test.dat.gz','bz4w01x008y006_01.dat']
    # file2=['bz4w01x006y006_phy.dat','0xD364','0x808B','test.dat.gz','bz4w01x008y006_02.dat']
    # file3=['bz4w01x006y006_phy.dat','0x19B6E','0x82AF','test.dat.gz','bz4w01x008y006_03.dat']
    # file4=['bz4w01x006y006_phy.dat','0x26508','0x8E41','test.dat.gz','bz4w01x008y006_04.dat']
    # file5=['bz4w01x006y006_phy.dat','0x343C2','0x8090','test.dat.gz','bz4w01x008y006_05.dat']
    # file6=['bz4w01x006y006_phy.dat','0x40A00','0x8C5A','test.dat.gz','bz4w01x008y006_06.dat']
    # file7=['bz4w01x006y006_phy.dat','0x4E6C2','0x8C6B','test.dat.gz','bz4w01x008y006_07.dat']
    # file8=['bz4w01x006y006_phy.dat','0x5C27B','0x8FFD','test.dat.gz','bz4w01x008y006_08.dat']
    # ChipData=[]
    # ChipData.insert(0, file1)
    # ChipData.insert(0, file2)
    # ChipData.insert(0, file3)
    # ChipData.insert(0, file4)
    # ChipData.insert(0, file5)
    # ChipData.insert(0, file6)
    # ChipData.insert(0, file7)
    # ChipData.insert(0, file8)
    
    #print(testString[1:])
    #print(int(testString[2:],16))
    

    
    for file in ChipData:
        
        #分割 fail bit data
        seperate_bit_data(file[0],file[1],file[2],'test.dat.gz')
    
        
        #gzip解座续    
        t1=GZipTool()
        localtime = time.asctime( time.localtime(time.time()) )
        print "unGzipstart time :", localtime
        t1.decompress('test.dat.gz','test.dat')
        localtime = time.asctime( time.localtime(time.time()) )
        print "unGzip end time :", localtime
        
        #get bit array from bit fail data
        
        #print(b.tobytes())
        #print(type(b))
        # Testing Data
        #c=b[:131072]
        
        #Bits-pack
        unPacktoBitarray('test.dat',file[4])
    
    #4bits-run-length
    #unPack_4bit_run_length('test.dat')
    
    #b=bitarray();
    #b=get_bit_array();
    #print(b.length())
    #c=reshap_for_chip_design(c)
    #print(c.shape)
    
    #b=numpy.reshape(b,(-1,3,48))
    #print(c[0][0][0][0])
    
    #print(c[0][0][0][1])
    #取得sub array 直行
    #print(c[0][0][0][0][:,2])
    
    #取得sub array 横列
    #print(c[0][0][0][0][2,:])
    
    #指定直行加总
    #d=numpy.sum(c[0][0][0][0], axis=0)
    #print(d)
    #print("...............................................")
    #d=numpy.sum(c[0][0][0][0], axis=1)
    #print(d)
    
    # save bit fail data 
    #with open('ChipBitData.dat', 'wb') as output:
    #    output.write(file_content)

    #a.fromstring(file_content[2:])
    #print(a)
def unPack_4bit_run_length(filename):
    
    localtime = time.asctime( time.localtime(time.time()) )
    print "unPack start time :", localtime
    
    a = bitarray()
    b=bitarray()
    ReadByte=''
    y=0
    k=0
    byteSize=int('7F80B',16)*10
    print(byteSize)
    with open(filename, 'rb') as fh:
        #fh.seek(int('0D',16))
       
        b=bitarray()
        temp=bitarray('0000')
        failPattern=bitarray()
        sequential=bitarray()
        k=0
        while True:
            b=bitarray()
            temp=bitarray('0000')
            if (k>=byteSize) :break
            b.frombytes(fh.read(2))
            failPattern=b[0:4]
            failPattern.reverse()
            sequential=b[4:]
            temp.extend(sequential)
            #print[temp]
            sequentialNum=bytestring2Int(temp[0:8].tobytes()) *256+ bytestring2Int(temp[8:].tobytes())
            a.extend(failPattern*(sequentialNum+1))
            #print(b)
            #print(failPattern)
            #print(temp)
            #print(sequentialNum)
            k+=2
        print(a[0:32])
        print(a.length())
        print(k)
        filename='test_1' +'.dat'
        with open(filename, 'wb') as output:
            output.write(a.tobytes())
    
    localtime = time.asctime( time.localtime(time.time()) )
    print "unPack end time :", localtime




def unPacktoBitarray(filename,destFilename):
    localtime = time.asctime( time.localtime(time.time()) )
    print "unPack start time :", localtime
    a = bitarray()
    b=bitarray()
    c=bitarray()
    ReadByte=''

    with open(filename, 'rb') as fh:
        while True:
            b=bitarray()
            ReadByte=fh.read(1)
            if ReadByte=='': break
            HeaderPart=getHeaderValue(ord(ReadByte))

            if HeaderPart==-128:
                continue
            if HeaderPart<=-1:
                b.frombytes(fh.read(1))
                for i in range(1,(1-HeaderPart+1)):
                    a.extend(b)
            else:
                b.frombytes(fh.read(HeaderPart+1))  
                a.extend(b)
    
    localtime = time.asctime( time.localtime(time.time()) )
    print "unPack Finish Decode :", localtime
    
    if a.length()>0:
        print(a.length())
        filename=destFilename
        with open(filename, 'wb') as output:
            output.write(a.tobytes())
    
    localtime = time.asctime( time.localtime(time.time()) )
    print "unPack  end time :", localtime
    
def bytestring2Int(byteStr):
    hexCode="{:02x}".format(ord(byteStr)) 
    number=int(hexCode,16)
    return number

def Bytes2Int(byteStr):
    number=int(byteStr,16)
    print(number)

def getHeaderValue(num):
    
    if num >=0x81:
        test=((num))-256
    else:
        test=(num)
    return test

def reshap_for_chip_design(fail_bit_array):
    # Bank 2*4; sub array 8*8; cell:16*16
    bank_x=2
    bank_y=4
    sub_array_x=8
    sub_array_y=8
    cell_x=16
    cell_y=16
    return numpy.reshape(fail_bit_array,(bank_x,bank_y,sub_array_x,sub_array_y,cell_x,cell_y));
    
def seperate_bit_data(filename,offset,size,destFileName):
    #position=0
    #txt_bytes=0
    RowDataBytes=""

    localtime = time.asctime( time.localtime(time.time()) )
    print "start time :", localtime
    
    with open(filename, 'rb') as fh:
        fh.seek(int(offset,16),0)
        RowDataBytes=fh.read(int(size,16))

    #将BinaryData(压缩)再写回档案
    with open(destFileName, 'wb') as output:
        output.write(RowDataBytes)
    
    localtime = time.asctime( time.localtime(time.time()) )
    print "分解时间 :", localtime

def seperate_bit_data1(filename):
    #position=0
    #txt_bytes=0
    
    localtime = time.asctime( time.localtime(time.time()) )
    print "start time :", localtime
    list1=[]
    headKey=0
    byte=''
    RowDataBytes=""
    with open(filename, 'rb') as fh:
        byte=fh.read(1)
        while (byte<>''):
            hexCode="{:02x}".format(ord(byte))
            if hexCode=="1f":
                position=fh.tell()
                hexCode="{:02x}".format(ord(fh.read(1)))
                
                if hexCode=="8b":
                    hexCode="{:02x}".format(ord(fh.read(1)))
                    if hexCode=="08":
                        hexCode="{:02x}".format(ord(fh.read(1)))
                        if hexCode=="00":
                            list1.insert(headKey, position)
                            headKey+=1
            byte=fh.read(1)
        print(list1)
        fh.seek(list1[0]-1,0)
        #截取BinaryData
        RowDataBytes=fh.read(list1[1]-list1[0])
        hexCode="{:02x}".format(ord(fh.read(1)))
        print(hexCode)
    
    #将BinaryData(压缩)再写回档案
    with open('test.dat.gz', 'wb') as output:
        output.write(RowDataBytes)
     
    localtime = time.asctime( time.localtime(time.time()) )
    print "分解时间 :", localtime
    
                #hexCode="{:02x}".format(ord(fh.read(3)))
                #if hexCode=="8B":
                #    hexCode="{:02x}".format(ord(fh.read(1)))
                      
             #hexCode="{:02x}".format(ord(byte)) 

                     
                
        #position=fh.tell()
        #
        #txt_bytes=fh.read()
    
    #截取BinaryData
    #RowDataBytes=txt_bytes[position:]
    
    
    
def un_gz(file_name):
    localtime = time.asctime( time.localtime(time.time()) )
    print "解压開始时间 :", localtime 
    
    file_content=""
    
    """ungz zip file"""  
    f_name = file_name.replace(".gz", "")  
    #获取文件的名称，去掉 
    with gzip.GzipFile(file_name, 'rb',9) as f:
        file_content = f.read() 
    
    
    #g_file = gzip.GzipFile(file_name)  
    #创建gzip对象  
    open(f_name, "w+").write(file_content)  
    #gzip对象用read()打开后，写入open()建立的文件中。  
    #g_file.close()  
    #关闭gzip对象
    
    localtime = time.asctime( time.localtime(time.time()) )
    print "解压結束时间 :", localtime 

    
def get_bit_array():
    a=bitarray()
    with open('test_1.dat', 'rb') as output:
        #bitArray
        a.fromfile(output)
        #b = numpy.unpackbits(a)
    #print(a.length())
    localtime = time.asctime( time.localtime(time.time()) )
    print "读取时间 :", localtime
    return a;

if __name__ == "__main__":
    test_load_xml()
    #test_Logical_file() 
    

    
    


