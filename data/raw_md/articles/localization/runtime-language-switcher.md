---
uid: "403027"
title: Runtime Language Switcher
owner: Alexey Kazakov
seealso:
  - linkId: DevExpress.ExpressApp.Blazor.Services.IXafCultureInfoService
---
# Runtime Language Switcher

The Language Switcher is displayed in:

- The login page

    ![localization ASP.NET Core Blazor login page language switcher](~/images/localization-blazor-login-page-language-switcher.png)
- The settings menu

    ![|localization ASP.NET Core Blazor settings language switcher|](~/images/localization-blazor-settings-language-switcher.png)

To enable the runtime language switcher, set the `DevExpress: ExpressApp: ShowLanguageSwitcher` value to `True` in `appsettings.json`:

``` 
"DevExpress": { 
    "ExpressApp": { 
        "Languages": "en;de", 
        "ShowLanguageSwitcher": true,  
    } 
} 
```

The `Languages` section must contain at least 2 supported languages. These languages will be displayed in the Language switcher's drop-down list.


The language name is retrieved from `CultureInfo.NativeName`.


> [!NOTE]
> 
> The runtime language switcher requires that `IModelApplication.PreferredLanguage` is set to `(User language)`. 

