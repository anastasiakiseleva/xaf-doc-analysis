---
uid: DevExpress.Persistent.Base.CreatableItemAttribute.IsCreatableItem
name: IsCreatableItem
type: Property
summary: Specifies whether an item is added to the New Action's item list.
syntax:
  content: public bool IsCreatableItem { get; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true** if an item should be added to the **New** Action's item list; otherwise, **false**."
seealso: []
---
Having an item which corresponds to the required class in the **New** Action's item list allows end-users to create objects of this class. This is useful when the current View represents objects of another type.

The default value of this property is **true**.