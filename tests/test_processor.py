import unittest
from src.processor import process_message

class TestProcessor(unittest.TestCase):

    def test_process_message_success(self):
        # Mock de uma mensagem de venda
        message = {
            "order_number": 123,
            "order_items": [
                {"item_id": 1, "qty": 2, "value_unit": 50.0},
                {"item_id": 2, "qty": 1, "value_unit": 100.0}
            ]
        }

        result = process_message(message)

        # Verifica se o resultado não é None
        self.assertIsNotNone(result)

        # Verifica se o order_number bate
        self.assertEqual(result[0], 123)

        # Verifica se o total está correto (2*50 + 1*100 = 200)
        self.assertEqual(result[1], 200.0)

        # Verifica se o processed_at é do tipo datetime
        from datetime import datetime
        self.assertIsInstance(result[2], datetime)

    def test_process_message_invalid(self):
        # Mensagem inválida (faltando campos)
        message = {
            "wrong_field": "no_order_number"
        }

        result = process_message(message)

        # Deveria retornar None em caso de erro
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()