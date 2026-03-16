---
uid: DevExpress.ExpressApp.IObjectSpace.Database
name: Database
type: Property
summary: Gets the name of the database used when a connection associated with the current Object Space's container for in-memory objects is opened.
syntax:
  content: string Database { get; }
  parameters: []
  return:
    type: System.String
    description: A string that is the name of the database used when a connection is opened.
seealso:
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.Database
  altText: EFCoreObjectSpace.Database
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.Database
  altText: XPObjectSpace.Database
---
By the container for in-memory objects, we mean a Session in the case of an XPObjectSpace (see [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session)) or an Object Context in the case of an EFCoreObjectSpace (see [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext))