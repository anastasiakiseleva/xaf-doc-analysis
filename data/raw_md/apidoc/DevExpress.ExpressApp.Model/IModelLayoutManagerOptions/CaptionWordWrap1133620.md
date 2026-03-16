---
uid: DevExpress.ExpressApp.Model.IModelLayoutManagerOptions.CaptionWordWrap
name: CaptionWordWrap
type: Property
summary: Specifies the default layout group and item captions wrapping mode.
syntax:
  content: |-
    [DefaultValue(WordWrap.Default)]
    WordWrap CaptionWordWrap { get; set; }
  parameters: []
  return:
    type: DevExpress.Utils.WordWrap
    description: A **DevExpress.Utils.WordWrap** enumeration value specifying the default layout group and item captions wrapping mode.
seealso:
- linkId: "112817"
---
This property is in effect for **XAF** Windows Forms applications only.

The following values are available:

* **Default** - the actual wrapping mode is determined by a control.
* **NoWrap** - the word wrapping feature is disabled.
* **Wrap** - the word wrapping feature is enabled.