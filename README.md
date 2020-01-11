# Title page in LaTeX for UPB students
This LaTeX template may be used by students at [University POLITEHNICA of Bucharest](https://upb.ro/en/) (UPB) to generate a title page for their Project, Lab work, Report and other kinds of schoolwork. It offers the option to choose the faculty you are in and between four languages (Romanian and English for all students and French and German for FILS students).

## How to use

- Open your Linux terminal and clone your repository to your machine
  ```
  git clone https://github.com/cristiancristea00/upb-title-page.git
  ```
- Change the working directory to the one downloaded
  ```
  cd upb-title-page
  ```
- Execute make with the language as the parameter. <br /> <br />
  For Romanian:
  ```
  make RO
  ```
  For English:
  ```
  make EN
  ```
  For French (only FILS students):
  ```
  make FR
  ```
  For German (only FILS students):
  ```
  make DE
  ```

### Choices
You will be greeted with the option to choose the faculty you are studying at. You just have to type the initials before the hyphen. After that you just have to enter the details of your paper. Now there should be a pdf in the working directory.

### LaTeX
On how to acquire and install LaTeX you can check out this [page](https://www.tug.org/texlive/quickinstall.html).

## Multiple students
This script was designed with one student per paper in mind, so it doesn't offer the option to add multiple names. So here is workaround for those documents that require more students. When you are prompted to enter your first name, you follow the example below (without the parentheses) and leave empty the last name.
  ```
  (Student1 First name) (Student1 Last name) \\\\ (Student2 First name) (Student2 Last name) \\\\ ... \\\\ (StudentN First name) (StudentN Last name)
  ```

## How to contribute
You have ideas how to improve this template?
Or found any problems?

- [Fork the repository](https://help.github.com/articles/fork-a-repo/) and create a [pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/).
- Report an [issue](https://github.com/cristiancristea00/upb-title-page/issues).
