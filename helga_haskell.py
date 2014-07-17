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


def show_value(result):
    if not result.ok:
        # Reduce multiple white spaces with a single space.
        msg = ' '.join(result.value.split())
        return 'ERROR: ' + msg
    if result.stdout:
        return ' '.join(result.stdout)
    if result.value:
        return result.value
    return show_type(result)


@command('haskell', aliases=['h'],
         help='Run haskell expressions. Usage: helga h(askell) (:t|> :t|>) <expression>')
@clean_output
def haskell(client, channel, nick, message, cmd, args):
    # Simplify checking matches.
    argstr = ' '.join(args)

    if ':t' in argstr:
        _, exp = message.split(':t', 1)
        r = TryHaskell.get(exp)
        return show_type(r) if r.ok else show_value(r)
    elif '>' in argstr:
        return show_value(TryHaskell.get(argstr[1:]))
