---
uid: "403000"
title: 'How to: Use the Entity Framework Core Data Model Located in an External Assembly'
seealso: []
---
# How to: Use the Entity Framework Core Data Model Located in an External Assembly

If you have a non-XAF application, and want to develop an XAF application that utilizes the same database, you can generate business classes for an existing database to achieve this task (see [Reverse Engineering](https://learn.microsoft.com/en-us/ef/core/managing-schemas/scaffolding)). However, if your existing application is based on the Entity Framework Core data model, you can reuse this model in XAF to avoid code duplication. This topic describes how to use the data model located within an external assembly.

> [!NOTE]
> If the external assembly is an XAF Module, then you do not need to follow this topic. Entities declared within XAF modules are automatically recognized and added to the Application Model.

1. [Create a new XAF solution](xref:405447#create-a-new-project) using the DevExpress Template Kit. In the **ORM** section, select **EF Core**.
2. Reference the external assembly that contains the Entity Framework Core data model to be used.
3. A @Microsoft.EntityFrameworkCore.DbContext class is required to use entities from the external assembly. To declare it, do one of the following.

	* In the module project (_MySolution.Module_), inherit the **DbContext** declared in the external assembly.
	* Add required entity types from the external assembly to the existing **DbContext** located in the _BusinessObjects\\MySolutionEFCoreDbContext.cs_ file.
4. Open the _MySolution.Module_\\_Module.cs_ file and add the required entity types to the [ModuleBase.AdditionalExportedTypes](xref:DevExpress.ExpressApp.ModuleBase.AdditionalExportedTypes) collection in the module's constructor:

	# [C#](#tab/tabid-csharp)

	```csharp
	using MyDataModelLibrary;
	// ...
	public sealed partial class MySolutionModule : ModuleBase {
		public MySolutionModule() {
			// ...
			AdditionalExportedTypes.Add(typeof(Employee));
			AdditionalExportedTypes.Add(typeof(Task));
		}
	}
	```
	***

5. Rebuild your solution, so that the changes made in the Module are loaded to the Application Model, and run the [Model Editor](xref:112582). Make sure that the entities added in the previous step are available in the **BOModel** node.
	
	![EF_ExternalAssembly_ModelEditor](~/images/ef_externalassembly_modeleditor117223.png)
6. Add navigation items for the added entities by following the steps described in the [Add an Item to the Navigation Control](xref:402131) tutorial.
	
	![EF_ExternalAssembly_Navigation](~/images/ef_externalassembly_navigation117224.png)

7. Configure your application to use the correct `DbContext` type.

	**File:** _Startup.cs_

	```csharp
	builder.ObjectSpaceProviders
		.AddEFCore(options => 
			// ...
		)
		.WithDbContext<MySolutionDbContext>((application, options) => {
			// ...
		})
	```

	For details, refer to the **Specify the Entity Container (Context)** section of the [Use the Entity Framework Core Data Model](xref:402972) topic.