from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_data():
    print request.form;
    return '<div>REPLACE YO HTML WITH DIS</div>'

if __name__ == '__main__':
    app.run()
