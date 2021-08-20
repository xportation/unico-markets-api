import uvicorn

from markets import application

app = application.app

if __name__ == '__main__':
    uvicorn.run(app)
