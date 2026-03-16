---
uid: DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider.#ctor(DevExpress.ExpressApp.Security.ISelectDataSecurityProvider,System.String,System.Data.IDbConnection,System.Boolean,System.Boolean)
name: SecuredObjectSpaceProvider(ISelectDataSecurityProvider, String, IDbConnection, Boolean, Boolean)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider class with specified settings.
syntax:
  content: public SecuredObjectSpaceProvider(ISelectDataSecurityProvider selectDataSecurityProvider, string databaseConnectionString, IDbConnection connection, bool threadSafe, bool useSeparateDataLayers = false)
  parameters:
  - id: selectDataSecurityProvider
    type: DevExpress.ExpressApp.Security.ISelectDataSecurityProvider
    description: An object that implements the **ISelectDataSecurityProvider** interface (for example, a @DevExpress.ExpressApp.Security.SecurityStrategyComplex instance).
  - id: databaseConnectionString
    type: System.String
    description: An application's connection string.
  - id: connection
    type: System.Data.IDbConnection
    description: An @System.Data.IDbConnection object that specifies the database connection.
  - id: threadSafe
    type: System.Boolean
    description: '**true**, if the [](xref:DevExpress.Xpo.ThreadSafeDataLayer) [Data Access Layer](xref:2123#data-access-layer) should be used; otherwise, **false**.'
  - id: useSeparateDataLayers
    type: System.Boolean
    defaultValue: "False"
    description: '**true**, if the [](xref:DevExpress.Xpo.SimpleDataLayer) [Data Access Layer](xref:2123#data-access-layer) should be created when the _threadSafe_ parameter is set to **false**; otherwise, **false**.'
seealso: []
---
