"""
The Smallest Agent SDK
======================

The whole framework, distilled to the minimum that still holds:

  - **Identity**      every actor is attributable.
  - **Instruction**   defined, with a *verifiable outcome* — not a prompt.
  - **One step**      now -> next; propose -> verify -> commit.
  - **The third**     a verifier checks the outcome; it cannot verify its own work.
  - **Resolve**       the loop runs until it resolves, or it fails closed.

Two can act; only three can be trusted.

Run:  python3 sdk/smallest_agent_sdk.py
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class Identity:
    """Who acts. Every agent and verifier has one — actions are attributable."""
    name: str


@dataclass(frozen=True)
class Instruction:
    """A defined command, not a prompt.

    `run`     : input -> output (what it does)
    `outcome` : (input, output) -> bool (the *defined, checkable* result)
    """
    name: str
    run: Callable[[Any], Any]
    outcome: Callable[[Any, Any], bool]


@dataclass(frozen=True)
class Result:
    instruction: str
    actor: str
    output: Any
    verified_by: str
    ok: bool


class Agent:
    """Can act. Cannot certify itself."""
    def __init__(self, identity: Identity):
        self.identity = identity

    def propose(self, instr: Instruction, inp: Any) -> Any:
        return instr.run(inp)            # produces an output — not yet trusted


class Verifier:
    """The third. Verifies an outcome — and never its own action (no self-approval)."""
    def __init__(self, identity: Identity):
        self.identity = identity

    def verify(self, instr: Instruction, inp: Any, output: Any, actor: Identity) -> bool:
        if actor.name == self.identity.name:
            raise PermissionError("no self-approval: a verifier cannot verify its own work")
        return bool(instr.outcome(inp, output))


def step(agent: Agent, verifier: Verifier, instr: Instruction, inp: Any) -> Result:
    """One step: propose -> verify (by a third) -> commit. Never further."""
    output = agent.propose(instr, inp)                              # two can act...
    ok = verifier.verify(instr, inp, output, agent.identity)        # ...only three can be trusted
    return Result(instr.name, agent.identity.name, output, verifier.identity.name, ok)


def loop(agent: Agent, verifier: Verifier, program: list[Instruction], inp: Any):
    """Run instructions one verified step at a time. Must resolve, or fail closed."""
    state = inp
    trail: list[Result] = []
    for instr in program:
        r = step(agent, verifier, instr, state)
        trail.append(r)
        if not r.ok:
            return False, state, trail        # unresolved step halts the loop (fail closed)
        state = r.output                       # the verified output becomes the next input
    return True, state, trail


# --------------------------------------------------------------------------- demo
if __name__ == "__main__":
    # Two parties, with identity — never the same one verifying itself.
    worker = Agent(Identity("agent.worker"))
    third = Verifier(Identity("agent.verifier"))

    # Defined instructions: each carries its own checkable outcome.
    double = Instruction("double", run=lambda x: x * 2,
                         outcome=lambda i, o: o == i * 2)
    inc = Instruction("increment", run=lambda x: x + 1,
                      outcome=lambda i, o: o == i + 1)

    ok, value, trail = loop(worker, third, [double, inc, double], 5)
    for r in trail:
        print(f"  {r.instruction:10s} by {r.actor} -> {r.output}  "
              f"verified_by {r.verified_by}  ok={r.ok}")
    print(f"resolved={ok}  result={value}")

    # The third cannot certify itself — no self-approval.
    try:
        third.verify(double, 5, 10, actor=third.identity)
        print("ERROR: self-approval was allowed")
    except PermissionError as e:
        print(f"self-approval correctly rejected: {e}")

    # A wrong output fails closed (the loop does not resolve).
    liar = Instruction("liar", run=lambda x: 999, outcome=lambda i, o: o == i + 1)
    ok2, _, _ = loop(worker, third, [liar], 1)
    print(f"unverifiable step resolved={ok2}  (expected False — fails closed)")
