---
uid: DevExpress.ExpressApp.FrameworkSettings.DefaultSettingsCompatibilityMode
name: DefaultSettingsCompatibilityMode
type: Property
summary: Sets [configuration options and feature toggles](https://supportcenter.devexpress.com/ticket/details/t501418/default-xaf-configuration-options-and-feature-toggles) to match the default behavior of the specified version of DevExpress frameworks and libraries.
syntax:
  content: public static FrameworkSettingsCompatibilityMode DefaultSettingsCompatibilityMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.FrameworkSettingsCompatibilityMode
    description: The version of DevExpress frameworks and libraries. XAF sets configuration options and feature toggles to match the selected version's default behavior.
seealso: []
---
Set the `DefaultSettingsCompatibilityMode` property to DevExpress version to retain this version's feature toggles and configuration options when you update an application.

If you want to automatically enable all the options for the latest version, set the `DefaultSettingsCompatibilityMode` to `Latest` (the [Template Kit](xref:405447) sets this value for all applications). In this case, you do not need to specify the options individually or check their compatibility. If some of these options cause issues with your application, you can change their values after you initialize the application. Options specified directly in code have a higher priority than `DefaultSettingsCompatibilityMode`.

The following code snippets specify this property in your applications: 

# [MySolution.Win\Program.cs](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
// ...
public class Program {
    static void Main(string[] arguments) {
        FrameworkSettings.DefaultSettingsCompatibilityMode = FrameworkSettingsCompatibilityMode.v25_1;
        // ...
        MySolutionWinApplication winApplication = new MySolutionWinApplication();
        // change a feature toggle value here
        // ...
    }
    // ...
}
```

# [MySolution.Blazor\Program.cs](#tab/tabid-csharp1)

```csharp
using DevExpress.ExpressApp;
// ...
public class Program {
    public static void Main(string[] arguments) {
        FrameworkSettings.DefaultSettingsCompatibilityMode = FrameworkSettingsCompatibilityMode.v25_1;
        // change a feature toggle value here
        // ...
    }
    // ...
}
```

***
