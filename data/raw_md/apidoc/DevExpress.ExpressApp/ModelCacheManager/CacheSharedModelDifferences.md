---
uid: DevExpress.ExpressApp.ModelCacheManager.CacheSharedModelDifferences
name: CacheSharedModelDifferences
type: Field
summary: Specifies if the [shared (administrator's) Model Differences](xref:403527) are cached. To use this option, set the @DevExpress.ExpressApp.XafApplication.EnableModelCache property to **true**.
syntax:
  content: public static bool CacheSharedModelDifferences
  return:
    type: System.Boolean
    description: '**true** if shared Model Differences is cashed; otherwise, **false**.'
seealso: []
---
Note that the _Model.Cache.xafml_ file is not updated automatically after the shared Model Differences are changed. Remove this file and XAF recreates it with updated Model Differences on the application start.