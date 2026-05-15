---
uid: "404243"
title: Add Reports V2 Module to an Existing XAF Application
seealso:
- linkId: 118047
---
# Add Reports V2 Module to an Existing XAF Application

1. Install the following NuGet packages:

    * [DevExpress.ExpressApp.ReportsV2.Blazor](https://nuget.org/packages/DevExpress.ExpressApp.ReportsV2.Blazor)
    * [DevExpress.ExpressApp.ReportsV2.Win](https://nuget.org/packages/DevExpress.ExpressApp.ReportsV2.Win)

2. Call the `AddReports` method in the _Startup.cs_ file of each project that will use Reports. In the method call, specify the @DevExpress.ExpressApp.ReportsV2.ReportModuleOptions.ReportDataType property value.

    **Files**: _SolutionName.WebApi\Startup.cs_, _SolutionName.Blazor.Server\Startup.cs_, _SolutionName.Win\Startup.cs_, _SolutionName.MiddleTier\Startup.cs_.

    # [EF Core](#tab/tabid-core)
    
    ```csharp
    // ...
    builder.Modules
        .AddReports(options => {
            options.ReportDataType = typeof(DevExpress.Persistent.BaseImpl.EF.ReportDataV2);
        // ...
    ```
    
    # [XPO](#tab/tabid-xpo)
    
    ```csharp
    // ...
    builder.Modules
        .AddReports(options => {
            options.ReportDataType = typeof(DevExpress.Persistent.BaseImpl.ReportDataV2);
        // ...
    ```
    
    ***


3. If your application is based on the **Entity Framework Core**, navigate to the _SolutionName.Module\BusinessObjects\SolutionDbContextName.cs_ file and include the @DevExpress.Persistent.BaseImpl.EF.ReportDataV2 class in the data model:

    ```csharp{4}
    using DevExpress.Persistent.BaseImpl.EF;
    // ...
    public class SolutionEFCoreDbContextName : DbContext {
        public DbSet<ReportDataV2> ReportData { get; set; }
        // ...
    }
    ```