from fastapi import APIRouter

from .logger import logger

router = APIRouter()


@router.get("/sum")
async def calculate_sum(a: float, b: float) -> dict:
    """Calculate the sum of two numbers."""
    result = a + b
    logger.info(f"Calculated sum of {a} and {b}: {result}")
    return {"sum": result}
