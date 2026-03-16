---
uid: '400836'
title: 'Localize a Splash Form (WinForms)'
owner: Vera Ulitina
---
# Localize a Splash Form (WinForms)

Use one of the approaches below to localize [splash forms](xref:112680) that have customizable text: a [Splash Screen](xref:10823) or a [Wait Form](xref:10824).

> [!Tip]
> Do not use the [standard XAF localization approach](xref:112595) to localize splash forms. This approach requires the [Application Model](xref:112580). The Application Model is not available on startup, when some splash forms are shown.

## Use the SetDisplayText Method to Localize ISplash Descendants

Use this approach for [splash forms](xref:112680) that support the [](xref:DevExpress.ExpressApp.Win.ISplash) interface.

Open the _Program.cs_ (_Program.vb_) file in the [WinForms Application project](xref:118045). Call the [ISplash.SetDisplayText](xref:DevExpress.ExpressApp.Win.ISplash.SetDisplayText(System.String)) method before methods that start the application. Specify the text you require. A Splash Screen or a Wait Form that is currently open displays this text.
	
# [C#](#tab/tabid-csharp)

```csharp
static class Program {
    // ...
    static void Main() {
        // ...
        MySolutionWindowsFormsApplication winApplication = 
            new MySolutionWindowsFormsApplication();
        // ...
        try {
            winApplication.SplashScreen.SetDisplayText("Custom Text");
            winApplication.Setup();
            winApplication.Start();
            // ...
        }
    }
}
```
***

You can also customize text as described in the [Customize the Default Splash Screen](xref:400971#customize-the-default-splash-screen) section.

## Use the UpdateStatus Method to Localize ISupportUpdateSplash Descendants

To localize [splash forms](xref:112680) that support the @DevExpress.ExpressApp.Win.ISupportUpdateSplash interface, use one of the following approaches:

* [Localize Status Messages Manually](#localize-status-messages-manually)
* [Use Satellite Assemblies to Localize Status Messages](#use-satellite-assemblies-to-localize-status-messages)

### Localize Status Messages Manually

Access the _WinApplication.cs_ (_WinApplication.vb_) file in the [WinForms Application project](xref:118045). Override the [WinApplication.UpdateStatus](xref:DevExpress.ExpressApp.Win.WinApplication.UpdateStatus(System.String,System.String,System.String,System.Object[])) method. To determine the current context, compare the _context_ parameter with one of the **ApplicationStatusMessageId** enumeration values.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Localization;
// ...
namespace MySolution.Win {
    public partial class MySolutionWindowsFormsApplication : WinApplication {
        // ...
        public override void UpdateStatus(
            string context, string title, string message, params object[] additionalParams) {
            if(context == ApplicationStatusMesssageId.ApplicationSetupStarted.ToString()) {
                title = "My localized title";
                message = "My localized message";
            }
            base.UpdateStatus(context, title, message, additionalParams);
        }
    }
}

```
***

### Use Satellite Assemblies to Localize Status Messages

XAF can retrieve localized messages from the _DevExpress.ExpressApp.v<:xx.x:>.resources.dll_ satellite assembly and assign them to the **ApplicationStatusMessageId** enum values. 

Satellite assemblies for German (**de**), Spanish (**es**), and Japanese (**ja**) languages are installed in %PROGRAMFILES%\DevExpress <:xx.x:>\Components\Bin folder and GAC. You can download satellite assemblies for other languages from the [DevExpress Localization Service](xref:16235). Refer to the [How to: Install an assembly into the global assembly cache](https://learn.microsoft.com/en-us/dotnet/framework/app-domains/how-to-install-an-assembly-into-the-gac) article for more information on how to register satellite assemblies in the GAC.
