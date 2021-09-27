from fastapi import APIRouter
import multiprocessing as mp
import platform as pl
import os

router = APIRouter()

@router.get('/system_info')
def get_cores():
    return {
        'core_count': mp.cpu_count(),
        'sys_info': pl.uname()
    }

@router.get('/create_file')
def create_file():
    os.system('echo hola >> hola.txt')

    with open('hola.txt', 'r') as file:
        return {
            'msg': file.readlines()
        }
