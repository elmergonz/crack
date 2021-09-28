from fastapi import APIRouter
import multiprocessing as mp
import os

router = APIRouter()

@router.get('/run_crack')
def run_crack():
    global demo_count
    cores = mp.cpu_count()
    file_name = './file/VjEII3VODa2T.zip'
    
    os.system(f'./bin/script.sh {cores} {file_name}')

    return {
        'crack': 'running'
    }

@router.get('/stop_crack')
def stop_crack():
    os.system(f'pkill rarcrack')

    return {
        'crack': 'stopped'
    }
