---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.GetDataStoreProvider(System.String,System.Data.IDbConnection)
name: GetDataStoreProvider(String, IDbConnection)
type: Method
summary: Returns the data store provider.
syntax:
  content: public static IXpoDataStoreProvider GetDataStoreProvider(string connectionString, IDbConnection connection)
  parameters:
  - id: connectionString
    type: System.String
    description: A string containing the database connection settings.
  - id: connection
    type: System.Data.IDbConnection
    description: An [IDbConnection](https://learn.microsoft.com/en-us/dotnet/api/system.data.idbconnection) object specifying the database connection.
  return:
    type: DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider
    description: An **IXpoDataStoreProvider** object.
seealso: []
---
You can pass the object returned by the static **GetDataStoreProvider** method to the [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider) constructor when registering the Object Space Provider in the [XafApplication.CreateCustomObjectSpaceProvider](xref:DevExpress.ExpressApp.XafApplication.CreateCustomObjectSpaceProvider) event handler.

If you need to enable connection pooling, use another overload of this method that takes the _enablePooling_ parameter.
