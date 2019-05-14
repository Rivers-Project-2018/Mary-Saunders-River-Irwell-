# River Irwell 
As part of my final year project for my Mathematics degree at the University of Leeds, I have completed an analysis of the River Irwell in Greater Manchester, my motivation being the proximity in which I live to this river, and my interest in investigating how a large-scale flood might impact a large city. The River Irwell also flooded on Boxing Day in 2015, so I chose to focus on this flood to see how it compared to the floods already researched by the whole group.

I chose to use the monitoring station at Adelphi Weir, as it is very near to Manchester city centre, so it allowed me to analyse the effects of the flood on the busiest areas of the city.

## Quadrant plot

The Environment Agency provided me with the data I required to carry out this investigation [1] - river height and the rating curve information for the required time period. This data allowed me to plot the following graph, showing the relationships between river height, flow and time of the flood.

![adelphiweirpythongraph](https://github.com/Rivers-Project-2018/River-Irwell-Mary-Saunders/blob/master/adelphiweirpythongraph.png)

*Figure 1: Quadrant plot for the December 2015 flood of the River Irwell at Adelphi Weir monitoring station. A threshold height of 3m was used, indicated by the dotted line. A rating curve and its linear approximation can be seen in the upper left quadrant. Views of the river height and its flow rate across the flood duration T<sub>f</sub> = 10.00hrs can be seen in the lower left and upper right quadrants respectively. An estimation of the FEV was calculated to yield FEV = 6.58Mm<sup>3</sup> and can be represented by the area of the pink shaded region. The black rectangle has an area representative of an estimate FEV = 6.57 Mm<sup>3</sup>.*

My threshold height *h<sub>T</sub>* was chosen by looking at multiple sources. Shoothill's GaugeMap estimates that minor flooding is possible in the surrounding areas at a height of 2m [2]. However, From local knowledge, I know that on this day there was no flooding on the most recent highest height, 2.66m. A news article from the day of the Boxing Day flood states that the Mark Addy pub, near the Adelphi Weir station, was flooded by 3 to 4 feet of water by 3pm [3]. At 3pm, the height of the river was 3.592m (from the information provided by the Environment Agency). Therefore I estimated my threshold height above which flooding occurs as 3m, to ensure that the river has broken its banks by this height.

## Estimating FEV 

Using the Python code provided in https://github.com/Rivers-Project-2018/How-to-do-FEV-Analysis, I was able to calculate the flood excess volume to be 6.58 Mm<sup>3</sup>. Reaching this value allowed me to analyse current and proposed flood mitigation plans, along with suggesting some other hypothetical schemes.

## Current mitigation methods

In Salford there are two operational flood basins, only one of which was constructed before the Boxing Day 2015 flood. Both operate to alleviate flooding of the River Irwell, and are both upstream of the Adelphi Weir monitoring station, meaning we can look at them when mitigating the FEV. Together the Castle Irwell and Littleton Road flood basins can hold up to 1.24 Mm<sup>3</sup> of flood water, just 19% of the FEV value calculated. This value shows how much Greater Manchester would benefit from more flood defences against a flood of this magnitude.
 
## Proposed mitigation methods

Further upstream to Adelphi Weir is the city of Bury, which was heavily affected by the 2015 Boxing Day flood. As a result of this Bury Counci have announced the Radcliffe and Redvales Flood Defence Scheme [4], due to start construction in summer 2019 and is estimated to provide protection to around 870 properties. 

One proposed method is the construction of a further flood storage basin at Swan Lodge. Using an online tool and the volume and depth of the Castle Irwell storage area, I was able to estimate the volume of this basin to be 124,000 m<sup>3</sup>. Then, using a formula provided by the Environment Agency, the cost of the construction and maintenance of this proposed basin was estimated to be £0.88M.
 
## Hypothetical flood mitigation scenarios

In my full report I looked at multiple hypothetical mitigation schemes, such as tree planting and high flood walls, and investigated the cost and effectiveness of full mitigation scenarios. One of these included the two flood basins in Salford working in tandem with the proposed flood basin at Swan Lodge.

![irwellscenario3](https://github.com/Rivers-Project-2018/River-Irwell-Mary-Saunders/blob/master/irwellscenario3.png)

*Figure 2: Square lake graph showing the hypothetical flood mitigation scheme involving the two flood basins in Salford and the proposed basin at Swan Lodge.*

Figure 2 is a square lake graph which show that 20.89% of the FEV would be mitigated by the three basins together. It is provided to give a more realistic idea of a typical flood alleviation plan, as no hypothetical mitigation methods are
used. The purple area represents the two Salford basins, and the pink area the basin at Swan Lodge.

More full hypothetical flood mitigation scenarios and my cost-effectiveness analyses of these can be found at https://github.com/Rivers-Project-2018/River-Irwell-Mary-Saunders/blob/master/MATH3001%20Report.pdf.


## References

[1] Cooke, C. on behalf of the Environment Agency in Greater Manchester, Merseyside and Cheshire. Email to Mary Saunders, 8th November, 2018. 

[2] Shoothill GaugeMap. Shoothill GaugeMap. [Online]. [Accessed 19th March 2019]. Available from: https://www.gaugemap.co.uk.

[3] Manchester Evening News. Live updates: Clean-up continues after Greater Manchester hit by Boxing Day floods. [Online]. 2015. [Accessed 17th March 2019]. Available from: https://www.manchestereveningnews.co.uk/news/greater-manchester-news/live-updates-rain-flooding-manchester-10652325.

[4] Bury Council. Radclie and Redvales Flood defence scheme. [Online]. 2018. [Accessed 20th March 2019]. Available from: https://www.bury.gov.uk/index.aspx?articleid=13483.

