#必要なモジュールのインポート
from flask import Flask

#　Flask をインスタンス化
app = Flask(__name__)

# ルートディレクトリにアクセスがあった時の処理
# ルートディレクトリ = URL に一番最初にアクセスした時に表示する場所
@app.route('/') 
def hello():
    return 'Hello World!'

# エントリーポイント
if __name__ == '__main__': # ファイルを実行した時
    app.run()
