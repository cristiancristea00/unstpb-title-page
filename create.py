#!/usr/bin/env python3
from argparse import ArgumentParser, RawTextHelpFormatter
from subprocess import run
from os.path import join

description: str = 'Script that generates the PDF file based on the information provided by the user.'
additional_information: str = 'The options available for the faculty parameter are:\n' \
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

argument_parser = ArgumentParser(allow_abbrev = False, description = description, epilog = additional_information,
                                 formatter_class = RawTextHelpFormatter)
argument_parser.add_argument('-ni', '--non-interactive', action = 'store_false',
                             help = 'Used if you want to pass the details in an non-interactive manner')
argument_parser.add_argument('-l', '--language', choices = ['RO', 'EN', 'FR', 'DE'], metavar = '', type = str,
                             help = 'One of the four languages: RO/EN and FR/DE just for FILS students')
argument_parser.add_argument('-f', '--faculty', metavar = '', type = str,
                             help = 'The faculty at which you are a student')
argument_parser.add_argument('-t', '--type', metavar = '', type = str,
                             help = 'The document type (e.g. Project/Lab work/...)')
argument_parser.add_argument('-s', '--subject', metavar = '', type = str, help = 'The university subject in question')
argument_parser.add_argument('-ti', '--title', metavar = '', type = str, help = 'The title of the document')
argument_parser.add_argument('-fn', '--first-name', metavar = '', type = str, help = 'Your first name')
argument_parser.add_argument('-ln', '--last-name', metavar = '', type = str, help = 'Your last name')
argument_parser.add_argument('-g', '--group', metavar = '', type = str, help = 'The group you belong to')
arguments = vars(argument_parser.parse_args())

program: str = R'xelatex'
interaction: str = R'--interaction=scrollmode'
job_name: str = R'--jobname={}'

delim: str = '"'
document_type: str = R'\newcommand{{\docType}}{{{}}}'
subject: str = R'\newcommand{{\subject}}{{{}}}'
title: str = R'\renewcommand{{\title}}{{{}}}'
first_name: str = R'\newcommand{{\firstName}}{{{}}}'
last_name: str = R'\newcommand{{\lastName}}{{{}}}'
group: str = R'\newcommand{{\group}}{{{}}}'
template: str = R'\input{{{}}}'

clean: str = 'rm'
clean_option: str = '-f'
log_file: str = '{}.log'
aux_file: str = '{}.aux'

if not arguments['non_interactive']:
    template = template.format(join(join('faculties', input('Language: ')), input('Faculty: ') + '.tex'))
    document_type = document_type.format(input('Type: '))
    subject = subject.format(input('Subject: '))
    temp_title = input('Title: ')
    title = title.format(temp_title)
    job_name = job_name.format(temp_title)
    log_file = log_file.format(temp_title)
    aux_file = aux_file.format(temp_title)
    first_name = first_name.format(input('First name: '))
    last_name = last_name.format(input('Last name: '))
    group = group.format(input('Group: '))

else:
    for elem in arguments:
        if arguments[elem] is None:
            argument_parser.error(f'Argument {elem} is empty. Every argument is required if -ni is not provided.')
    template = template.format(join(join('faculties', arguments['language']), arguments['faculty'] + '.tex'))
    document_type = document_type.format(arguments['type'])
    subject = subject.format(arguments['subject'])
    temp_title = arguments['title']
    title = title.format(temp_title)
    job_name = job_name.format(temp_title)
    log_file = log_file.format(temp_title)
    aux_file = aux_file.format(temp_title)
    first_name = first_name.format(arguments['first_name'])
    last_name = last_name.format(arguments['last_name'])
    group = group.format(arguments['group'])

information = ' '.join([document_type, subject, title, first_name, last_name, group, template])
run([program, interaction, job_name, information])
run([clean, clean_option, log_file, aux_file])
