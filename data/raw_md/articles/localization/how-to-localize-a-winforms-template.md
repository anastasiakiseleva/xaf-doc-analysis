---
uid: "114495"
seealso: []
title: 'How to: Localize a WinForms Template'
owner: Ekaterina Kiseleva
---
# How to: Localize a WinForms Template

This topic demonstrates how to [localize](xref:113298) a WinForms [Template](xref:112696) using the [Model Editor](xref:112582). You can customize custom and built-in WinForms templates. Both of these cases are considered in this topic.

## Localize a Built-In WinForms Template
To do the translation manually, either directly in the Model Editor or using the [Localization Tool](xref:113297), the culture-specific resources should be exported to the Application Model.

* Invoke the Application Designer.
* In the **Properties** window, press the ellipsis button of the **ResourcesExportedToModel** property (see [XafApplication.ResourcesExportedToModel](xref:DevExpress.ExpressApp.XafApplication.ResourcesExportedToModel)). In the invoked dialog, check the templates you want to localize. Submit the selection by pressing the OK button.
	
	![ResourcesExportedToModel](~/images/resourcesexportedtomodel122329.png)
* Invoke the Model Editor for the current application project. In the **Localization** node, you will find child nodes corresponding to the selected resources. Localize them, as with any other XAF string.
	
	![LocalizeTemplates_ModelEditor](~/images/localizetemplates_modeleditor122330.png)

## Localize a Custom WinForms Template
It is assumed that you have created a custom template, as described in the [How to: Create a Custom WinForms Ribbon Template](xref:112618) topic. However, a similar approach is applicable to any other custom WinForms Template (e.g., created in accordance with the [How to: Create a Custom WinForms Standard Template ](xref:113706)).

![LocalizeCustomTemplate](~/images/localizecustomtemplate118951.png)

Follow the steps below to make localization items related to your custom template available in the [Application Model](xref:112579).

* Inherit the **FrameTemplateLocalizer\<T>** class. Pass your custom template type (e.g., **DetailRibbonForm1**) as the generic parameter.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.Win.Templates;
	// ...
	public class MyTemplateLocalizer : FrameTemplateLocalizer<DetailRibbonForm1> { }
	```
	***
* In the [](xref:DevExpress.ExpressApp.Win.WinApplication) descendant's constructor, add the **MyTemplateLocalizer** to the [XafApplication.ResourcesExportedToModel](xref:DevExpress.ExpressApp.XafApplication.ResourcesExportedToModel) list.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	public partial class MySolutionWindowsFormsApplication : WinApplication {
	    public MySolutionWindowsFormsApplication () {
	        InitializeComponent();
	        this.ResourcesExportedToModel.Add(typeof(MyTemplateLocalizer));
	    }
	    // ...
	}
	```
	***
* In the code-behind file of your custom template (e.g., _DetailRibbonForm1.Designer.cs_), find the line where the **resources** private field is declared and initialized.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	System.ComponentModel.ComponentResourceManager resources = 
	    new System.ComponentModel.ComponentResourceManager(typeof(DetailRibbonForm1));
	```
	***
	
	Replace the **ComponentResourceManager** type with **XafComponentResourceManager**.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	DevExpress.ExpressApp.Win.Templates.XafComponentResourceManager resources = 
	    new DevExpress.ExpressApp.Win.Templates.XafComponentResourceManager(typeof(DetailRibbonForm1));
	```
	***
* Rebuild the solution and run the [Model Editor](xref:112582). Expand the **Localization** | **FrameTemplates** | **DetailRibbonForm1** node. The localization items related to your custom templates are available here.
	
	![LocalizeCustomTemplateME](~/images/localizecustomtemplateme118950.png)
	
	You can localize these items using the standard approach described in the [Localization Basics](xref:112595) topic.