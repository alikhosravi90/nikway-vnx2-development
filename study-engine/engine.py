"""Deterministic educational prototype; not an API or assessment certification."""
from dataclasses import dataclass, field
from typing import List, Dict

LESSON = {
    "id": "five-whys-packaging-001",
    "version": "0.1.0",
    "title": "5 Whys: evidence before conclusions",
    "steps": [
        {"id": "define", "question": "A packaging line stops repeatedly. What comes first?",
         "options": ["Replace the machine", "Define the problem with evidence", "Blame the operator"],
         "correct": 1, "feedback": "Define an observable, measurable problem before asking why."},
        {"id": "why", "question": "Logs show film jams. What is the next step?",
         "options": ["Investigate why film jams", "Assume operator error", "Stop analysis"],
         "correct": 0, "feedback": "Follow causal hypotheses with evidence; exactly five questions are not mandatory."},
        {"id": "verify", "question": "The team suspects incorrect film tension. What next?",
         "options": ["Accept without testing", "Ask why without checking", "Check settings and stoppage records"],
         "correct": 2, "feedback": "Test the hypothesis using observations and relevant records."},
    ],
}

@dataclass
class Session:
    session_id: str
    step_index: int = 0
    answers: List[Dict] = field(default_factory=list)

    def __post_init__(self):
        if not self.session_id or not self.session_id.strip():
            raise ValueError("session_id required")

    def question(self):
        if self.completed:
            return None
        step = LESSON["steps"][self.step_index]
        return {"step_id": step["id"], "question": step["question"], "options": list(step["options"])}

    @property
    def completed(self):
        return self.step_index == len(LESSON["steps"])

    def submit(self, selected_index):
        if self.completed:
            raise ValueError("session already completed")
        step = LESSON["steps"][self.step_index]
        if type(selected_index) is not int or not 0 <= selected_index < len(step["options"]):
            raise ValueError("invalid option")
        correct = selected_index == step["correct"]
        self.answers.append({"step_id": step["id"], "selected_index": selected_index, "correct": correct})
        self.step_index += 1
        return {"correct": correct, "feedback": step["feedback"], "completed": self.completed}

    def snapshot(self):
        return {"schema_version": "0.1.0", "session_id": self.session_id,
                "lesson_id": LESSON["id"], "lesson_version": LESSON["version"],
                "step_index": self.step_index,
                "status": "completed" if self.completed else "in_progress",
                "answers": list(self.answers)}

    def score(self):
        if not self.completed:
            raise ValueError("score only available after completion")
        return {"correct": sum(a["correct"] for a in self.answers),
                "total": len(LESSON["steps"]),
                "certified": False}
