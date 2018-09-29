from app import app

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
    import threading
    import pandas as pd
    from bs4 import BeautifulSoup
    import requests
