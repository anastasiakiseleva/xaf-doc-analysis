---
uid: DevExpress.ExpressApp.Office.InplaceDocumentCacheStorageBase
name: InplaceDocumentCacheStorageBase
type: Class
summary: Provides methods to manage the in-place [mail merge](xref:400006) documents cache.
syntax:
  content: public class InplaceDocumentCacheStorageBase
seealso:
- linkId: DevExpress.ExpressApp.Office.InplaceDocumentCacheStorageBase._members
  altText: InplaceDocumentCacheStorageBase Members
---
The in-place mail merge documents cache is updated automatically only after an application restarts (or after the browser page refreshes in ASP.NET Core Blazor applications). If you want to update the cache after you create or delete mail merge template objects, use the @DevExpress.ExpressApp.Office.InplaceDocumentCacheStorageBase.ClearCache method.

To access an instance of `InplaceDocumentCacheStorageBase`, use the static `ShowInDocumentController.InplaceDocumentCache` property.
