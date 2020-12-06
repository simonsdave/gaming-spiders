#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import json
import os
import sys
import subprocess
import time


class SpidersContainer(object):

    def __init__(self, docker_image):
        object.__init__(self)

        self.docker_image = docker_image

    def spiders(self):
        args = [
            'docker',
            'run',
            self.docker_image,
            'spiders.py',
        ]

        output = json.loads(subprocess.check_output(args).decode('UTF-8').strip())

        rv = list(output.keys())
        rv.remove('_metadata')
        rv.sort()

        return rv


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

    def is_success(self):
        if not self.is_finished():
            return False

        return self.output()['_metadata']['status']['code'] == 0

    def save_output(self, output_dir):
        spider_output_dir = os.path.join(output_dir, os.path.splitext(self.spider)[0])
        os.makedirs(spider_output_dir)

        output = self.output()
        if not output:
            return

        self._copy_debug_file(output, 'screenshot', spider_output_dir, 'screenshot.png')
        self._copy_debug_file(output, 'crawlLog', spider_output_dir, 'crawl-log.txt')
        self._copy_debug_file(output, 'chromeDriverLog', spider_output_dir, 'chrome-driver-log.txt')

        with open(os.path.join(spider_output_dir, 'crawl-output.json'), 'w', encoding='utf8') as f:
            json.dump(output, f, ensure_ascii=False)

    def _copy_debug_file(self, output, debug_file_property, spider_output_dir, debug_filename):
        filename_in_docker_container = output.get('_debug', {}).get(debug_file_property, None)
        if not filename_in_docker_container:
            return None

        args = [
            'docker',
            'container',
            'cp',
            '{container_id}:{filename_in_docker_container}'.format(
                container_id=self.container_id,
                filename_in_docker_container=filename_in_docker_container),
            os.path.join(spider_output_dir, debug_filename),
        ]
        subprocess.check_output(args)

        output['_debug'][debug_file_property] = debug_filename


if __name__ == "__main__":
    if len(sys.argv) != 4:
        fmt = "usage: {app} <#-spiders-2-run-at-same-time> <output-dir> <docker-image>"
        print(fmt.format(app=os.path.split(sys.argv[0])[1]))
        sys.exit(1)

    max_number_spiders_to_run = int(sys.argv[1])
    output_dir = sys.argv[2]
    docker_image = sys.argv[3]

    spiders_left_to_run = SpidersContainer(docker_image).spiders()

    running_spiders = []
    run_spiders = []

    while spiders_left_to_run or running_spiders:
        # check if any of the running spiders have finished
        for running_spider in running_spiders:
            if running_spider.is_finished():
                print('>>>{spider}<<< finished running - {status}'.format(
                    spider=running_spider.spider,
                    status='success' if running_spider.is_success() else 'failure'))
                running_spider.save_output(output_dir)

                running_spiders.remove(running_spider)
                run_spiders.append(running_spider)
            else:
                print('>>>{spider}<<< still running'.format(spider=running_spider.spider))

        # start spiders left to run until max # of spiders running reached
        while spiders_left_to_run:
            if len(running_spiders) < max_number_spiders_to_run:
                spider = spiders_left_to_run.pop(0)
                cc = CrawlContainer(spider, docker_image)
                cc.start()
                running_spiders.append(cc)
                print('>>>{spider}<<< started running'.format(spider=spider))
            else:
                break

        time.sleep(1)

    sys.exit(0)
