---
uid: DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase
name: ReportDataSourceHelperBase
type: Class
summary: Implements API used to manage reports and their data sources.
syntax:
  content: 'public abstract class ReportDataSourceHelperBase : IReportDataSourceHelper'
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase._members
  altText: ReportDataSourceHelperBase Members
- linkId: DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper
---

Use [Dependency Injection](xref:404364) to access this service:

# [C#](#tab/tabid-csharp)

```csharp
// Use Dependency Injection to access the IServiceProvider.
var signInManager = serviceProvider.GetRequiredService<SignInManager>();
IReportDataSourceHelper reportDataSourceHelper = serviceProvider.GetRequiredService<IReportDataSourceHelper>();
```

***

For more information about how to access services, refer to the following help section: [Access Services Using XafApplication](xref:404430#access-services-using-xafapplication).

Additional examples: 
* [](xref:113601)
* [](xref:114515)