---
uid: DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions.EnablePoolingInConnectionString
name: EnablePoolingInConnectionString
type: Property
summary: Specifies whether XPO Data Store Pooling is enabled.
syntax:
  content: public bool EnablePoolingInConnectionString { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, if the connection pooling is enabled; otherwise, `false`.'
seealso: []
---
When XAF creates a Data Store, it checks this property value. If `true`, XAF uses the @DevExpress.Xpo.XpoDefault.GetConnectionPoolString(System.String) method to add pooling parameters to the initial connection string.

This option has no effect if you specify the @DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions.UseCustomDataStoreProvider(DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider) option and use a custom [data store provider](xref:DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.GetDataStoreProvider(System.String,System.Data.IDbConnection,System.Boolean)).