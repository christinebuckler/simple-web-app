# Web App Starter

This repo can be cloned to AWS instance to run a simple web [Flask](http://flask.pocoo.org/ "Flask") app using templates and formatting from [Boostrap](https://getbootstrap.com/ "Bootstrap").   

Setup AWS EC2 Instance:  
Launch EC2 Instance  
Use Community AMI "DSI-Template3"  
Use free instance type "t2.micro"  
Configure instance details  
(Add storage)  
Add tags "Name", "webapp"  
Configure security group: Add Rule  
  Type: HTTP  
  Type: Custom TCP Rule, Port Range: 8105, Source: 0.0.0.0/0, ::/0   
Review and launch, Launch  
Create or use existing your_keypair.pem  
Connect to remote via local terminal: $ ssh -i ~/.ssh/your_keypair.pem username@PublicDNS(IPv4)  

Remote Terminal:  
$ git clone https://github.com/christinebuckler/simple-web-app.git   
$ cd simple-web-app
$ screen -S webapp   
$ python app.py    
ctrl+a, d       (to detach, now able to close terminal or computer without terminating)  
ssh back into instance... 
$ screen -ls    (to  see screen sessions)  
$ screen -R webapp
ctrl+c          (to stop running app)  

View web app in browser:
$ open -a "Google Chrome" http://ec2-107-22-157-155.compute-1.amazonaws.com:8105/  
