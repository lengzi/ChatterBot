from .base_case import ChatBotTestCase


class StringInitalizationTestCase(ChatBotTestCase):

    def get_kwargs(self):
        return {
            'input_adapter': 'chatterbot.input.VariableInputTypeAdapter',
            'output_adapter': 'chatterbot.output.OutputFormatAdapter',
            'database': self.create_test_data_directory(),
            'silence_performance_warning': True
        }

    def test_storage_initialized(self):
        from chatterbot.storage import JsonFileStorageAdapter
        self.assertTrue(isinstance(self.chatbot.storage, JsonFileStorageAdapter))

    def test_logic_initialized(self):
        from chatterbot.logic import ClosestMatchAdapter
        self.assertEqual(len(self.chatbot.logic.adapters), 1)
        self.assertTrue(isinstance(self.chatbot.logic.adapters[0], ClosestMatchAdapter))

    def test_input_initialized(self):
        from chatterbot.input import VariableInputTypeAdapter
        self.assertTrue(isinstance(self.chatbot.input, VariableInputTypeAdapter))

    def test_output_initialized(self):
        from chatterbot.output import OutputFormatAdapter
        self.assertTrue(isinstance(self.chatbot.output, OutputFormatAdapter))


class DictionaryInitalizationTestCase(ChatBotTestCase):

    def get_kwargs(self):
        return {
            'storage_adapter': {
                'import_path': 'chatterbot.storage.JsonFileStorageAdapter',
                'database': self.create_test_data_directory(),
                'silence_performance_warning': True
            },

            'input_adapter': {
                'import_path': 'chatterbot.input.VariableInputTypeAdapter'
            },
            'output_adapter': {
                'import_path': 'chatterbot.output.OutputFormatAdapter'
            },
            'logic_adapters': [
                {
                    'import_path': 'chatterbot.logic.ClosestMatchAdapter',
                },
                {
                    'import_path': 'chatterbot.logic.MathematicalEvaluation',
                }
            ]
        }

    def test_storage_initialized(self):
        from chatterbot.storage import JsonFileStorageAdapter
        self.assertTrue(isinstance(self.chatbot.storage, JsonFileStorageAdapter))

    def test_logic_initialized(self):
        from chatterbot.logic import ClosestMatchAdapter
        from chatterbot.logic import MathematicalEvaluation
        self.assertEqual(len(self.chatbot.logic.adapters), 2)
        self.assertTrue(isinstance(self.chatbot.logic.adapters[0], ClosestMatchAdapter))
        self.assertTrue(isinstance(self.chatbot.logic.adapters[1], MathematicalEvaluation))

    def test_input_initialized(self):
        from chatterbot.input import VariableInputTypeAdapter
        self.assertTrue(isinstance(self.chatbot.input, VariableInputTypeAdapter))

    def test_output_initialized(self):
        from chatterbot.output import OutputFormatAdapter
        self.assertTrue(isinstance(self.chatbot.output, OutputFormatAdapter))
