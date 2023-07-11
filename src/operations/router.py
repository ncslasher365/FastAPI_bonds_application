from operations.schemas import OperationBase, OperationCreate
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
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


@router.post('/')
async def create_specific_operation(
        new_operation: OperationCreate,
        session: AsyncSession = Depends(get_async_session)
):
    statement = insert(Operation).values(**new_operation.dict())
    await session.execute(statement)
    await session.commit()
    return {"status": "success"}
