from commands.help import help
from commands.version import version
from commands.authors import authors

import argparse
import sys


class MusicArgumentParser(argparse.ArgumentParser):
    def error(self, _):
        help()
        sys.exit(0)


def parse_args():
    parser = MusicArgumentParser(add_help=False)

    parser.add_argument('-v', '--version', action='store_true')
    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('-a', '--authors', action='store_true')

    parser.add_argument('--yandex-oauth', type=str)
    parser.add_argument('--spotify-oauth', type=str)

    subparsers = parser.add_subparsers(dest='command')
    download_parser = subparsers.add_parser('download')

    download_parser.add_argument('link')
    return parser.parse_args()


def main():
    args = parse_args()

    if args.help or len(sys.argv) == 1:
        help()

    elif args.version:
        version()

    elif args.authors:
        authors()

    elif args.command == 'download':
        if 'music.yandex' in args.link:
            if not args.yandex_oauth:
                print('need a yandex-oauth token')
                sys.exit(1)
            
            print('download from yandex...')
        
        elif 'spotify.com' in args.link:
            if not args.spotify_oauth:
                print('need a spotify-oauth token')
                sys.exit(1)

            print('download from spotify...')

    else:
        help()

if __name__ == '__main__':
    main()