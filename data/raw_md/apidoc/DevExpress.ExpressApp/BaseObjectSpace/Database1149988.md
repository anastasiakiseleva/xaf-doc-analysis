---
uid: DevExpress.ExpressApp.BaseObjectSpace.Database
name: Database
type: Property
summary: Gets the name of the database.
syntax:
  content: public virtual string Database { get; }
  parameters: []
  return:
    type: System.String
    description: A string that is the name of the database used when a connection is opened.
seealso: []
---
In [](xref:DevExpress.ExpressApp.BaseObjectSpace), this method always returns empty string, but this behavior is overridden in descendants (see [EFCoreObjectSpace.Database](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.Database) and [XPObjectSpace.Database](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Database)).