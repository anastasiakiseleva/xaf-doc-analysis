---
uid: DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider.#ctor(DevExpress.ExpressApp.Security.ISelectDataSecurityProvider,DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider,System.Boolean,System.Boolean)
name: SecuredObjectSpaceProvider(ISelectDataSecurityProvider, IXpoDataStoreProvider, Boolean, Boolean)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider class with specified settings.
syntax:
  content: public SecuredObjectSpaceProvider(ISelectDataSecurityProvider selectDataSecurityProvider, IXpoDataStoreProvider dataStoreProvider, bool threadSafe, bool useSeparateDataLayers = false)
  parameters:
  - id: selectDataSecurityProvider
    type: DevExpress.ExpressApp.Security.ISelectDataSecurityProvider
    description: An object that implements the **ISelectDataSecurityProvider** interface (for example, a @DevExpress.ExpressApp.Security.SecurityStrategyComplex instance).
  - id: dataStoreProvider
    type: DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider
    description: An **IXpoDataStoreProvider** object.
  - id: threadSafe
    type: System.Boolean
    description: '**true**, if the [](xref:DevExpress.Xpo.ThreadSafeDataLayer) [Data Access Layer](xref:2123#data-access-layer) should be used; otherwise, **false**.'
  - id: useSeparateDataLayers
    type: System.Boolean
    defaultValue: "False"
    description: '**true**, if the [](xref:DevExpress.Xpo.SimpleDataLayer) [Data Access Layer](xref:2123#data-access-layer) should be created when the _threadSafe_ parameter is set to **false**; otherwise, **false**.'
seealso: []
---
