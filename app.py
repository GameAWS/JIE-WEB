import json
from urllib.request import Request, urlopen

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# 首页路由
@app.route('/')
def home():
    return render_template('index.html')

# 学术经历页路由
@app.route('/academic')
def academic():
    return render_template('academic.html')

# 实践与作品页路由
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/api/visits')
def visits():
    action = 'up' if request.args.get('increment') == '1' else ''
    counter_url = f'https://api.counterapi.dev/v1/jie-hu-portfolio/homepage/{action}'.rstrip('/')

    try:
        counter_request = Request(counter_url, headers={'User-Agent': 'Jie-Hu-Portfolio/1.0'})
        with urlopen(counter_request, timeout=5) as response:
            data = json.load(response)
        return jsonify({'count': data.get('count', 0)})
    except Exception:
        return jsonify({'error': 'Visit counter unavailable'}), 503

# ... 上面的路由代码保持不变 ...

# 只要确保上面有 app = Flask(__name__) 即可
# 下面这段是为了兼容本地测试和 Vercel 部署
if __name__ == '__main__':
    app.run(debug=True)
