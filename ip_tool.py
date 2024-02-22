import sys
import os


class Actions():
    def __init__(self, boolean=True):
        self.toggle_all(boolean)

    def toggle_all(self, boolean):
        self.ip_class = boolean    # returns what class the IP is in
        self.boundary = boolean    # returns if internal or external IP
        self.binary = boolean      # returns binary conversion
        self.hex = boolean         # returns hex conversion
        self.octal = boolean       # returns octal conversion

    def valid_args(self):
        valid_attrs = []
        for attr in dir(self): # ignore dunder methods and callable method attributes
            if not attr.startswith("__") and not callable(getattr(self, attr)):
                valid_attrs.append(attr)
        return valid_attrs



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    guide()  # custom function prints from document
    actions = Actions()
    while True:
        try:
            entry = input('IPv4 address: ').lower().split()
        except (KeyboardInterrupt, EOFError):
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()

        os.system('cls' if os.name == 'nt' else 'clear')
        if len(entry) < 1:
            print('Too few command-line arguments\n')
            continue
        elif entry[0] in ['exit', 'ex', 'close', 'quit', 'end']:
            sys.exit()
        elif entry[0] == 'help':
            guide()
            continue

        ip_addr = ip_validate(entry)  # input validate and return IPv4
        if ip_addr:
            print(f'{" ".join(entry)}:\n')
            if actions.ip_class:
                print(f'{get_ip_class(ip_addr)} address')
            if actions.boundary:
                print(get_boundary(ip_addr))
            if actions.binary:
                print(f'Binary:  {get_binary(ip_addr)}')
            if actions.hex:
                print(f'Hex:     {get_hex(ip_addr)}')
            if actions.octal:
                print(f'Octal:   {get_octal(ip_addr)}')
            print()
        else:
            toggle_controls(actions, entry) # modify boolean values in Actions instance


# prints the guide on how to use this program. Invoked at launch and upon command.
def guide():
    try:
        with open('guide.txt', "r") as f:
            file_contents = f.read()
            print(file_contents)
            return True
    except FileNotFoundError:
        raise FileNotFoundError


def ip_validate(entry):
    if len(entry) == 1:
        try:
            ip_addr = [int(octet) for octet in entry[0].split('.', 3)]
            if not 0 <= int(ip_addr[0]) <= 255:
                print('invalid IPv4 address, try again...\n')
                return False
            elif not 0 <= int(ip_addr[1]) <= 255:
                print('invalid IPv4 address, try again...\n')
                return False
            elif not 0 <= int(ip_addr[2]) <= 255:
                print('invalid IPv4 address, try again...\n')
                return False
            elif not 0 <= int(ip_addr[3]) <= 255:
                print('invalid IPv4 address, try again...\n')
                return False
            else:
                return ip_addr
        except (ValueError, IndexError):
            print('invalid IPv4 address, try again...\n')
            return False


def toggle_controls(actions, entry):
    if len(entry) > 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        joined_entry = ' '.join(entry)
        if joined_entry == 'enable all':
            actions.toggle_all(True)
        elif joined_entry == 'disable all':
            actions.toggle_all(False)
        elif entry[0] == 'enable':
            return toggle_selection(actions, entry, True) # below function
        elif entry[0] == 'disable':
            return toggle_selection(actions, entry, False) # below function

# called from above functions elif statements
def toggle_selection(actions, entry, boolean):
    toggle_list = []
    invalid_args = []
    i = 1
    while i < len(entry):
        if entry[i] not in actions.valid_args():
            invalid_args.append(entry[i])
        else:
            toggle_list.append(entry[i])
        i += 1
    if invalid_args:
        print(f'Invalid arguments used: {invalid_args}\n'+
                'Enter "help" to see all valid commands\n')
        return invalid_args
    else:
        for arg in toggle_list:
            setattr(actions, arg, boolean)
        return toggle_list, boolean


def get_ip_class(octet):
    if octet[0] <= 127:
        return 'Class A'
    elif octet[0] <= 191:
        return 'Class B'
    elif octet[0] <= 223:
        return 'Class C'
    elif octet[0] <= 239:
        return 'Class D'
    elif octet[0] <= 255:
        return 'Class F'
    else:
        return 'Invalid class range'

def get_boundary(octet):
    if octet[0] == 10:
        return 'Internal network'
    elif octet[0] == 172 and octet[1] in [16,31]:
        return 'Internal network'
    elif octet[0] == 192 and octet[1] == 168:
        return 'Internal network'
    else:
        return 'External network'

def get_binary(octet):
    binary = (f'{octet[0]:08b} {octet[1]:08b} {octet[2]:08b} {octet[3]:08b}')
    return binary

def get_hex(octet):
    hex = (f'{octet[0]:x} {octet[1]:x} {octet[2]:x} {octet[3]:x}')
    return hex

def get_octal(octet):
    octal = (f'{octet[0]:04o} {octet[1]:04o} {octet[2]:04o} {octet[3]:04o}')
    return octal




if __name__ == "__main__":
    main()
