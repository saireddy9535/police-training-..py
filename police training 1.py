class TrainingSession:
    def __init__(self, training_id, name, participants):
        self.training_id = training_id
        self.name = name
        self.participants = participants
        self.is_completed = False
        self.outcomes = {}

    def mark_completed(self, outcomes):
        self.is_completed = True
        self.outcomes = outcomes

    def __str__(self):
        return f"TrainingSession({self.training_id}, {self.name}, {'Completed' if self.is_completed else 'Pending'})"

    def __eq__(self, other):
        return (
            self.training_id == other.training_id and
            self.name == other.name and
            self.participants == other.participants and
            self.is_completed == other.is_completed and
            self.outcomes == other.outcomes
        )


class TrainingScheduler:
    def __init__(self):
        self.sessions = {}

    def create_session(self, training_id, name, participants):
        session = TrainingSession(training_id, name, participants)
        self.sessions[training_id] = session
        return session

    def read_session(self, training_id):
        return self.sessions.get(training_id)

    def update_session(self, training_id, name=None, participants=None):
        session = self.sessions.get(training_id)
        if session:
            if name:
                session.name = name
            if participants:
                session.participants = participants
        return session

    def delete_session(self, training_id):
        if training_id in self.sessions:
            del self.sessions[training_id]
            return True
        return False

    def schedule_training(self, training_id):
        return self.sessions.get(training_id)

    def track_training_completion(self, training_id, outcomes):
        session = self.sessions.get(training_id)
        if session:
            session.mark_completed(outcomes)
        return session
import unittest

class TestTrainingScheduler(unittest.TestCase):

    def setUp(self):
        self.scheduler = TrainingScheduler()
        self.scheduler.create_session('001', 'Hand-to-hand Combat', ['John Doe', 'Jane Smith'])

    def test_create_and_read_session(self):
        session = self.scheduler.create_session('002', 'Firearms Training', ['Alice Jones'])
        read_session = self.scheduler.read_session('002')
        self.assertEqual(session, read_session)

    def test_update_session(self):
        updated = self.scheduler.update_session('001', name='Advanced Hand-to-hand Combat')
        self.assertEqual(updated.name, 'Advanced Hand-to-hand Combat')

    def test_delete_session(self):
        self.assertTrue(self.scheduler.delete_session('001'))
        self.assertIsNone(self.scheduler.read_session('001'))

    def test_schedule_training(self):
        session = self.scheduler.schedule_training('001')
        self.assertIsNotNone(session)

    def test_track_completion(self):
        outcomes = {'John Doe': 'Passed', 'Jane Smith': 'Passed'}
        session = self.scheduler.track_training_completion('001', outcomes)
        self.assertTrue(session.is_completed)
        self.assertEqual(session.outcomes, outcomes)

if __name__ == '__main__':
    unittest.main()
