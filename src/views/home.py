from src import app

@app.route('/')
def home():
    return 'Home page'