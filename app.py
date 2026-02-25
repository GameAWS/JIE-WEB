from flask import Flask, render_template

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

# ... 上面的路由代码保持不变 ...

# 只要确保上面有 app = Flask(__name__) 即可
# 下面这段是为了兼容本地测试和 Vercel 部署
if __name__ == '__main__':
    app.run(debug=True)