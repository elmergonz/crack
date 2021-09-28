from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

import crack, demo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(crack.router, tags=['crack'])
app.include_router(demo.router, tags=['demo'])

@app.get('/', tags=['Home'])
async def get_root():
    return {
        'api': 'proyecto de crackeo',
        'docs': 'https://rarcrack-gg.herokuapp.com/' + app.docs_url
    }
