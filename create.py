#!/usr/bin/env python3
from argparse import ArgumentParser, RawTextHelpFormatter
from os import remove
from os.path import exists, join
from subprocess import CalledProcessError, CompletedProcess, run
from sys import stderr
from typing import Dict, Tuple


class OptionsGetter:

    def __init__(self):
        self.arguments: Dict[str] = {}

        self.description: str = 'Script that generates the PDF file based on the information provided by the user.'
        self.additional_information: str = 'The options available for the faculty parameter are:\n' \
                                           'FAIMA - Faculty of Entrepreneurship, Business Engineering and Management\n' \
                                           'FAC - Faculty of Automatic Control and Computers\n' \
                                           'FCASM - Faculty of Applied Chemistry and Materials Science\n' \
                                           'FETTI - Faculty of Electronics, Telecommunications and Information Technology\n' \
                                           'FE - Faculty of Power Engineering\n' \
                                           'FISB - Faculty of Biotechnical Systems Engineering\n' \
                                           'FIA - Faculty of Aerospace Engineering\n' \
                                           'FIE - Faculty of Electrical Engineering\n' \
                                           'FIIR - Faculty of Industrial Engineering and Robotics\n' \
                                           'FILS - Faculty of Engineering in Foreign Languages\n' \
                                           'FIMM - Faculty of Mechanical Engineering and Mechatronics\n' \
                                           'FIM - Faculty of Medical Engineering\n' \
                                           'FSIM - Faculty of Material Science and Engineering\n' \
                                           'FSA - Faculty of Applied Sciences\n' \
                                           'FT - Faculty of Transports\n'

        self.argument_parser = ArgumentParser(allow_abbrev=False, formatter_class=RawTextHelpFormatter,
                                              description=self.description, epilog=self.additional_information, )

    def parse_arguments(self):

        self.argument_parser.add_argument('-ni', '--non-interactive', action='store_false',
                                          help='Used if you want to input the details in an non-interactive manner\n'
                                               'by passing all the information to command line arguments')
        self.argument_parser.add_argument('-l', '--language', choices=['RO', 'EN', 'FR', 'DE'], metavar='',
                                          type=str,
                                          help='One of the four languages: RO/EN and FR/DE just for FILS students')
        self.argument_parser.add_argument('-f', '--faculty', metavar='', type=str,
                                          help='The faculty at which you are a student (the initials provided below)')
        self.argument_parser.add_argument('-t', '--type', metavar='', type=str,
                                          help='The document type (e.g. Project/Lab work/...)')
        self.argument_parser.add_argument('-s', '--subject', metavar='', type=str,
                                          help='The university subject in question')
        self.argument_parser.add_argument('-ti', '--title', metavar='', type=str,
                                          help='The title of the document')
        self.argument_parser.add_argument('-fn', '--first-name', metavar='', type=str, help='Your first name')
        self.argument_parser.add_argument('-ln', '--last-name', metavar='', type=str, help='Your last name')
        self.argument_parser.add_argument('-g', '--group', metavar='', type=str, help='The group you belong to')
        self.arguments = vars(self.argument_parser.parse_args())

    def process_arguments_or_input(self) -> Tuple[str, str, str, str, str, str, str, str]:
        if not self.arguments['non_interactive']:
            for elem in self.arguments:
                if self.arguments[elem] is None:
                    self.argument_parser.error(f'Argument {elem} is empty. Every argument is required if -ni is provided.')
            return self.arguments['language'], self.arguments['faculty'], self.arguments['type'], self.arguments['subject'], \
                   self.arguments['title'], self.arguments['first_name'], self.arguments['last_name'], self.arguments['group']

        return input('Language: '), input('Faculty: '), input('Type: '), input('Subject: '), input('Title: '), input('First Name: '), \
               input('Last Name: '), input('Group: ')


class PDFGenerator:

    def __init__(self):
        self.program: str = R'xelatex'
        self.interaction: str = R'-interaction=nonstopmode'
        self.halt: str = R'-halt-on-error'
        self.job_name: str = R'-jobname={}'

        self.template: str = R'\input{{{}}}'
        self.document_type: str = R'\newcommand{{\docType}}{{{}}}'
        self.subject: str = R'\newcommand{{\subject}}{{{}}}'
        self.title: str = R'\renewcommand{{\title}}{{{}}}'
        self.first_name: str = R'\newcommand{{\firstName}}{{{}}}'
        self.last_name: str = R'\newcommand{{\lastName}}{{{}}}'
        self.group: str = R'\newcommand{{\group}}{{{}}}'
        self.information: str = R''
        self.name: str = R''

        self.log_file: str = R'{}.log'
        self.aux_file: str = R'{}.aux'

    def get_options(self, options: Tuple[str, str, str, str, str, str, str, str]):
        self.template = self.template.format(join(join('faculties', options[0]), options[1] + '.tex'))
        self.document_type = self.document_type.format(options[2])
        self.subject = self.subject.format(options[3])
        self.title = self.title.format(options[4])
        self.first_name = self.first_name.format(options[5])
        self.last_name = self.last_name.format(options[6])
        self.group = self.group.format(options[7])

        self.information = ' '.join([self.document_type, self.subject, self.title, self.first_name, self.last_name, self.group, self.template])

        self.job_name = self.job_name.format(options[4])
        self.log_file = self.log_file.format(options[4])
        self.aux_file = self.aux_file.format(options[4])
        self.name = options[4]

    def create_pdf(self) -> CompletedProcess:
        return run([self.program, self.halt, self.interaction, self.job_name, self.information], capture_output=True, check=True)

    def clean_files(self):
        if exists(self.log_file):
            remove(self.log_file)
        if exists(self.aux_file):
            remove(self.aux_file)

    def run(self):
        try:
            self.create_pdf()
            print(F'PDF creation completed successfully. Output written to: {self.name}.pdf')
        except CalledProcessError as error:
            print(F'PDF creation failed with exit code {error.returncode}. Maybe you provided an invalid language or '
                  F'faculty. Check the output for more information.', '-' * 80, error.output, '-' * 80, sep='\n', file=stderr)
            raise
        finally:
            self.clean_files()


def main():
    options_getter = OptionsGetter()
    options_getter.parse_arguments()
    pdf_generator = PDFGenerator()
    pdf_generator.get_options(options_getter.process_arguments_or_input())
    pdf_generator.run()


if __name__ == '__main__':
    main()
