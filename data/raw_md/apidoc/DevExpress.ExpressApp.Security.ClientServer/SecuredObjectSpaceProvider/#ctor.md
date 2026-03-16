---
uid: DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider.#ctor(DevExpress.ExpressApp.Security.ISelectDataSecurityProvider,DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider,DevExpress.ExpressApp.DC.ITypesInfo,DevExpress.ExpressApp.DC.Xpo.XpoTypeInfoSource,System.Boolean,System.Boolean)
name: SecuredObjectSpaceProvider(ISelectDataSecurityProvider, IXpoDataStoreProvider, ITypesInfo, XpoTypeInfoSource, Boolean, Boolean)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider class with specified settings.
syntax:
  content: public SecuredObjectSpaceProvider(ISelectDataSecurityProvider selectDataSecurityProvider, IXpoDataStoreProvider dataStoreProvider, ITypesInfo typesInfo, XpoTypeInfoSource xpoTypeInfoSource, bool threadSafe, bool useSeparateDataLayers = false)
  parameters:
  - id: selectDataSecurityProvider
    type: DevExpress.ExpressApp.Security.ISelectDataSecurityProvider
    description: An object that implements the **ISelectDataSecurityProvider** interface (for example, a @DevExpress.ExpressApp.Security.SecurityStrategyComplex instance).
  - id: dataStoreProvider
    type: DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider
    description: An **IXpoDataStoreProvider** object.
  - id: typesInfo
    type: DevExpress.ExpressApp.DC.ITypesInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypesInfo) object that provides access to XAF-related information on business classes.
  - id: xpoTypeInfoSource
    type: DevExpress.ExpressApp.DC.Xpo.XpoTypeInfoSource
    description: A source of XPO-related information on business classes.
  - id: threadSafe
    type: System.Boolean
    description: '**true**, if the [](xref:DevExpress.Xpo.ThreadSafeDataLayer) [Data Access Layer](xref:2123#data-access-layer) should be used; otherwise, **false**.'
  - id: useSeparateDataLayers
    type: System.Boolean
    defaultValue: "False"
    description: '**true**, if the [](xref:DevExpress.Xpo.SimpleDataLayer) [Data Access Layer](xref:2123#data-access-layer) should be created when the _threadSafe_ parameter is set to **false**; otherwise, **false**.'
seealso: []
---
