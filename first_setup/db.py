import os
import subprocess


class DBSetup():
    
    def migration_list(self) -> str:

        out = subprocess.run(['python', 'manage.py', 'showmigrations'], shell=True, stdout=subprocess.PIPE)

        return out.stdout
