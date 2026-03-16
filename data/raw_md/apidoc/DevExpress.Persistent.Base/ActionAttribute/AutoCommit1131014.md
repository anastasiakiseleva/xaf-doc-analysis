---
uid: DevExpress.Persistent.Base.ActionAttribute.AutoCommit
name: AutoCommit
type: Property
summary: Specifies whether to commit the changes made to data when the **Action** attribute's target method is executed in ListView.
syntax:
  content: public bool AutoCommit { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if data changes are to be committed; otherwise, `false`.'
    description: '`true` if data changes are to be committed; otherwise, `false`.'
seealso: []
---
If the `AutoCommit` property is set to `true`, the Action Attribute ([](xref:DevExpress.Persistent.Base.ActionAttribute)) has the following behavior:

If the **AutoCommit** property is set to **false**, the data changes performed when executing the Action attribute's target method are not committed at once.

By default, this property is set to **true**.