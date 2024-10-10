#test init
import unittest
from unittest.mock import patch, MagicMock
from fundamental_analysis import FundamentalAnalyzer
from internet_openai_chat import Chatbot

# Test cases for FundamentalAnalyzer and Chatbot classes
class TestFundamentalAnalyzer(unittest.TestCase):

# Set up method to initialize the analyzer with verbose mode on
    def setUp(self):
        self.analyzer = FundamentalAnalyzer(verbose=True)

# Test method to check if the initial scores are all zero
    def test_initial_scores(self):
        #  Test that the initial scores are all zero
        for score in self.analyzer.df.columns[1:]:
            self.assertEqual(self.analyzer.df[score].sum(), 0)

    def test_final_score_calculation(self):
#get_final_score
        self.analyzer.df.loc[self.analyzer.df['categories'] == "Team", "Yes"] += 1
        self.analyzer.df.loc[self.analyzer.df['categories'] == "Developers_Activity", "Excellent"] += 1
        final_score = self.analyzer.get_final_score()
        self.assertGreaterEqual(final_score, 0)
        self.assertLessEqual(final_score, 100)

# Test cases for Chatbot class
    def test_rescale_to_0_100(self):
        # تست تابع rescale_to_0_100
        scores = [10, 20, 30, 40, 50]
        rescaled = self.analyzer.rescale_to_0_100(scores)
        self.assertEqual(len(rescaled), len(scores))

class TestChatbot(unittest.TestCase):

#Test method to check if the chatbot is initialized correctly
    @patch('internet_openai_chat.OpenAI')
    @patch('internet_openai_chat.TavilyClient')
    def setUp(self, mock_tavily_client, mock_openai_client):
        self.chatbot = Chatbot()
        self.chatbot.client = MagicMock()
        self.chatbot.tavily_client = MagicMock()

    def test_create_thread(self):
        thread = self.chatbot.create_thread()
        self.assertIsNotNone(thread)

    @patch('internet_openai_chat.Chatbot.chat', return_value="This is a test response.")
    def test_chat_functionality(self, mock_chat):
        response = self.chatbot.chat("Test message", None)
        self.assertEqual(response, "This is a test response.")

if __name__ == '__main__':
    unittest.main()
