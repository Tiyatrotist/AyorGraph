"""Deterministic two-agent graph example with no external services or credentials."""

from ayorgraph.core import Graph, State


def research_agent(state: State) -> State:
    """Collect deterministic facts for the next agent."""
    topic = state.values["topic"]
    facts = [
        f"{topic} workflows can be represented as explicit nodes.",
        "Deterministic nodes are straightforward to test.",
    ]
    return State({**state.values, "facts": facts})


def writing_agent(state: State) -> State:
    """Turn the first agent's facts into a short handoff summary."""
    facts = state.values["facts"]
    summary = " ".join(facts)
    return State({**state.values, "summary": summary})


def build_graph() -> Graph:
    return Graph().node("researcher", research_agent).node("writer", writing_agent)


def run_example(topic: str = "Agent") -> State:
    return build_graph().run(State({"topic": topic}), ["researcher", "writer"])


def main() -> None:
    result = run_example()
    print(result.values["summary"])


if __name__ == "__main__":
    main()
