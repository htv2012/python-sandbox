#!/usr/bin/env python3
import io
import json
import logging
import os
import sys
import traceback

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QWidget,
)
from PyQt5.QtCore import pyqtSlot

import jsonquery


logging.basicConfig(level=os.getenv('LOGLEVEL', 'WARN'))
LOGGER = logging.getLogger(__name__)


class DemoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        query_button = QPushButton("Query", self)
        grid.addWidget(query_button, 1, 1)
        query_button.clicked.connect(self.on_query_click)
        query_button.setAutoDefault(True)

        label = QLabel(
            "result = jsonquery.query("
            "json_object, key_path, "
            "predicate, selector)"
        )
        grid.addWidget(label, 1, 2)

        key_path_label = QLabel('key_path')
        self.key_path_edit = QLineEdit()
        grid.addWidget(key_path_label, 2, 0)
        grid.addWidget(self.key_path_edit, 2, 1)

        predicate_label = QLabel('predicate')
        self.predicate_edit = QLineEdit()
        grid.addWidget(predicate_label, 3, 0)
        grid.addWidget(self.predicate_edit, 3, 1)

        selector_label = QLabel('selector')
        self.selector_edit = QLineEdit()
        grid.addWidget(selector_label, 4, 0)
        grid.addWidget(self.selector_edit, 4, 1)

        json_object_label = QLabel('json_object')
        grid.addWidget(json_object_label, 5, 1)
        self.json_object_edit = QTextEdit()
        self.json_object_edit.setFontFamily("Courier")
        grid.addWidget(self.json_object_edit, 6, 1, 1, 1)
        
        with open("component.json") as stream:
            text = stream.read()
        self.json_object_edit.setText(text)
        
        label = QLabel("result")
        grid.addWidget(label, 5, 2)
        self.result_edit = QTextEdit()
        self.result_edit.setFontFamily("Courier")
        grid.addWidget(self.result_edit, 6, 2, 1, 1)

        self.setLayout(grid) 
        
        self.setGeometry(0, 0, 1000, 600)
        self.setWindowTitle('jsonquery sandbox')    
        self.showMaximized()

    @pyqtSlot()
    def on_query_click(self):
        try:
            # json_object
            json_object = self.json_object_edit.toPlainText()
            json_object = json.loads(json_object)

            # Parse other parameters
            key_path = eval(self.key_path_edit.text())
            predicate = eval(self.predicate_edit.text() or "None")
            selector = eval(self.selector_edit.text() or "None")

            result = jsonquery.query(json_object, key_path, predicate, selector)
            buffer = io.StringIO()
            for obj in result:
                json.dump(obj, buffer, sort_keys=True, indent=4)
                buffer.write("\n")
                buffer.write("-" * 20)
                buffer.write("\n")
            self.result_edit.setText(buffer.getvalue())
        except:
            message = traceback.format_exc()
            LOGGER.debug("ERROR------\n%s", message)
            self.result_edit.setText(message)

        self.result_edit.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DemoWidget()
    sys.exit(app.exec_())
