from flask import Flask, render_template
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    # Set host to '0.0.0.0' to have the server available externally
    # replace '0.0.0.0' with ec2 IP
