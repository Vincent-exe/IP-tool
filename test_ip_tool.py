from project import Actions, guide, ip_validate, toggle_controls, get_ip_class, get_boundary, get_binary, get_hex, get_octal
import sys

def main():
    test_guide()
    test_ip_validate()
    test_toggle_controls()
    test_get_ip_class()
    test_get_boundary()
    test_get_binary()
    test_get_hex()
    test_get_octal()


def test_guide(): # True if not FileNotFoundError raised. Does not take input therefore no error test.
    assert guide() == True


def test_ip_validate():
    assert ip_validate(['192.168.56.100']) == ([192, 168, 56, 100])
    assert ip_validate(['20.112.250.113']) == ([20, 112, 250, 113])
    assert ip_validate(['1000.1.1.1']) == False
    assert ip_validate(['500.1 1 1']) == False
    assert ip_validate(["1.2.3.4.5"]) == False
    assert ip_validate(['1.2.3']) == False
    assert ip_validate(['word']) == False

    # Do nothing if list > 1
    assert ip_validate(['multiple', 'list']) == None


def test_toggle_controls(): # toggle_selection() is invoked and tested via toggle_selection()
    actions = Actions(False)

    toggle_controls(actions, ['enable', 'all'])
    for action in (actions.ip_class, actions.boundary, actions.binary, actions.hex, actions.octal):
        assert action
    toggle_controls(actions, ['disable', 'all'])
    for action in (actions.ip_class, actions.boundary, actions.binary, actions.hex, actions.octal):
        assert not action

    toggle_controls(actions, ['enable', 'binary', 'ip_class'])
    assert actions.binary == True
    assert actions.ip_class == True

    toggle_controls(actions, ['enable', 'hex'])
    assert actions.hex == True

    toggle_controls(actions, ['disable', 'binary', 'ip_class'])
    assert actions.binary == False
    assert actions.ip_class == False

    toggle_controls(actions, ['disable', 'hex'])
    assert actions.hex == False

    assert toggle_controls(actions, ['enable', 'invalid', 'arg']) == ['invalid', 'arg']
    assert toggle_controls(actions, ['disable', 'invalid']) == ['invalid']

    # Do nothing if list < 2
    assert toggle_controls(actions, ['single']) == None


def test_get_ip_class():
    assert get_ip_class([0, 0, 0, 0]) == 'Class A'
    assert get_ip_class([127, 255, 255, 255]) == 'Class A'

    assert get_ip_class([128, 0, 0, 0]) == 'Class B'
    assert get_ip_class([191, 255, 255, 255]) == 'Class B'

    assert get_ip_class([192, 0, 0, 0]) == 'Class C'
    assert get_ip_class([223, 255, 255, 255]) == 'Class C'

    assert get_ip_class([224, 0, 0, 0]) == 'Class D'
    assert get_ip_class([239, 255, 255, 255]) == 'Class D'

    assert get_ip_class([240, 0, 0, 0]) == 'Class F'
    assert get_ip_class([255, 255, 255, 255]) == 'Class F'

    # Function should never receive a call in this instance
    assert get_ip_class([500, 0, 0, 0]) == 'Invalid class range'


def test_get_boundary():
    # External boundary 1
    assert get_boundary([9, 0, 0, 0]) == 'External network'

    # Internal boundary 1
    assert get_boundary([10, 0, 0, 0]) == 'Internal network'
    assert get_boundary([10, 255, 255, 255]) == 'Internal network'

    # External boundary 2
    assert get_boundary([11, 0, 0, 0]) == 'External network'
    assert get_boundary([171, 16, 0, 0]) == 'External network'
    assert get_boundary([172, 15, 0, 0]) == 'External network'
    assert get_boundary([172, 32, 0, 0]) == 'External network'

    # Internal boundary 2
    assert get_boundary([172, 16, 0, 0]) == 'Internal network'
    assert get_boundary([172, 31, 0, 0]) == 'Internal network'

    # External boundary 3
    assert get_boundary([172, 32, 0, 0]) == 'External network'
    assert get_boundary([173, 31, 0, 0]) == 'External network'
    assert get_boundary([191, 168, 0, 0]) == 'External network'
    assert get_boundary([192, 167, 0, 0]) == 'External network'

    # Internal boundary 3
    assert get_boundary([192, 168, 0, 0]) == 'Internal network'

    # External boundary 4
    assert get_boundary([192, 169, 0, 0]) == 'External network'
    assert get_boundary([193, 0, 0, 0]) == 'External network'


def test_get_binary():
    assert get_binary([192, 168, 56, 100]) == '11000000 10101000 00111000 01100100'
    assert get_binary([10, 239, 74, 111]) == '00001010 11101111 01001010 01101111'


def test_get_hex():
    assert get_hex([192, 168, 56, 100]) == 'c0 a8 38 64'
    assert get_hex([10, 239, 74, 111]) == 'a ef 4a 6f'


def test_get_octal():
    assert get_octal([192, 168, 56, 100]) == '0300 0250 0070 0144'
    assert get_octal([10, 239, 74, 111]) == '0012 0357 0112 0157'



if __name__ == "__main__":
    main()