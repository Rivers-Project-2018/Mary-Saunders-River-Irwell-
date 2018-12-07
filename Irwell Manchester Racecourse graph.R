### 1. Figure out how to find intersections between qm/qt and Q time curve,
### in order to plot and find Tf lines and value automatically. 
### 2. Then plot FEV box and use polygon or fill function to fill in FEV 
### area. 
### 3. Work out Tf and draw Tf arrow automatically.
### 4. Work out FEV automatically. 

### Import data and change values specific to each river
IrwellData <- read.csv("Irwell Manchester Racecourse data.csv", header = TRUE)
t <- IrwellData$Day
flow <- IrwellData$Flowrate
h <- IrwellData$Riverheight
ht <- c(3.75)
### Rating curve values and matrices
a <- c()
b <- c()
c <- c()
lowlims <- c()
uplims <- c()
### Axis ticks labels
negxaxis <- c(6,5,4,3,2,1)
posxaxis <- c(0.2,0.4,0.6,0.8,1)
negyaxis <- c(-1,-0.8,-0.6,-0.4,-0.2,0)
posyaxis <- c(100,200,300,400,500,600,700)

### REMEMBER TO CHANGE PLOT TITLE AND LABELS ETC LATER ON IN CODE


### Create initial vectors for each variable
tvec <- c(t)
flowvec <- c(flow)
hvec <- c(h)
qvec <- c(flow)


### Create function to scale data to between 0 and 1
scalevec <- function(x) {
  return ((x - min(x)) / (max(x) - min(x)))
}


### Scale variables and create vectors for each 
scaledt <- scalevec(tvec)
scaledflow <- scalevec(flowvec)
scaledh <- scalevec(hvec)
negt <- -(scaledt)
negh <- -(scaledh)


### Scale Q vectors to allow them to be plotted
scaledq <- scalevec(qvec)


### Find hm, then find Qm and Qt from hm and ht using rating curve formula
hm <- c()
for(i in h) {
  if(i > ht) hm<-c(hm, i)
}
hm<-sum(hm)/length(hm)


### Scale values of straight lines
scaledht <- (ht - min(h)) / (max(h) - min(h))
scaledhm <- (hm - min(h)) / (max(h) - min(h))
scaledqm <- (qmvec - min(Qhvec)) / (max(Qhvec) - min(Qhvec))
scaledqt <- (qtvec - min(Qhvec)) / (max(Qhvec) - min(Qhvec))


### Scale positions of axis ticks
minh <- min(h)
maxh <- max(h)
minq <- min(qvec)
maxq <- max(qvec)

scalexaxis <- function(x) {
  return ((x - minh) / (maxh - minh))
}

scaleyaxis <- function(x) {
  return ((x - minq) / (maxq - minq))
}

scaledxaxis <- scalexaxis(negxaxis)
scaledyaxis <- scaleyaxis(posyaxis)

xaxis <- c(-(scaledxaxis), posxaxis)
yaxis <- c(negyaxis, scaledyaxis)

### Plot graph
plot(1, type="n", xlim=c(-1, 1), ylim=c(-1, 1), axes=FALSE, xlab=NA, ylab=NA, xaxt='n', yaxt='n', main="Irwell (Manchester Racecourse) graph")
axis(side=1, cex.axis=0.5, pos=0, at=xaxis,labels=c("6","5","4","3","2","1","26","27","28","29","30"))
axis(side=2,cex.axis=0.5, pos=0, at=yaxis,labels=c("30","29","28","27","26","0","100","200","300","400","500","600","700"), las=1)
lines(negh,negt)
lines(negh,scaledq)
lines(scaledt,scaledq)
segments(x0=0, y0=0, x1 = -max(scaledh), y1 = max(scaledq), lty=2)
segments(x0=-(scaledht), y0=-1, x1=-(scaledht), y1=1, lty=3)
segments(x0=-(scaledhm), y0=-1, x1=-(scaledhm), y1=1, lty=3)


### Fill FEV area manually
polygon(x=scaledt[], y=scaledflow[], col="seagreen1")


### Axes and line labels ###
text(x=0, y=-1 ,label="t", cex=0.5, pos=4, font=3)
text(x=0.03, y=-1 ,label="[day]", cex=0.5, pos=4)
text(x=0, y=1 ,label="Q", cex=0.5, pos=4, font=3)
text(x=0.135, y=1 ,label=expression("[m"^3), cex=0.5)
text(x=0.125, y=0.99 ,label="/s]", cex=0.5, pos=4)
text(x=0.93, y=-0.05 ,label="t", cex=0.5, pos=1, font=3)
text(x=1, y=-0.05 ,label="[day]", cex=0.5, pos=1)
text(x=-0.98, y=-0.01 ,label=bquote(bar(h)), cex=0.5, pos=3, font=3)
text(x=-0.92, y=-0.01 ,label="[m]", cex=0.5, pos=3)
text(x=-(scaledht), y=-1 ,label="hT", cex=0.5, pos=4, font=3)
text(x=-(scaledhm), y=-1 ,label="hM", cex=0.5, pos=4, font=3)
text(x=1, y=scaledqm ,label="Qm", cex=0.5, pos=1, font=3)
text(x=1, y=scaledqt ,label="Qt", cex=0.5, pos=1, font=3)
text(x=scaledt[201], y=-0.35, label="Tf", cex=0.5, pos=1, font=3)
text(x=scaledt[400], y=-0.55, label="FEV ≈ 9.34Mm^3", cex=0.5)
text(x=scaledt[418], y=-0.62, label="Tf = 32.00hrs", cex=0.5)
text(x=scaledt[424], y=-0.69, label="hT = 3.75m", cex=0.5)
text(x=scaledt[424], y=-0.76, label="hM = 4.93m", cex=0.5)
text(x=scaledt[390], y=-0.83, label="Qt = 219.1", cex=0.5)
text(x=scaledt[444], y=-0.82 ,label=expression("m"^3), cex=0.5)
text(x=scaledt[464], y=-0.82 ,label="/s", cex=0.5)
text(x=scaledt[380], y=-0.9, label="Qm = 299.3", cex=0.5)
text(x=scaledt[444], y=-0.89 ,label=expression("m"^3), cex=0.5)
text(x=scaledt[464], y=-0.89,label="/s", cex=0.5)
text(x=0.42, y=0.7, label="FEV")


### Straight lines plotted manually which I need to figure out how to plot
### automatically
segments(x0=scaledt[139], y0=scaledqt, x1=scaledt[265], y1=scaledqt)
segments(x0=scaledt[139], y0=scaledqm, x1=scaledt[265], y1=scaledqm)
segments(x0=scaledt[139], y0=scaledqt, x1=scaledt[139], y1=scaledqm)
segments(x0=scaledt[265], y0=scaledqt, x1=scaledt[265], y1=scaledqm)


### Tf lines and arrow plotted manually
segments(x0=scaledt[137], y0=-0.35, x1=scaledt[137], y1=scaledqt, lty=3)
segments(x0=scaledt[265], y0=-0.35, x1=scaledt[265], y1=scaledqt, lty=3)
arrows(x0=scaledt[137], y0=-0.35, x1=scaledt[265], y1=-0.35, length = 0.05, code=3)



### DOESN'T WORK, NEED TO ADAPT THIS CODE. Fill grey area, x coordinates 
### manually but y automatically
ypolygon <- c()

for(i in Qhvec) {
  if(i > qt) ypolygon<-c(ypolygon, i)
}

polygon(x=scaledt[139:266],y=ypolygon,col="grey")
