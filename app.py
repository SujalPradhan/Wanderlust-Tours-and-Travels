from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/darjeeling_deluxe')
def darjeeling_deluxe():
    return render_template('darjeeling_deluxe.html')

@app.route('/darjeeling_premium')
def darjeeling_premium():
    return render_template('darjeeling_premium.html')

@app.route('/darjeeling_suite')
def darjeeling_suite():
    return render_template('darjeeling_suite.html')

@app.route('/kalimpong_deluxe')
def kalimpong_deluxe():
    return render_template('kalimpong_deluxe.html')

@app.route('/kalimpong_premium')
def kalimpong_premium():
    return render_template('kalimpong_premium.html')

@app.route('/kalimpong_suite')
def kalimpong_suite():
    return render_template('kalimpong_suite.html')

@app.route('/dooars')
def dooars():
    return render_template('dooars.html')

@app.route('/darjeeling')
def darjeeling():
    return render_template('darjeeling.html')

@app.route('/kalimpong')
def kalimpong():
    return render_template('kalimpong.html')

@app.route('/eastsikkim')
def eastsikkim():
    return render_template('eastsikkim.html')

@app.route('/southsikkim')
def southsikkim():
    return render_template('southsikkim.html')


if __name__ == '__main__':
    app.run(debug=True)



