"""Run from repository root: python study-engine/demo.py"""
from engine import Session, LESSON

session = Session("synthetic-demo")
for step in LESSON["steps"]:
    print("\n" + step["question"])
    for index, option in enumerate(step["options"]):
        print(f"  {index}: {option}")
    # Deterministic synthetic demonstration; not learner input.
    print(session.submit(step["correct"])["feedback"])
print("\nSynthetic result:", session.score())
