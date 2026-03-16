---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.#ctor(System.String,System.Data.IDbConnection,System.Boolean,System.Boolean)
name: XPObjectSpaceProvider(String, IDbConnection, Boolean, Boolean)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider class.
syntax:
  content: public XPObjectSpaceProvider(string connectionString, IDbConnection connection, bool threadSafe, bool useSeparateDataLayers = false)
  parameters:
  - id: connectionString
    type: System.String
    description: A string value that is the application's connection string.
  - id: connection
    type: System.Data.IDbConnection
    description: An [IDbConnection](https://learn.microsoft.com/en-us/dotnet/api/system.data.idbconnection) object that specifies the database connection.
  - id: threadSafe
    type: System.Boolean
    description: '**true**, if the [](xref:DevExpress.Xpo.ThreadSafeDataLayer) [Data Access Layer](xref:2123#data-access-layer) should be used; otherwise, **false**.'
  - id: useSeparateDataLayers
    type: System.Boolean
    defaultValue: "False"
    description: '**true**, if a separate [](xref:DevExpress.Xpo.SimpleDataLayer) [Data Access Layer](xref:2123#data-access-layer) should be created for each Object Space when the _threadSafe_ parameter is set to **false**; otherwise, **false**.'
seealso: []
---
