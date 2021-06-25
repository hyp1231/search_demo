from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods = ['GET'])
def query():
    key = request.args.get('key')

    # Implement your search engine here.
    # Generate a list of search results.

    results = [
        {'title': '百度', 'url': 'https://www.baidu.com/'},
        {'title': '哔哩哔哩', 'url': 'https://www.bilibili.com/'},
        {'title': '知乎', 'url': 'https://www.zhihu.com/'}
    ]

    return render_template('res.html', key=key, results=results)

app.run(host='0.0.0.0', port=12345, debug=True)
