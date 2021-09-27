from fastapi import APIRouter
import multiprocessing as mp
import platform as pl

router = APIRouter()

@router.get('/system_info')
def get_cores():
    return {
        'core_count': mp.cpu_count(),
        'sys_info': pl.uname()
    }
