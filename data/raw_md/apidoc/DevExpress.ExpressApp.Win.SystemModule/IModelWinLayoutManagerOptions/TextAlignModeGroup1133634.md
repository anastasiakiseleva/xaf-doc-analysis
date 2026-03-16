---
uid: DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutManagerOptions.TextAlignModeGroup
name: TextAlignModeGroup
type: Property
summary: Specifies the default alignment settings of the controls displayed in layout groups.
syntax:
  content: |-
    [DefaultValue(TextAlignModeGroup.UseParentOptions)]
    TextAlignModeGroup TextAlignModeGroup { get; set; }
  parameters: []
  return:
    type: DevExpress.XtraLayout.TextAlignModeGroup
    description: An integer value specifying the default alignment settings of the controls displayed in layout groups.
seealso:
- linkId: "112817"
---
This property is in effect for **XAF** Windows Forms applications only.

The following values are available:

* **AlignLocal** - controls displayed within a group are automatically aligned independently from other groups.
* **AutoSize** - the auto-size feature is applied to the layout items of a group. The text regions of the layout items are automatically resized to the minimum width that allows the text to be displayed in its entirety.
* **CustomSize** - enables custom size mode, in which the size of the text regions of a group's layout items must be specified manually using the [BaseLayoutItem.TextSize](xref:DevExpress.XtraLayout.BaseLayoutItem.TextSize) property.
* **UseParentOptions** - alignment settings are determined by a group's parent.