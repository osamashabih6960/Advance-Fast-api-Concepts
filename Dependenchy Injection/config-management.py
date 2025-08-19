from fastapi import FastAPI, Depends

app = FastAPI()

class Settings:
    def __init__(self):
        self.api_key = 'my_secret'
        self.debug = True
        
def get_settings():
    return Settings() # conf define
        
@app.get('/config')
def get_config(setting: Settings = Depends(get_settings)):
    return {'api_key':Settings.api_key}