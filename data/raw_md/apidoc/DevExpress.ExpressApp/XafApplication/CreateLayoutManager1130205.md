---
uid: DevExpress.ExpressApp.XafApplication.CreateLayoutManager(System.Boolean)
name: CreateLayoutManager(Boolean)
type: Method
summary: Creates a Layout Manager.
syntax:
  content: public LayoutManager CreateLayoutManager(bool simple)
  parameters:
  - id: simple
    type: System.Boolean
    description: A Boolean value that indicates whether a simple Layout Manager must be created.
  return:
    type: DevExpress.ExpressApp.Layout.LayoutManager
    description: A `LayoutManager` object.
seealso: []
---
This method returns an instance of a platform-specific layout manager. Override the `CreateLayoutManager` method to use a custom Layout Manager type.

You may need to use this method, if your control contains other controls that must be arranged by a Layout Manager.