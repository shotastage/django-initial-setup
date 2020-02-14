import os
from subprocess import Popen, PIPE


class DBSetup():
    
    def migration_list(self) -> str:
        proc = Popen(
            "python manage.py showmigrations",
            shell=True,
            stdout=PIPE, stderr=PIPE
        )
        proc.wait()    
        res = proc.communicate()

        return str(res[0]).split('b\'')[1].split('\\n')


    def migrate(self):
        proc = Popen(
            "python manage.py migrate",
            shell=True,
            stdout=PIPE, stderr=PIPE
        )
        proc.wait()
