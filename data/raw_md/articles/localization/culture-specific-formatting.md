---
uid: "113299"
seealso: []
title: Culture-Specific Formatting
owner: Ekaterina Kiseleva
---
# Culture-Specific Formatting

In XAF applications, formatting options for currency, numbers, and dates are not related to the application's UI language specified as the [Thread.CurrentUICulture](xref:System.Threading.Thread.CurrentUICulture) property value. The formatting options that are set in the current user's operating system or passed by the Internet browser are used. You can also specify a specific formatting culture or customize the default settings.

## Change the Formatting Culture
You can set another formatting culture using the [XafApplication.SetFormattingCulture](xref:DevExpress.ExpressApp.XafApplication.SetFormattingCulture(System.String)) method, which changes the [Thread.CurrentCulture](https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.currentculture#System_Threading_Thread_CurrentCulture) value. The following code demonstrates how to do this in a Windows Forms application project's _Program.cs_ file:

# [C#](#tab/tabid-csharp)

```csharp
static void Main() {
    // ...
    MySolutionWindowsFormsApplication winApplication = 
        new MySolutionWindowsFormsApplication();
    winApplication.SetFormattingCulture("de");
    // ...
}
```

***

The following image illustrates the result.

![CustomizeCultureWin2](~/images/customizeculturewin2116713.png)

[!include[net5-currency-symbol-note](~/templates/currency-symbol-note.md)]


> [!TIP]
> **For ASP.NET Core Blazor UI applications** 
>
> Refer to the following articles for information on how to change the language at runtime:
> 
> - [](xref:402956)
> - [IXafCultureInfoService](xref:DevExpress.ExpressApp.Blazor.Services.IXafCultureInfoService)

## Override the Default Formatting Options
You can override the default formatting options in the [XafApplication.CustomizeFormattingCulture](xref:DevExpress.ExpressApp.XafApplication.CustomizeFormattingCulture) event handler. The following code demonstrates how to do this in a Windows Forms application project's _Program.cs_ file:

# [C#](#tab/tabid-csharp)

```csharp
public static void Main() {
    //...
    MySolutionWindowsFormsApplication winApplication = new MySolutionWindowsFormsApplication(); 
    winApplication.CustomizeFormattingCulture += 
        new EventHandler<CustomizeFormattingCultureEventArgs>(
            winApplication_CustomizeFormattingCulture);
      // ...
}
static void winApplication_CustomizeFormattingCulture(
    object sender, CustomizeFormattingCultureEventArgs e) {
    e.FormattingCulture.NumberFormat.CurrencySymbol = "USD";
}
```

***

The following image illustrates the currency symbol before and after implementing the code above:

![CustomizeCultureWin](~/images/customizeculturewin116712.png)
