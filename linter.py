from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class Miniwdl(Linter):
    cmd = ('miniwdl', 'check', '--no-quant-check', '${file}')
    regex = r'^\s*\(Ln (?P<line>\d+), Col (?P<col>\d+)\) (?P<message>.*)$'
    multiline = False
    defaults = {
        'selector': 'source.wdl'
    }
    tempfile_suffix = '.wdl'
