---
uid: DevExpress.Persistent.Base.IValueManagerBase
name: IValueManagerBase
type: Interface
summary: Serves as the base interface, from which the [](xref:DevExpress.Persistent.Base.IValueManager`1) interface is derived.
syntax:
  content: public interface IValueManagerBase
seealso:
- linkId: DevExpress.Persistent.Base.IValueManagerBase._members
  altText: IValueManagerBase Members
---
The **IValueManagerBase** interface declares a single [IValueManagerBase.Clear](xref:DevExpress.Persistent.Base.IValueManagerBase.Clear) method, which when implemented by a value manager, sets the [IValueManager`1.Value](xref:DevExpress.Persistent.Base.IValueManager`1.Value) to the default value of the type parameter. The default value is `null` for reference types, and zero for value types.