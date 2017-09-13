# Web App Starter


This repo contains files to run a simple [Flask](http://flask.pocoo.org/ "Flask") app that uses [Boostrap](https://getbootstrap.com/ "Bootstrap") templates and formatting.

These files can be cloned to AWS instance to run a simple web Flask app using templates and formatting from Bootstrap.   

Setup AWS EC2 Instance:  



Remote Terminal:  
$ git clone https://github.com/christinebuckler/simple-web-app.git   
$ cd simple-web-app
$ screen -S webapp   
$ python app.py    
ctrl+a, d       (to detach, now able to close terminal or computer without terminating)  
ssh back into instance... 
$ screen -ls    (to  see screen sessions)  
$ screen -R webapp
ctrl+c          to stop running app  



view app in browser: 
$ open -a "Google Chrome" .html  
http://ec2-107-22-157-155.compute-1.amazonaws.com:8105/
