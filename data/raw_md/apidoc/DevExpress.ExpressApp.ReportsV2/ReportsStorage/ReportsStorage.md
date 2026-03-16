---
uid: DevExpress.ExpressApp.ReportsV2.ReportsStorage
name: ReportsStorage
type: Class
summary: Manages loading and persisting reports in the [Reports V2 Module](xref:113591).
syntax:
  content: 'public class ReportsStorage : ReportStorageBase'
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.ReportsStorage._members
  altText: ReportsStorage Members
---
The `ReportsStorage` class is a [Custom Report Storage](xref:10001). It uses XAF-specific report serialization -- reports are loaded from and saved to the database using [](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2) persistent objects.

> [!NOTE]
> This is a legacy class. In most customization scenarios, we recommend that you create and register a custom `IReportStorage` service implementation as described in the following topic: [](xref:113674).
>
> Use the `ReportsStorage` class only if you are developing a .NET Core WinForms application in a configuration that does not use [Dependency Injection](xref:404364) and XAF Application Builder.

You can access the `ReportsStorage` instance from the static `DevExpress.ExpressApp.ReportsV2.ReportDataProvider.ReportsStorage` property. You can also assign a custom report storage to this property.