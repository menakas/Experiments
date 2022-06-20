This folder contains files relevant to [this post](https://www.linkedin.com/pulse/visualization-graphviz-menaka-sankaralingam/?trackingId=sCsFkXpPTZ6m43hW9mU5OA%3D%3D).

**Example 1**

Run

`dot -Tpng example01.dot > example01.png`

to generate the graph for example 1.

![](https://github.com/menakas/Experiments/blob/main/GraphViz/example01.png?raw=true)

**Example 2**

Run

`dot -Tpng example02.dot > example02.png`

to generate the graph for example 2.

![](https://github.com/menakas/Experiments/blob/main/GraphViz/example02.png?raw=true)

**Bags**

Run the following for each sample of the bags graph.

```
        python bags.py < sample1.input > bags1.dot
        dot -Tpng bags1.dot > bags1.png
```  
![](https://github.com/menakas/Experiments/blob/main/GraphViz/bags1.png?raw=true)
        
```
        python bags.py < sample2.input > bags2.dot
        dot -Tpng bags2.dot > bags2.png
        
```
![](https://github.com/menakas/Experiments/blob/main/GraphViz/bags2.png?raw=true)
for the bags graph
