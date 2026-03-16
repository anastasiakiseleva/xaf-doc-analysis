---
uid: DevExpress.ExpressApp.CloneObject.CloneObjectViewController.AllowCloneWhenModified
name: AllowCloneWhenModified
type: Property
summary: Specifies whether to disable cloning when the current object has unsaved changes.
syntax:
  content: |-
    [DefaultValue(false)]
    public bool AllowCloneWhenModified { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` when cloning of modified object is allowed; otherwise - `false`.'
seealso: []
---
The [CloneObjectViewController.CloneObjectAction](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CloneObjectAction) Action is disabled when the current object has unsaved changes. The reason is that the cloning process works in a separate Object Space (see [](xref:DevExpress.ExpressApp.BaseObjectSpace)). To change this behavior set the `AllowCloneWhenModified` property to `true`.