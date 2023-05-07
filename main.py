import sys
import utils
import requests_cache

requests_cache.install_cache('dictionary_cache', expire_after=3600)

if __name__ == "__main__":
    utils.creat_folder()
    app = utils.QtWidgets.QApplication(sys.argv)
    main_win = utils.MainWindow()
    main_win.show()
    sys.exit(app.exec_())