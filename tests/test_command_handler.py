# tests/test_command_handler.py
from calc_app.commands.command_handler import CommandHandler
from unittest.mock import MagicMock, patch
import io
import pytest

@pytest.fixture
def command_handler():
    return CommandHandler()

def test_register_command(command_handler):
    command_mock = MagicMock()
    command_handler.register_command('test', command_mock)
    assert command_handler.commands['test'] == command_mock

def test_execute_command_existing(command_handler):
    command_mock = MagicMock()
    command_handler.commands['test'] = command_mock
    with io.StringIO() as mock_stdout:
        with patch('sys.stdout', mock_stdout):
            command_handler.execute_command('test')
            assert mock_stdout.getvalue().strip() == ''
    command_mock.execute.assert_called_once()

def test_execute_command_nonexistent(command_handler):
    with io.StringIO() as mock_stdout:
        with patch('sys.stdout', mock_stdout):
            command_handler.execute_command('nonexistent')
            assert mock_stdout.getvalue().strip() == "Command 'nonexistent' not recognized"
