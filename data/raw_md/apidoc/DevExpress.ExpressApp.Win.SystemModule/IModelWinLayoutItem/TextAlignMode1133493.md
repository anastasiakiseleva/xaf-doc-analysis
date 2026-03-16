---
uid: DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutItem.TextAlignMode
name: TextAlignMode
type: Property
summary: Specifies the alignment settings of the layout item's control.
syntax:
  content: |-
    [DefaultValue(TextAlignModeItem.UseParentOptions)]
    TextAlignModeItem TextAlignMode { get; set; }
  parameters: []
  return:
    type: DevExpress.XtraLayout.TextAlignModeItem
    description: A **TextAlignModeItem** enumeration value specifying the alignment settings of the layout item's control.
seealso:
- linkId: "112817"
---
This property is considered in **XAF** Windows Forms applications.

The following values are available:

* **AutoSize** - the auto-size feature is applied to the current layout item. The item's text region is automatically resized to the minimum width that allows the text to be displayed in its entirety.
* **CustomSize** - enables custom size mode, in which the size of the layout item's text region must be specified manually using the [BaseLayoutItem.TextSize](xref:DevExpress.XtraLayout.BaseLayoutItem.TextSize) property.
* **UseParentOptions** - alignment settings are determined by the item's group.