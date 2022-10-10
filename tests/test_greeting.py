from src.greeting import name


def test_name() -> None:
    assert name("Kuba") == "My name is: Kuba"
