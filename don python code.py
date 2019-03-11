#To Do:
#could automate more by doing lists with upper limits for rating curve and figuring
#out a quick way to place the ticks, e.g. a function or a loop.
#need to find a way to work out F.E.Q and Tf accurately.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Make plain plot
plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams['axes.edgecolor']='white'
fig, ax = plt.subplots()

#Import the Data
don=pd.read_csv('Don data.csv')
day = don['Day']
flow = don['Flowrate ']
height = don['Riverheight']

#CHANGE WITH EACH GRAPH
a = [0.223, 0.3077, 0.34, -0.5767]
b = [1.7742, 1.3803, 1.2967, 1.1066]
c = [78.4407, 77.2829, 79.5956, 41.3367]
lowlims = [0, 0.52, 0.931, 1.436]
uplims = [0.52, 0.931, 1.436, 3.58]
ht = 2.9

#Scale our Data
def scale(x):
    return ((x-min(x))/(max(x)-min(x)))
scaledday = scale(day)
scaledflow = scale(flow)
scaledheight = scale(height)
negday = -(scaledday)
negheight = -(scaledheight)

#Finding HM from HT
HM = []
for i in height:
    if i>=ht:
        HM.append(i)
hm=sum(HM)/len(HM)

#Finding qt and qm.
def Q(x):
    if x<=uplims[0] and x>=lowlims[0]:
        y = (c[0]*((x-a[0])**b[0]))
    elif x<=uplims[1] and x>lowlims[1]:
        y = (c[1]*((x-a[1])**b[1]))
    elif i<=uplims[2] and i>lowlims[2]:
        Flow.append(c[2]*((i-a[2])**b[2]))
    elif x<=max(height) and x>lowlims[3]:
        y = (c[3]*((x-a[3])**b[3]))
    return(y)
qt = Q(ht)
qm = Q(hm)   

#Rating Curve
Flow = []
for i in height:
    if i<=uplims[0] and i>=lowlims[0]:
        Flow.append(c[0]*((i-a[0])**b[0]))
    elif i<=uplims[1] and i>lowlims[1]:
        Flow.append(c[1]*((i-a[1])**b[1]))
    elif i<=uplims[2] and i>lowlims[2]:
        Flow.append(c[2]*((i-a[2])**b[2]))
    elif i<=max(height) and i>lowlims[3]:
        Flow.append(c[3]*((i-a[3])**b[3]))
scaledFlow = []
for i in Flow:
    scaledFlow.append((i-min(Flow))/(max(Flow)-min(Flow)))


#Plot the Rating Curve using Q NOT the Flow Rate.
negheight = -scaledheight
ax.plot(negheight,scaledFlow,'black',linewidth=2)
ax.plot([0,-1],[0,1],'black',linestyle='--', marker='', linewidth=2)
#Originally the dotted line was wrong because it went to the positional origin
#and not the actual origin.

#Plot the Flow Rate and Height against the Date.
negday = -(scaledday)
ax.plot(scaledday, scaledFlow, 'black', linewidth=2)
ax.plot(negheight, negday, 'black', linewidth=2)

#Plot the lines illustrating ht,hm,qt,qm
#Scaling ht,hm,qt and qm.
scaledht = (ht-min(height))/(max(height)-min(height))
scaledhm = (hm-min(height))/(max(height)-min(height))
scaledqt = (qt-min(Flow))/(max(Flow)-min(Flow))
scaledqm = (qm-min(Flow))/(max(Flow)-min(Flow))
ax.plot([-scaledht,-scaledht],[-1,scaledqt], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhm,-scaledhm],[-1,scaledqm], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledht,1],[scaledqt,scaledqt], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhm,1],[scaledqm,scaledqm], 'black', linestyle='--', linewidth=1)

