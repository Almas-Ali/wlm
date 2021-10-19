# import argparse
# import os
# import getpass
# import datetime

# import click


# def author_info():
#     info = '''\
# WLM - Windows and Linux Manager
# A all in one tool that will help you in your work productivity, which works both windows and linux.

# Author    :  Md. Almas Ali
# Copyright :  2021\
# '''
#     print(info)


# def configure():
#     '''To configure system for advance tasks.'''

#     print('Configuring your system for future task.')

#     config_time = datetime.datetime.now()
#     os_name = os.name
#     user_name = getpass.getuser()

#     with open('config.py', 'r') as cfg:
#         cfg.write(f'''\
# config_time = {config_time}
# os = {os_name}
# username = {user_name}
# ''')
#     print('Configuration Complete Successfully !')


# def linux_installer(filename):
#     os.system(f'sudo apt-get install {filename}')


# @click.command()
# def main():
#     # parser = argparse.ArgumentParser(
#     #     prog='wlm', add_help='Windows and Linux Manager')

#     # parser.add_argument('-a', '--author', action='store_true',
#     #                     help='to see author informations.')
#     # parser.add_argument('-i', '--install', metavar='filename',
#     #                     help='to install a new package in linux.')
#     # parser.add_argument('-c', '--config', action='store_true',
#     #                     help='to configure or reconfigure wlm for first use.')

#     # args = parser.parse_args()

#     # print(args)

#     # if args.author:
#     #     author_info()

#     # elif args.config:
#     #     configure()

#     # elif args.install:
#     #     linux_installer(args.install)

#     # elif not any(vars(args).values()):
#     #     parser.print_help()

#     click.echo('test world !')


import click
import os
from . import config


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        # if os.name == 'posix':
        #     system = 'linux'
        # elif os.name == 'nt':
        #     system = 'windows'
        # else:
        #     system = 'unknown'

        commands_folder = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'linux'))
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename.replace(
                    "cmd_", "").replace(".py", ""))

        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"wlm.linux.cmd_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI)
def cli():
    """Welcome to WLM (Windows and Linux Manager)! An all-in-one cli utility tool!"""
    pass
