#import GPIO
from gpiozero import LED
import numpy 
import numpy as np
import math
import cv2
import cv2 as cv
 
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
low_range = np.array([0,0,0])
high_range = np.array([255,30,255])
 
class Sobelxy():
       
        def sobelxy(self,img):
                self_img = img
                sobelx = cv2.Sobel(self_img,cv2.CV_64F,1,0)
                sobelx = cv2.convertScaleAbs(sobelx)
                sobely = cv2.Sobel(self_img,cv2.CV_64F,0,1)
                sobely = cv2.convertScaleAbs(sobely)
 
                sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
                return sobelxy
        
class Rxy():
	def rxy(self,erzhi,x,y,r):
		self_erzhi = erzhi
		self_x = x
		self_y = y
		self_r = r
		a = b = c = c1 =1
#		print("xyr",self_x,self_y,self_r)
		for l in range(self_x-self_r,self_x+self_r,3):
			if l < 0:
				l = 0
			if l > 236:
				l = 236
				
			for h in range(self_y-self_r,self_y+self_r,3):
				if h < 0:
					h = 0
				if h > 316:
					h = 316
				s = int(math.sqrt((l-self_x)**2+(h-self_y)**2))
#				print("lhs",l,h,s)
				if s <= self_r:
					print(l,h)
					a = a+self_erzhi[l,h]
					c = c+1
		for zx in range(self_x-self_r-20,self_y+self_r+20,5):
			for zy in range(self_y-self_r-20,self_y+self_r+20,5):
				b = b+self_erzhi[zx,zy]
				c1 = c1+1
		print(a/c,b/c1)
		if int(a/c) >= (int(b/c1)+50):
			print("yuan")
			cv.circle(frame1,(self_x,self_y),self_r,(255,0,0),2)
			cv.circle(frame1,(self_x,self_y),2,(255,0,0),2)
										
						
pin = LED(2) 
while (cap.isOpened()):
	erzhi = Rxy()
	ret,frame1 = cap.read()
	erzhi3 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
#	print(np.shape(frame1))
	cv2.imshow('2',erzhi3)
	frame = np.copy(frame1)
	frame1 = cv2.GaussianBlur(frame1,(5,5),0)
	bian = cv2.Canny(frame1,20,80)
	r1,erzhi2 = cv2.threshold(bian,128,255,cv2.THRESH_BINARY_INV)
	huofu = cv.HoughCircles(erzhi2,cv.HOUGH_GRADIENT,1,50,param1=80,param2=30,minRadius=0,maxRadius=0)
	
#	h = [huofu]
	if type(huofu) == numpy.ndarray:
		r_ball = huofu[0][0][2]
		print(huofu[0][0][2])
		if r_ball > 50:

			pin.on()	
#		huofu = np.uint16(np.around(huofu))
#		for i in huofu[0,:]:
#			x = int(i[0])
#			y = int(i[1])
#			r = int(i[2])
#			if erzhi2[y,x]:
#			               erzhi.rxy(erzhi3,x,y,r)
#			               print("x=,y=",x,y)
#			               print("r=",r)
#			               print("erzhi2=",erzhi2[y,x])
#			               cv.circle(frame1,(i[0],i[1]),i[2],(255,0,0),2)
#			               cv.circle(frame1,(i[0],i[1]),2,(255,0,0),2)
	else:
		print("bad")
		pin.off()
#	print(type(huofu))
	#b = None in h
	#if not any(None in h):
	#	print("YEP")
#if not huofu == None:
		#if not None in huofu:
	
#	print(len(huofu[0]))
#
#	if huofu != None:
#	huofu = np.uint16(np.around(huofu))
#	for i in huofu[0,:]:
#		x = int(i[0])
#		y = int(i[1])
#		r = int(i[2])
#		if erzhi2[y,x] and r<20 and r>5:
#				erzhi.rxy(erzhi3,x,y,r)
#				print("x=,y=",x,y)
#				print("r=",r)
#				print("erzhi2=",erzhi2[y,x])
#				cv.circle(frame1,(i[0],i[1]),i[2],(255,0,0),2)
#				cv.circle(frame1,(i[0],i[1]),2,(255,0,0),2)

	cv2.imshow('frame',frame)
	cv2.imshow('bian',bian)
	cv2.imshow('frame1',frame1)
	cv2.imshow('erzhi1',erzhi2)
	
	if cv2.waitKey(1) & 0XFF == ord('q'):
		break;
 
cap.release()
cv2.destroyAllWindows()
