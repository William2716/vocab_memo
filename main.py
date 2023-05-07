import sys
import utils

if __name__ == "__main__":
    utils.creat_folder()
    app = utils.QtWidgets.QApplication(sys.argv)
    main_win = utils.MainWindow()
    main_win.show()
    sys.exit(app.exec_())