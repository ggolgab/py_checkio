


def bigger_price(limit: int, data: list) -> list:

    d = data
    d1 = sorted(d.items(), key=operator.itemgetter(1))
    print(f'change         : {dict(d1)}\n')
  #  print("\n2-1) sorted(d.items(), key=lambda x: x[1])의 결과")
  #  print(d2)
  #  print("\n2-2) dict(sorted(d.items(), key=lambda x: x[1]))의 결과")
  #  print(dict(d2))

    return None


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
