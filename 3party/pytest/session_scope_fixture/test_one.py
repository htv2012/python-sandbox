def test_port1(get_port):
    port = get_port()
    assert port > 10000


def test_port2(get_port):
    port = get_port()
    assert port > 10000


def test_range1(get_ports_range):
    ports_range = get_ports_range()
    assert isinstance(ports_range, str)
