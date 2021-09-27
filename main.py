from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

import crack

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(crack.router, tags=['Crack'])

@app.get('/', tags=['Home'])
async def get_root():
    return {
        'api': 'proyecto final :D',
        'docs': 'https://rarcrack-gg.herokuapp.com/' + app.docs_url
    }
