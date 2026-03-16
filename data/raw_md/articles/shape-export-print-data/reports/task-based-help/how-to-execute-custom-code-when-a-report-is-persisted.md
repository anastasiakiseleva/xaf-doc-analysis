---
uid: "113674"
seealso: []
title: 'How to: Create a Custom Report Storage to Customize UI and Behavior Globally'
owner: Eugeniy Burmistrov
---
# How to: Create a Custom Report Storage to Customize UI and Behavior Globally

This topic describes how you can customize the `DevExpress.ExpressApp.ReportsV2.IReportStorage` service in various use case scenarios. 

## Implement a Custom Report Storage Service (Base Implementation)

To create a custom report storage, implement a class that extends the `ReportStorageService` class. Override the `ReportStorageService` class methods to implement your custom logic.

# [C#](#tab/tabid-csharp)

```csharp
public class CustomReportStorage : ReportStorageService {
	public CustomReportStorage(ITypesInfo typesInfo, IServiceProvider serviceProvider, IObjectSpaceFactory 
		objectSpaceFactory, IOptions<ReportOptions> options, IDataManipulationRight dataManipulationRight)
		: base(typesInfo, serviceProvider, objectSpaceFactory, options, dataManipulationRight) {
		// Override methods of the `CustomReportStorage` class to implement custom report storage logic.
	}
}
```

***

## Register the Custom Report Storage Service

Register `CustomReportsStorage` in your XAF application. The required steps differ depending on the target platform:

* In an **XAF Blazor** application, add a line that registers your service to the `ConfigureServices` method, after the `AddXaf` method call.

    **File:** _MySolution.Blazor.Server\Startup.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp{9}
    using DevExpress.ExpressApp.ReportsV2;
    //...
        public class Startup {
            // ...
            public void ConfigureServices(IServiceCollection services) {
                services.AddXaf(Configuration, builder => {
                    //...
                });
                services.AddScoped<IReportStorage, CustomReportStorage>();
            }
            // ...
        }
    ```

    ***

* In an **XAF WinForms** application, add a line that registers your service to the `BuildApplication` method, after the `WinApplication.CreateBuilder` method call.

    **File:** _MySolution.Win\Startup.cs_.

    # [C#](#tab/tabid-csharp)

    ```csharp{6}
    using DevExpress.ExpressApp.ReportsV2;
    //...
    public class ApplicationBuilder : IDesignTimeApplicationFactory {
        public static WinApplication BuildApplication(string connectionString) {
            var builder = WinApplication.CreateBuilder();
            builder.Services.AddScoped<IReportStorage, CustomReportStorage>();
            //...
        }
        // ...
    }
    ```

    ***

* In a **Web API** application, add a line that registers your service to the `ConfigureServices` method, after the `AddXafWebApi` method call.

    **File:** _MySolution.WebApi\Startup.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp{10}
    using DevExpress.ExpressApp.ReportsV2;
    //...
    namespace MySolution.WebApi {
        public class Startup {
            // ...
            public void ConfigureServices(IServiceCollection services) {
                services.AddXafWebApi(builder => {
                    // ...
                }, Configuration);
                services.AddScoped<IReportStorage, CustomReportStorage>();
            }
            // ...
        }
    }
    ```

    ***

## Customize a Report Storage Service in Various Scenarios

### Customize the Display Name of a Copied Report

To change the @DevExpress.ExpressApp.ReportsV2.IReportDataV2.DisplayName of a copied report, override the `CopyFrom` method of your `CustomReportStorage` as shown below:

# [C#](#tab/tabid-csharp)

```csharp{16-22}
using DevExpress.ExpressApp.Core;
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.ReportsV2;
using DevExpress.ExpressApp.ReportsV2.Services;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Services.Security;
using DevExpress.Persistent.BaseImpl.EF;
using DevExpress.XtraReports.UI;
using Microsoft.Extensions.Options;

namespace MySolution.Module;
    public class CustomReportStorage : ReportStorageService {
		public CustomReportStorage(ITypesInfo typesInfo, IServiceProvider serviceProvider, IObjectSpaceFactory objectSpaceFactory, IOptions<ReportOptions> options, IDataManipulationRight dataManipulationRight)
			: base(typesInfo, serviceProvider, objectSpaceFactory, options, dataManipulationRight) {
		}
		public override void CopyFrom(IReportDataV2 sourceReportData, IReportDataV2Writable targetReportData) {
			base.CopyFrom(sourceReportData, targetReportData);
			if(sourceReportData.IsPredefined) {
				// Specify the required name.
				targetReportData.SetDisplayName("custom - " + sourceReportData.DisplayName); 
			}
		}
}

```

***

### Use a Custom Report Type as a Template in the UI (an XtraReport Descendant)

In certain scenarios you may want to customize the base report class to add custom functionality available in all new reports. This topic describes how to register a custom [](xref:DevExpress.XtraReports.UI.XtraReport) descendant that will be used as a template for new reports that end users create at runtime.

Assume you have the following custom report class:

# [C#](#tab/tabid-csharp)

```csharp
public class MyXtraReport : XtraReport {
   // ...
}
```

***

Override the `CreateReport` method of your `CustomReportStorage` so this method returns a new instance of your custom report class.
	
# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Core;
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.ReportsV2;
using DevExpress.ExpressApp.ReportsV2.Services;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Services.Security;
using DevExpress.XtraReports.UI;
using Microsoft.Extensions.Options;

public class CustomReportStorage : ReportStorageService {
	protected override XtraReport CreateReport() {
		return new MyXtraReport();
	}
}
```

***

Run the application and [create a report](xref:404206).

![Result](~/images/xtrareport_descendant118847.png)


## Use a Custom ORM Business Object with Custom Storage Logic (a ReportDataV2 Descendant)

Assume you have a [customized ReportDataV2 class](xref:113672), to which you added a `ModifiedBy` property that should return the name of the user who last edited the report layout. You need to update this property value each time a report layout is saved. To do this, override the [ReportStorageBase.SaveReport](xref:DevExpress.ExpressApp.ReportsV2.ReportStorageBase.SaveReport(DevExpress.ExpressApp.ReportsV2.IReportDataV2Writable,DevExpress.XtraReports.UI.XtraReport)) method of your `CustomReportStorage` as shown below:
	
# [C#](#tab/tabid-csharp)

```csharp{16-24}
using DevExpress.ExpressApp.Core;
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.ReportsV2;
using DevExpress.ExpressApp.ReportsV2.Services;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Services.Security;
using DevExpress.XtraReports.UI;
using Microsoft.Extensions.Options;

public class CustomReportStorage : ReportStorageService {
	readonly ISecurityStrategyBase security;
	public CustomReportStorage(ISecurityStrategyBase security, ITypesInfo typesInfo, IServiceProvider serviceProvider, IObjectSpaceFactory objectSpaceFactory, IOptions<ReportOptions> options, IDataManipulationRight dataManipulationRight)
		: base(typesInfo, serviceProvider, objectSpaceFactory, options, dataManipulationRight) {
		this.security = security;
	}
	public override void SaveReport(IReportDataV2Writable reportData, XtraReport report) {
		if(reportData is MyReportDataV2) {
			ISecurityUser currentUser = security.User as ISecurityUser;
			if(currentUser != null) {
				((MyReportDataV2)reportData).ModifiedBy = currentUser.UserName;
			}
		}
		base.SaveReport(reportData, report);
	}
}
```

***

