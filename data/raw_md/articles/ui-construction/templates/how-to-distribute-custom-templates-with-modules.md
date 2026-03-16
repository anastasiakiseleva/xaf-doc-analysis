---
uid: "113047"
seealso: []
title: 'How to: Distribute Custom Templates with Modules'
owner: Ekaterina Kiseleva
---
# How to: Distribute Custom Templates with Modules

XAF uses default [Templates](xref:112609) when constructing Windows Forms UIs. You can customize them. Approaches for customization are defined in the [Template Customization](xref:112696) and [How to: Create a Custom WinForms Ribbon Template](xref:112618) topics. Once you have developed a custom Template, you may need to use it in several applications. The appropriate way to distribute Windows Forms Templates is to add them to a module that will then be added to the required Windows Forms applications. This topic demonstrates how to do this. ASP.NET Core Blazor templates can be easily distributed, as is. You can add them to an ASP.NET Core Blazor application project replacing the defaults.

When constructing a Windows Forms UI, the [](xref:DevExpress.ExpressApp.Win.WinApplication) class instance uses its Frame Template Factory to create a Template that is appropriate in the current context. A Frame Template Factory is a class that implements the `IFrameTemplateFactory` interface. This interface exposes a single method, `CreateTemplate`, that gets the current Template context as a parameter. XAF has a base class that implements this interface, `FrameTemplateFactoryBase`, and its descendant, `DefaultLightStyleFrameTemplateFactory`. The base class exposes abstract methods that are called by the `CreateTemplate` method, dependent on the passed Template context. They are: `CreateNestedFrameTemplate`, `CreatePopupWindowTemplate`, `CreateLookupControlTemplate`, `CreateLookupWindowTemplate`, `CreateApplicationWindowTemplate` and `CreateViewTemplate`. The `DefaultLightStyleFrameTemplateFactory` class overrides these methods to create the default XAF Templates.

To make an application use custom Templates, do the following:

* Add the custom Templates to the module project to be distributed.
* Implement a Frame Template Factory class in the module to be distributed.
	
	This class should return the required custom Template in an appropriate context. The code below demonstrates how to implement this for two custom Templates: the **MyMainForm** Template, which is created to represent the main Window, and the **MyDetailViewForm** Template, which is created to represent a detail form. These templates have custom constructors taking an [](xref:DevExpress.ExpressApp.Model.IModelTemplate) object as the only parameter, for initialization purposes. The newly implemented `MyFrameTemplateFactory` class is inherited from the `DefaultLightStyleFrameTemplateFactory` class, to override the `CreateApplicationWindowTemplate` and `CreateViewTemplate` methods only.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp;
	using DevExpress.ExpressApp.Model;
	using DevExpress.ExpressApp.Utils;
	using DevExpress.ExpressApp.Win;
	//...
	public class MyFrameTemplateFactory : DefaultLightStyleFrameTemplateFactory {
	    private WinApplication application;
	    public MyFrameTemplateFactory(WinApplication application) {
	        Guard.ArgumentNotNull(application, nameof(application));
	        this.application = application;
	    }
	    protected IModelTemplate GetTemplateInfo(TemplateContext templateContext) {            
	        return application.Model.Templates[templateContext.Name];
	    }
	    protected override DevExpress.ExpressApp.Templates.IFrameTemplate           
	        CreateApplicationWindowTemplate() {            
	        return new MyMainForm(GetTemplateInfo(TemplateContext.ApplicationWindow));
	    }
	    protected override DevExpress.ExpressApp.Templates.IFrameTemplate CreateViewTemplate() {
	        return new MyDetailViewForm(GetTemplateInfo(TemplateContext.View));
	    }
	}
	```
	
	***
* Set the custom Frame Template Factory for the application.
	
	To make the application use the custom Frame Template Factory to create Templates, set it for the `WinApplication.FrameTemplateFactory` property in the `Setup` method of the distributed module. The following code demonstrates this:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.Win;
	//...
	public class MyWindowsFormsModule : ModuleBase {
	   public override void Setup(XafApplication application) {
	      base.Setup(application);
	      ((WinApplication)application).FrameTemplateFactory = 
	         new MyFrameTemplateFactory((WinApplication)application);
	   }
	   //...
	}
	```
	
	***
* Compile the module project and add it to the required application project (see [Application Solution Structure](xref:118045)).
