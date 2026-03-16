---
uid: "118047"
title: Register a Built-in XAF Module
seealso:
  - linkType: HRef
    linkId: https://community.devexpress.com/blogs/xaf/archive/2011/07/04/best-practices-of-creating-reusable-xaf-modules-by-example-of-a-view-variants-module-extension.aspx
    altText: Best practices for creating reusable XAF modules with a View Variants module extension
  - linkId: '405025'
---
# Register a Built-in XAF Module

XAF includes a number of ready-to-use built-in [modules](xref:118046). This topic describes how to register a built-in module in a [new](#add-a-built-in-xaf-module-in-a-new-application) or [existing](#register-a-built-in-xaf-module-in-an-existing-application) XAF application.

## Register a Built-in XAF Module in an Existing Application

1. Install the NuGet package that contains the module.
2. Navigate to the _MyApplication.Blazor.Server\Startup.cs_ (Blazor) or _MyApplication.Win\Startup.cs_ (WinForms) file and call the module-related `Add*` method to register the module. 

The following code samples register [Reports](xref:113591), [Dashboards](xref:117449), and [Office](xref:400003) modules in the application.


# [ASP.NET Core Blazor](#tab/tabid-appbuilder-blazor)

```csharp
public class Startup {
   // ...
   public void ConfigureServices(IServiceCollection services) {
         // ...
         services.AddXaf(Configuration, builder => {
            // ...
            builder.Modules
               .AddReports(/*...*/)
               .AddDashboards(/*...*/)
               .AddOffice(/*...*/)
            // ...
         });
   }
}
```

# [Windows Forms](#tab/tabid-appbuilder-winforms)

```csharp
public class ApplicationBuilder : IDesignTimeApplicationFactory {
   public static WinApplication BuildApplication(string connectionString) {
         // ...
         builder.Modules
            .AddReports(/*...*/)
            .AddDashboards(/*...*/)
            .AddOffice(/*...*/)
         // ...
   }
   // ...
}
```
***

> [!spoiler][Display the list of module NuGet packages and AddModule methods][Hide the list]
> Module | NuGet Packages | Module-Related Methods
---|---|---
| [Audit Trail Module](xref:112782) | [DevExpress.ExpressApp.AuditTrail.EFCore](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.AuditTrail.EFCore)<br/>[DevExpress.ExpressApp.AuditTrail.Xpo](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.AuditTrail.Xpo) | [AddAuditTrailEFCore](xref:DevExpress.ExpressApp.ApplicationBuilder.AuditTrailEFCoreApplicationBuilderExtensions.AddAuditTrailEFCore``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0}))<br/>[AddAuditTrailXpo](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.AuditTrailXpoApplicationBuilderExtensions.AddAuditTrailXpo*) |
| [Chart Module](xref:113302) | [DevExpress.ExpressApp.Chart.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Chart.Win) | [AddCharts](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.ChartsApplicationBuilderExtensions.AddCharts(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder})) (WinForms) |
| [Clone Object Module](xref:112835) | [DevExpress.ExpressApp.CloneObject](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.CloneObject)<br/>[DevExpress.ExpressApp.CloneObject.Xpo](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.CloneObject.Xpo) | [AddCloning](xref:DevExpress.ExpressApp.ApplicationBuilder.ObjectCloningApplicationBuilderExtensions.AddCloning``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0},System.Action{DevExpress.ExpressApp.CloneObject.ObjectCloningOptions})) |
| [ConditionalAppearance](xref:113286) | [DevExpress.ExpressApp.ConditionalAppearance](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.ConditionalAppearance) | [AddConditionalAppearance](xref:DevExpress.ExpressApp.ApplicationBuilder.ConditionalAppearanceApplicationBuilderExtensions.AddConditionalAppearance``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0})) |
| [Dashboards Module](xref:117449) | [DevExpress.ExpressApp.Dashboards.Blazor](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Dashboards.Blazor)<br/>[DevExpress.ExpressApp.Dashboards.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Dashboards.Win) | [AddDashboards](xref:DevExpress.ExpressApp.Blazor.ApplicationBuilder.DashboardsApplicationBuilderExtensions.AddDashboards(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Dashboards.Blazor.DashboardsOptions})) (Blazor)<br/>[AddDashboards](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.DashboardsApplicationBuilderExtensions.AddDashboards(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Dashboards.Win.DashboardsOptions})) (WinForms) |
| [File Attachments Module](xref:112781) | [DevExpress.ExpressApp.FileAttachment.Blazor](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.FileAttachment.Blazor)<br/>[DevExpress.ExpressApp.FileAttachment.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.FileAttachment.Win) | [AddFileAttachments](xref:DevExpress.ExpressApp.Blazor.ApplicationBuilder.FileAttachmentsApplicationBuilderExtensions.AddFileAttachments(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.FileAttachments.Blazor.FileAttachmentsOptions})) (Blazor)<br/>[AddFileAttachments](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.FileAttachmentsApplicationBuilderExtensions.AddFileAttachments(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsOptions})) (WinForms) |
| [Multi-Tenancy (Data per Tenant) Module](xref:404436) | [DevExpress.ExpressApp.MultiTenancy.Blazor.EFCore](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.MultiTenancy.Blazor.EFCore)<br/>[DevExpress.ExpressApp.MultiTenancy.Blazor.XPO](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.MultiTenancy.Blazor.XPO)<br/>[DevExpress.ExpressApp.MultiTenancy.Win.EFCore](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.MultiTenancy.Win.EFCore)<br/>[DevExpress.ExpressApp.MultiTenancy.Win.XPO](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.MultiTenancy.Win.XPO) | [AddMultiTenancy](xref:DevExpress.ExpressApp.ApplicationBuilder.BlazorEFCoreMultiTenancyApplicationBuilderExtensions.AddMultiTenancy(DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder)) (EF Core Blazor)<br/>[AddMultiTenancy](xref:DevExpress.ExpressApp.ApplicationBuilder.BlazorXpoMultiTenancyApplicationBuilderExtensions.AddMultiTenancy(DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder,System.Boolean)) (XPO Blazor)<br/>[AddMultiTenancy](xref:DevExpress.ExpressApp.ApplicationBuilder.WinEFCoreMultiTenancyApplicationBuilderExtensions.AddMultiTenancy(DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder)) (EF Core WinForms)<br/>[AddMultiTenancy](xref:DevExpress.ExpressApp.ApplicationBuilder.WinXpoMultiTenancyApplicationBuilderExtensions.AddMultiTenancy(DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder,System.Boolean)) (XPO WinForms) |
| [Notifications Module](xref:113688) | [DevExpress.ExpressApp.Notifications.Blazor](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Notifications.Blazor)<br/>[DevExpress.ExpressApp.Notifications.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Notifications.Win) | [AddNotifications](xref:DevExpress.ExpressApp.Blazor.ApplicationBuilder.NotificationsApplicationBuilderExtensions.AddNotifications*) (Blazor)<br/>[AddNotifications](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.NotificationsApplicationBuilderExtensions.AddNotifications(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Notifications.Win.NotificationsOptions})) (WinForms) |
| [Office Module](xref:400003) | [DevExpress.ExpressApp.Office.Blazor](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Office.Blazor)<br/>[DevExpress.ExpressApp.Office.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Office.Win) | [AddOffice](xref:DevExpress.ExpressApp.Blazor.ApplicationBuilder.OfficeApplicationBuilderExtensions.AddOffice(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Blazor.ApplicationBuilder.OfficeOptions})) (Blazor)<br/>[AddOffice](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.OfficeApplicationBuilderExtensions.AddOffice(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Office.Win.OfficeOptions})) (WinForms) |
| [Pivot Grid Module](xref:113303) | [DevExpress.ExpressApp.PivotGrid.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.PivotGrid.Win) | [AddPivotGrid](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.PivotGridApplicationBuilderExtensions.AddPivotGrid(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder})) (WinForms) |
| [Reports V2 Module](xref:113591) | [DevExpress.ExpressApp.ReportsV2.Blazor](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.ReportsV2.Blazor)<br/>[DevExpress.ExpressApp.ReportsV2.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.ReportsV2.Win) | [AddReports](xref:DevExpress.ExpressApp.Blazor.ApplicationBuilder.ReportsApplicationBuilderExtensions.AddReports*) (Blazor)<br/>[AddReports](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.ReportsApplicationBuilderExtensions.AddReports(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.ReportsV2.Win.ReportsOptions})) (WinForms) |
| [Scheduler Module](xref:112811) | [DevExpress.ExpressApp.Scheduler.Blazor](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Scheduler.Blazor)<br/>[DevExpress.ExpressApp.Scheduler.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Scheduler.Win) | [AddScheduler](xref:DevExpress.ExpressApp.Blazor.ApplicationBuilder.SchedulerApplicationBuilderExtensions.AddScheduler*) (Blazor)<br/>[AddScheduler](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.SchedulerApplicationBuilderExtensions.AddScheduler(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Scheduler.Win.SchedulerOptions})) (WinForms) |
| [State Machine Module](xref:113336) | [DevExpress.ExpressApp.StateMachine](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.StateMachine) | [AddStateMachine](xref:DevExpress.ExpressApp.ApplicationBuilder.StateMachineApplicationBuilderExtensions.AddStateMachine``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0},System.Action{DevExpress.ExpressApp.StateMachine.StateMachineOptions})) |
| [TreeList Editors Module](xref:112841) | [DevExpress.ExpressApp.TreeListEditors.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.TreeListEditors.Win) | [AddTreeListEditors](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.TreeListEditorsApplicationBuilderExtensions.AddTreeListEditors(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditorOptions})) (WinForms) |
| [Validation Module](xref:113684) | [DevExpress.ExpressApp.Validation.Blazor](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Validation.Blazor)<br/>[DevExpress.ExpressApp.Validation.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Validation.Win) |[AddValidation](xref:DevExpress.ExpressApp.Blazor.ApplicationBuilder.ValidationApplicationBuilderExtensions.AddValidation(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Validation.ValidationModuleOptions})) (Blazor)<br/>[AddValidation](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.ValidationApplicationBuilderExtensions.AddValidation(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Validation.ValidationModuleOptions})) (WinForms) |
| [View Variants Module](xref:113011) | [DevExpress.ExpressApp.ViewVariantsModule](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.ViewVariantsModule) | [AddViewVariants](xref:DevExpress.ExpressApp.ApplicationBuilder.ViewVariantsApplicationBuilderExtensions.AddViewVariants``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0},System.Action{DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsOptions})) |

