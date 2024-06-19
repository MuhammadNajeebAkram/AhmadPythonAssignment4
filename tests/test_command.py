# tests/test_command.py
from calc_app.commands.command import Command
import pytest

def test_execute_raises_not_implemented_error():
    command = Command()
    with pytest.raises(NotImplementedError) as exc_info:
        command.execute()
    
    assert str(exc_info.value) == "Subclasses should implement this!"
