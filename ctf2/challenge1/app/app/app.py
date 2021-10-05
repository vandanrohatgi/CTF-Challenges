from flask import Flask, render_template, request,session
import re
import requests

app=Flask(__name__,static_url_path='',static_folder='web/static',template_folder='web/templates')
app.secret_key="BABABooey"
app.env="production"

@app.route('/')
def index():
    if 'logged_in' not in session:
        session['logged_in'] = False

    if session['logged_in']:
        return 'dc_9111{4n0th3r_One_B1tes_7h3_DusT!}'
    else:
        return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    if (request.form.to_dict()['message']):
        message=request.form.to_dict()['message']
        try:
            url=re.search("(?P<url>https?://[^\s]+)", message).group("url")
            header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0","X-Referrer":"/secretDashboard420"}
            requests.get(url,headers=header)
        except:
            return render_template('response.html')
    return render_template('response.html')

@app.route('/secretDashboard420')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run()