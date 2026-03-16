---
uid: DevExpress.ExpressApp.ModelCacheManager
name: ModelCacheManager
type: Class
summary: Manages the [Application Model](xref:2596) cache designed to improve the startup speed and performance.
syntax:
  content: public class ModelCacheManager
seealso:
- linkId: DevExpress.ExpressApp.ModelCacheManager._members
  altText: ModelCacheManager Members
---
You can customize the **ModelCacheManager** behavior using the following _static_ fields.

| Field | Description |
|---|---|
| [ModelCacheManager.UseMultithreadedLoading](xref:DevExpress.ExpressApp.ModelCacheManager.UseMultithreadedLoading) | Enables multi-thread loading of the Application Model cache. |
| [ModelCacheManager.SkipEmptyNodes](xref:DevExpress.ExpressApp.ModelCacheManager.SkipEmptyNodes) | Enables skipping empty nodes when creating and loading the Application Model cache. |

Setting both these fields to **true** may reduce the application startup time when the Application Model cache is enabled (see [XafApplication.EnableModelCache](xref:DevExpress.ExpressApp.XafApplication.EnableModelCache)). As these fields are _static_, you can access them from any code location that is executed before the Application Model cache is accessed:

[!include[CodeLocationsBeforeLogon](~/templates/codelocationsbeforelogon111430.md)]

> [!IMPORTANT]
> If **SkipEmptyNodes** is enabled and there is a custom [Node Generator or Generator Updater](xref:112810) which can create empty nodes, these nodes will not be cached and will not be restored from cache. You will need to override the **UpdateCachedNodes** method of your **Node Generator**, or **UpdateCachedNode** of your **Generator Updater** to recreate these empty nodes when the Application Model is being loaded from the cache.

For deeper customizations, inherit this class, handle the [XafApplication.CreateCustomModelCacheManager](xref:DevExpress.ExpressApp.XafApplication.CreateCustomModelCacheManager) event and pass your custom **ModelCacheManager** descendant to the [CreateCustomModelCacheManagerEventArgs.ModelCacheManager](xref:DevExpress.ExpressApp.CreateCustomModelCacheManagerEventArgs.ModelCacheManager) parameter. An example is provided in the [XafApplication.CreateCustomModelCacheManager](xref:DevExpress.ExpressApp.XafApplication.CreateCustomModelCacheManager) event description.