import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from engine import Session, LESSON


class StudyEngineTests(unittest.TestCase):
    def test_happy_path(self):
        session = Session("synthetic-session")
        for step in LESSON["steps"]:
            result = session.submit(step["correct"])
            self.assertTrue(result["correct"])
        self.assertTrue(session.completed)
        self.assertEqual(session.score(), {"correct": 3, "total": 3, "certified": False})
        self.assertEqual(session.snapshot()["status"], "completed")

    def test_invalid_option_does_not_advance(self):
        session = Session("synthetic-session")
        for invalid in (-1, 3, True, "1"):
            with self.assertRaises(ValueError):
                session.submit(invalid)
        self.assertEqual(session.step_index, 0)

    def test_cannot_submit_after_completion(self):
        session = Session("synthetic-session")
        for step in LESSON["steps"]:
            session.submit(step["correct"])
        with self.assertRaises(ValueError):
            session.submit(0)

    def test_score_requires_completion(self):
        with self.assertRaises(ValueError):
            Session("synthetic-session").score()

    def test_empty_session_id(self):
        with self.assertRaises(ValueError):
            Session(" ").question()

    def test_wrong_answer_gives_feedback(self):
        session = Session("synthetic-session")
        result = session.submit(0)
        self.assertFalse(result["correct"])
        self.assertTrue(result["feedback"])
        self.assertEqual(len(session.snapshot()["answers"]), 1)


if __name__ == "__main__":
    unittest.main()
