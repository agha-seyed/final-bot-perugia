import pytest
from ai.question_answering import get_answer

@pytest.mark.asyncio
async def test_get_answer_exact_match():
    """Test exact match in Q&A data."""
    question = "What is the cost of living in Perugia?"
    answer = await get_answer(question)
    assert answer == "The average cost of living in Perugia is around €800-€1000 per month."

@pytest.mark.asyncio
async def test_get_answer_semantic_match():
    """Test semantic match in Q&A data."""
    question = "Where can I find food in Perugia?"
    answer = await get_answer(question)
    assert "places to eat" in answer.lower()