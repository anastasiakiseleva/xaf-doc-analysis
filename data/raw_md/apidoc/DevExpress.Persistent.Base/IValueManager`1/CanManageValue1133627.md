---
uid: DevExpress.Persistent.Base.IValueManager`1.CanManageValue
name: CanManageValue
type: Property
summary: Indicates whether the value manager can currently be used.
syntax:
  content: bool CanManageValue { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, if the value manager can currently be used; otherwise, `false`.'
seealso: []
---
Check this property to make sure the `ValueManager` can currently manage values. This property returns `false` if the `ValueManager`'s storage is not initialized or is inaccessible from the current place.
<!--TODO: rewrite for a different example --!>