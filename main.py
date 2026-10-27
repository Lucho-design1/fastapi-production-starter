from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def read_root(): return {'status': 'ready', 'payment_support': 'https://paypal.me/LucianoBenechCenoz'}