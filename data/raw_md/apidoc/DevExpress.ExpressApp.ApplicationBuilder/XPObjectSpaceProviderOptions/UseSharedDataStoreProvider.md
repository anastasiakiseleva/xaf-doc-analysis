---
uid: DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions.UseSharedDataStoreProvider
name: UseSharedDataStoreProvider
type: Property
summary: Specifies whether to use a shared instance of `IXpoDataStoreProvider`. If `false`, XAF creates a new data store provider each time an object space provider is instantiated.
syntax:
  content: public bool UseSharedDataStoreProvider { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` to use a shared instance of `IXpoDataStoreProvider`. Otherwise, `false`.'
seealso: []
---
This option has no effect if you specify the @DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions.UseCustomDataStoreProvider(DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider) option and use a custom [data store provider](xref:DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.GetDataStoreProvider(System.String,System.Data.IDbConnection,System.Boolean)).