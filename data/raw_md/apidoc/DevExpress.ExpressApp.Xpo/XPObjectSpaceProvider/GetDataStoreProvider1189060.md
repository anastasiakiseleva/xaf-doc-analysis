---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.GetDataStoreProvider(System.String,System.Data.IDbConnection,System.Boolean)
name: GetDataStoreProvider(String, IDbConnection, Boolean)
type: Method
summary: Returns the data store provider.
syntax:
  content: public static IXpoDataStoreProvider GetDataStoreProvider(string connectionString, IDbConnection connection, bool enablePoolingInConnectionString)
  parameters:
  - id: connectionString
    type: System.String
    description: A string containing the database connection settings.
  - id: connection
    type: System.Data.IDbConnection
    description: An [IDbConnection](https://learn.microsoft.com/en-us/dotnet/api/system.data.idbconnection) object specifying the database connection.
  - id: enablePoolingInConnectionString
    type: System.Boolean
    description: '**true**, if the connection pooling is enabled; otherwise, **false**.'
  return:
    type: DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider
    description: An **IXpoDataStoreProvider** object.
seealso: []
---
You can pass the object returned by the static **GetDataStoreProvider** method to the [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider) constructor when registering the Object Space Provider in the [XafApplication.CreateCustomObjectSpaceProvider](xref:DevExpress.ExpressApp.XafApplication.CreateCustomObjectSpaceProvider) event handler.

If you do not need to enable connection pooling, use another overload of this method that does not take the _enablePooling_ parameter.
