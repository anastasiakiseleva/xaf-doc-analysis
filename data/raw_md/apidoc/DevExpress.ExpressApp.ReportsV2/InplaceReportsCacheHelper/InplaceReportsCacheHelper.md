---
uid: DevExpress.ExpressApp.ReportsV2.InplaceReportsCacheHelper
name: InplaceReportsCacheHelper
type: Class
summary: Provides helper methods used to manage [in-place reports](xref:113602) cache.
syntax:
  content: 'public class InplaceReportsCacheHelper : InplaceReportCacheHelperService'
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.InplaceReportsCacheHelper._members
  altText: InplaceReportsCacheHelper Members
---
The in-place reports cache is created when the [InplaceReportsCacheHelper.GetReportDataInfoList](xref:DevExpress.ExpressApp.ReportsV2.InplaceReportCacheHelperService.GetReportDataInfoList(System.Type)) method is called for the first time. The cache is not updated automatically when in-place report data objects are created or deleted. To reset the cache manually, call the [InplaceReportsCacheHelper.ClearInplaceReportsCache](xref:DevExpress.ExpressApp.ReportsV2.InplaceReportCacheHelperService.ClearInplaceReportsCache) method.

To access an instance of **InplaceReportsCacheHelper**, use the [ReportsModuleV2.InplaceReportsCacheHelper](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.InplaceReportsCacheHelper) property.