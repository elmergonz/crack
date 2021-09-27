from fastapi import APIRouter
import multiprocessing as mp

router = APIRouter()

@router.get('/cores')
def get_cores():
    return {
        'core_count': mp.cpu_count()
    }
