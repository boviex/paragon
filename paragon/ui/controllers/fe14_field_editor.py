import os

from paragon.ui.auto_widget_generator import AutoWidgetGenerator

from paragon.ui.views.ui_fe14_field_editor import Ui_FE14FieldEditor


class FE14FieldEditor(Ui_FE14FieldEditor):
    def __init__(self, ms, gs, key):
        super().__init__()

        self.setWindowTitle(f"Paragon - Field Editor ({key})")

        self.gd = gs.data
        self.config_rid = self._get_field_config_rid(key)
        self.refer_rid = self.gd.multi_open("field_references", key)
        self.files_rid = self.gd.multi_open("field_files", key)
        self.parts_rid = self.gd.multi_open("field_parts", key)

        gen = AutoWidgetGenerator(ms, gs)
        self.config_ui = gen.generate_for_type("FieldConfig")
        self.config_ui.set_target(self.config_rid)
        self.refer_ui = gen.generate_for_type("__table_inject__FieldReferData")
        self.refer_ui.set_target(self.refer_rid)
        self.files_ui = gen.generate_for_type("__table_inject__FieldFileListEntry")
        self.files_ui.set_target(self.files_rid)
        self.parts_ui = gen.generate_for_type("__table_inject__FieldPart")
        self.parts_ui.set_target(self.parts_rid)

        self.tabs.addTab(self.refer_ui, "Refer")
        self.tabs.addTab(self.files_ui, "Files")
        self.tabs.addTab(self.parts_ui, "Parts")
        self.tabs.addTab(self.config_ui, "Config")

    def _get_field_config_rid(self, key):
        basename = os.path.basename(key)
        if basename.endswith(".lz"):
            basename = basename[:-3]
        path = os.path.join("GameData", "Field", basename)
        if not self.gd.file_exists(path, False):
            return None
        try:
            return self.gd.multi_open("field_config", path)
        except:
            return None
