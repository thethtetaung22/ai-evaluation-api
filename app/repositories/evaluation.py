from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Evaluation


class EvaluationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(
        self,
        evaluation: Evaluation,
    ) -> Evaluation:
        self.session.add(evaluation)

        await self.session.flush()

        return evaluation

    async def get_by_id(
        self,
        evaluation_id: UUID,
    ) -> Evaluation | None:

        result = await self.session.execute(
            select(Evaluation).where(Evaluation.id == evaluation_id)
        )

        return result.scalar_one_or_none()
