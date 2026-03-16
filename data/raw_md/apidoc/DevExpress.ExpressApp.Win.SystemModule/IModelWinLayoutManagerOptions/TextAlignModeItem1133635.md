---
uid: DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutManagerOptions.TextAlignModeItem
name: TextAlignModeItem
type: Property
summary: Specifies the default alignment settings of layout items' controls.
syntax:
  content: |-
    [DefaultValue(TextAlignModeItem.UseParentOptions)]
    TextAlignModeItem TextAlignModeItem { get; set; }
  parameters: []
  return:
    type: DevExpress.XtraLayout.TextAlignModeItem
    description: An integer value specifying the default alignment settings of layout items' controls.
seealso:
- linkId: "112817"
---
This property is in effect for **XAF** Windows Forms applications only.

The following values are available:

* **AutoSize** - the auto-size feature is applied to a layout item. The item's text region is automatically resized to the minimum width that allows the text to be displayed in its entirety.
* **CustomSize** - enables custom size mode, in which the size of a layout item's text region must be specified manually using the [BaseLayoutItem.TextSize](xref:DevExpress.XtraLayout.BaseLayoutItem.TextSize) property.
* **UseParentOptions** - alignment settings are determined by an item's group.