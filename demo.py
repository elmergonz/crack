from fastapi import APIRouter
import multiprocessing as mp
import os

router = APIRouter()
demo_count = 1

@router.get('/run_demo')
def run_demo():
    global demo_count
    cores = mp.cpu_count()
    file_name = './demo/demo.zip'

    if demo_count:
        demo_count = 0
        os.system(f'./bin/script.sh {cores} {file_name} -d')
    else:
        os.system(f'./bin/script.sh {cores} {file_name}')

    return {
        'crack': 'running'
    }
