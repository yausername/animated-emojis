"""
Download all animated emojis from Google Noto Emoji
"""

import requests


def get_emoji_list():
    emojis = []
    r = requests.get('https://googlefonts.github.io/noto-emoji-animation/data/api.json')
    for icon in r.json()['icons']:
        name = icon['tags'][0][1:-1]
        emojis.append((icon['codepoint'], name))
    return emojis


def download_emoji(code, name):
    r = requests.get(f'https://fonts.gstatic.com/s/e/notoemoji/latest/{code}/512.gif')
    r.raise_for_status()

    with open(f'{name}.gif', 'wb') as f:
        f.write(r.content)


def main():
    emojis = get_emoji_list()

    for code, name in emojis:
        print(f'downloading {name} ({code})')

        try:
            download_emoji(code, name)
        except requests.RequestException:
            print(f'could not get emoji {name}')
            pass


if __name__ == '__main__':
    raise SystemExit(main())

