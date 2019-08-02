import subprocess as sp
from pathlib import Path

import subprocess as sp
from pathlib import Path

class VarsFile:
    def __init__(self):
        self.hostname_list = []

    def generate_hostname_list(self, path):
        self.cmd = "ls " + path
        self.p = sp.Popen(self.cmd,shell=True, stdout=sp.PIPE)
        self.path = path

        for line in self.p.stdout:
            line = line.decode("utf-8")
            self.hostname_list.append(line.strip())
        return self.hostname_list

    '''
    Provide the method with a output_filename
    Filetype will be a variable for cert, key, or pem
    Search word for interesting string to match on
    '''
    def output_file(self, output_filename, filetype, searchword):
        self.filetype = filetype
        self.output_filename = open(output_filename, 'w')

        for i in self.hostname_list:
            self.file_verify = Path(f"{self.path}/{i}/var/tmp/{i}_search_{filetype}.txt")
            self.input_filename = f"{self.path}/{i}/var/tmp/{i}_search_{filetype}.txt"
            self.read_file = open(self.input_filename, 'r')
            self.output_filename.write(f"{i}: \n")
            if file_verify.is_file():
              for line in self.read_file:
                  if searchword in line:
                      self.output_filename.writelines(f"  - {line}")
