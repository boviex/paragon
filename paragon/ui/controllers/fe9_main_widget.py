from paragon.ui.controllers.fe9_dialogue_editor import FE9DialogueEditor
from paragon.ui.controllers.fe9_script_editor import FE9ScriptEditor
from paragon.ui.controllers.layered_dir_editor import LayeredDirEditor
from paragon.ui.views.ui_fe9_main_widget import Ui_FE9MainWidget


class FE9MainWidget(Ui_FE9MainWidget):
    def __init__(self, ms, gs, main_window):
        super().__init__()
        self.gs = gs
        self.ms = ms
        self.main_window = main_window

        self.script_editor = None
        self.dialogue_editor = None

        self.chapters_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("chapters")
        )
        self.characters_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("characters")
        )
        self.classes_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("jobs")
        )
        self.items_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("items")
        )
        self.skills_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("skills")
        )
        self.armies_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("groups")
        )
        self.tiles_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("tiles")
        )
        self.supports_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("main_support_table")
        )
        self.no_battle_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("no_battle")
        )
        self.portraits_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("facedata")
        )
        self.conversations_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("base_conversations")
        )
        self.yell_fe8_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("fe8_yell")
        )
        self.yell_mini_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("yell_mini")
        )
        self.epilogue_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("epilogue")
        )
        self.weapon_interactions_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("weapon_interactions")
        )
        self.effects_button.clicked.connect(
            lambda: self.main_window.open_node_by_id("effect_data")
        )
        self.scripts_button.clicked.connect(self._on_scripts)
        self.dialogue_button.clicked.connect(self._on_dialogue)

    def on_close(self):
        if self.script_editor:
            self.script_editor.close()
        if self.dialogue_editor:
            self.dialogue_editor.close()

    def _on_scripts(self):
        if not self.script_editor:
            self.script_editor = FE9ScriptEditor(self.ms, self.gs)
        self.script_editor.show()

    def _on_dialogue(self):
        if not self.dialogue_editor:
            self.dialogue_editor = FE9DialogueEditor(self.ms, self.gs)
        self.dialogue_editor.show()
