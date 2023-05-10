import argparse

def get_args():
    parse = argparse.ArgumentParser(description='Say hello')

    # 명령행 인수 : -n(축약형), --name
    parse.add_argument('-n',
                       '--name',
                       metavar='name',
                       default='World',
                       help='Name to greet')
    return parse.parse_args()

def main():
    args = get_args()
    print('Hello,' + args.name + '!')


if __name__=="__main__":
    main()