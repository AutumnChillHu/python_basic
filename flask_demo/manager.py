# -*- coding: utf-8 -*-
from flask_demo.app import create_app

app = create_app()

if __name__ == '__main__':
    # app.run([,debug=True] [,host='0.0.0.0'] [,port='8090'])
    #   -debug=True：文件有改动时，会自动重启服务器。
    #   -可以显示指定host、port。
    app.run(debug=True)
