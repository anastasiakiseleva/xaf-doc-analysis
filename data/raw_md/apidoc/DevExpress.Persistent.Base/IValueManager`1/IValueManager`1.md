---
uid: DevExpress.Persistent.Base.IValueManager`1
name: IValueManager<ValueType>
type: Interface
summary: Declares members implemented by value managers.
syntax:
  content: 'public interface IValueManager<ValueType> : IValueManagerBase'
  typeParameters:
  - id: ValueType
    description: ''
seealso:
- linkId: DevExpress.Persistent.Base.IValueManager`1._members
  altText: IValueManager<ValueType> Members
---
Value managers are used to store data in memory on a per-user basis in a platform-independent way. The **IValueManager\<ValueType>** interface exposes the [IValueManager`1.Value](xref:DevExpress.Persistent.Base.IValueManager`1.Value) property, which represents the data stored by a value manager. For a detailed explanation of value managers, refer to the [](xref:DevExpress.Persistent.Base.ValueManager) class description.