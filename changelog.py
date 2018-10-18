#!/usr/bin/env python
import subprocess
import sys

AUTHOR = 'cmccandless'
REPO = 'easy_getch'
URL_BASE = "https://github.com/{}/{}/commit/".format(AUTHOR, REPO)


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


def changelog():
    fmt = "- %s ([%h]({}%H))%n".format(URL_BASE)
    tag_prev, tag_current = command_output(['git', 'tag'])[-2:]
    lines = ['## Changelog']
    lines.extend(
        command_output(
            [
                'git',
                'log',
                '--pretty=format:"{}"'.format(fmt),
                '{}..{}'.format(tag_prev, tag_current)
            ],
            strip_chars=' \n\t"'
        )[::-1]
    )
    lines.append('')
    return lines


if __name__ == '__main__':
    print('\n'.join(changelog()))
