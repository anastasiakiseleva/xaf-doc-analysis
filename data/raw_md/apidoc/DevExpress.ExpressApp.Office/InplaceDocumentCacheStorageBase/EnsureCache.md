---
uid: DevExpress.ExpressApp.Office.InplaceDocumentCacheStorageBase.EnsureCache(System.Type,System.Func{DevExpress.ExpressApp.IObjectSpace})
name: EnsureCache(Type, Func<IObjectSpace>)
type: Method
summary: Checks whether the in-place document cache is initialized. If not, initializes the cache.
syntax:
  content: public virtual void EnsureCache(Type mailMergeDataType, Func<IObjectSpace> createObjectSpaceHandler)
  parameters:
  - id: mailMergeDataType
    type: System.Type
    description: The mail merge template type specified in the [OfficeModule.RichTextMailMergeDataType](xref:DevExpress.ExpressApp.Office.OfficeModule.RichTextMailMergeDataType) property.
  - id: createObjectSpaceHandler
    type: System.Func{DevExpress.ExpressApp.IObjectSpace}
    description: The delegate to create the [](xref:DevExpress.ExpressApp.IObjectSpace) instance.
seealso: []
---
