REQUIRED = (3, 11)
STATUS = {'python': False, 'kernel': False}
import sys 
import os
def check_basics ():
    if sys.version_info < REQUIRED:
        print(f'**** BEWARE **** - Your current Python version is {sys.version_info.major}.{sys.version_info.minor}')
        print(f'_____ Please upgrade to version 3.11 before the course _____ ')
    else:
        print(f'Your current Python version is: {sys.version_info.major}.{sys.version_info.minor} — This is fine :)')
        print('✓ Python version is OK')
        STATUS['python'] = True
        
    expected = os.path.abspath(".venv")
    actual = sys.prefix

    if actual.startswith(expected):
        print(f"✓ Correct kernel: {actual}")
        STATUS['kernel'] = True
    else:
        print (f'Incorrect kernel: {actual}')
        # print('Please see below for instructions on how to switch to the right kernel')
        # print('If you have some problems here, please contact me before the course starts so we can fix it together :)')

# def check_spacy ():
#     try:
#         nlp = spacy.load("en_core_web_sm")
#         print("OK!!!! -------------->  Spacy ready, model loaded")
#         STATUS['spacy'] = True
#     except Exception as e:
#         print(f"Something went wrong, error {str (e)}")

def prepare_user(USERNAME):
    while not USERNAME:
        USERNAME = input ('Please specify your username: ')
    with open ('user.txt', 'w') as fout:
        fout.write (f'USER={USERNAME}')
    

def check_environment ():
    check_basics ()
    # check_spacy ()
    return all (STATUS.values ())

def help_kernel ():
    print ('''If you have some issues, you will probably have to do the following:**

**1. Click on the kernel name in the top-right of this notebook**

**2. Click 'Select Another Kernel...'**

**3. Click 'Python Environments...'**

**4. Choose the option whose path contains '.venv' and DHSI.**

**5. Re-run the cell.**

**6. Please contact me before the course if you have some problems, so we can fix it together**''')