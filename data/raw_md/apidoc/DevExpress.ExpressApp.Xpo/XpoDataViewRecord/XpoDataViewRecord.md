---
uid: DevExpress.ExpressApp.Xpo.XpoDataViewRecord
name: XpoDataViewRecord
type: Class
summary: A XPO-oriented class that represents a lightweight read-only data record (a data view) retrieved from a database without loading a complete business object.
syntax:
  content: 'public class XpoDataViewRecord : XafDataViewRecord'
seealso:
- linkId: DevExpress.ExpressApp.Xpo.XpoDataViewRecord._members
  altText: XpoDataViewRecord Members
---
The **XpoDataViewRecord** objects are contained in the [](xref:DevExpress.ExpressApp.Xpo.XpoDataView) collection and returned by the [ListView.CurrentObject](xref:DevExpress.ExpressApp.ListView.CurrentObject) and [ListView.SelectedObjects](xref:DevExpress.ExpressApp.ListView.SelectedObjects) properties instead of original business objects when the List View operates in the [DataView](xref:118452) mode.