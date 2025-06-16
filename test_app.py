import unittest
from filters import moderate_response
from emotion_detector import detect_emotion

class TestChatbot(unittest.TestCase):

    def test_filter_advice(self):
        risky = "You should talk to a doctor."
        safe = moderate_response(risky)
        self.assertNotIn("you should", safe.lower())

    def test_emotion_detection(self):
        emotion = detect_emotion("I’m really sad and tired today.")
        self.assertIn(emotion.lower(), ["sadness", "anger", "joy", "surprise", "love", "fear"])

if __name__ == '__main__':
    unittest.main()