---
uid: DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutGroup.TextAlignMode
name: TextAlignMode
type: Property
summary: Specifies the alignment settings of the controls displayed in the current group.
syntax:
  content: |-
    [DefaultValue(TextAlignModeGroup.UseParentOptions)]
    TextAlignModeGroup TextAlignMode { get; set; }
  parameters: []
  return:
    type: DevExpress.XtraLayout.TextAlignModeGroup
    description: A **TextAlignModeGroup** enumeration value specifying the alignment settings of the controls displayed in the current group.
seealso:
- linkId: "112817"
---
This property is considered in **XAF** Windows Forms applications.

The following values are available:

* **AlignLocal** - controls displayed within the current group are automatically aligned independently from other groups.
* **AutoSize** - the auto-size feature is applied to the layout items of the current group. The text regions of the layout items are automatically resized to the minimum width that allows the text to be displayed in its entirety.
* **CustomSize** - enables custom size mode, in which the size of the text regions of the group's layout items must be specified manually using the [BaseLayoutItem.TextSize](xref:DevExpress.XtraLayout.BaseLayoutItem.TextSize) property.
* **UseParentOptions** - alignment settings are determined by the group's parent.