#Fiddly plot to plot the box around the F.E.V. and the Tf line.
ax.plot([1/8,1/8,1/8],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([107/400,107/400,107/400],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([1/8,1/8],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([1/8,107/400],[scaledqm,scaledqm], 'black',linewidth=1.5)
ax.plot([1/8,107/400],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([107/400,107/400],[scaledqm,scaledqt], 'black',linewidth=1.5)

#Formatting the ticks and the Axis.
ticks_x = [-1.0782002,-0.8375842,-0.5969682,-0.3563523,-0.1157363,0,0.25,0.5,0.75,1]
#This describes the position I want each tick to be on a graph with x axis from -1 to 1.
#done by doing (2-min(height))/(max(height)-min(height)) to find where 2 should be 
#positioned on the axis.
ticks_y = [-1,-0.75,-0.5,-0.25,0,0.1637957,0.3637762,0.5637566,0.7637370,0.9637174]
ax.set_xticks(ticks_x)
ax.set_yticks(ticks_y)
Ticks_x = [5,4,3,2,1,25,26,27,28,29]
Ticks_y = [29,28,27,26,0,50,100,150,200,250]
ax.set_xticklabels(Ticks_x)
ax.set_yticklabels(Ticks_y)
ax.spines['left'].set_position(('center'))
ax.spines['bottom'].set_position(('center'))
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x', colors='black', direction='out', length=10, width=1)
ax.tick_params(axis='y', colors='black', direction='out', length=10, width=1)

#Graph Title.
plt.title('Don graph')

#Graph labels.
plt.text(-0.55, -1,'$h_T$')
plt.text(-0.83, -1,'$h_m$')
plt.text(1, scaledqm,'$Q_m$')
plt.text(1, scaledqt,'$Q_T$')
plt.text(0.3,0.7,'FEV', size=15)
plt.text(scaledday[70],-0.3,'$T_f$',size=13)
plt.annotate(s='', xy=(scaledday[47],-0.22), xytext=(scaledday[107],-0.22), arrowprops=dict(arrowstyle='<->'))

#Axis Labels.
plt.text(0.02, 1.05,'Q $[m^3/s]$', size=10)
plt.text(0.95, -0.2,'t [day]', size=10)
plt.text(-0.18, -1.11,'t [day]', size=10)
plt.text(-1.1, 0.05,r'$\bar{h}$  $[m]$', size=10)

#Arrows at end of Axis.
plt.text(-0.015,1.05,'^')
plt.text(-0.01,-1.11,'v')
plt.text(1.08,-0.02,'>')
plt.text(-1.105,-0.02,'<')

#Text on Graph.
plt.text(0.4,-0.6,'$FEV≈3.00Mm^3$', size=15)
plt.text(0.4,-0.7,'$T_f=13.50hrs$', size=15)
plt.text(0.4,-0.8,'$h_T=2.90m$', size=15)
plt.text(0.4,-0.9,'$h_m=4.06m$', size=15)
plt.text(0.4,-1,'$Q_T=164.1m^3/s$', size=15)
plt.text(0.4,-1.1,'$Q_m=225.9m^3/s$', size=15)

#Fill in the F.E.V.
QT=[]
for i in scaledFlow:
    i = scaledqt
    QT.append(i)
#Because I have to make qt into a list otherwise I get an error because I'm comparing
#a list with a float.
a=np.array(scaledFlow)
b=np.array(QT)
#Puts lists into an array as opposed to a list. Means that Python finds it easier to
#compare the 2.
ax.fill_between(scaledday,a,b,where=a>=b,facecolor='pink')

#Find the Tf
idx = np.argwhere(np.diff(np.sign(b - a))).flatten()
print(scaledday[idx])
def unscaleday(x):
    return (((max(day)-min(day))*x)+min(day))
c=unscaleday(0.283)
d=unscaleday(0.55)
Tf=(d-c)*24
print(Tf)
#find Tf in seconds
Tfs=Tf*(60**2)

#Find F.E.V
FEV=(qm-qt)*Tfs
print(FEV)