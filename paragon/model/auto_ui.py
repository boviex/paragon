from typing import Literal, Optional, Union, Dict, List

from pydantic import BaseModel


class AutoWidgetSpec(BaseModel):
    widget_id: Optional[str] = None


class FormSpec(AutoWidgetSpec):
    type: Literal["form"]
    ids: Optional[List[str]] = None
    no_margins: bool = False
    tooltips: Optional[Dict[str, str]] = None


class WidgetSpec(AutoWidgetSpec):
    type: Literal["widget"]
    id: str
    margins: Optional[List[int]] = None
    tooltip: Optional[str] = None


class LabelSpec(AutoWidgetSpec):
    type: Literal["label"]
    text: str


class SpinBoxMatrixSpec(AutoWidgetSpec):
    type: Literal["spin_box_matrix"]
    ids: List[str]
    columns: List[str]
    height: int
    column_counts: Optional[List[int]] = None
    signed: Dict[int, bool] = {}


class GroupBoxSpec(AutoWidgetSpec):
    type: Literal["group_box"]
    inner: "AnyTopLevelSpec"
    title: Optional[str] = None
    flat: bool = False
    height: Optional[int] = None


class VBoxSpec(AutoWidgetSpec):
    type: Literal["vbox"]
    inner: List["AnyTopLevelSpec"]
    spacing: int = 5
    spacer: bool = False


class HBoxSpec(AutoWidgetSpec):
    type: Literal["hbox"]
    inner: List["AnyTopLevelSpec"]
    height: Optional[int] = None
    stretch_index: Optional[int] = None
    spacing: int = 5


class ScrollSpec(AutoWidgetSpec):
    type: Literal["scroll"]
    inner: "AnyTopLevelSpec"


class CollapsibleSpec(AutoWidgetSpec):
    type: Literal["collapsible"]
    inner: "AnyTopLevelSpec"


class TabSpec(BaseModel):
    title: str
    inner: "AnyTopLevelSpec"


class TabsSpec(AutoWidgetSpec):
    type: Literal["tabs"]
    tabs: List[TabSpec]


class GridCellSpec(BaseModel):
    inner: "AnyTopLevelSpec"
    row: int = 0
    column: int = 0
    row_span: int = 1
    column_span: int = 1
    no_stretch: bool = False


class GridSpec(AutoWidgetSpec):
    type: Literal["grid"]
    cells: List[GridCellSpec]
    no_margins: bool = False


class PortraitViewerSpec(AutoWidgetSpec):
    type: Literal["portrait_viewer"]
    retrieve_mode: Literal["character", "class", "face_data"]


class MiniPortraitBoxSpec(AutoWidgetSpec):
    type: Literal["mini_portrait_box"]
    retrieve_mode: Literal["character", "class", "reference"]
    mode: str
    image_dim: int = 128
    image_height: Optional[int] = None
    box_dim: int = 140
    box_height: Optional[int] = None
    x_transform: int = 0
    y_transform: int = 0
    reference_type: Optional[Literal["character", "class"]] = None
    reference_field: Optional[str] = None


class RenderedPortraitBoxSpec(AutoWidgetSpec):
    type: Literal["rendered_portrait_box"]
    retrieve_mode: Literal["character", "class"]
    mode: str
    image_dim: int = 128
    image_height: Optional[int] = None
    box_dim: int = 140
    box_height: Optional[int] = None
    x_transform: int = 0
    y_transform: int = 0


class FE15SpriteViewerSpec(AutoWidgetSpec):
    type: Literal["fe15_sprite_viewer"]


class AwakeningSupportDialogueButtonSpec(AutoWidgetSpec):
    type: Literal["awakening_support_dialogue_button"]
    field_id: str


class FE14SupportWidgetSpec(AutoWidgetSpec):
    type: Literal["fe14_support_widget"]


class FE15SupportWidgetSpec(AutoWidgetSpec):
    type: Literal["fe15_support_widget"]


class FE15BaseConversationButtonSpec(AutoWidgetSpec):
    type: Literal["fe15_base_conversation_button"]


class DependentMessagesEntrySpec(BaseModel):
    path: str
    localized: bool
    key: str
    label: str
    param_count: int
    multiline: bool = False


class DependentMessagesWidgetSpec(AutoWidgetSpec):
    type: Literal["dependent_messages"]
    key_prefix: str
    lines: List[DependentMessagesEntrySpec]


class UISpec(BaseModel):
    top_level: Optional["AnyTopLevelSpec"] = None
    typename: str
    width: Optional[int] = None
    height: Optional[int] = None
    overrides: Dict[str, "AnyFieldSpec"] = {}


class StringLineEditSpec(AutoWidgetSpec):
    type: Literal["string_line_edit"]


class RegexValidatedStringLineEditSpec(AutoWidgetSpec):
    type: Literal["regex_validated_string_line_edit"]
    regex: str
    tooltip: Optional[str] = None


class FileInputSpec(AutoWidgetSpec):
    type: Literal["file_input"]
    dirs: List[str]
    optional: bool = True
    suffix: str = ""


