---
uid: DevExpress.ExpressApp.Model.IModelLayoutManagerOptions.CaptionHorizontalAlignment
name: CaptionHorizontalAlignment
type: Property
summary: Specifies the default horizontal alignment of the layout group and item captions.
syntax:
  content: |-
    [DefaultValue(HorzAlignment.Default)]
    HorzAlignment CaptionHorizontalAlignment { get; set; }
  parameters: []
  return:
    type: DevExpress.Utils.HorzAlignment
    description: A [](xref:DevExpress.Utils.HorzAlignment) enumeration value specifying the default horizontal alignment of the layout group and item captions.
seealso:
- linkId: "112817"
---
This property is in effect for **XAF** Windows Forms applications only.

The following values are available:

* **Center** - centers captions.
* **Default** - places captions at the left.
* **Far** - places captions to the right.
* **Near** - places captions to the left.