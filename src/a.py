#!/usr/bin/python2.7


import imp

n1=imp.load_source('iface','./iface/iface.py')
n2=imp.load_source('cache','./cache/cache.py')
n3=imp.load_source('com','./com/com.py')
n4=imp.load_source('mem','./mem/mem.py')
n5=imp.load_source('NobFS','./NobFS/NobFS.py')

if __name__=='__main__':
	
	print '[Notice]: NobBot init ......'
	
	n1.iface()
	n2.cache()
	n3.com()
	n4.mem()
	n5.NobFS()
	
	print '[NobBot]: hello'
