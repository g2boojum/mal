from mal_types import Symbol
from printer import pr_str
import re
mal_tokens_re = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}('"`,;)]*)""")
re_float = re.compile("""(?x)
   ^
      [+-]?\ *      # first, match an optional sign *and space*
      (             # then match integers or f.p. mantissas:
          \d+       # start out with a ...
          (
              \.\d* # mantissa of the form a.b or a.
          )?        # ? takes care of integers of the form a
         |\.\d+     # mantissa of the form .b
      )
      ([eE][+-]?\d+)?  # finally, optionally match an exponent
   $""")
re_int = re.compile(r'-?[0-9]+$')
re_string = re.compile(r'"(?:[\\].|[^\\"])*"')

class Reader:
    def __init__(self, tokens, position=0):
        self.tokens = tokens
        self.position = position


    def next(self):
        self.position += 1
        return self.tokens[self.position-1]
    

    def peek(self):
        if len(self.tokens) > self.position:
            return self.tokens[self.position]
        else:
            return None

def tokenize(s):
    'Take a single string, s, and return a list of all tokens'
    tokens = mal_tokens_re.findall(s)
    if tokens[-1] == '':
        return tokens[:-1]
    return tokens

def read_atom(rdr):
    token = rdr.next()
    if 'nil' == token:
        return None
    elif 'true' == token:
        return True
    elif 'false' == token:
        return False
    elif re.match(re_string, token):
        return token[1:-1]
    elif re.match(re_int, token):
        return int(token)
    elif re.match(re_float, token):
        return float(token)
    else:
        return Symbol(token)


def read_list(rdr):
    lst = []
    rdr.next() # move past initial '('
    token = rdr.peek()
    while ')' != token:
        lst.append(read_form(rdr))
        token = rdr.peek()
    rdr.next() # move onto ')'
    return lst


def read_form(rdr):
    t = rdr.peek()
    if '(' == t:
         form = read_list(rdr)
    else:
         form = read_atom(rdr)
    return form


def read_str(s):
    tokens = tokenize(s)
    reader = Reader(tokens)
    return read_form(reader)


if __name__ == '__main__':
         s = '(+ 1 (- foo 2))'
         form = read_str(s)
         print(form)
         s = pr_str(form)
         print(s)



