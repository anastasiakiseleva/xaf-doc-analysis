---
uid: "402956"
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/Blazor-Reporting-UI-Customization-API
  altText: Blazor Reporting - UI Customization API
title: 'Localize an XAF Application'
owner: Alexey Kazakov
---
# Localize an XAF Application

This topic describes how to localize XAF applications (WinForms and ASP.NET Core Blazor). 

Review the [Application Model Basics](xref:112580) and [Localization Basics](xref:112595) topics before proceeding.


1. Choose the language you want to use in your XAF application.
    
    **Pre-installed languages:**  German (de), Spanish (es), and Japanese (ja). These assemblies are available in the DevExpress Local NuGet Feed (for example, `DevExpress.ExpressApp.de` or `DevExpress.ExpressApp.Core.All.de`).
    
    **Other languages:**
    
    * Use the [Localization Service](xref:16235) to download satellite assemblies. See the [Localize Standard XAF Modules and DevExpress Controls Used in an Application](xref:113301) topic for more information on how to use this service to localize XAF modules.
    * Place the downloaded assemblies in the following folders:
        - In your application _bin_ folder (for example, `\Solution1.BlazorServer\bin\Debug\net8.0\fr` for French). This enables runtime localization.
        - In your Model Editor's folder (for example, `C:\Program Files\DevExpress 22.1\Components\Tools\eXpressAppFrameworkNetCore\Model Editor\fr` for French). This enables design-time localization.
    
    
    You can reuse satellite assemblies in any other project.
    
    > [!NOTE]
    > Remember to deploy the required satellite assemblies when you [deploy](xref:112691) an XAF application. Refer to the [Deployment Tutorial](xref:112691#deployment-tutorial----lessons) for more details.

2. **For XAF ASP.NET Core Blazor applications**, add the [ApplicationBuilderExtensions.UseRequestLocalization()](xref:Microsoft.AspNetCore.Builder.ApplicationBuilderExtensions.UseRequestLocalization*) method call. This enables the **RequestLocalizationMiddleware**. 

    # [C#](#tab/tabid-csharp)
     
    ```csharp{8}
     namespace MainDemo.Blazor.ServerSide { 
        public class Startup { 
            // ...
            public void Configure(IApplicationBuilder app, IWebHostEnvironment env) { 
                // ...
                app.UseHttpsRedirection(); 
                // Enable the RequestLocalizationMiddleware 
                app.UseRequestLocalization(); 
                app.UseStaticFiles(); 
                app.UseRouting(); 
                // ...
            } 
        } 
    } 
    ```
     
    ***

    In `appsettings.json`, specify languages used in your application in the `DevExpress:ExpressApp:Languages` section. You should always use the fully qualified language name (for example: `xx-YY` instead of `xx`). This language list is used for the following purposes:
    
    - To load satellite assemblies.
    - To specify the `RequestLocalizationMiddleware`'s [RequestLocalizationOptions.SupportedCultures](xref:Microsoft.AspNetCore.Builder.RequestLocalizationOptions.SupportedCultures) option.

    The first language in this list is the default language (specified in the [RequestLocalizationOptions.DefaultRequestCulture](xref:Microsoft.AspNetCore.Builder.RequestLocalizationOptions.DefaultRequestCulture)). 

    # [appsettings.json](#tab/tabid-csharp)
    
    ```JSON
    {
        //
        "DevExpress": {
            "ExpressApp": {
                "Languages": "en-US;de-DE;fr-FR"
                 // ...
            }
        }
    }
    ```
    
    ***

 
3. In the module project, double-click the _Model.DesignedDiffs.xafml_ file to invoke the [Model Editor](xref:112582). Focus the root node and click **Languages Manager…** in the **Language** combo box on the [Model Editor Toolbar](xref:113327). Add the target language in the invoked dialog and click **OK**. Restart Visual Studio to load localized values from the satellite assemblies and specify the application's target language in the **Language** combo box.
    
    ![Tutorial_UIC_Lesson11_0_1](~/images/tutorial_uic_lesson11_0_1115628.png)
    
    All the changes for a particular language are saved to the corresponding _Model.DesignedDiffs.Localization.\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml_ or _Model_\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml_ file. These files resemble the _Model.DesignedDiffs.xafml_ and _Model.xafml_ files, which store the changes made in the Application Model in the default language (English).

    Ensure that the newly created _Model.DesignedDiffs.Localization.XX.xafml_ files are processed as embedded resources (in the Property Editor, **Build Action** is set to **Embedded resource**).

    Refer to the [Localization Basics](xref:112595) topic for more information.
4. To learn how to add a new or modify an existing translation value, refer to the following topic: [How to: Localize XAF Application Items Using XAF Tools](xref:119411).
5. To specify an application's language, invoke the Model Editor for an application project, navigate to the **Application** node, and set the [IModelApplication.PreferredLanguage](xref:DevExpress.ExpressApp.Model.IModelApplication.PreferredLanguage) property to a language. Refer to the [Localization Basics](xref:112595) topic for more details. If you want your application's language to match the language on the user's device, set the **PreferredLanguage** property to **(User language)**.
6. Localizable resources of Windows Forms [Templates](xref:112609) are not available in the Application Model (the default setting). Refer to the [How to: Localize a WinForms Template](xref:114495) topic to learn how you can localize Windows Forms templates.
7. The splash screen form displayed on the Windows Forms application at startup contains a "**Loading**" text label. To change the text, refer to the following topic: [Localize a Splash Form](xref:112680).
8. Start the application to ensure that all the text values are localized.

## Change Language at Runtime (Blazor UI)

### In UI (Runtime Language Switcher)

For XAF ASP.NET Core Blazor UI applications, you can enable the **Runtime Language Switcher**. You can see the Language Switcher in the following locations:

- The login page

    ![localization ASP.NET Core Blazor login page language switcher](~/images/localization-blazor-login-page-language-switcher.png)
- The settings menu

    ![|localization ASP.NET Core Blazor settings language switcher|](~/images/localization-blazor-settings-language-switcher.png)

To enable the Runtime Language Switcher, set the `DevExpress: ExpressApp: ShowLanguageSwitcher` value to `True` in `appsettings.json`:

# [appsettings.json](#tab/tabid-csharp)

```JSON
{
    //
    "DevExpress": {
        "ExpressApp": {
            "Languages": "en-US;de-DE;fr-FR",
            "ShowLanguageSwitcher": true
        }
    }
}
```

***


The `Languages` section must contain at least two supported languages to enable the Runtime Language Switcher. These languages will be displayed in the Language Switcher's drop-down list.

The application retrieves the language name from `CultureInfo.NativeName`.


> [!NOTE]
> 
> The Runtime Language Switcher requires that `IModelApplication.PreferredLanguage` is set to `(User language)`. 

## In Code

To change the XAF ASP.NET Core Blazor application language in code, use the [IXafCultureInfoService.SetCultureAsync](xref:DevExpress.ExpressApp.Blazor.Services.IXafCultureInfoService.SetCultureAsync(System.String)) method.

The call of the `SetCultureAsync` method initiates the following:

- Recreation of the [](xref:DevExpress.ExpressApp.XafApplication) in a new culture. The new culture is read from cookies in `RequestLocalizationMiddleware`. 
- Reload of the ASP.NET Core Blazor application even if there were no changes in the culture.


The code sample below demonstrates how to use `IXafCultureInfoService` to change the application localization:

[!include[<MySolution.Blazor.Server\Controllers\GermanCultureController.cs>](~/templates/platform_specific_file_path.md)]

# [C#](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp; 
using DevExpress.ExpressApp.Actions; 
using DevExpress.ExpressApp.Blazor; 
using DevExpress.ExpressApp.Blazor.Services; 
using DevExpress.Persistent.Base; 
// ...
public class GermanCultureController : ViewController { 
    BlazorApplication BlazorApplication => (BlazorApplication)Application; 
    IXafCultureInfoService CultureInfoService => (IXafCultureInfoService)BlazorApplication.ServiceProvider.GetService(typeof(IXafCultureInfoService)); 
    public GermanCultureController() { 
        SimpleAction myAction = new SimpleAction(this, "SetGermanCulture", PredefinedCategory.Edit); 
        myAction.Execute += async (s, e) => await CultureInfoService.SetCultureAsync("de-DE"); 
    } 
} 
```

***

[!include[net5-currency-symbol-note](~/templates/currency-symbol-note.md)]

## Current Culture in XAF ASP.NET Core Blazor Applications

In XAF ASP.NET Core Blazor applications, the current culture is set in the following order of priority:

1. From a user's cookies.
2. If the culture is not set in cookies, the application uses the default culture from a user's browser. The `Languages` collection in `appsettings.json` should contain this culture.
3. If the `Languages` collection does not contain the user's culture, the application uses the first culture from the collection.

When users change the current culture in the [Language Switcher](#in-ui-runtime-language-switcher), their cookies are updated with the new culture value.

The [IModelApplication.PreferredLanguage](xref:DevExpress.ExpressApp.Model.IModelApplication.PreferredLanguage) option affects only the XAF parts of the application (Action's captions, navigation, layout, etc.), and do not affect the application's culture. 

The application's current culture depends on both of the following settings:
- The `Languages` option in `appsettings.json`.
- The browser's preferred language, if the application supports multiple languages.

## Single Language Support

If your application supports only a single language, specify this language in both `appsettings.json` and [IModelApplication.PreferredLanguage](xref:DevExpress.ExpressApp.Model.IModelApplication.PreferredLanguage). You should always use the fully qualified language name, for example: `xx-YY` instead of `xx`:

# [appsettings.json](#tab/tabid-csharp)

```JSON
{
    //
    "DevExpress": {
        "ExpressApp": {
            "Languages": "de-DE"
                // ...
        }
    }
}
```
***

![localization model preferred language](~/images/localization-model-preferred-language.png)

## Localize Reports and Filter Editor in ASP.NET Core Blazor Applications

> [!NOTE]
> The technique described in this section applies to projects that use @DevExpress.Blazor.Reporting.DxDocumentViewer - the default component in XAF since v.24.1. For more information about migrating to `DxDocumentViewer`, refer to the following Breaking Change ticket: [ReportsV2Module - Migration from DxDocumentViewer to DxReportViewer](https://supportcenter.devexpress.com/ticket/details/t1228848/reportsv2module-migration-from-dxdocumentviewer-to-dxreportviewer)
> @DevExpress.Blazor.Reporting.DxReportViewer does not require additional changes. You can follow the [common scenario](#localize-an-xaf-application) of an XAF application localization.

The [Reporting](xref:113591) Module and [Filter Editor](xref:113564#filterpropertyeditor) use DevExpress [Web Reporting](xref:9814) components - you can use the same technique to localize both.

>[!NOTE]
>The example described in this section is available in the following demo and reference materials:
>* [Blazor Reporting - UI Customization API](https://github.com/DevExpress-Examples/Blazor-Reporting-UI-Customization-API)
>* [XAF's Blazor UI Demo](https://demos.devexpress.com/XAF/BlazorMainDemo/)
>* The **MainDemo** demo project. This project is installed as a part of the XAF package. The default project location is _%PUBLIC%\Documents\DevExpress Demos 23.1\Components\XAF_.

The example below shows how to localize an XAF ASP.NET Core Blazor application to German.

1. Add German language to the _YourSolutionName.Blazor.Server\appsettings.json_ file of your ASP.NET Core Blazor application.

    ```JSON
    {
        //
        "DevExpress": {
            "ExpressApp": {
                "Languages": "en-US;de-DE"
                        //
            }
        }
    }
    ```

1. Add the JSON files with localization resources to the _wwwroot\js\localization_ folder. You can obtain the JSON files from the DevExpress [Localization Service](https://localization.devexpress.com/). For additional information, refer to the following help topic: [Obtain JSON Files from the Localization Service](xref:400932#obtain-json-files-from-the-localization-service). For the purposes of this example, the following files are used:

    * _de-DE.json_
    * _dx-analytics-core.de-DE.json_
    * _dx-reporting.de-DE.json_

1. In the _YourSolutionName.Blazor.Server\Controllers_ folder, create a View Controller. In this Controller, specify the `CustomizeLocalization` handler for `DxReportDesigner`, `DxDocumentViewer`, and `FilterEditor` and set the current culture to the client using `JSInterop`.

    **File:** _YourSolutionName.Blazor.Server\Controllers\ReportLocalizationController.cs_

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Blazor.Editors;
    using DevExpress.ExpressApp.Blazor.Services;
    using DevExpress.ExpressApp.ReportsV2.Blazor;
    using Microsoft.JSInterop;

    namespace YourSolutionName.Blazor.Server.Controllers;

    public class ReportLocalizationController : ViewController<DetailView> {
        
        private readonly IXafCultureInfoService cultureInfoService;
        private readonly IJSRuntime jSRuntime;
        public ReportLocalizationController() { }
        [ActivatorUtilitiesConstructor]

        public ReportLocalizationController(IXafCultureInfoService cultureInfoService, IJSRuntime jSRuntime) {
            this.cultureInfoService = cultureInfoService;
            this.jSRuntime = jSRuntime;
        }

        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl<ReportViewerViewItem>(this, CustomizeReportViewer);
            View.CustomizeViewItemControl<ReportDesignerViewItem>(this, CustomizeReportDesigner);
            View.CustomizeViewItemControl<FilterPropertyEditor>(this, CustomizeFilterPropertyEditor);
        }

        private async void CustomizeReportDesigner(ReportDesignerViewItem propertyEditor) {
            propertyEditor.CallbacksModel.CustomizeLocalization = "ReportingLocalization.onCustomizeLocalization";
            await jSRuntime.InvokeVoidAsync("ReportingLocalization.setCurrentCulture", cultureInfoService.CurrentCulture.Name);
        }

        private async void CustomizeReportViewer(ReportViewerViewItem propertyEditor) {
            if(propertyEditor.DocumentViewerCallbacksModel is not null) {
                propertyEditor.DocumentViewerCallbacksModel.CustomizeLocalization = "ReportingLocalization.onCustomizeLocalization";
                await jSRuntime.InvokeVoidAsync("ReportingLocalization.setCurrentCulture", cultureInfoService.CurrentCulture.Name);
            }
        }

        private async void CustomizeFilterPropertyEditor(FilterPropertyEditor filterPropertyEditor) {
            filterPropertyEditor.ComponentModel.CustomizeLocalization = "ReportingLocalization.onCustomizeLocalization";
            await jSRuntime.InvokeVoidAsync("ReportingLocalization.setCurrentCulture", cultureInfoService.CurrentCulture.Name);
        }
    }
    ```
1. Add the `CustomizeLocalization` handler to the _YourSolutionName.Blazor.Server\wwwroot\js\scripts.js_ file:

    ```csharp
    window.ReportingLocalization = {
        currentCulture: null,
        setCurrentCulture: function (culture) {
            window.ReportingLocalization.currentCulture = culture;
        },
        onCustomizeLocalization: function (_, e) {
            const currentCulture = window.ReportingLocalization.currentCulture;
            if (currentCulture == "de-DE") {
                e.LoadMessages($.get("/js/localization/dx-analytics-core." + currentCulture + ".json"));
                e.LoadMessages($.get("/js/localization/dx-reporting." + currentCulture + ".json"));
                $.get("/js/localization/" + currentCulture + ".json").done(result => {
                    e.WidgetLocalization.loadMessages(result);
                }).always(() => {
                    e.WidgetLocalization.locale(currentCulture);
                })
            }
        }
    }
    ```

1. Add a jQuery library to your project's _YourSolutionName.Blazor.Server\wwwroot\js_ folder.

1. Add `scripts.js` and jQuery references to the _YourSolutionName.Blazor.Server\Pages\\_Host.cshtml_ file.

    ```CSHTML{3-4}
    <!---->
    <script src="_framework/blazor.server.js"></script>
    <script src="js/jquery.min.js"></script>
    <script src="js/scripts.js"></script>
    <!---->
    ```

>[!TIP]
> Since the components' UI is built on DevExtreme widgets, you can also use one of the techniques described in the following topic: [Localization](xref:js-DevExtreme.Guide.Common.Localization).

## Localize Scheduler Module

To localize the Scheduler module, you need to take additional steps after you follow the general localization scenario for XAF applications described in this topic.

1. Navigate to the DevExpress [Localization Service](https://localization.devexpress.com/) web page. Add or modify translations for the following strings: `SchedulerStringId.AppointmentLabel_*` and `SchedulerStringId.Caption_*`.

2. Save changes and download updated assemblies.

3. Add all assemblies from the downloaded package to the corresponding language folder in your application's _bin_ folder (for example, _\YourSolutionName.BlazorServer\bin\Debug
etX.X\fr-FR_ and _\YourSolutionName.Win\bin\Debug
etX.X\fr-FR_ for the French language).

4. Build and run the application.
