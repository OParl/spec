#!/usr/bin/env python3
# This program is part of OParl and may be used to build the specification

import os
import shlex
import shutil
import subprocess
import sys
from argparse import ArgumentParser
from glob import glob
from os import path

from scripts.json_schema2markdown import schema_to_markdown

SPECIFICATION_BUILD_ACTIONS = [
    'all',
    'clean',
    'test',
    'live',
    'html',
    'pdf',
    'odt',
    'docx',
    'txt',
    'epub',
    'archives',
    'zip',
    'gz',
    'bz'
]

SPECIFICATION_BUILD_TOOLS = [
    'pandoc',
    'dot',
    'xelatex',
    'gs',
    'convert',
    'python3',
    'tar',
    'zip'
]

SPECIFICATION_BUILD_FLAGS = {
    'gs': '-dQUIET -dSAFER -dBATCH -dNOPAUSE -sDisplayHandle=0 -sDEVICE=png16m -r600 -dTextAlphaBits=4',
    'pandoc': '--from markdown --standalone --table-of-contents --toc-depth=3 --number-sections'
}


def configure_argument_parser():
    parser = ArgumentParser(
        prog='./build.py',
        epilog='''
            build.py is part of the OParl Specification and thus distributed
            under the terms of the Creative Commons SA 4.0 License.
        '''
    )

    parser.add_argument(
        '--language',
        '-l',
        help='Specification language',
        default='de',
        action='store',
    )

    parser.add_argument(
        '--version',
        '-V',
        help='This will be displayed as version in the specification. Defaults to `git desribe`',
        action='store',
    )

    parser.add_argument(
        '--print-basename',
        help='This will output the base name used for build output',
        action='store_true',
        dest='print_basename'
    )

    parser.add_argument(
        '--latex-template',
        help='Change the latex template used for PDF generation',
        action='store',
        default='resources/template.tex'
    )

    parser.add_argument(
        '--html-style',
        help='Change the CSS file used for styling the HTML output',
        action='store',
        default='resources/html5.css'
    )

    parser.add_argument(
        'action',
        help='Build action to take, available actions are: {}'.format(', '.join(SPECIFICATION_BUILD_ACTIONS)),
        action='store',
        nargs='*'
    )

    return parser


def check_build_action(action):
    if len(action) == 0:
        return 'all'

    if action[0] in SPECIFICATION_BUILD_ACTIONS:
        return action[0]

    raise Exception(
        'Unknown build action: {}, choose one of: {}'.format(action, ', '.join(SPECIFICATION_BUILD_ACTIONS)))


def get_git_describe_version():
    return subprocess.check_output('git describe', shell=True, universal_newlines=True).strip()


def check_available_tools():
    tools = {}
    for tool in SPECIFICATION_BUILD_TOOLS:
        executable = shutil.which(tool)
        if executable:
            tools[tool] = executable
        else:
            raise Exception('{} not found, aborting.'.format(tool))

    return tools


def get_filename_base(language, version):
    return 'OParl-{}-{}'.format(version, language)


def prepare_builddir(filename_base):
    os.makedirs('build/src/images')
    os.makedirs('build/{}'.format(filename_base))


def prepare_schema(language):
    output_file = 'build/src/3-99-schema.md'
    schema = schema_to_markdown('schema', 'examples')

    with open(output_file, 'w+') as f:
        f.write(schema)

def prepare_markdown(language):
    glob_pattern = 'src/*.md'
    if language != 'de':
        glob_pattern = 'locales/en/*.md'

    files = glob(glob_pattern)
    for f in files:
        shutil.copy2(f, 'build/src/')


def prepare_images(tools):
    glob_pattern = 'src/images/*.*'

    files = glob(glob_pattern)
    for f in files:
        convert_command = ''
        filename, extension = os.path.splitext(f)
        fout = path.join('build', 'src', 'images', os.path.basename(filename) + '.png')

        shutil.copy2(f, fout)

        if extension == '.pdf':
            convert_command = '{} {} -sOutputFile={} -f {}'.format(
                tools['gs'],
                SPECIFICATION_BUILD_FLAGS['gs'],
                fout,
                f
            )

        if extension == '.dot':
            convert_command = '{} -Tpng {} -o {}'.format(
                tools['dot'],
                f,
                fout
            )

        if extension == '.svg':
            convert_command = '{} {} {}'.format(
                tools['convert'],
                f,
                fout
            )

        cmd = shlex.split(convert_command)
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError:
            raise Exception(
                'Errored on image prep for {}, please check the command:\n{}'.format(
                    f, convert_command
                )
            )


