from model.chatplatform import ChatPlatform
from view.iapplicationview import ApplicationView
from viewmodel.iapplicationviewmodel import ApplicationViewModel

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit, QComboBox, QPushButton, QLineEdit)
from typing import Callable, List

class ApplicationViewImpl(ApplicationView):

  def __init__(self, viewmodel: ApplicationViewModel):
    self.__viewmodel: ApplicationViewModel = viewmodel
    self.__app: QApplication = QApplication([])
    # TODO: End the bot client when it's active and the application window is
    # closed.
    self.__window: QWidget = self.create_window()

  def create_window(self) -> QWidget:
    # Please don't assign me to GUI code ever.
    window: QWidget = QWidget()
    window.setWindowTitle("WIP")
    layout: QVBoxLayout = QVBoxLayout()

    header_font: QFont = QFont()
    header_font.setPointSize(12)
    header_font.setBold(True)

    label_font: QFont = QFont()
    label_font.setPointSize(10)
    label_font.setBold(False)

    header_general: QLabel = QLabel(window)
    header_general.setText("General")
    header_general.setFont(header_font)
    layout.addWidget(header_general)

    description_general: QLabel = QLabel(window)
    description_general.setText("Keep this window open even after the bot is "
      + "started!")
    description_general.setFont(label_font)
    layout.addWidget(description_general)

    fields_general: QVBoxLayout = QVBoxLayout()

    general_prefix: QHBoxLayout = QHBoxLayout()
    label_prefix: QLabel = QLabel(window)
    label_prefix.setText("Prefix")
    label_prefix.setFont(label_font)
    line_edit_prefix: QLineEdit = QLineEdit(window)
    line_edit_prefix.setPlaceholderText("Prefix")
    line_edit_prefix.setText(self.__viewmodel.prefix)
    general_prefix.addWidget(label_prefix)
    general_prefix.addWidget(line_edit_prefix)
    fields_general.addLayout(general_prefix)

    general_platform: QHBoxLayout = QHBoxLayout()
    label_platform: QLabel = QLabel(window)
    label_platform.setText("Platform")
    label_platform.setFont(label_font)
    combo_box_platform: QComboBox = QComboBox(window)
    combo_box_platform.addItems(["none", "discord", "twitch"])
    combo_box_platform.setCurrentText(self.__viewmodel.platform.value)
    combo_box_platform.currentIndexChanged.connect(self.__viewmodel.write_config)
    general_platform.addWidget(label_platform)
    general_platform.addWidget(combo_box_platform)
    fields_general.addLayout(general_platform)

    general_token: QHBoxLayout = QHBoxLayout()
    label_token: QLabel = QLabel(window)
    label_token.setText("Token")
    label_token.setFont(label_font)
    line_edit_token: QLineEdit = QLineEdit(window)
    line_edit_token.setPlaceholderText("Token")
    line_edit_token.setText(self.__viewmodel.token)
    general_token.addWidget(label_token)
    general_token.addWidget(line_edit_token)
    fields_general.addLayout(general_token)
    
    layout.addLayout(fields_general)

    header_twitch: QLabel = QLabel(window)
    header_twitch.setText("Twitch")
    header_twitch.setFont(header_font)

    layout.addWidget(header_twitch)

    description_twitch: QLabel = QLabel(window)
    description_twitch.setText("You do not have to fill this out if you aren't "
      + "using Twitch!")

    layout.addWidget(description_twitch)

    twitch_username: QHBoxLayout = QHBoxLayout()
    label_username: QLabel = QLabel(window)
    label_username.setText("Username")
    label_username.setFont(label_font)
    line_edit_username: QLineEdit = QLineEdit(window)
    line_edit_username.setPlaceholderText("Username")
    line_edit_username.setText(self.__viewmodel.username)
    twitch_username.addWidget(label_username)
    twitch_username.addWidget(line_edit_username)

    layout.addLayout(twitch_username)

    button_toggle: QPushButton = QPushButton(window)
    button_toggle.setText("Start")
    button_toggle.clicked.connect((lambda: self.toggle_start(button_toggle)))

    layout.addWidget(button_toggle)

    fields_to_config: Callable[..., None] = (lambda:
      self.__viewmodel.write_config(
        line_edit_prefix.text(),
        ChatPlatform(combo_box_platform.currentText()),
        line_edit_token.text(),
        line_edit_username.text()))

    line_edit: QLineEdit
    line_edits: List[QLineEdit] = [
      line_edit_prefix,
      line_edit_token,
      line_edit_username
    ]
    for line_edit in line_edits:
      line_edit.textChanged.connect(fields_to_config)

    combo_box_platform.currentIndexChanged.connect(fields_to_config)

    window.setLayout(layout)
    return window

  # Override
  def initialize(self) -> None:
    self.__window.show()
    self.__app.exec()

  # Helper
  def toggle_start(self, button_toggle: QPushButton) -> None:
    print("Apparently clicked the start button???")
    if button_toggle.text() == "Start":
      self.__viewmodel.initialize()
      button_toggle.setText("Stop")
    elif button_toggle.text() == "Stop":
      self.__viewmodel.stop()
      button_toggle.setText("Start")
    else:
      print("This shouldn't be happening.")
