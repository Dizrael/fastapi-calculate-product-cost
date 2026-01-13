from src.schemas.calc import CalcRequest, CalcResponse


async def calculate_total_material_cost(request: CalcRequest) -> CalcResponse:
    """
    Метод для расчета стоимости всех материалов в запросе.

    Args:
        request: Запрос на расчет стоимости, содержащий список материалов.

    Returns:
        CalcResponse: Ответ с общей стоимостью материалов в рублях.
    """
    if len(request.materials) == 0:
        return CalcResponse(total_cost_rub=0)
    total = sum(material.qty * material.price_rub for material in request.materials)
    return CalcResponse(total_cost_rub=round(total, 2))
