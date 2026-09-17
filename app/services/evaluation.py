from uuid import UUID, uuid4
from app.models.evaluation import EvaluationRequest
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Evaluation
from app.repositories.evaluation import EvaluationRepository


class EvaluationService:
    def __init__(self):
        pass

    async def create_evaluation(
        self,
        db: AsyncSession,
        req: EvaluationRequest,
    ) -> Evaluation:
        evaluation = Evaluation(
            id=uuid4(),
            prompt=req.prompt,
            model=req.model,
            status="queued",
        )
        repository = EvaluationRepository(db)

        await repository.create(evaluation)

        await db.commit()
        return evaluation

    async def get_evaluation_by_id(self, db: AsyncSession, id: UUID) -> Evaluation:
        repo = EvaluationRepository(db)
        return await repo.get_by_id(id)
