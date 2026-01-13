from datetime import datetime
from sqlalchemy import Column, Integer, Numeric, DateTime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base(cls=AsyncAttrs)


class CalcResult(Base):
    """
    Модель для хранения результатов расчета в базе данных.

    Атрибуты:
        id: Уникальный идентификатор записи
        total_cost_rub: Общая стоимость материалов в рублях
        created_at: Дата и время создания записи
    """

    __tablename__ = "calc_results"

    id = Column(Integer, primary_key=True, index=True)
    total_cost_rub = Column(Numeric, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
