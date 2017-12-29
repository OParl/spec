# This program is part of OParl and may be used to build the specification

from argparse import ArgumentParser
import subprocess
import os
from os import path
from shutil import copy2, rmtree
from glob import glob
import shlex
from scripts.json_schema2markdown import schema_to_markdown

SPECIFICATION_BUILD_ACTIONS = [
    'all',
    'clean',
    'test',
    'live',
    'html',
    'pdf',
    'odt',
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
    'pandoc': '--from markdown --standalone --table-of-contents --toc-depth=2 --number-sections'
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
        dest='language'
    )

    parser.add_argument(
        '--version',
        '-V',
        help='Specification version descriptor',
        action='store',
        # default: git-describe based version
        dest='version'
    )

    parser.add_argument(
        '--latex-template',
        help='Change the latex template used for PDF generation',
        action='store',
        dest='latex_template',
        default='resources/template.tex'
    )

    parser.add_argument(
        '--html-style',
        help='Change the CSS file used for styling the HTML output',
        action='store',
        dest='html_style',
        default='resources/html5.css'
    )

    parser.add_argument(
        'action',
        help='Build action to take, available actions are: {}'.format(', '.join(SPECIFICATION_BUILD_ACTIONS)),
        action='store',
        default='all',
        nargs='*'
    )

    return parser

def check_build_action(action):
    if action in SPECIFICATION_BUILD_ACTIONS:
        return action

    raise Exception('Unknown build action: {}, choose one of: {}'.format(action, ', '.join(SPECIFICATION_BUILD_ACTIONS)))

def get_git_describe_version():
    return subprocess.getoutput('git describe')

def find_executable(program_name):
    # adapated from https://stackoverflow.com/a/377028/718752
    exec_path, exec_name = path.split(program_name)
    def is_executable(fpath):
        return path.isfile(fpath) and os.access(fpath, os.X_OK)

    if exec_path and is_executable(exec_path):
        return program_name
    else:
        for env_path in os.environ['PATH'].split(os.pathsep):
            exec_file = path.join(env_path, program_name)
            if is_executable(exec_file):
                return exec_file

    return None

def check_available_tools():
    tools = {}
    for tool in SPECIFICATION_BUILD_TOOLS:
        executable = find_executable(tool)
        if executable:
            tools[tool] = executable
        else:
            raise Exception('{} not found, aborting.'.format(tool))

    return tools

def prepare_builddir():
    os.makedirs('build/src/images')

def prepare_schema(language):
    language_file = 'schema/strings.yml'
    if language != 'de':
        language_file = 'locales/{}/schema/strings.yml'.format(language)

    output_file = 'build/src/9-99-schema.md'

    schema_to_markdown('schema', 'examples', output_file, language, language_file)


def prepare_markdown(language):
    glob_pattern = 'src/*.md'
    if language != 'de':
        glob_pattern = 'locales/en/*.md'

    files = glob(glob_pattern)
    for f in files:
        copy2(f, 'build/src/')

def prepare_images(tools):
    glob_pattern = 'src/images/*.*'

    files = glob(glob_pattern)
    for f in files:
        convert_command = ''
        fname, fext = os.path.splitext(f)
        fout = path.join('build', 'src', 'images', os.path.basename(fname)) + '.png'

        if fext == '.pdf':
            convert_command = '{} {} -sOutputFile={} -f {}'.format(
                tools['gs'],
                SPECIFICATION_BUILD_FLAGS['gs'],
                fout,
                f
            )

        if fext == '.dot':
            convert_command = '{} -Tpng {} -o {}'.format(
                tools['dot'],
                f,
                fout
            )

        if fext == '.svg':
            convert_command = '{} {} {}'.format(
                tools['convert'],
                f,
                fout
            )

        try:
            cmd = shlex.split(convert_command)
            output = subprocess.run(cmd, check=True)
        except:
            raise Exception(
                'Errored on image prep for {}, please check the command:\n{}'.format(
                    f, convert_command
                )
            )

def action_clean():
    if path.isdir('build'):
        rmtree('build')

def action_test():
    pass

def action_live():
    pass

def action_html():
    pass

def action_pdf():
    pass

def action_odt():
    pass

def action_txt():
    pass

def action_epub():
    pass

def action_all():
    action_html()
    action_pdf()
    action_odt()
    action_txt()
    action_epub()

def action_zip():
    pass

def action_gz():
    pass

def action_bz():
    pass

def action_archives():
    action_zip()
    action_gz()
    action_bz()

def main():
    options = configure_argument_parser().parse_args()
    action = check_build_action(options.action[0])

    if options.version == None:
        options.version = get_git_describe_version()

    tools = check_available_tools()

    # always clean
    action_clean()

    if action == 'clean':
        exit(0)

    prepare_builddir()
    prepare_schema(options.language)
    prepare_markdown(options.language)
    prepare_images(tools)

    # pandoc all the things
    action_function = 'action_{}()'.format(action)
    eval(action_function)

if __name__ == '__main__':
    main()