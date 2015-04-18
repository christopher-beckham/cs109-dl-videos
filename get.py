#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess


def compose_cmd(url, video_filename):
    return 'rtmpdump -r rtmp://flash.dce.harvard.edu/bounce -e -C B:0 -C Z: -C S:/%s ' \
           '-C S:BounceAPI3.0 -C N:0.000000 -C S:mp4 -y mp4:%s -o %s' % (url,
                                                                         url,
                                                                         video_filename)

print sys.argv
lecture_urlfile = 'hq-%s-lecture.txt' % sys.argv[1]
section_urlfile = 'hq-%s-section.txt' % sys.argv[1]
lecture_urls = [l.strip() for l in open(lecture_urlfile)]
section_urls = [l.strip() for l in open(section_urlfile)]

for idx, url in enumerate(lecture_urls):
    cmd = compose_cmd(url, 'lecture%d.mp4' % idx)
    print cmd
    subprocess.call(cmd, shell=True)

for idx, url in enumerate(section_urls):
    cmd = compose_cmd(url, 'section%d.mp4' % idx)
    print cmd
    subprocess.call(cmd, shell=True)
