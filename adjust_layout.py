#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 2:
	print 'You need to provide a path to the layout file.'
	print 'on Windows: python adjust_layout.py US-Private.klc'
	print 'on macOS: python adjust_layout.py US-Private.bundle/Contents/Resources/US-Private.keylayout'
	sys.exit()

filename = sys.argv[1]

with open(filename, 'rb') as f:
	s = f.read()
	
	#Windows
	if filename.endswith('.klc'):
		s = s.replace(b'\x45\x00\x09\x00\x09\x00\x31\x00\x09\x00\x65\x00\x09\x00\x45\x00', b'\x45\x00\x09\x00\x09\x00\x31\x00\x09\x00\x35\x04\x09\x00\x95\x03') #e/E
		s = s.replace(b'\x54\x00\x09\x00\x09\x00\x31\x00\x09\x00\x74\x00\x09\x00\x54\x00', b'\x54\x00\x09\x00\x09\x00\x31\x00\x09\x00\x74\x00\x09\x00\xa4\x03') #T
		s = s.replace(b'\x59\x00\x09\x00\x09\x00\x31\x00\x09\x00\x79\x00\x09\x00\x59\x00', b'\x59\x00\x09\x00\x09\x00\x31\x00\x09\x00\x43\x04\x09\x00\xae\x04') #y/Y
		s = s.replace(b'\x49\x00\x09\x00\x09\x00\x31\x00\x09\x00\x69\x00\x09\x00\x49\x00', b'\x49\x00\x09\x00\x09\x00\x31\x00\x09\x00\x56\x04\x09\x00\x99\x03') #i/I
		s = s.replace(b'\x4f\x00\x09\x00\x09\x00\x31\x00\x09\x00\x6f\x00\x09\x00\x4f\x00', b'\x4f\x00\x09\x00\x09\x00\x31\x00\x09\x00\x3e\x04\x09\x00\x9f\x03') #o/O
		s = s.replace(b'\x50\x00\x09\x00\x09\x00\x31\x00\x09\x00\x70\x00\x09\x00\x50\x00', b'\x50\x00\x09\x00\x09\x00\x31\x00\x09\x00\x40\x04\x09\x00\xa1\x03') #p/P
		s = s.replace(b'\x41\x00\x09\x00\x09\x00\x31\x00\x09\x00\x61\x00\x09\x00\x41\x00', b'\x41\x00\x09\x00\x09\x00\x31\x00\x09\x00\x30\x04\x09\x00\x91\x03') #a/A
		s = s.replace(b'\x48\x00\x09\x00\x09\x00\x31\x00\x09\x00\x68\x00\x09\x00\x48\x00', b'\x48\x00\x09\x00\x09\x00\x31\x00\x09\x00\x68\x00\x09\x00\x1d\x04') #H
		s = s.replace(b'\x4a\x00\x09\x00\x09\x00\x31\x00\x09\x00\x6a\x00\x09\x00\x4a\x00', b'\x4a\x00\x09\x00\x09\x00\x31\x00\x09\x00\x58\x04\x09\x00\x08\x04') #j/J
		s = s.replace(b'\x4b\x00\x09\x00\x09\x00\x31\x00\x09\x00\x6b\x00\x09\x00\x4b\x00', b'\x4b\x00\x09\x00\x09\x00\x31\x00\x09\x00\x6b\x00\x09\x00\x9a\x03') #K
		s = s.replace(b'\x58\x00\x09\x00\x09\x00\x31\x00\x09\x00\x78\x00\x09\x00\x58\x00', b'\x58\x00\x09\x00\x09\x00\x31\x00\x09\x00\x45\x04\x09\x00\xa7\x03') #x/X
		s = s.replace(b'\x43\x00\x09\x00\x09\x00\x31\x00\x09\x00\x63\x00\x09\x00\x43\x00', b'\x43\x00\x09\x00\x09\x00\x31\x00\x09\x00\x41\x04\x09\x00\x21\x04') #c/C
		s = s.replace(b'\x42\x00\x09\x00\x09\x00\x31\x00\x09\x00\x62\x00\x09\x00\x42\x00', b'\x42\x00\x09\x00\x09\x00\x31\x00\x09\x00\x62\x00\x09\x00\x92\x03') #B
		s = s.replace(b'\x4e\x00\x09\x00\x09\x00\x31\x00\x09\x00\x6e\x00\x09\x00\x4e\x00', b'\x4e\x00\x09\x00\x09\x00\x31\x00\x09\x00\x6e\x00\x09\x00\x9d\x03') #N
		s = s.replace(b'\x4d\x00\x09\x00\x09\x00\x31\x00\x09\x00\x6d\x00\x09\x00\x4d\x00', b'\x4d\x00\x09\x00\x09\x00\x31\x00\x09\x00\x6d\x00\x09\x00\x9c\x03') #M

	#macOS
	if filename.endswith('.keylayout'):
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x61\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd0\xb0\x22') #а
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x79\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd1\x83\x22') #у
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x78\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd1\x85\x22') #х
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x63\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd1\x81\x22') #с
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x65\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd0\xb5\x22') #е
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x6f\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd0\xbe\x22') #о
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x69\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd1\x96\x22') #і
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x70\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd1\x80\x22') #р
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x6a\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd1\x98\x22') #ј
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x41\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xce\x91\x22') #Α
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x48\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd0\x9d\x22') #Н
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x59\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd2\xae\x22') #Ү
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x58\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xce\xa7\x22') #Χ
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x43\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd0\xa1\x22') #С
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x42\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xce\x92\x22') #Β
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x45\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xce\x95\x22') #Ε
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x54\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xce\xa4\x22') #Τ
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x4f\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xce\x9f\x22') #Ο
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x49\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xce\x99\x22') #Ι
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x50\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xce\xa1\x22') #Ρ
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x4a\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xd0\x88\x22') #Ј
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x4b\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xce\x9a\x22') #Κ
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x4e\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xce\x9d\x22') #Ν
		s = s.replace(b'\x6f\x75\x74\x70\x75\x74\x3d\x22\x4d\x22', b'\x6f\x75\x74\x70\x75\x74\x3d\x22\xce\x9c\x22') #Μ

with open(filename, 'wb') as f:
	f.write(s)

print 'Done. '+filename+' adjusted.'
if filename.endswith('.klc'):
	print 'Proceed with compiling the layout into DLL.'
if filename.endswith('.keylayout'):
	print 'Proceed with installing the layout bundle.'
