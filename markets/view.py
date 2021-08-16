from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def read_index():
    return {'Hello': 'World'}
