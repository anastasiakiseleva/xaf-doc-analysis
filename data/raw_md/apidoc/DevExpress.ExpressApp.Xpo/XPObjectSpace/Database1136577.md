---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.Database
name: Database
type: Property
summary: Gets the name of the database used when a connection associated with the current Object Space's [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) is opened.
syntax:
  content: public override string Database { get; }
  parameters: []
  return:
    type: System.String
    description: A string that is the name of the database used when a connection is opened.
seealso: []
---
If the an SQLConnection is associated with the Object Space's [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session), the **Database** property returns the database name in the following format: \<_The name of an SQL Server instance_>.\<_The database name_>. Otherwise, only the database name is returned.