---
uid: "112595"
seealso:
- linkId: "113297"
- linkId: "113301"
- linkId: DevExpress.ExpressApp.Utils.CaptionHelper
- linkId: "403184"
- linkId: "402956"
- linkId: "112655"
title: Localization Basics
owner: Ekaterina Kiseleva
---
# Localization Basics

XAF allows you to localize your WinForms and ASP.NET Core Blazor applications. All strings in the UI are read from the [Application Model](xref:112580). Some properties in the Application Model are localizable, i.e., they can have different values depending on their language. For instance, generally the Caption property of any Application Model node is localizable. In this topic, you will learn how to use these properties to localize your applications. To see how a WinForms application can be localized, refer to the **Localization** section in the **FeatureCenter** demo, which is supplied with XAF. This demo is located in the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ folder by default.

## UI Elements to be Localized
All UI elements related to data presentation and functionalities can be localized: [View Item](xref:112612) captions,  [List View](xref:112611) column captions, business object captions, [Action](xref:112622) captions and Action item captions, and so on. For this purpose, the Application Model's appropriate nodes have the localizable **Caption** property.

In addition, UI elements such as messages, exceptions, button captions, form captions, etc., can also be localized. For this purpose, the Application Model has the special **Localization** node. This node's child nodes represent groups of the listed elements. Each group item has the **Value** property that can be localized.

If you [extend the Application Model](xref:112810) with new properties, you can specify which properties are to be localized. Refer to the [Application Model Structure](xref:112580) topic to learn how to do this. You can also localize custom string constants via the **Localization** node. Refer to the [How to: Localize Custom String Constants](xref:112655) topic to learn how.

## General Information
To localize the user interface, use the [Model Editor](xref:112582). There you will find the **Language** combo box on the [Model Editor Toolbar](xref:113327).

![LocalizationToolbar](~/images/localizationtoolbar115643.png)

By default, the drop-down list contains two options: **(Default language)** and **Languages Manager…**. The **(Default language)** option corresponds to the default language (English),  but not to any country/region. To add more language options, select the **Languages Manager…**. In the invoked dialog, add the desired languages.

![Tutorial_UIC_Lesson11_0](~/images/tutorial_uic_lesson11_0115495.png)

> [!NOTE]
> You can use a specific language (such as "fr-FR"), rather than a neutral language (such as "fr"). The specific language is recommended, because formatting options (for example, currencies) can be different for cultures that speak the same language (for example, for France, Belgium, and Luxembourg). See the [Culture-Specific Formatting](xref:113299) topic for details.

Restart the Visual Studio and select the required language using the **Language** combo-box within the toolbar.

![Tutorial_UIC_Lesson11_0_1](~/images/tutorial_uic_lesson11_0_1115628.png)

You can setup as many languages as you want. All the changes for a particular language are saved to the corresponding _Model.DesignedDiffs.Localization.\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml_ or *Model\_\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml* file. These files resemble the _Model.DesignedDiffs.xafml_ and _Model.xafml_ files, which store the changes made in the Application Model in the default language (English). The changes stored in the _Model.DesignedDiffs.Localization.\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml_ and *Model\_\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml* files are also superimposed on the previous model layer. To view these changes, right-click one of these files and choose **View Code**. For information about files with changes and layers of the Application Model, refer to the [Application Model Basics](xref:112580) topic.

Refer to the [How to: Localize an XAF Application](xref:402956) topics to learn more about the application localization process.

## Ways to Specify an Application Language
### In the Application Model

To specify the language in which your application will run, invoke the Model Editor, navigate to the **Application** node and set the required language for the [IModelApplication.PreferredLanguage](xref:DevExpress.ExpressApp.Model.IModelApplication.PreferredLanguage) property. The following options are available.

* (Default language)
	
	None of the generated *Model.DesignedDiffs\_\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml* and *Model\_\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml* files will be considered. All localizable elements will be set to the values specified in the _Model.DesignedDiffs.xafml_ and _Model.xafml_ files.
* (User language)
	
	The values from the *Model.DesignedDiffs\_\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml* and *Model\_\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml* files will be superimposed on the values from the files with the default language (_Model.DesignedDiffs.xafml_ and _Model.xafml_). In Windows Forms applications, the _\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>_ is taken from the operating system settings.
* Certain Language
	
	The values from the *Model.DesignedDiffs\_\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml* and *Model\_\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml* files, which correspond to the specified language, will be superimposed.

### In code

If you need to set the preferred language in dependence to a condition, handle the [XafApplication.CustomizeLanguage](xref:DevExpress.ExpressApp.XafApplication.CustomizeLanguage) event. Note that the language you set in this event handler cannot be changed via the Application Model at runtime.

## Localization Rules
When building a UI, the system uses the appropriate language-specific xafml files. For instance, if German must be used in an application, the system uses the *Model\_de.xafml* file, where properties are set to German values. However, some values might not be found in language-specific xafml files. This may occur if you omitted a property when you were localizing your application to the required language. In this instance, there are two rules with which to get the value.

* If the property, whose localized value is not found, is not calculated from another property, its value is taken from the xafml file in the default language.
	
	![LocalizationForTypicalAttributes](~/images/localizationfortypicalattributes116152.png)
* If the property, whose localized value is not found, is calculated from another property, the localized value of the source property is taken. However, if the source property's localized value is not found, the calculated property's value is taken from the xafml file in the default language (dotted arrow in the image below).
	
	![LocalizationForCalculatedAttributes](~/images/localizationforcalculatedattributes116153.png)

The list of supported languages can be retrieved from these sources:

1. The **Languages** key from the configuration file's **appSettings** section:
	
	# [XML](#tab/tabid-xml)
	
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
	
	***
	
	The value of this key consists of available language codes, separated by a semicolon.
2. **For ASP.NET Core Blazor UI applications.** From `appsettings.json`. This languages list is used to:
    - load satellite assemblies
    - specify the RequestLocalizationMiddleware's [RequestLocalizationOptions.SupportedCultures](xref:Microsoft.AspNetCore.Builder.RequestLocalizationOptions.SupportedCultures) option.
	
	The first language in this list is used as a default language and is specified in the [RequestLocalizationOptions.SupportedCultures](xref:Microsoft.AspNetCore.Builder.RequestLocalizationOptions.DefaultRequestCulture). 

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
3. From the current project/application differences file names.
	
	![LanguageSpecificModel](~/images/languagespecificmodel131723.png)

When the Model Editor is invoked as the Visual Studio designer, only the last source is available. At runtime, these sources are joined. So, if there are no differences for a certain language, but this language is added in the configuration file, then this language can be specified as preferred, and the values stored in the corresponding satellite assembly will be used in the UI.

> [!NOTE]
> To load localized property values from satellite assemblies, the Visual Studio or running application must be restarted. When the language is added, but satellite assemblies are unavailable, you can get the System.IO.FileNotFoundException exceptions while debugging. These exceptions are properly handled internally, and do not cause the application crash at runtime. To skip these exceptions automatically, click the **Debug** | **Exceptions…** item in Visual Studio menu and uncheck **Common Language Runtime Exceptions** | **System.IO**.
