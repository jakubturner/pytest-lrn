from src.greeting import my_name


def test_name() -> None:
    assert my_name("Kuba") == "My name is: Kuba"
