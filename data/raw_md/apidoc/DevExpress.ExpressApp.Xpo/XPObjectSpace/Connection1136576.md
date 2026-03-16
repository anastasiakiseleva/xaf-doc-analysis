---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.Connection
name: Connection
type: Property
summary: Gets the connection to the underlying data source.
syntax:
  content: public override IDbConnection Connection { get; }
  parameters: []
  return:
    type: System.Data.IDbConnection
    description: An **IDbConnection** object that is the connection to the underlying data source.
seealso: []
---
This property returns the connection used by the DataLayer of the current Object Space's [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) (See [Session.DataLayer](xref:DevExpress.Xpo.Session.DataLayer) property).