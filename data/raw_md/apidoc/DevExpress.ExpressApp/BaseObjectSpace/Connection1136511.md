---
uid: DevExpress.ExpressApp.BaseObjectSpace.Connection
name: Connection
type: Property
summary: Gets the connection to the underlying data source.
syntax:
  content: public virtual IDbConnection Connection { get; }
  parameters: []
  return:
    type: System.Data.IDbConnection
    description: An **IDbConnection** object that is the connection to the underlying data source.
seealso: []
---
This property returns null. It must be overridden in the **BaseObjectSpace** class descendants.