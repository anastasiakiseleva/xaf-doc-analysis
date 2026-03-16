---
uid: DevExpress.ExpressApp.Office.Win.InplaceDocumentCacheStorage
name: InplaceDocumentCacheStorage
type: Class
summary: Provides methods used to manage the in-place [mail merge](xref:400006) documents cache.
syntax:
  content: 'public class InplaceDocumentCacheStorage : InplaceDocumentCacheStorageBase'
seealso:
- linkId: DevExpress.ExpressApp.Office.Win.InplaceDocumentCacheStorage._members
  altText: InplaceDocumentCacheStorage Members
---
The in-place mail merge documents cache is updated automatically only after application restart. If you want to update the cache manually after you created or deleted mail merge template objects, use the @DevExpress.ExpressApp.Office.InplaceDocumentCacheStorageBase.ClearCache method.

To access an instance of **InplaceDocumentCacheStorage**, use the static **ShowInDocumentController.InplaceDocumentCache** property.
