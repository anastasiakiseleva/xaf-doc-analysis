---
uid: DevExpress.ExpressApp.CloneObject.IModelClassCloneable.IsCloneable
name: IsCloneable
type: Property
summary: Indicates whether objects of the current class can be cloned.
syntax:
  content: bool IsCloneable { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, if objects of the current class can be cloned; otherwise, `false`.'
seealso: []
---
If this property is set to `true`, the **CloneObject** Action's Items collection contains an element of the current class type. In addition, the descendants of this class are added to the collection, if the `IsClonable` property is set to `true` for descendants.