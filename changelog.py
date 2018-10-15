#!/usr/bin/env python
import subprocess
import sys


def command_output(args, strip_chars=' \n\t'):
    output = subprocess.check_output(args)
    if sys.version_info[0] > 2:
        output = output.decode()
    return [
        line
        for line in (
            x.strip(strip_chars)
            for x in output.split('\n')
        )
        if line
    ]


AUTHOR = 'cmccandless'
REPO = 'easy_getch'
URL_BASE = "https://github.com/{}/{}/commit/".format(AUTHOR, REPO)
FMT = "- %s ([%h]({}%H))%n".format(URL_BASE)
TAG_PREV, TAG_CURRENT = command_output(['git', 'tag'])[-2:]


def changelog():
    lines = ['## Changelog']
    lines.extend(
        command_output(
            [
                'git',
                'log',
                '--pretty=format:"{}"'.format(FMT),
                '{}..{}'.format(TAG_PREV, TAG_CURRENT)
            ],
            strip_chars=' \n\t"'
        )[::-1]
    )
    lines.append('')
    return lines


if __name__ == '__main__':
    print('\n'.join(changelog()))
