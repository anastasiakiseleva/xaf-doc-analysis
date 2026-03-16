---
uid: DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions.ConnectionString
name: ConnectionString
type: Property
summary: Specifies the connection string used by the Object Space Provider's data store.
syntax:
  content: public string ConnectionString { get; set; }
  parameters: []
  return:
    type: System.String
    description: A connection string used by the Object Space Provider's data layer.
seealso: []
---
This option has no effect if you specify the @DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions.UseCustomDataStoreProvider(DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider) option and use a custom [data store provider](xref:DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.GetDataStoreProvider(System.String,System.Data.IDbConnection,System.Boolean)).