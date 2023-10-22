import prettytable, random, sys, hashlib, hmac, secrets

moves = (sys.argv[1:len(sys.argv)])
p2 = int(random.randrange(len(moves)))

def calc_digest(key, message):
    key = bytes(key, 'utf-8')
    message = bytes(message, 'utf-8')
    dig = hmac.new(key, message, hashlib.sha256)
    return dig.hexdigest()

p2move = str(p2)
secret = str(secrets.randbits(256))

print("HMAC:", calc_digest(secret, p2move))


def calc(moves, p1, p2):
    if p1 == p2:
        return "DRAW"
    result = ("WIN" if (p2 > p1 and p2 - p1 <= len(moves) / 2) or (p2 < p1 and p1 - p2 > len(moves) / 2) else "LOSE")

    return result


def menu(args):
    while True:
        try:
            moves = args[0:]
            if len(moves) < 3 or len(moves) % 2 == 0:
                print("Invalid options: please pass odd number of moves (3 or more odd arguments)")
                break

            print("Available moves: ")
            for i, v in enumerate(moves):
                print(f"{i + 1} - {v}")
            print("0 - exit")
            print("? - help")

            p1 = input("Enter your move: ")
            if p1 == chr(63):
                return print_pretty_table(moves)
            if p1 == str(0):
                break
            print("Your move:", moves[int(p1) - 1])


            print("PC move:", moves[p2 - 1])

            if p1 == p2:
                return print("DRAW")
            result = (
                "WIN" if (p2 > int(p1) and p2 - int(p1) <= len(moves) / 2) or (
                            p2 < int(p1) and int(p1) - p2 > len(moves) / 2) else "LOSE")
            return print(result)

        except ValueError:
            return menu(args)



def print_pretty_table(moves):
    x = prettytable.PrettyTable()
    data = get_table(moves)
    x.field_names = data[0]
    for i in data[1:]:
        x.add_row(i)
    print(x)


def get_table(moves):
    result = [["v PC | User >"] + moves]
    for i in moves:
        line = [i]
        y = moves.index(i) + 1
        for j in moves:
            x = moves.index(j) + 1
            line.append(calc(moves, x, y))

        result.append(line)
    return result


if __name__ == "__main__":
    moves = (sys.argv[1:len(sys.argv)])
    menu(moves)