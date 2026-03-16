---
uid: "114515"
seealso:
  - linkId: "113703"
  - linkId: "113601"
title: 'How to: Use XAF Reports in a non-XAF Application'
owner: Ekaterina Kiseleva
---
# How to: Use XAF Reports in a non-XAF Application

This topic describes how to create, set up, and export XAF reports in a non-XAF application. Since XAF stores reports in the database, and XAF reports use [Object Space](xref:113707) to retrieve data, you should connect to the XAF database and create an Object Space in a non-XAF application.

[!example[XAF - How to create and setup an XtraReport report for exporting to a Stream in a non-XAF application](https://github.com/DevExpress-Examples/xaf-how-to-create-and-setup-an-xtrareport-report-for-exporting-to-a-stream-in-a-non-xaf)]

1. Implement the @DevExpress.ExpressApp.Core.IObjectSpaceProviderFactory interface.
   
    [!codesnippet-csharp[dx-examples](xaf-how-to-create-and-setup-an-xtrareport-report-for-exporting-to-a-stream-in-a-non-xaf/CS/EFCore/ExportReportEF/ExportXAFReport/CustomObjectSpaceProviderFactory.cs)]
    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Core;
    using DevExpress.ExpressApp.EFCore;
    using ExportReportEF.Module.BusinessObjects;
    using Microsoft.EntityFrameworkCore;
    
    namespace MyApp // Note: actual namespace depends on the project name.
    {
        class CustomObjectSpaceProviderFactory : IObjectSpaceProviderFactory {
            const string connectionString = @"Integrated Security=SSPI;Pooling=false;Data Source=(localdb)\mssqllocaldb;Initial Catalog=ExportReportEF";
            public IEnumerable<IObjectSpaceProvider> CreateObjectSpaceProviders() {
                return new IObjectSpaceProvider[] {
                    new EFCoreObjectSpaceProvider<ExportReportEFEFCoreDbContext>((builder, _) => { builder.UseSqlServer(connectionString).UseChangeTrackingProxies(); })
                };
            }
        }
    }
    ```

2. Create the `ServiceCollection` to register XAF services and your `CustomObjectSpaceProviderFactory` service (the _Program.cs_ file).
   
    [!codesnippet-csharp[dx-examples](xaf-how-to-create-and-setup-an-xtrareport-report-for-exporting-to-a-stream-in-a-non-xaf/CS/EFCore/ExportReportEF/ExportXAFReport/Program.cs?line=12-13,16-21,33,41)]
    ```csharp
    internal class Program {
        static void Main(string[] args) {
        // ...
            ServiceCollection serviceDescriptors = new ServiceCollection();
            serviceDescriptors.AddXafCore();
            serviceDescriptors.AddXafReportingCore();
            serviceDescriptors.AddScoped<IObjectSpaceProviderFactory, CustomObjectSpaceProviderFactory>();
    
            IServiceProvider serviceProvider = serviceDescriptors.BuildServiceProvider();
            // ...
        }
        // ...
    }
    ```

3. Register the required types in the [Types Info Subsystem](xref:113669).

    [!codesnippet-csharp[dx-examples](xaf-how-to-create-and-setup-an-xtrareport-report-for-exporting-to-a-stream-in-a-non-xaf/CS/EFCore/ExportReportEF/ExportXAFReport/Program.cs?line=12-13,23-25,33-41)]
    ```csharp
    internal class Program {
        static void Main(string[] args) {
        // ...
            var typesInfo = serviceProvider.GetRequiredService<ITypesInfo>();
            InitTypesInfo(typesInfo, serviceProvider.GetRequiredService<IObjectSpaceProviderFactory>());
            RegisterBOTypes(typesInfo);
            // ...
        }
        static void InitTypesInfo(ITypesInfo typesInfo, IObjectSpaceProviderFactory osProviderFactory) {
            var osProviders = osProviderFactory.CreateObjectSpaceProviders();
            osProviders.ForEach(osProvider => ((TypesInfo)typesInfo).AddEntityStore(osProvider.EntityStore));
        }
        static void RegisterBOTypes(ITypesInfo typesInfo) {
            typesInfo.RegisterEntity(typeof(Employee));
        }
    }
    ```

4. Use the `IReportExportService` service to load and prepare a report.

    [!codesnippet-csharp[dx-examples](xaf-how-to-create-and-setup-an-xtrareport-report-for-exporting-to-a-stream-in-a-non-xaf/CS/EFCore/ExportReportEF/ExportXAFReport/Program.cs?line=12-13,27-29,33,41)]
    ```csharp
    internal class Program {
        static void Main(string[] args) {
        // ...
            IReportExportService reportExportService = serviceProvider.GetRequiredService<IReportExportService>();
            using var report = reportExportService.LoadReport<ReportDataV2>(data => data.DisplayName == "Employees Report");
            reportExportService.SetupReport(report);
            // ...
        }
        // ...
    }
    ```