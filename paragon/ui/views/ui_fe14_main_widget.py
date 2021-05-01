from PySide2 import QtGui
from PySide2.QtWidgets import QWidget, QPushButton, QGroupBox, QVBoxLayout, QGridLayout


class Ui_FE14MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.chapters_button = QPushButton("Chapters")
        self.characters_button = QPushButton("Characters")
        self.items_button = QPushButton("Items")
        self.classes_button = QPushButton("Classes")
        self.skills_button = QPushButton("Skills")
        self.forge_button = QPushButton("Forge")
        self.armies_button = QPushButton("Armies")
        self.weapon_bonuses_button = QPushButton("Weapon Bonuses")
        self.weapon_interactions_button = QPushButton("Weapon Interactions")
        self.weapon_ranks_button = QPushButton("Weapon Ranks")
        self.move_costs_button = QPushButton("Move Costs")

        core_box = QGroupBox("Core Data")
        core_layout = QVBoxLayout()
        core_layout.setAlignment(QtGui.Qt.AlignTop)
        core_layout.addWidget(self.chapters_button)
        core_layout.addWidget(self.characters_button)
        core_layout.addWidget(self.items_button)
        core_layout.addWidget(self.classes_button)
        core_layout.addWidget(self.skills_button)
        core_layout.addWidget(self.forge_button)
        core_layout.addWidget(self.armies_button)
        core_layout.addWidget(self.weapon_bonuses_button)
        core_layout.addWidget(self.weapon_interactions_button)
        core_layout.addWidget(self.weapon_ranks_button)
        core_layout.addWidget(self.move_costs_button)
        core_box.setLayout(core_layout)

        self.edit_dialogue_button = QPushButton("Edit Dialogue")
        self.configure_avatar_button = QPushButton("Configure Avatar")

        misc_box = QGroupBox("Misc.")
        misc_layout = QVBoxLayout()
        misc_layout.setAlignment(QtGui.Qt.AlignTop)
        misc_layout.addWidget(self.edit_dialogue_button)
        misc_layout.addWidget(self.configure_avatar_button)
        misc_box.setLayout(misc_layout)

        self.path_bonuses_button = QPushButton("Path Bonuses")
        self.visit_bonuses_button = QPushButton("Visit Bonuses")
        self.battle_bonuses_button = QPushButton("Battle Bonuses")

        bonuses_box = QGroupBox("Bonuses")
        bonuses_layout = QVBoxLayout()
        bonuses_layout.setAlignment(QtGui.Qt.AlignTop)
        bonuses_layout.addWidget(self.path_bonuses_button)
        bonuses_layout.addWidget(self.visit_bonuses_button)
        bonuses_layout.addWidget(self.battle_bonuses_button)
        bonuses_box.setLayout(bonuses_layout)

        self.accessories_button = QPushButton("Accessories")
        self.buildings_button = QPushButton("Buildings")
        self.init_buildings_button = QPushButton("Init Buildings")
        self.castle_recruitment_button = QPushButton("Castle Recruitment")
        self.butlers_button = QPushButton("Butlers")
        self.arena_combatants_low_button = QPushButton("Arena Combatants (Low)")
        self.arena_combatants_high_button = QPushButton("Arena Combatants (High)")

        my_castle_box = QGroupBox("My Castle")
        my_castle_layout = QVBoxLayout()
        my_castle_layout.setAlignment(QtGui.Qt.AlignTop)
        my_castle_layout.addWidget(self.accessories_button)
        my_castle_layout.addWidget(self.buildings_button)
        my_castle_layout.addWidget(self.init_buildings_button)
        my_castle_layout.addWidget(self.castle_recruitment_button)
        my_castle_layout.addWidget(self.butlers_button)
        my_castle_layout.addWidget(self.arena_combatants_low_button)
        my_castle_layout.addWidget(self.arena_combatants_high_button)
        my_castle_box.setLayout(my_castle_layout)

        self.field_button = QPushButton("Map Field / 3D Models")
        self.cameras_button = QPushButton("Cameras")
        self.effects_button = QPushButton("Effects")
        self.ground_attributes_button = QPushButton("Ground Attributes")
        self.portraits_button = QPushButton("Portraits")
        self.rom0_button = QPushButton("ROM0")
        self.rom1_button = QPushButton("ROM1")
        self.rom2_button = QPushButton("ROM2")
        self.rom3_button = QPushButton("ROM3")
        self.rom4_button = QPushButton("ROM4")
        self.rom5_button = QPushButton("ROM5")
        self.rom6_button = QPushButton("ROM6")

        assets_box = QGroupBox("Assets && Visuals")
        assets_layout = QVBoxLayout()
        assets_layout.setAlignment(QtGui.Qt.AlignTop)
        assets_layout.addWidget(self.field_button)
        assets_layout.addWidget(self.portraits_button)
        assets_layout.addWidget(self.rom0_button)
        assets_layout.addWidget(self.rom1_button)
        assets_layout.addWidget(self.rom2_button)
        assets_layout.addWidget(self.rom3_button)
        assets_layout.addWidget(self.rom4_button)
        assets_layout.addWidget(self.rom5_button)
        assets_layout.addWidget(self.rom6_button)
        assets_layout.addWidget(self.effects_button)
        assets_layout.addWidget(self.ground_attributes_button)
        assets_layout.addWidget(self.cameras_button)
        assets_box.setLayout(assets_layout)

        self.sound_sets_button = QPushButton("Sound Sets")
        self.multi_sound_sets_button = QPushButton("Multi Sounds")
        self.sound_parameters_button = QPushButton("Sound Parameters")
        self.support_music_button = QPushButton("Support Music")

        audio_box = QGroupBox("Audio")
        audio_layout = QVBoxLayout()
        audio_layout.setAlignment(QtGui.Qt.AlignTop)
        audio_layout.addWidget(self.sound_sets_button)
        audio_layout.addWidget(self.multi_sound_sets_button)
        audio_layout.addWidget(self.sound_parameters_button)
        audio_layout.addWidget(self.support_music_button)
        audio_box.setLayout(audio_layout)

        layout = QGridLayout()
        layout.addWidget(core_box, 0, 0)
        layout.addWidget(misc_box, 1, 0)
        layout.addWidget(assets_box, 0, 1)
        layout.addWidget(audio_box, 1, 1)
        layout.addWidget(my_castle_box, 0, 2)
        layout.addWidget(bonuses_box, 1, 2)

        self.setLayout(layout)
