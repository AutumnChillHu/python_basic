# -*- coding: utf-8 -*-
from flask_script import Manager

from flask_demo import app

manager = Manager(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8090)
    # manager.run()
