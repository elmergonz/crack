from fastapi import APIRouter
import multiprocessing as mp
from xml.dom import minidom
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
        'demo': 'running'
    }

@router.get('/stop_demo')
def stop_demo():
    os.system(f'pkill rarcrack')

    return {
        'demo': 'stopped'
    }

@router.get('/current_pwd_demo')
def current_pwd_demo():
    file = minidom.parse('./demo/demo.zip.xml')

    current = file.getElementsByTagName('current')[0].firstChild.data

    return {
        'current_pwd': current
    }

@router.get('/good_pwd_demo')
def good_pwd_demo():
    file = minidom.parse('./demo/demo.zip.xml')

    good = file.getElementsByTagName('good_password')[0].firstChild.data

    return {
        'good_pwd': good
    }
