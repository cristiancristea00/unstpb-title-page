from argparse import ArgumentParser, RawTextHelpFormatter
from os import remove
from os.path import exists, join
from subprocess import CalledProcessError, CompletedProcess, run
from sys import stderr
from typing import Final


class DataCollector:
    """
    Class to get options from command line.
    """

    def __init__(self) -> None:
        """
        Initializes the class.
        """

        DESCRIPTION: Final[str] = 'Creates a PDF document using LaTeX for your university project.'
        FACULTIES: Final[str] = 'The options available for the faculty parameter are:\n' \
                                'FAIMA -> Faculty of Entrepreneurship, Business Engineering and Management\n' \
                                'FAC   -> Faculty of Automatic Control and Computers\n' \
                                'FICB  -> Faculty of Chemical Engineering and Biotechnologies\n' \
                                'FETTI -> Faculty of Electronics, Telecommunications and Information Technology\n' \
                                'FE    -> Faculty of Power Engineering\n' \
                                'FISB  -> Faculty of Biotechnical Systems Engineering\n' \
                                'FIA   -> Faculty of Aerospace Engineering\n' \
                                'FIE   -> Faculty of Electrical Engineering\n' \
                                'FIIR  -> Faculty of Industrial Engineering and Robotics\n' \
                                'FILS  -> Faculty of Engineering in Foreign Languages\n' \
                                'FIMM  -> Faculty of Mechanical Engineering and Mechatronics\n' \
                                'FIM   -> Faculty of Medical Engineering\n' \
                                'FSIM  -> Faculty of Material Science and Engineering\n' \
                                'FSA   -> Faculty of Applied Sciences\n' \
                                'FT    -> Faculty of Transports\n'

        self.__parser = ArgumentParser(allow_abbrev=False, formatter_class=RawTextHelpFormatter, description=DESCRIPTION, epilog=FACULTIES)

        self.__parser.add_argument('-al', '--arg-like', action='store_false',
                                   help='Use it if you want to pass the data to arguments instead of live input')

        self.__parser.add_argument('-l', '--language', choices=['RO', 'EN', 'FR', 'DE'], type=str,
                                   help='One of the four languages: RO/EN for everyone and FR/DE just for FILS students')

        self.__parser.add_argument('-f', '--faculty', type=str,
                                   help='The faculty at which you are enrolled (the initials provided below)')

        self.__parser.add_argument('-t', '--type', type=str,
                                   help='The document type (e.g. Project/Lab work/...)')

        self.__parser.add_argument('-s', '--subject', type=str,
                                   help='The university subject (e.g. Calculus/Algebra/...)')

        self.__parser.add_argument('-ti', '--title', type=str,
                                   help='The title of the document')

        self.__parser.add_argument('-fn', '--first-name', type=str,
                                   help='Your first name')

        self.__parser.add_argument('-ln', '--last-name', type=str,
                                   help='Your last name')

        self.__parser.add_argument('-g', '--group', type=str,
                                   help='The group you belong to')

        self.__parser._actions[0].help = 'Show this help message and exit'

        self.__arguments: dict[str] = {}

    def __parse_arguments(self) -> None:
        """
        Parses the command line arguments.
        """

        self.__arguments = vars(self.__parser.parse_args())

    def process_options(self) -> tuple[str, str, str, str, str, str, str, str]:
        """
        Processes the arguments or inputs the information from the user.

        Returns:
            tuple[str, str, str, str, str, str, str, str]: The processed information
        """

        self.__parse_arguments()

        if not self.__arguments['arg_like']:

            for elem in self.__arguments:

                if self.__arguments[elem] is None:

                    self.__parser.error(f'Argument {elem} is empty. Every argument is required if -ni is provided.')

            return (self.__arguments['language'], self.__arguments['faculty'], self.__arguments['type'], self.__arguments['subject'],
                    self.__arguments['title'], self.__arguments['first_name'], self.__arguments['last_name'], self.__arguments['group'])

        else:

            return (input('Language: '), input('Faculty: '), input('Type: '), input('Subject: '),
                    input('Title: '), input('First Name: '), input('Last Name: '), input('Group: '))


class PDFGenerator:
    """
    Class that generates the PDF file.
    """

    def __init__(self, options: tuple[str, str, str, str, str, str, str, str]) -> None:

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

        self.__process_options(options)

    def __process_options(self, options: tuple[str, str, str, str, str, str, str, str]) -> None:
        """
        Processes the options.

        Args:
            options (tuple[str, str, str, str, str, str, str, str]): The options provided by the user
        """

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

    def __create_pdf(self) -> CompletedProcess:
        """
        Creates the PDF file.

        Returns:
            CompletedProcess: The process that was executed
        """

        return run([self.program, self.halt, self.interaction, self.job_name, self.information], capture_output=True, check=True)

    def __clean_files(self) -> None:
        """
        Cleans the unnecessary files after the PDF file was created.
        """

        if exists(self.log_file):

            remove(self.log_file)

        if exists(self.aux_file):

            remove(self.aux_file)

    def run(self) -> None:
        """
        Runs the program.
        """

        try:

            self.__create_pdf()
            print(F'PDF creation completed successfully. Output written to: {self.name}.pdf')

        except CalledProcessError as error:

            print(F'PDF creation failed with exit code {error.returncode}. Maybe you provided an invalid language or '
                  F'faculty. Check the output for more information.', '-' * 80, error.output, '-' * 80, sep='\n', file=stderr)

            raise

        finally:

            self.__clean_files()


def main() -> None:
    """
    The main function.
    """

    data_collector = DataCollector()
    pdf_generator = PDFGenerator(data_collector.process_options())
    pdf_generator.run()


if __name__ == '__main__':
    main()
