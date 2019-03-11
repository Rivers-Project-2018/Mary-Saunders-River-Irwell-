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
adelphi=pd.read_csv('Irwell Adelphi Weir data.csv')
day = adelphi['Day']
flow = adelphi['Flowrate ']
height = adelphi['Riverheight']

#CHANGE WITH EACH GRAPH
a = [0,-0.024]
b = [1.5728,1.8282]
c = [75.298,75.224]
lowlims = [0.158,0.815]
uplims = [0.815,2.1]
ht = 3

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
    elif x<=max(height) and x>lowlims[1]:
        y = (c[1]*((x-a[1])**b[1]))
    return(y)
qt = Q(ht)
qm = Q(hm)   

#Rating Curve
Flow = []
for i in height:
    if i<=uplims[0] and i>=lowlims[0]:
        Flow.append(c[0]*((i-a[0])**b[0]))
    elif i<=max(height) and i>lowlims[1]:
        Flow.append(c[1]*((i-a[1])**b[1]))
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
ax.plot([scaledday[144],scaledday[144],scaledday[144]],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([scaledday[182],scaledday[182],scaledday[182]],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([scaledday[144],scaledday[144]],[scaledqt,scaledqm], 'black',linewidth=1.5)
ax.plot([scaledday[182],scaledday[182]],[scaledqt,scaledqm], 'black',linewidth=1.5)
ax.plot([scaledday[144],scaledday[182]],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([scaledday[144],scaledday[182]],[scaledqm,scaledqm], 'black',linewidth=1.5)

#Formatting the ticks and the Axis.
ticks_x = [-1.0425281,-0.7471943,-0.4518606,-0.1565269,0,0.2,0.4,0.6,0.8,1]
#This describes the position I want each tick to be on a graph with x axis from -1 to 1.
#done by doing (2-min(height))/(max(height)-min(height)) to find where 2 should be 
#positioned on the axis.
ticks_y = [-1,-0.8,-0.6,-0.4,-0.2,0,0.08810069,0.20251716,0.31693364,0.43135011,0.54576659,0.66018307,0.77459954,0.88901602,1.00343249]
ax.set_xticks(ticks_x)
ax.set_yticks(ticks_y)
Ticks_x = [4,3,2,1,25,26,27,28,29,30]
Ticks_y = [30,29,28,27,26,0,100,200,300,400,500,600,700,800,900]
ax.set_xticklabels(Ticks_x)
ax.set_yticklabels(Ticks_y)
ax.spines['left'].set_position(('center'))
ax.spines['bottom'].set_position(('center'))
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x', colors='black', direction='out', length=10, width=1)
ax.tick_params(axis='y', colors='black', direction='out', length=10, width=1)

#Graph Title.
plt.title('Irwell (Adelphi Weir) graph')

#Graph labels.
plt.text(-scaledht+0.02, -1,'$h_T$')
plt.text(-scaledhm+0.02, -1,'$h_m$')
plt.text(1, scaledqm,'$Q_m$')
plt.text(1, scaledqt,'$Q_T$')
plt.text(0.43,0.7,'FEV', size=15)
plt.text(scaledday[150],-0.32,'$T_f$',size=13)
plt.annotate(s='', xy=(scaledday[140],-0.23), xytext=(scaledday[186],-0.23), arrowprops=dict(arrowstyle='<->'))


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
plt.text(0.4,-0.6,'$FEV≈6.36Mm^3$', size=15)
plt.text(0.4,-0.7,'$T_f=9.60hrs$', size=15)
plt.text(0.4,-0.8,'$h_T=3.00m$', size=15)
plt.text(0.4,-0.9,'$h_m=3.50m$', size=15)
plt.text(0.4,-1,'$Q_T=568.8m^3/s$', size=15)
plt.text(0.4,-1.1,'$Q_m=752.8m^3/s$', size=15)

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
c=unscaleday(0.299)
d=unscaleday(0.379)
Tf=(d-c)*24
print(Tf)
#find Tf in seconds
Tfs=Tf*(60**2)

#Find F.E.V
FEV=(qm-qt)*Tfs
print(FEV)