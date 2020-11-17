#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import json
import os
import sys
import subprocess
import time


class CrawlContainer(object):

    def __init__(self, spider, docker_image):
        object.__init__(self)

        self.spider = spider
        self.docker_image = docker_image

        self.container_id = None

    def start(self):
        if self.container_id:
            return None

        args = [
            'docker',
            'run',
            '-d',
            self.docker_image,
            self.spider,
        ]
        self.container_id = subprocess.check_output(args).decode('UTF-8').strip()

        return self.container_id

    def is_finished(self):
        if not self.container_id:
            return False

        args = [
            'docker',
            'inspect',
            self.container_id,
        ]
        status = json.loads(subprocess.check_output(args).decode('UTF-8').strip())[0]['State']['Status']
        return status != 'running'

    def output(self):
        if not self.is_finished():
            return None

        args = [
            'docker',
            'logs',
            self.container_id,
        ]
        return json.loads(subprocess.check_output(args).decode('UTF-8').strip())


if __name__ == "__main__":
    if len(sys.argv) < 4:
        fmt = "usage: {app} <# spiders to run> <docker-image> <spider-1> ... <spider-N>"
        print(fmt.format(app=os.path.split(sys.argv[0])[1]))
        sys.exit(1)

    max_number_spiders_to_run = int(sys.argv[1])
    docker_image = sys.argv[2]
    spiders_left_to_run = sys.argv[3:]

    running_spiders = []
    run_spiders = []

    while spiders_left_to_run or running_spiders:
        # check if any of the running spiders have finished
        for running_spider in running_spiders:
            if running_spider.is_finished():
                running_spiders.remove(running_spider)
                run_spiders.append(running_spider)
                print('>>>{spider}<<< finished running'.format(spider=running_spider.spider))
            else:
                print('>>>{spider}<<< still running'.format(spider=running_spider.spider))

        # start spiders left to run until max # of spiders running reached
        while spiders_left_to_run:
            if len(running_spiders) < max_number_spiders_to_run:
                spider = spiders_left_to_run.pop()
                cc = CrawlContainer(spider, docker_image)
                cc.start()
                running_spiders.append(cc)
                print('>>>{spider}<<< started running'.format(spider=spider))
            else:
                break

        time.sleep(1)

    sys.exit(0)
