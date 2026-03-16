---
uid: DevExpress.ExpressApp.Xpo.XpoDataView
name: XpoDataView
type: Class
summary: A lightweight read-only list of data records (a data view) retrieved from a database without loading complete XPO objects. Can be queried much more quickly than a real objects collection.
syntax:
  content: 'public class XpoDataView : XafDataView'
seealso:
- linkId: DevExpress.ExpressApp.Xpo.XpoDataView._members
  altText: XpoDataView Members
---
This class is the XPO-specific implementation of [](xref:DevExpress.ExpressApp.XafDataView). Objects of the **XpoDataView** type are returned by the [IObjectSpace.CreateDataView](xref:DevExpress.ExpressApp.IObjectSpace.CreateDataView*) method when the Object Space is [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace). For details, refer to the base class description.