import argparse

def get_args():
    parse = argparse.ArgumentParser(
        description="Picnic Game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parse.add_argument('item',
                       metavar='str',
                       nargs='+',  # 인수를 1개이상 전달함
                       help='Item(s) to bring')

    parse.add_argument('-s',
                       '--sorted',
                       action='store_true',
                       help='Sort the items')
    return parse.parse_args()  # 명령줄 인수를 처리해서 반환함

def main():
    args = get_args()
    items = args.item  # 리스트
    # print(args.item)
    num = len(items)  # 아이템의 개수

    # 정렬 기능 구현
    if args.sorted:
        items.sort()

    bringing = ''
    if num == 1:  # 명령행의 인수가 1개이면
        bringing = items[0]
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print('You are bringing {}.'.format(bringing))

if __name__=="__main__":
    main()