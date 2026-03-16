---
uid: DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutManagerOptions.ItemToTabBorderDistance
name: ItemToTabBorderDistance
type: Property
summary: Specifies the indents between a tabbed group's edges and Layout Items contained in the group's tabbed pages.
syntax:
  content: |-
    [DefaultValue(2)]
    int ItemToTabBorderDistance { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying the indents between a tabbed group's edges and Layout Items contained in the group's tabbed pages.
seealso:
- linkId: "112817"
---
This property is considered for the tabbed pages that contain a single Layout Item. If a tabbed page contains several Layout Items, this property has no effect.

This property is in effect for **XAF** Windows Forms applications only.