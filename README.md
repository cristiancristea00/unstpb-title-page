# Title page in LaTeX for UPB students

This LaTeX template may be used by students at [University POLITEHNICA of Bucharest](https://upb.ro/en/) (UPB) to generate a title page for their Project, Lab work, Report and other kinds of schoolwork. It offers the option to choose the faculty you are in and between four languages (Romanian and English for all students and French and German for FILS students).

## How to use

- Open your Linux terminal and clone your repository to your machine

  ```shell
  git clone https://github.com/cristiancristea00/upb-title-page.git
  ```

- Change the working directory to the one downloaded

  ```shell
  cd upb-title-page
  ```

- Execute the following command to give execution permissions to the script for Unix-like system users

  ```shell
  sudo chmod +x create.py
  ```

- Now, for more information, run the following on Unix-like systems

  ```shell
  ./create.py --help
  ```

  or on Windows

  ```shell
  python create.py --help
  ```

### Choices

If you use interactive mode, you will be greeted with the option to input the faculty at which you are studying and the details of your paper. Also, there is the option to pass the details as command line arguments. For this option, inputs that require multiple words have to be passed using double quotes (e.g. "John Doe"). Now there should be a pdf in the working directory with the title of the paper as the name if the operation completed successfully.

### LaTeX

On how to acquire and install LaTeX and Python you can check out this [page](https://www.tug.org/texlive/quickinstall.html) and this [page](https://www.python.org/) respectively.

## Multiple students

This script was designed with one student per paper in mind, so it doesn't offer the option to add multiple names. So here is workaround for those documents that require more students. When you are prompted to enter your first name, you follow the example below (without the parentheses) and leave empty the last name.

```bash
(Student1 First name) (Student1 LAST NAME) \\ (Student2 First name) (Student2 LAST NAME) \\ ... \\ (StudentN First name) (StudentN LAST NAME)
```

## How to contribute

You have ideas how to improve this template?
Or found any problems?

- [Fork the repository](https://help.github.com/articles/fork-a-repo/) and create a [pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/).
- Report an [issue](https://github.com/cristiancristea00/upb-title-page/issues).
