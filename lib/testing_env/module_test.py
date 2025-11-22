from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_python_version():
    version_info = python_version()
    # Require at least Python 3.8
    assert (version_info.major, version_info.minor) >= (3, 8)


def test_requests_version():
    # Allow requests newer than or equal to 2.27.1
    def _ver_tuple(v, parts=3):
        vals = []
        for p in v.split('.'):
            try:
                vals.append(int(p))
            except ValueError:
                # handle cases like '1rc1' by taking leading digits
                import re
                m = re.match(r"(\d+)", p)
                vals.append(int(m.group(1)) if m else 0)
        while len(vals) < parts:
            vals.append(0)
        return tuple(vals[:parts])

    assert _ver_tuple(requests_version()) >= _ver_tuple("2.27.1")


def test_pytest_version():
    # Allow pytest newer than or equal to 7.1.3
    def _ver_tuple(v, parts=3):
        vals = []
        for p in v.split('.'):
            try:
                vals.append(int(p))
            except ValueError:
                import re
                m = re.match(r"(\d+)", p)
                vals.append(int(m.group(1)) if m else 0)
        while len(vals) < parts:
            vals.append(0)
        return tuple(vals[:parts])

    assert _ver_tuple(pytest_version()) >= _ver_tuple("7.1.3")
