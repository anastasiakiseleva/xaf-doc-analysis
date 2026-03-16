---
uid: DevExpress.ExpressApp.XafDataViewRecord
name: XafDataViewRecord
type: Class
summary: An abstract class that implements @DevExpress.ExpressApp.IObjectRecord and represents a lightweight read-only data record (a data view) retrieved from a database without loading a complete business object.
syntax:
  content: 'public abstract class XafDataViewRecord : ICustomTypeDescriptor, IObjectRecord'
seealso:
- linkId: DevExpress.ExpressApp.XafDataViewRecord._members
  altText: XafDataViewRecord Members
---
The **XafDataViewRecord** objects are contained in the [](xref:DevExpress.ExpressApp.XafDataView) collection and returned by the [ListView.CurrentObject](xref:DevExpress.ExpressApp.ListView.CurrentObject) and [ListView.SelectedObjects](xref:DevExpress.ExpressApp.ListView.SelectedObjects) properties instead of original business objects when the List View operates in the [DataView](xref:118452) mode.