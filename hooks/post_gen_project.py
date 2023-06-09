
import os
import shutil

def remove_celery_file():
    os.remove("./{{cookiecutter.project_slug}}/celery.py")

def remove_dotgitlabciyml_file():
    os.remove(".gitlab-ci.yml")

def remove_dotgithub_folder():
    shutil.rmtree(".github", ignore_errors=True)

def remove_dotcircleci_folder():
    shutil.rmtree(".circleci", ignore_errors=True)

def move_dotgitlabciyml_file():
    shutil.move(".gitlab-ci.yml", "..")

def move_dotgithub_folder():
    shutil.move(".github", "..", copy_function = shutil.copytree)

def move_dotcircleci_folder():
    shutil.move(".circleci", "..", copy_function = shutil.copytree)

def main():

    if "{{ cookiecutter.ci_tool }}".lower() == "github":

        remove_dotgitlabciyml_file()
        remove_dotcircleci_folder()
        

    if "{{ cookiecutter.ci_tool }}".lower() == "gitlab":
        
        remove_dotcircleci_folder()
        remove_dotgithub_folder()

    if "{{ cookiecutter.ci_tool }}".lower() == "circleci":
        
        remove_dotgithub_folder()
        remove_dotgitlabciyml_file()
        
    if "{{ cookiecutter.add_celery }}" == "no":
        remove_celery_file()
    print("Project initialized, keep up the good work!")


if __name__ == "__main__":
    main()
