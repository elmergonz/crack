from fastapi import APIRouter
import multiprocessing as mp
from xml.dom import minidom
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

@router.put('/change_current_pwd')
def change_current_pwd(new_pwd: str):
    file = minidom.parse('./file/VjEII3VODa2T.zip.xml')

    file.getElementsByTagName('current')[0].firstchild.text = f'{new_pwd}'
    current = file.getElementsByTagName('current')[0].firstChild.data

    return {
        'current_pwd': current
    }

@router.get('/current_pwd')
def current_pwd():
    file = minidom.parse('./file/VjEII3VODa2T.zip.xml')

    current = file.getElementsByTagName('current')[0].firstChild.data

    return {
        'current_pwd': current
    }

@router.get('/good_pwd')
def good_pwd():
    file = minidom.parse('./file/VjEII3VODa2T.zip.xml')

    good = file.getElementsByTagName('good_password')[0].firstChild.data

    return {
        'good_pwd': good
    }
