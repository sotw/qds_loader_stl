---
title: A python utility for loading stl and visualization
date: 2017-03-07 17:00:00
tags: QDS
---
![](http://sotw.servebeer.com:8086/img/brainSkull.png)

##A python utility for loading stl and visualization

Get your copy from

```
git clone https://github.com/sotw/qds_loader_stl.git
```

Simply issue install and make sure 

```
~/bin/sh is existed inside your bashrc $PATH variable
```

[refer1](https://gist.github.com/Hodapp87/8874941)

#### Dependency
You will need to make sure your python can import everything.
for example: vtk

#### Note

I found the performance will be a problem if I try to X11 forwarding form SAS. 
So I decide to develop a little python tool for my mac mini.
I wrap a python script found from internet to a tiny scale project.

Here is what I made.

A infrastructure design makes user can issue 

```
$ qds_loader_stl xxx.stl
```
from anywhere.

So he/her can put all image file in a folder and use this utility to see the result.

#### First sample : A brain skull

![](http://sotw.servebeer.com:8086/img/brainSkull.png)

For this sample, it runs well

#### Second sample : Hairy Einstien

![](http://sotw.servebeer.com:8086/img/hairyEinstien.png)

For this one, I realize that maybe I do need a machine with right graphic card.
Einstien's hair looks bad.


