from uuid import UUID

from fastapi import APIRouter, HTTPException, Depends

from app.models.evaluation import EvaluationRequest, EvaluationResponse

from app.services.evaluation import EvaluationService

from app.db.database import get_db
from sqlalchemy.exc import SQLAlchemyError

service = EvaluationService()

router = APIRouter(prefix="/evaluations", tags=["Evaluations"])

db = Depends(get_db)


@router.get("/{evaluation_id}")
async def get_evaluation(evaluation_id: UUID, db=db) -> EvaluationResponse:
    try:
        evaluation = await service.get_evaluation_by_id(db=db, id=evaluation_id)
    except SQLAlchemyError:
        await db.rollback()

        raise HTTPException(
            status_code=503,
            detail="Database temporarily unavailable",
        )

    if evaluation is None:
        raise HTTPException(
            status_code=404,
            detail="Evaluation not found",
        )

    return {
        "id": str(evaluation.id),
        "prompt": evaluation.prompt,
        "model": evaluation.model,
        "status": evaluation.status,
        "created_at": evaluation.created_at,
    }


@router.post("/", response_model=EvaluationResponse, status_code=202)
async def create_evaluation(request: EvaluationRequest, db=db) -> EvaluationResponse:
    try:
        evaluation = await service.create_evaluation(db=db, req=request)

        return EvaluationResponse(
            id=str(evaluation.id),
            prompt=evaluation.prompt,
            model=evaluation.model,
            status=evaluation.status,
            created_at=evaluation.created_at,
        )
    except SQLAlchemyError:
        await db.rollback()

        raise HTTPException(
            status_code=503,
            detail="Database temporarily unavailable",
        )
