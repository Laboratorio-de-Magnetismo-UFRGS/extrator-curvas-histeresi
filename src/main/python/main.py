# -*- coding: utf-8 -*-

import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext

import Controller.MainWindow

class AppContext(ApplicationContext):
    def run(self):
        window = Controller.MainWindow()
        version = self.build_settings['version']
        window.setWindowTitle(f"LAM - Extrator de Curvas de Histerese v{version}")
        window.show()
        return self.app.exec_()
    

if __name__ == '__main__':
    appctxt = AppContext()       # 1. Instantiate ApplicationContext
    exit_code = appctxt.run()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)