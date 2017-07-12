import xml.dom.minidom
import time
import test_001 as bp
import filemerge as fm


def xmlparser(xmlfile):    
    dom = xml.dom.minidom.parse(xmlfile)
    root = dom.documentElement
    basedata = []
    file = []
    filemergelist = []
    chiplist = root.getElementsByTagName('wafer-chip')
    for chip in chiplist:
        if chip.getAttribute('prober-address-x') == '8' and chip.getAttribute(
            'prober-address-y') == '14':
            scalelist = chip.getElementsByTagName('image-fail-data')
            scalecount = 0
            for scale in scalelist:
                if scale.getAttribute('scale') == '256':
                    #scalenum = scale.getAttribute('scale')
                    #startx = scale.getAttribute('start-address-x')
                    #starty = scale.getAttribute('start-address-y')
                    #stopx = scale.getAttribute('stop-address-x')
                    #stopy = scale.getAttribute('stop-address-y')
                    filename = scale.getElementsByTagName('filename')[
                        0].firstChild.data
                    offset = scale.getElementsByTagName('offset')[
                        0].firstChild.data
                    size = scale.getElementsByTagName('size')[0].firstChild.data
#                    compresslist = scale.getElementsByTagName('compress')
#                     for i in compresslist:
#                         if i.getElementsByTagName('compress-type')[
#                                 0].firstChild.data == 'pack-bits':
#                             packsize = i.getElementsByTagName('uncompress-size')[
#                                 0].firstChild.data
#                         elif i.getElementsByTagName('compress-type')[
#                                 0].firstChild.data == 'gzip':
#                             gzipsize = i.getElementsByTagName('uncompress-size')[
#                                 0].firstChild.data
                    scalecount += 1
                    file = [
                        filename, offset, size,
                        'test' + str(scalecount) + '.dat.gz',
                        filename[:filename.find('_')] + '_' +
                        str(scale.getAttribute('scale')) + '_' + str(scalecount) +
                        '.dat'
                    ]
                    basedata.append(file)
                    filemergelist.append(file[4])
                    tofile = filename[:filename.find('_')] + '_'+str(scale.getAttribute('scale'))+'_'+'All'+'.dat'
            print basedata
            print len(basedata)
            print scalecount   
    bp.test_load_xml(basedata)
    fm.join(filemergelist,tofile)
    

xmlfile = 'D:\\BitFailData\\4g_69chip\\xml_phy\\bz4w01_wafer.xml'
localtime = time.asctime(time.localtime(time.time()))
print "xml start time :", localtime
xmlparser(xmlfile)
localtime = time.asctime(time.localtime(time.time()))
print "xml end time :", localtime  
