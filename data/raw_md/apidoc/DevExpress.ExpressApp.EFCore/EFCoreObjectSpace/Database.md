---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.Database
name: Database
type: Property
summary: Returns the name of a database that specified in the Object Space's [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext) if connection to this database is established.
syntax:
  content: public override string Database { get; }
  parameters: []
  return:
    type: System.String
    description: A name of a database that specified in the Object Space's [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext).
seealso: []
---
If the an SQLConnection is associated with the Object Space's [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext), the **Database** property returns the database name in the following format: \<_The name of an SQL Server instance_>.\<_The database name_>. Otherwise, this property returns only the database name. 