from pydantic import BaseModel, Field


class Material(BaseModel):
    """
    Класс для представления материала.

    Атрибуты:
        name: Название материала (от 1 до 50 символов)
        qty: Количество материала (больше 0)
        price_rub: Цена материала в рублях (больше 0)
    """

    name: str = Field(..., min_length=1, max_length=50)
    qty: float = Field(..., gt=0)
    price_rub: float = Field(..., gt=0)


class CalcRequest(BaseModel):
    """
    Класс для представления запроса на расчет стоимости.

    Атрибуты:
        materials: Список материалов для расчета
    """

    materials: list[Material]


class CalcResponse(BaseModel):
    """
    Класс для представления ответа на запрос расчета стоимости.

    Атрибуты:
        total_cost_rub: Общая стоимость материалов в рублях
    """

    total_cost_rub: float
