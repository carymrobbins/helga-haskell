from functools import wraps
from tryhaskell import TryHaskell
from helga.plugins import match


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
        return 'ERROR: ' + result.value
    if result.value:
        return result.value
    return show_type(result)


@match(r'^(\:t |>\s*\:t |>).*$')
@clean_output
def haskell(client, channel, nick, message, matches):
    # Simplify checking matches.
    print matches
    matches = ''.join(matches)
    print matches
    if ':t' in matches:
        _, exp = message.split(':t', 1)
        r = TryHaskell.get(exp)
        return show_type(r) if r.ok else show_value(r)
    elif '>' in matches:
        return show_value(TryHaskell.get(message[1:]))
