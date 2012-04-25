from Tkinter import *
from PIL import Image, ImageTk
import sys
import os
from subprocess import call
import subprocess
import util
import random
from random import choice
import time
import string

lastx, lasty = 0, 0

def xy(event):
	global lastx, lasty
	lastx, lasty = event.x, event.y

def startLine(event):
	global lastx, lasty
	lastx, lasty = event.x, event.y

def endLine(event):
	global lastx, lasty
	canvas.create_line((lastx, lasty, event.x, event.y), width=5, fill="#B35F32")
	print "canvas.create_line(({0}, {1}, {2}, {3}), width=5, fill='#B35F32')".format(lastx, lasty, event.x, event.y)
	lastx, lasty = event.x, event.y

def collectConnected(event):
	f = open('data.txt', 'a')
	print event.x
	print event.y
	location = (event.x, event.y)
	for i in range(300):
		agrCtlRSSI = int(subprocess.check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep agrCtlRSSI", shell = True).strip().split(" ")[1])
		line = str(location[0]) + "," + str(location[1]) + "|" + str(agrCtlRSSI) + "\n"
		print line
		f.write(line)
		time.sleep(0.1)
	print "Collected"
	f.close()

def collectAll(event):
	f = open('data_all.txt', 'a')
	print event.x
	print event.y
	location = (event.x, event.y)
	for i in range(20):
		output = subprocess.check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s", shell=True).strip()
		networks = output.split("\n")
		del networks[0]
		for i in networks:
			row = i.strip().split(" ")
			BSSID = row[1]
			agrCtlRSSI = row[2]
			line = str(location[0]) + "," + str(location[1]) + "|" + str(BSSID) + "|" + agrCtlRSSI.strip() + "\n"
			print line
			f.write(line)
	print "Collected"
	f.close()


def loadMap(floorPlan):
	if floorPlan == "home":
		canvas.create_line((97, 67, 720, 73), width=5, fill='#B35F32')
		canvas.create_line((717, 471, 95, 463), width=5, fill='#B35F32')
		canvas.create_line((95, 463, 99, 69), width=5, fill='#B35F32')
		canvas.create_line((720, 75, 716, 473), width=5, fill='#B35F32')
		canvas.create_line((257, 70, 253, 286), width=5, fill='#B35F32')
		canvas.create_line((253, 286, 99, 286), width=5, fill='#B35F32')
		canvas.create_line((200, 164, 99, 162), width=5, fill='#B35F32')
		canvas.create_line((233, 165, 255, 166), width=5, fill='#B35F32')
		canvas.create_line((199, 138, 152, 111), width=5, fill='#B35F32')
		canvas.create_line((152, 111, 104, 111), width=5, fill='#B35F32')
		canvas.create_line((232, 138, 257, 139), width=5, fill='#B35F32')
		canvas.create_line((235, 118, 254, 119), width=5, fill='#B35F32')
		canvas.create_line((254, 315, 253, 415), width=5, fill='#B35F32')
		canvas.create_line((253, 415, 98, 416), width=5, fill='#B35F32')
		canvas.create_line((228, 318, 99, 322), width=5, fill='#B35F32')
		canvas.create_line((256, 318, 255, 288), width=5, fill='#B35F32')
		canvas.create_line((254, 285, 362, 200), width=5, fill='#B35F32')
		canvas.create_line((298, 303, 377, 233), width=5, fill='#B35F32')
		canvas.create_line((363, 203, 612, 195), width=5, fill='#B35F32')
		canvas.create_line((610, 228, 377, 234), width=5, fill='#B35F32')
		canvas.create_line((613, 196, 636, 212), width=5, fill='#B35F32')
		canvas.create_line((636, 213, 611, 230), width=5, fill='#B35F32')
		canvas.create_line((614, 197, 612, 75), width=5, fill='#B35F32')
		canvas.create_line((638, 211, 676, 185), width=5, fill='#B35F32')
		canvas.create_line((676, 185, 719, 185), width=5, fill='#B35F32')
		canvas.create_line((376, 203, 375, 72), width=5, fill='#B35F32')
		canvas.create_line((496, 198, 493, 74), width=5, fill='#B35F32')
		canvas.create_line((497, 126, 614, 126), width=5, fill='#B35F32')
		canvas.create_line((616, 145, 497, 145), width=5, fill='#B35F32')
		canvas.create_line((533, 124, 532, 96), width=5, fill='#B35F32')
		canvas.create_line((532, 96, 574, 98), width=5, fill='#B35F32')
		canvas.create_line((574, 98, 576, 124), width=5, fill='#B35F32')
		canvas.create_line((613, 232, 609, 365), width=5, fill='#B35F32')
		canvas.create_line((609, 365, 717, 368), width=5, fill='#B35F32')
	else:
		canvas.create_line((112, 63, 114, 459), width=5, fill='#B35F32')
		canvas.create_line((114, 459, 692, 471), width=5, fill='#B35F32')
		canvas.create_line((692, 471, 690, 69), width=5, fill='#B35F32')
		canvas.create_line((690, 69, 112, 67), width=5, fill='#B35F32')
		canvas.create_line((116, 350, 169, 351), width=5, fill='#B35F32')
		canvas.create_line((169, 351, 168, 277), width=5, fill='#B35F32')
		canvas.create_line((116, 240, 167, 245), width=5, fill='#B35F32')
		canvas.create_line((167, 245, 164, 233), width=5, fill='#B35F32')
		canvas.create_line((164, 233, 169, 233), width=5, fill='#B35F32')
		canvas.create_line((218, 232, 329, 231), width=5, fill='#B35F32')
		canvas.create_line((375, 230, 556, 230), width=5, fill='#B35F32')
		canvas.create_line((556, 69, 568, 467), width=5, fill='#B35F32')
		canvas.create_line((205, 353, 311, 349), width=5, fill='#B35F32')
		canvas.create_line((311, 349, 314, 464), width=5, fill='#B35F32')
		canvas.create_line((229, 233, 231, 108), width=5, fill='#B35F32')
		canvas.create_line((382, 230, 386, 72), width=5, fill='#B35F32')
		canvas.create_line((310, 352, 564, 352), width=5, fill='#B35F32')

def loadDataAll(floorPlan):
	if floorPlan == "home":
		f = open('san_diego_data_all.txt', 'r')
	else:
		f = open('data_all.txt', 'r')
	bssidScoreLoc = dict()
	BSSIDs = set()
	for line in f:
		array = line.split("|")
		location = array[0]
		xcoor = int(location.split(",")[0])
		ycoor = int(location.split(",")[1])
		bssid = array[1]
		score = int(array[2])
		point = (xcoor, ycoor)
		BSSIDs.add(bssid)
		if bssidScoreLoc.has_key(bssid):
			if bssidScoreLoc[bssid].has_key(score):
				if bssidScoreLoc[bssid][score].has_key(point):
					bssidScoreLoc[bssid][score][point] += 1
				else:
					bssidScoreLoc[bssid][score][point] = 1
			else:
				bssidScoreLoc[bssid][score] = dict()
				bssidScoreLoc[bssid][score][point] = 1
		else:
			bssidScoreLoc[bssid] = dict()
			bssidScoreLoc[bssid][score] = dict()
			bssidScoreLoc[bssid][score][point] = 1
	print BSSIDs
	return normalizeDictAll(bssidScoreLoc)
	f.close()
def loadDataConnected(floorPlan):
	if floorPlan == "home":
		f = open('san_diego_data.txt', 'r')
	else:
		f = open('data.txt', 'r')
	scoreLoc = dict()
	for line in f:
		array = line.split("|")
		location = array[0]

		xcoor = int(location.split(",")[0])
		ycoor = int(location.split(",")[1])
		score = int(array[1])
		point = (xcoor, ycoor)
		if scoreLoc.has_key(score):
			if scoreLoc[score].has_key(point):
				scoreLoc[score][point] += 1
			else:
				scoreLoc[score][point] = 1
		else:
			scoreLoc[score] = dict()
			scoreLoc[score][point] = 1
	return normalizeDictConnected(scoreLoc)

def normalizeDictAll(d):
	for bssid,scoreLoc in d.items():
		for score, locCount in scoreLoc.items():
			total = 0.
			for kv in locCount.items():
				total += kv[1]
			for kv in locCount.items():
				d[bssid][score][kv[0]] = kv[1]/total
	return d
def normalizeDictConnected(d):
	for score, locCount in d.items():
		total = 0.
		for kv in locCount.items():
			total += kv[1]
		for kv in locCount.items():
			d[score][kv[0]] = kv[1]/total
	return d

def trackAll(d):
	width = 2
	networks = subprocess.check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s", shell=True).strip().split("\n")
	del networks[0]
	canvas.delete("oval")
	for i in networks:
		row = i.strip().split(" ")
		BSSID = row[1]
		try:
			agrCtlRSSI = int(row[2])
		except:
			agrCtlRSSI = None
		try:
			locs = d[BSSID][agrCtlRSSI]
			color = "#"+BSSID[3:11]
			color = string.replace(color, ":", "")
			for k,v in locs.items():
				for i in range(int(2*v)):
					xoffset = random.randint(-5,5)
					yoffset = random.randint(-5,5)
					oval = canvas.create_oval(k[0]-width+xoffset,k[1]-width+yoffset,k[0]+width+xoffset,k[1]+width+yoffset, fill=color, tags="oval")
		except Exception, e:
			print BSSID, agrCtlRSSI
	root.after(1, trackAll, d)

def trackConnected(d):
	width = 2
	agrCtlRSSI = int(subprocess.check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep agrCtlRSSI", shell = True).strip().split(" ")[1])
	try:
		locs = d[agrCtlRSSI]
		color = "red"
		canvas.delete("oval")
		for k,v in locs.items():
			for i in range(int(10*v)):
				xoffset = random.randint(-5,5)
				yoffset = random.randint(-5,5)
				oval = canvas.create_oval(k[0]-width+xoffset,k[1]-width+yoffset,k[0]+width+xoffset,k[1]+width+yoffset, fill=color, tags="oval")
		print agrCtlRSSI
	except Exception, e:
		print agrCtlRSSI
	root.after(1, trackConnected, d)

if __name__ == "__main__":
	print "Starting..."
	root = Tk()
	width = 800
	height = 600
	state = sys.argv[1]
	floorPlan = sys.argv[2]
	size = sys.argv[3]
	print size
	canvas = Canvas(root, width=width, height=height)
	canvas.pack()
	im = Image.open("back.gif")
	tk_im = ImageTk.PhotoImage(im)
	canvas.create_image(width/2.,height/2.,image=tk_im)
	canvas.config(bg = "black")
	if state == "b":
		canvas.bind("<Button-1>", startLine)
		canvas.bind("<Button-2>", endLine)
	elif state == "c":
		if size == "all":
			canvas.bind("<Button-1>", collectAll)
		else:
			canvas.bind("<Button-1>", collectConnected)
	else:
		if size == "all":
			data = loadDataAll(floorPlan)
			root.after(1000, trackAll, data)
		else:
			data = loadDataConnected(floorPlan)
			root.after(1000, trackConnected, data)

	loadMap(floorPlan)
	print "Map Loaded"
	root.mainloop()