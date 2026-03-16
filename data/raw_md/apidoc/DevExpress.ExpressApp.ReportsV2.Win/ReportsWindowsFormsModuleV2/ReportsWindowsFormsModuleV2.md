---
uid: DevExpress.ExpressApp.ReportsV2.Win.ReportsWindowsFormsModuleV2
name: ReportsWindowsFormsModuleV2
type: Class
summary: The module contained in the _DevExpress.ExpressApp.ReportsV2.Win.v<:xx.x:>.dll_ assembly.
syntax:
  content: 'public sealed class ReportsWindowsFormsModuleV2 : ModuleBase'
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.Win.ReportsWindowsFormsModuleV2._members
  altText: ReportsWindowsFormsModuleV2 Members
- linkId: "113591"
---
This module adds a handler to the **ReportDesignExtensionManager.CustomizeReportExtension** event in its static constructor to provide [Repositories and Repository Items](xref:114580) for report parameters. Use the [ReportsWindowsFormsModuleV2.CreateCustomReportDesignRepositoryItem](xref:DevExpress.ExpressApp.ReportsV2.Win.ReportsWindowsFormsModuleV2.CreateCustomReportDesignRepositoryItem) event to specify your custom repository items.