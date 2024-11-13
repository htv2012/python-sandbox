from numericlib import NumericRange


def test_get_ports_single_port(get_ports):
    port = get_ports()
    assert isinstance(port, int)


def test_unique_single_port(get_ports):
    ports = {get_ports() for _ in range(10)}
    assert len(ports) == 10


def test_get_ports_multiple_ports(get_ports):
    ports = get_ports(3)
    assert isinstance(ports, NumericRange)

    ports_list = list(ports)
    assert len(ports_list) == 3

    first, second, third = ports_list
    assert first + 1 == second
    assert second + 1 == third


def test_unique_multiple_ports(get_ports):
    ports = {tuple(get_ports(3)) for _ in range(10)}
    assert len(ports) == 10
