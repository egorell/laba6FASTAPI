from typing import List

from fastapi import APIRouter
from .models import OutputGroup

router = APIRouter()

@router.get('/')
def get_group() -> List[OutputGroup]:
    return ({'id': 1, 'name': '3ИСПк2'},
            {'id': 2, 'name': '3ИСПк1'})