### Register a Module in the Module Project

You can use the [ModuleBase.RequiredModuleTypes](xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes) property to specify required dependencies for your module. XAF loads these dependent modules with the current module. Follow the steps below to register additional modules in the Module project:

1. Install the NuGet package that contains the module to register.
2. Add additional modules to the @DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes list in the _MyApplication.Module\Module.cs_ file.

```csharp
public sealed class _MyApplicationModule : ModuleBase {
   //...
   public _MyApplicationModule() {
      InitializeComponent();
      this.RequiredModuleTypes.Add(typeof(DevExpress.ExpressApp.SystemModule.SystemModule));
      this.RequiredModuleTypes.Add(typeof(DevExpress.ExpressApp.ReportsV2.ReportsModuleV2));
      this.RequiredModuleTypes.Add(typeof(DevExpress.ExpressApp.Dashboards.DashboardsModule));
      this.RequiredModuleTypes.Add(typeof(DevExpress.ExpressApp.Office.OfficeModule));
      // ...
   }
}
```

> [!spoiler][Display the list of module types and NuGet packages][Hide the list]
> Module | NuGet Packages | Module Type
---|---|---
| [Audit Trail Module](xref:112782) | [DevExpress.ExpressApp.AuditTrail.EFCore](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.AuditTrail.EFCore)<br/>[DevExpress.ExpressApp.AuditTrail.Xpo](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.AuditTrail.Xpo) | @DevExpress.ExpressApp.AuditTrail.AuditTrailModule |
| [Chart Module](xref:113302) | [DevExpress.ExpressApp.Chart](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Chart) | @DevExpress.ExpressApp.Chart.ChartModule |
| [Clone Object Module](xref:112835) | [DevExpress.ExpressApp.CloneObject](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.CloneObject)<br/>[DevExpress.ExpressApp.CloneObject.Xpo](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.CloneObject.Xpo) | @DevExpress.ExpressApp.CloneObject.CloneObjectModule |
| [ConditionalAppearance](xref:113286) | [DevExpress.ExpressApp.ConditionalAppearance](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.ConditionalAppearance) | @DevExpress.ExpressApp.ConditionalAppearance.ConditionalAppearanceModule |
| [Dashboards Module](xref:117449) | [DevExpress.ExpressApp.Dashboards](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Dashboards) | @DevExpress.ExpressApp.Dashboards.DashboardsModule |
| [Notifications Module](xref:113688) | [DevExpress.ExpressApp.Notifications](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Notifications) | @DevExpress.ExpressApp.Notifications.NotificationsModule |
| [Office Module](xref:400003) | [DevExpress.ExpressApp.Office](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Office) | @DevExpress.ExpressApp.Office.OfficeModule |
| [Pivot Grid Module](xref:113303) | [DevExpress.ExpressApp.PivotGrid](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.PivotGrid) | @DevExpress.ExpressApp.PivotGrid.PivotGridModule |
| [Reports V2 Module](xref:113591) | [DevExpress.ExpressApp.ReportsV2](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.ReportsV2) | @DevExpress.ExpressApp.ReportsV2.ReportsModuleV2 |
| [Scheduler Module](xref:112811) | [DevExpress.ExpressApp.Scheduler](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Scheduler) | @DevExpress.ExpressApp.Scheduler.SchedulerModuleBase |
| [State Machine Module](xref:113336) | [DevExpress.ExpressApp.StateMachine](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.StateMachine) | @DevExpress.ExpressApp.StateMachine.StateMachineModule |
| [TreeList Editors Module](xref:112841) | [DevExpress.ExpressApp.TreeListEditors](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.TreeListEditors) | @DevExpress.ExpressApp.TreeListEditors.TreeListEditorsModuleBase |
| [Validation Module](xref:113684) | [DevExpress.ExpressApp.Validation](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Validation) | @DevExpress.ExpressApp.Validation.ValidationModule |
| [View Variants Module](xref:113011) | [DevExpress.ExpressApp.ViewVariantsModule](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.ViewVariantsModule) | @DevExpress.ExpressApp.ViewVariantsModule |


## Add a Built-in XAF Module in a New Application

[!include[](~/templates/extramodulesnote1111180.md)]

![XAF Template Kit Additional Modules section](~/images/template-kit/template-kit-additional-modules.png)
