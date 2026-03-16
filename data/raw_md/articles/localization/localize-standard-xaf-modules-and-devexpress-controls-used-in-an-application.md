---
uid: "113301"
seealso:
- linkType: HRef
  linkId: https://www.youtube.com/watch?v=iQI5cw8nAEk
  altText: DevExpress Localization Service (video)
title: Localize Standard XAF Modules and DevExpress Controls Used in an Application
owner: Ekaterina Kiseleva
---
# Localize Standard XAF Modules and DevExpress Controls Used in an Application

The standard XAF modules and DevExpress controls supply most of the English texts an XAF application's interface uses. The [DevExpress .NET Localization Service](xref:16235) provides the ready-to-use translations of these texts into different languages - satellite assemblies (required for WinForms platforms). This topic describes how to use these translations in your application and how to manually localize standard XAF Modules and DevExpress controls when there are no ready-to-use translations for your language.

## Satellite Assemblies for DevExpress Controls and XAF Modules
You can install pre-built satellite assemblies in the Global Assembly Cache (GAC) to avoid translating texts supplied with DevExpress controls and XAF Modules. 

The [.NET Product Installer](xref:2216) includes assemblies for **de**, **es**, and **ja** languages. You can install them at your discretion. Use the [DevExpress Localization Service](https://localization.devexpress.com/) to download satellite assemblies for other languages. Refer to the following topics for more information on how to register localization resources:
* [In the GAC](https://learn.microsoft.com/en-us/dotnet/framework/app-domains/install-assembly-into-gac)
* [From Localization Service and Product Installer](xref:5755#embed)

Add the new language aspect as described in the [Localization Basics](xref:112595) topic, and restart Visual Studio to display localized values in the [Model Editor](xref:112582).

Ensure that the Languages key from the configuration file's **appSettings** section contains all the languages your application supports:

# [*.config](#tab/tabid-xml)

```XML
<configuration>
  <appSettings>
    <!-- ... -->
    <add key="Languages" value="en;de;fr" />
    <!-- ... -->
  </appSettings>
  <!-- ... -->
<configuration>
```

# [appsettings.json](#tab/tabid-csharp)
    
```JSON
{ 
    // 
    "DevExpress": { 
        "ExpressApp": { 
            "Languages": "en;de;fr" 
              // ...
        } 
    } 
}  
```
    
***

> [!NOTE]
> You should [deploy](xref:112691) satellite assemblies with an XAF application. Refer to the corresponding [Deployment Tutorial](xref:112691#deployment-tutorial----lessons)'s topic for more information.

## Localization Using the Localization Service
The **Localization Service** allows you to download and modify satellite assemblies. Set the **.NET Platform** to **XAF** to translate only XAF-specific values. Follow the steps from the [Localization Service](xref:16235) topic to localize XAF Modules. Note the following restrictions:

* This service does not allow modifying default language text values.
* You can translate values for XPO classes from the [Business Class Library](xref:112571) only.
* Because the XAF Application Model has a tree-like structure, the **Name** column displays property names in a different format that contains a path to the property and property name. For example, the **Application** | **Views** | **Person_DetailView** node's **Tooltip** property has the "Application\Views\Person_DetailView\Tooltip" name in this table.
* Check **Show Calculated Values** to show items that do not require translation: calculated values, items without a value in a default language, Business Objects classes from the Business Class Library, and values that contain property names (for example, ObjectCaptionFormat, DisplayFormat).
* Calculated values are translated automatically based on the non-calculated values' translation. Input "non-calculated" in the search panel to show only the non-calculated values. 
	
	![LocalizationService_NonCalculated](~/images/localizationservice_noncalculated131848.png)
* An item is only translated if it has a text value; otherwise, you can add a value for the target language or leave it blank. 
* Values containing properties' names (**ObjectCaptionFormat**, **DisplayFormat**, etc.) should not be localized. [](xref:DevExpress.Persistent.Base.ObjectFormatter) processes these values and replaces properties' names with the corresponding values.

  > [!NOTE]
  > * If you received **FormatException** or **MemberNotFoundException**, ensure that you have not replaced a property name with a localized value. 
  > * Strings from the **DevExpress.Persistent.BaseImpl.EFCore** assembly are not available in the [Localization Service](xref:16235). To localize these strings, use the [Localization Tool](xref:113297).

## Manual Localization
If the technique described in the section above does not apply to you, follow the instructions from the following topic: [How to: Localize XAF Application Items Using XAF Tools](xref:119411).

Culture-specific resources should be exported to the Application Model when you localize DevExpress Controls.

* Invoke the Application Designer.
* In the **Properties** window, click the [XafApplication.ResourcesExportedToModel](xref:DevExpress.ExpressApp.XafApplication.ResourcesExportedToModel) property's ellipsis button. In the invoked dialog, check the resources you want to localize. Click OK to submit the selection.
	
	![ResourceLocalizers](~/images/resourcelocalizers116198.png)
* Invoke the Model Editor for the current application project and localize the **Localization** node's child nodes.
	
	![ResourceLocalizers_Model](~/images/resourcelocalizers_model116199.png)

You can also use the module's [ModuleBase.ResourcesExportedToModel](xref:DevExpress.ExpressApp.ModuleBase.ResourcesExportedToModel) property to add localizable resources in the Module Designer. The resources added in a module cannot be removed from the localizable resources list in another module or application. For example, if you added the resources in the base Module, these resources are used in a platform-specific Modules, but you cannot delete these resources from the platform-specific Module.

> [!NOTE]
> Certain components added to a Model require a reference. For instance, after adding the **XtraGrid Control** to the Model, you get the following error: "**The type 'DevExpress.XtraGrid.Localization.GridResLocalizer' is defined in an assembly that is not referenced. You should add a reference to assembly 'DevExpress.XtraGrid.v<:xx.x:>…**". Add a reference to the required assembly to resolve this issue.

## Reuse Your Translations
You can use one of the following approaches to reuse translations in different XAF applications:

* Localize all standard XAF module captions using the Model Editor invoked for the application project and share the resulting XAFML files with translations;
* Create a new XAF module and localize all standard XAF module captions using the Model Editor invoked for its _Model.DesignedDiffs.xafml_ file as described in the [How to: Localize XAF Application Items Using XAF Tools](xref:119411) topic. You can now use the Module or Application Designers to reuse this module in other applications.
