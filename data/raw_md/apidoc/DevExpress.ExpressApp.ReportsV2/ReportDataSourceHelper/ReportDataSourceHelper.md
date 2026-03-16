---
uid: DevExpress.ExpressApp.ReportsV2.ReportDataSourceHelper
name: ReportDataSourceHelper
type: Class
summary: Exposes helper methods and events used to manage reports and their data sources.
syntax:
  content: 'public class ReportDataSourceHelper : ReportDataSourceHelperBase'
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.ReportDataSourceHelper._members
  altText: ReportDataSourceHelper Members
---

> [!NOTE]
> This is a legacy class. Use the @DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper service instead.

Use the [ReportsModuleV2.ReportsDataSourceHelper](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportsDataSourceHelper) property to access this class' instance:

# [C#](#tab/tabid-csharp)

```csharp
IServiceProvider serviceProvider = /* XafApplication.ServiceProvider, IObjectSpace.ServiceProvider, etc...*/; 
IReportDataSourceHelper reportDataSourceHelper = serviceProvider.GetRequiredService<IReportDataSourceHelper>();
```

***

For more information about how to access services, refer to the following help section: [Access Services Using XafApplication](xref:404430#access-services-using-xafapplication).

Additional examples: 
* [](xref:113601)
* [](xref:114515)
