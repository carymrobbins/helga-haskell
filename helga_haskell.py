from functools import wraps
from tryhaskell import TryHaskell
from helga.plugins import command


def clean_output(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except TryHaskell.Error as e:
            result = 'Uh oh: ' + e.message
        # Truncate output and replace newlines to send only one message.
        return result.replace('\n', ' ')[:300] if result else result
    return wrapper


def show_type(result):
    return ' :: '.join([result.expr.strip(), result.type])


def show_value(result, display_errors):
    if not result.ok:
        if not display_errors:
            return None
        # Reduce multiple white spaces with a single space.
        msg = ' '.join(result.value.split())
        return 'ERROR: ' + msg
    if result.stdout:
        return ' '.join(result.stdout)
    if result.value:
        return result.value
    return show_type(result)


@command('haskell', aliases=['h'],
         help='Run haskell expressions. Usage: helga h(askell) (:t) <expression>')
@clean_output
def haskell(client, channel, nick, message, cmd, args):
    # Only show errors when using the explicit !haskell command.
    display_errors = cmd == 'haskell'
    if ':t' in args[:1]:
        _, exp = message.split(':t', 1)
        r = TryHaskell.get(exp)
        return show_type(r) if r.ok else show_value(r, display_errors)
    return show_value(TryHaskell.get(' '.join(args)), display_errors)
