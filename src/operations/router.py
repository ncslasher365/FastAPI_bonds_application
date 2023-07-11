from operations.schemas import OperationBase
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import Operation

router = APIRouter(
    prefix='/operations',
    tags=['operations']
)


@router.get('/', response_model=List[OperationBase])
async def get_specific_operations(
        operation_type: str,
        session: AsyncSession = Depends(get_async_session)
):
    query = select(Operation).where(Operation.operation_type == operation_type)
    query_result = await session.execute(query)
    return query_result.scalars().all()
