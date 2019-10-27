# Threads and Scheduling
> Producer and Consumer

## Table of contents
- [General info](#general-info)
- [How to use](#how-to-use)
- [How to execute the process](#how-to-execute-the-process)
- [Who helped me](#who-helped-me)
- [Author](#author)

## Description
This project simulates a First Come First Served scheduling algorithm for a distributed system that consists of mobile devices and a central computer server.

We assume that we have multiple mobile devices (mobile.py) that generate computational problems that are too heavy to be performed in their hardware, either because the device's battery will drain, they do not have enough memory, nor computational resources to perform them in a timely manner.

We will simulate a central server (scheduler.py) that will receive requests for computing time from the mobile devices, will put the jobs in a queue of processes, and then will “execute” them.


## How to use
Open mobile.py:
* Variable _numJobs_ assigns a random amount of jobs for a mobile. The user can determine an specific value.
* Variable _maxTime_ assigns a random number of maximum CPU time a jobs can have. The user can determine a value.

Open scheduler.py
* Variable _N_ stablishes the how many messages the server will insert in queue and the user can specify a number

## How to execute the process
To run the programs: 
1) First, run scheduler.py specifying the port that the server will run on. 
```sh
$ python scheduler.py 4444 
```
2) Open another terminal window

3)  Then, run mobile.py specifying the server address and port. 
```sh
$ python mobile.py 1 localhost 4444
```
4) Step 3 should be repeated until the number of _N_ is reached on the scheduler.


## Who helped me or discussed issues with me to finish the program
1) Manuel Álavarez-Rios


## Author
Created by Dianelys Soto-Cruz

## References

Python UDP Socket Programming
http://www.binarytides.com/programming-udp-sockets-in-python/




[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

