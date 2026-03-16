---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.#ctor(DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider,System.Boolean,System.Boolean)
name: XPObjectSpaceProvider(IXpoDataStoreProvider, Boolean, Boolean)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider class.
syntax:
  content: public XPObjectSpaceProvider(IXpoDataStoreProvider dataStoreProvider, bool threadSafe, bool useSeparateDataLayers = false)
  parameters:
  - id: dataStoreProvider
    type: DevExpress.ExpressApp.Xpo.IXpoDataStoreProvider
    description: An **IXpoDataStoreProvider** object.
  - id: threadSafe
    type: System.Boolean
    description: '**true**, if the [](xref:DevExpress.Xpo.ThreadSafeDataLayer) [Data Access Layer](xref:2123#data-access-layer) should be used; otherwise, **false**.'
  - id: useSeparateDataLayers
    type: System.Boolean
    defaultValue: "False"
    description: '**true**, if a separate [](xref:DevExpress.Xpo.SimpleDataLayer) [Data Access Layer](xref:2123#data-access-layer) should be created for each Object Space when the _threadSafe_ parameter is set to **false**; otherwise, **false**.'
seealso: []
---
