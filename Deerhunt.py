from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.debug = False

@app.route('/')
def initialize_index():
	return render_template("index.html")

if __name__ == '__main__':
    app.run()
