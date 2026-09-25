import runpy
from pathlib import Path

from ayorgraph.core import State

EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "multi_agent.py"


def test_multi_agent_example_is_deterministic_and_hands_state_between_agents():
    module = runpy.run_path(str(EXAMPLE))

    result = module["run_example"]("Graph")

    assert isinstance(result, State)
    assert result.values == {
        "topic": "Graph",
        "facts": [
            "Graph workflows can be represented as explicit nodes.",
            "Deterministic nodes are straightforward to test.",
        ],
        "summary": (
            "Graph workflows can be represented as explicit nodes. "
            "Deterministic nodes are straightforward to test."
        ),
    }
