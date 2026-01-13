from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_db
from src.db.models import CalcResult
from src.schemas.calc import CalcResponse, CalcRequest

from src.services.calculator import calculate_total_material_cost

router = APIRouter(prefix="/calc", tags=["calc"])


@router.post("", response_model=CalcResponse)
async def calculate_cost(request: CalcRequest, db: AsyncSession = Depends(get_db)):
    """
    Эндпоинт для расчета общей стоимости материалов.

    Принимает запрос с списком материалов, вычисляет общую стоимость,
    сохраняет результат в базу данных и возвращает общую стоимость.

    Args:
        request: Запрос с списком материалов
        db: Сессия базы данных

    Returns:
        CalcResponse: Ответ с общей стоимостью материалов
    """
    result: CalcResponse = await calculate_total_material_cost(request)

    db_result = CalcResult(total_cost_rub=result.total_cost_rub)
    db.add(db_result)
    await db.commit()

    return result
