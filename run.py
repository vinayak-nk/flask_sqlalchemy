from server.app import create_app

from Config import DevConfig, ProdConfig, TestConfig

if __name__ == '__main__':
    app = create_app(DevConfig)
    app.run(debug=True)