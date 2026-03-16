---
uid: DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper
name: IReportDataSourceHelper
type: Interface
summary: Defines API used to manage reports and their data sources.
syntax:
  content: public interface IReportDataSourceHelper
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper._members
  altText: IReportDataSourceHelper Members
- linkId: DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase
---

Use [Dependency Injection](xref:404364) to access the `IReportDataSourceHelper` service:

# [C#](#tab/tabid-csharp)

```csharp
// Use Dependency Injection to access the IServiceProvider.
IReportDataSourceHelper reportDataSourceHelper = serviceProvider.GetRequiredService<IReportDataSourceHelper>();
```

***

For more information about how to access services, refer to the following help section: [Access Services Using XafApplication](xref:404430#access-services-using-xafapplication).

Additional examples: 
* [](xref:113601)
* [](xref:114515)