def get_pandoc_version(pandoc_bin):
    version_tuple = subprocess.getoutput('{} --version'.format(pandoc_bin)).split('\n')[0].split(' ')[1].split('.')
    return [int(v) for v in version_tuple]


def run_pandoc(pandoc_bin, filename_base, output_format, extra_args='', extra_files=''):
    output_file = 'build/{}/{}.{}'.format(filename_base, filename_base, output_format)
    if path.exists(output_file):
        return

    source_files = glob('build/src/*.md')
    source_files.sort(key=lambda file: path.basename(file))

    # NOTE: Once we can safely assume pandoc 2.0, we can use resource-path
    #       for neater include management in the markdown files
    # pandoc_command = '{} {} {} --resource-path=.:build/src -o {} {} {}'.format(
    pandoc_command = '{} {} {} -o {} {} {}'.format(
        pandoc_bin,
        SPECIFICATION_BUILD_FLAGS['pandoc'],
        extra_args,
        output_file,
        extra_files,
        ' '.join(source_files)
    )

    cmd = shlex.split(pandoc_command)
    try:
        subprocess.run(cmd, check=True, stdout=sys.stdout, stderr=sys.stderr)
    except subprocess.CalledProcessError:
        raise Exception(
            'Errored on pandoc: {}'.format(pandoc_command)
        )


class Action:
    @staticmethod
    def clean():
        shutil.rmtree('build', ignore_errors=True)

    @staticmethod
    def test():
        # TODO: validate.py appears to be broken
        pass

    @staticmethod
    def live(tools, _, filename_base):
        args = '--to html5 --section-divs --no-highlight --template=resources/live.html'
        run_pandoc(tools['pandoc'], filename_base, 'html', extra_args=args)

    @staticmethod
    def html(tools, options, filename_base):
        args = '--to html5 --css {} --section-divs --self-contained'.format(options.html_style)
        run_pandoc(tools['pandoc'], filename_base, 'html', extra_args=args)

    @staticmethod
    def pdf(tools, options, filename_base):
        args = '--pdf-engine=xelatex'
        if get_pandoc_version(tools['pandoc'])[0] < 2:
            args = '--latex-engine=xelatex'

        args += ' --template {}'.format(options.latex_template)

        run_pandoc(tools['pandoc'], filename_base, 'pdf', extra_args=args)

    @staticmethod
    def odt(tools, _, filename_base):
        run_pandoc(tools['pandoc'], filename_base, 'odt')

    @staticmethod
    def docx(tools, _, filename_base):
        run_pandoc(tools['pandoc'], filename_base, 'docx')

    @staticmethod
    def txt(tools, _, filename_base):
        run_pandoc(tools['pandoc'], filename_base, 'txt')

    @staticmethod
    def epub(tools, _, filename_base):
        run_pandoc(tools['pandoc'], filename_base, 'epub')

    @staticmethod
    def all(tools, options, filename_base):
        Action.html(tools, options, filename_base)
        Action.pdf(tools, options, filename_base)
        Action.odt(tools, options, filename_base)
        Action.docx(tools, options, filename_base)
        Action.txt(tools, options, filename_base)
        Action.epub(tools, options, filename_base)

    @staticmethod
    def zip(tools, options, filename_base):
        Action.all(tools, options, filename_base)
        archive_name = '{}.zip'.format(filename_base)
        subprocess.run(['zip', '-qr', archive_name, filename_base], cwd='build')

    @staticmethod
    def gz(tools, options, filename_base):
        Action.all(tools, options, filename_base)
        archive_name = '{}.tar.gz'.format(filename_base)
        subprocess.run(['tar', '-czf', archive_name, filename_base], cwd='build')

    @staticmethod
    def bz(tools, options, filename_base):
        Action.all(tools, options, filename_base)
        archive_name = '{}.tar.bz2'.format(filename_base)
        subprocess.run(['tar', '-cjf', archive_name, filename_base], cwd='build')

    @staticmethod
    def archives(tools, options, filename_base):
        Action.zip(tools, options, filename_base)
        Action.gz(tools, options, filename_base)
        Action.bz(tools, options, filename_base)


def main():
    options = configure_argument_parser().parse_args()
    action = check_build_action(options.action)

    if options.version is None:
        options.version = get_git_describe_version()

    filename_base = get_filename_base(options.language, options.version)

    if options.print_basename:
        print(filename_base)
        exit(0)

    tools = check_available_tools()

    # always clean
    Action.clean()

    if action == 'clean':
        exit(0)

    prepare_builddir(filename_base)
    prepare_schema(options.language)
    prepare_markdown(options.language)
    prepare_images(tools)

    # Avoid much boilerplate
    getattr(Action, action)(tools, options, filename_base)


if __name__ == '__main__':
    main()
