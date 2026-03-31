---
uid: "114516"
seealso: []
title: 'How to: Display Non-Persistent Objects in a Report'
---
# How to: Display Non-Persistent Objects in a Report

This topic describes how to create a report based on [non-persistent](xref:116516) data. Use this approach to analyze and report data obtained from runtime calculations, stored procedures, arbitrary SQL queries, or third-party services.

## Create a Report and Bind It to a Non-Persistent Data Type

1. Declare a non-persistent class (for example, `MyNonPersistentObject`), and decorate it with the [DomainComponent](xref:DevExpress.ExpressApp.DC.DomainComponentAttribute) and [VisibleInReports](xref:DevExpress.Persistent.Base.VisibleInReportsAttribute) attributes.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.DC;
	using DevExpress.Persistent.Base;
	// ...
    [DomainComponent, VisibleInReports]
    public class MyNonPersistentObject : NonPersistentBaseObject {
        public string Name { get; set; }
    }
	```
	
	***
	
2. Create a report for the `MyNonPersistentObject` data type. You can add a [predefined static report](xref:113645) in Visual Studio or [create a report at runtime](xref:404206).
	
	![Blazor - Specify Object Type](~/images/nonpersistenreportvs118978.png)
	
	> [!IMPORTANT]
	> Non-persistent objects do not support the [](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource) component -- use [](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource) to bind a report to data.
	
	At this step, the created report displays no data in the preview.

	![Blazor - Empty Report](~/images/NonPersistentReportWin_empty.png)

## Supply the Report with Data (Initialize Non-Persistent Objects)

### Use the Application Builder

In the Application Builder code, handle the `NonPersistentObjectSpace.ObjectsGetting` event as shown below:

**File**: _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_

# [C# (Blazor)](#tab/tabid-csharp)

```csharp
using System.ComponentModel;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Core;
// ...
// Handle the `NonPersistentObjectSpace.ObjectsGetting` event.
builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
	if (context.ObjectSpace is NonPersistentObjectSpace nonPersistentObjectSpace) {
		nonPersistentObjectSpace.ObjectsGetting += NonPersistentObjectSpace_ObjectsGetting; 
	}
};
// ...
private static void NonPersistentObjectSpace_ObjectsGetting(object sender, ObjectsGettingEventArgs e) {
	// In the event handler, populate the `e.Objects` collection 
	// with non-persistent objects of the required type.
	if (e.ObjectType == typeof(MyNonPersistentObject)) {
		BindingList<MyNonPersistentObject> objects = new BindingList<MyNonPersistentObject>();
		for (int i = 1; i < 10; i++) {
			objects.Add(new MyNonPersistentObject() { Name = string.Format("Object {0}", i) });
		}
		e.Objects = objects;
	}
}
// ...

```

***

### Implement an IObjectSpaceCustomizer

1. In the module project, implement the `IObjectSpaceCustomizer` service as shown below:

	**File**: _MySolution.Module\NonPersistentObjectSpaceCustomizer.cs_

	# [C#](#tab/tabid-csharp)

	```csharp{18-19,26-36}
	using System.ComponentModel;
	using DevExpress.ExpressApp;
	using DevExpress.ExpressApp.Core;

	public class NonPersistentObjectSpaceCustomizer : IObjectSpaceCustomizer {
		private readonly IObjectSpaceProviderService objectSpaceProvider;
		private readonly IObjectSpaceCustomizerService objectSpaceCustomizerService;

		public NonPersistentObjectSpaceCustomizer(
		IObjectSpaceProviderService objectSpaceProvider, 
		IObjectSpaceCustomizerService objectSpaceCustomizerService) {
			this.objectSpaceProvider = objectSpaceProvider;
			this.objectSpaceCustomizerService = objectSpaceCustomizerService;
		}

		public void OnObjectSpaceCreated(IObjectSpace objectSpace) {
			if(objectSpace is NonPersistentObjectSpace nonPersistentObjectSpace) {
				// Handle the `NonPersistentObjectSpace.ObjectsGetting` event.
				nonPersistentObjectSpace.ObjectsGetting += NonPersistentObjectSpace_ObjectsGetting;
				nonPersistentObjectSpace.ObjectByKeyGetting += NonPersistentObjectSpace_ObjectByKeyGetting;
				nonPersistentObjectSpace.Committing += NonPersistentObjectSpace_Committing;
				nonPersistentObjectSpace.PopulateAdditionalObjectSpaces(objectSpaceProvider, objectSpaceCustomizerService);
			}
		}

		private void NonPersistentObjectSpace_ObjectsGetting(object? sender, ObjectsGettingEventArgs e) {
			// In the event handler, populate the `e.Objects` collection 
			// with non-persistent objects of the required type.
			if (e.ObjectType == typeof(MyNonPersistentObject)) {
				BindingList<MyNonPersistentObject> objects = new BindingList<MyNonPersistentObject>();
				for (int i = 1; i < 10; i++) {
					objects.Add(new MyNonPersistentObject() { Name = string.Format("Object {0}", i) });
				}
				e.Objects = objects;
			}
		}
		private void NonPersistentObjectSpace_ObjectByKeyGetting(object? sender, ObjectByKeyGettingEventArgs e) {
			//...
		}
		private void NonPersistentObjectSpace_Committing(object? sender, CancelEventArgs e) {
			//...
		}
	}
	```

	***

2. Register your `IObjectSpaceCustomizer` service implementation in the _Starup.cs_ file of the Blazor and WinForms applications. Use the [TryAddEnumerable](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.extensions.servicecollectiondescriptorextensions.tryaddenumerable) method to register these services:

	**File**: _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_
	
	# [C# (Blazor)](#tab/tabid-csharp-blazor)

	```csharp
	public void ConfigureServices(IServiceCollection services) {
		//...
		services.TryAddEnumerable(ServiceDescriptor.Scoped<IObjectSpaceCustomizer, 
		    NonPersistentObjectSpaceCustomizer>());
		//...
	}
	```

	# [C# (WinForms)](#tab/tabid-csharp-win)

	```csharp
	public static WinApplication BuildApplication(string connectionString) {
		var builder = WinApplication.CreateBuilder();
		//...
		builder.Services.TryAddEnumerable(ServiceDescriptor.Scoped<IObjectSpaceCustomizer, 
      	    NonPersistentObjectSpaceCustomizer>());
		//...
	}
	```

	***

The following image demonstrates the result:

![Blazor - Result](~/images/nonpersistentreport-result-blazor.png)