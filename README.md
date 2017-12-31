# Py-MuParser
This MuParser Python binding is not intended to be a general purpose binding. It's just a quickly written binding for my EventScripts Emulator:
https://github.com/Ayuto/EventScripts-Emulator

## Example
```python
import muparser

from cvars import cvar

def parse_var(name):
    var = cvar.find_var(name)
    if var is None:
        return 0
        
    return var.get_float()

muparser.init_parser(parse_var)

# Prints 30.3 if mp_timelimit is 25
print(muparser.parse_expr('3 + mp_timelimit + 2.3'))
```