---
uid: DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions.UseCustomDataStoreProvider(DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider)
name: UseCustomDataStoreProvider(IXpoDataStoreProvider)
type: Method
summary: Allows you to use a custom `IXpoDataStoreProvider`.
syntax:
  content: public void UseCustomDataStoreProvider(IXpoDataStoreProvider dataStoreProvider)
  parameters:
  - id: dataStoreProvider
    type: DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider
    description: A data store provider.
seealso:
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/k18356/how-to-use-xpo-data-layer-caching-in-xaf
  altText: 'How to use XPO data layer caching in XAF'
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/k18167/troubleshooting-how-to-resolve-the-entering-the-getobjectsnonreenterant-state-error
  altText: 'Troubleshooting - How to resolve the "Entering the GetObjectsNonReenterant state..." error'
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/q439032/how-do-i-map-persistent-classes-to-another-schema-e-g-other-than-the-default-dbo-in-ms
  altText: 'How do I map persistent classes to another schema, e.g. other than the default "dbo" in MS SQL Server?'
---
If you call this method, @DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions.ConnectionString and @DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions.UseSharedDataStoreProvider have no effect.