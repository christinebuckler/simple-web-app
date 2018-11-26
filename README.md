# Web App Starter

This repo can be cloned to AWS instance to run a simple web [Flask](http://flask.pocoo.org/ "Flask") app using templates and formatting from [Boostrap](https://getbootstrap.com/ "Bootstrap").   

Setup AWS EC2 Instance:  
Add tags "Name", "webapp"  
Configure security group: Add Rule  
  Type: HTTP  
  Type: Custom TCP Rule, Port Range:5000, Source:0.0.0.0/0, ::/0   
Review and launch  
Connect to remote via local terminal: $ ssh -i ~/.ssh/your_keypair.pem username@ec2-###-##-##-###.compute-1.amazonaws.com  

Remote Terminal:  
$ `git clone https://github.com/christinebuckler/simple-web-app.git`   
$ `cd simple-web-app`  
$ `screen -S webapp`  
$ `python app.py`  
ctrl+a, d       (to detach, now able to close terminal or computer without terminating)  
ssh back into instance...  
$ `screen -ls`  (to  see screen sessions)  
$ `screen -R webapp`  
ctrl+c          (to stop running app)  

View web app in browser:
$ `open -a "Google Chrome" http://ec2-###-##-###-###.compute-1.amazonaws.com:5000/` 