class HexLineEditSpec(AutoWidgetSpec):
    type: Literal["hex_line_edit"]


class IntSpinBoxSpec(AutoWidgetSpec):
    type: Literal["int_spin_box"]
    hex: bool = False


class FloatSpinBoxSpec(AutoWidgetSpec):
    type: Literal["float_spin_box"]


class DataComboBoxSpec(AutoWidgetSpec):
    type: Literal["data_combo_box"]
    enum: Optional[str] = None
    items: Optional[Dict] = None
    target_type: Literal["int", "float", "string"] = "int"


class CheckBoxSpec(AutoWidgetSpec):
    type: Literal["check_box"]
    invert: bool = False


class MessageWidgetSpec(AutoWidgetSpec):
    type: Literal["message_widget"]


class ReferenceWidgetSpec(AutoWidgetSpec):
    type: Literal["reference_widget"]
    width: Optional[int] = None
    multi: bool = False


class ReadOnlyPointerWidgetSpec(AutoWidgetSpec):
    type: Literal["read_only_pointer_widget"]


class RecordWidgetSpec(AutoWidgetSpec):
    type: Literal["record_widget"]
    read_only: bool = False


class UnionWidgetSpec(AutoWidgetSpec):
    type: Literal["union_widget"]


class ListWidgetSpec(AutoWidgetSpec):
    type: Literal["list_widget"]
    no_margins: bool = False
    no_ids: bool = False
    no_copies: bool = False
    no_search: bool = False
    stretch_index: Literal[0, 1] = 1
    orientation: Literal["horizontal", "vertical"] = "horizontal"
    static_items: bool = False


class FE15EventEditorSpec(AutoWidgetSpec):
    type: Literal["fe15_event_editor"]


class BitflagsSpec(AutoWidgetSpec):
    type: Literal["bitflags_widget"]
    flags: List[str]


class ColorPickerSpec(AutoWidgetSpec):
    type: Literal["color_picker"]


class SpinBoxesSpec(AutoWidgetSpec):
    type: Literal["spin_boxes"]


class LabeledSpinBoxesSpec(AutoWidgetSpec):
    type: Literal["labeled_spin_boxes"]
    labels: List[str]


class SpriteFormSpec(AutoWidgetSpec):
    type: Literal["sprite_form"]
    width: int = 160
    multi: bool = False


class IconComboBoxSpec(AutoWidgetSpec):
    type: Literal["icon_combo_box"]
    icons: str
    base_index: int = 0


class IconDisplaySpec(AutoWidgetSpec):
    type: Literal["icon_display"]
    icons: str
    display_dim: int
    base_index: int = 0


class DerefWidgetSpec(AutoWidgetSpec):
    type: Literal["deref_widget"]


class SwappableSpec(AutoWidgetSpec):
    type: Literal["swappable"]
    widgets: List["AnyFieldSpec"]
    names: List[str]


def update_forward_refs():
    UISpec.update_forward_refs()
    FormSpec.update_forward_refs()
    WidgetSpec.update_forward_refs()
    LabelSpec.update_forward_refs()
    VBoxSpec.update_forward_refs()
    HBoxSpec.update_forward_refs()
    GroupBoxSpec.update_forward_refs()
    ScrollSpec.update_forward_refs()
    CollapsibleSpec.update_forward_refs()
    TabsSpec.update_forward_refs()
    TabSpec.update_forward_refs()
    GridCellSpec.update_forward_refs()
    GridSpec.update_forward_refs()
    SwappableSpec.update_forward_refs()


AnyTopLevelSpec = Union[
    FormSpec,
    WidgetSpec,
    LabelSpec,
    VBoxSpec,
    HBoxSpec,
    GroupBoxSpec,
    ScrollSpec,
    CollapsibleSpec,
    TabsSpec,
    GridSpec,
    SpinBoxMatrixSpec,
    PortraitViewerSpec,
    FE15SpriteViewerSpec,
    MiniPortraitBoxSpec,
    RenderedPortraitBoxSpec,
    AwakeningSupportDialogueButtonSpec,
    FE14SupportWidgetSpec,
    FE15SupportWidgetSpec,
    DependentMessagesWidgetSpec,
    FE15BaseConversationButtonSpec,
]

AnyFieldSpec = Union[
    StringLineEditSpec,
    RegexValidatedStringLineEditSpec,
    IntSpinBoxSpec,
    HexLineEditSpec,
    DataComboBoxSpec,
    FloatSpinBoxSpec,
    CheckBoxSpec,
    ListWidgetSpec,
    ReferenceWidgetSpec,
    ReadOnlyPointerWidgetSpec,
    MessageWidgetSpec,
    BitflagsSpec,
    SpinBoxesSpec,
    LabeledSpinBoxesSpec,
    ColorPickerSpec,
    RecordWidgetSpec,
    UnionWidgetSpec,
    IconComboBoxSpec,
    SpriteFormSpec,
    DerefWidgetSpec,
    IconDisplaySpec,
    SwappableSpec,
    FileInputSpec,
    FE15EventEditorSpec,
]
