---
uid: DevExpress.ExpressApp.XafApplication.CustomizeLanguage
name: CustomizeLanguage
type: Event
summary: Occurs after a language has been set for the application internally.
syntax:
  content: public event EventHandler<CustomizeLanguageEventArgs> CustomizeLanguage
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.CustomizeFormattingCulture
---

Handle this event to set the required language to be used by the application. To get the language currently set, use the handler's [CustomizeLanguageEventArgs.LanguageName](xref:DevExpress.ExpressApp.CustomizeLanguageEventArgs.LanguageName) property. In addition, you can get the language which is set in the user's operating system or passed by the Internet browser. For this purpose, use the handler's [CustomizeLanguageEventArgs.UserLanguageName](xref:DevExpress.ExpressApp.CustomizeLanguageEventArgs.UserLanguageName) property. To get the language which is currently set for the **Application** node's [IModelApplication.PreferredLanguage](xref:DevExpress.ExpressApp.Model.IModelApplication.PreferredLanguage) property, use the handler's [CustomizeLanguageEventArgs.PreferredLanguageName](xref:DevExpress.ExpressApp.CustomizeLanguageEventArgs.PreferredLanguageName) property. Note that the language you set in this event handler cannot be changed via the Application Model at runtime.

The following code snippet sets the default language to German:

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
// ...

namespace MySolution.Module;

public sealed partial class MySolutionModule : ModuleBase {
   // ... 
   public override void Setup(XafApplication application) { 
      base.Setup(application); 
      application.CustomizeLanguage += Application_CustomizeLanguage; 
   } 
      private void Application_CustomizeLanguage(object sender, CustomizeLanguageEventArgs e) { 
         e.LanguageName = "de"; 
         // To use the default (English) language, use the following code line instead: 
         // e.LanguageName = "en"; } 
         // ... 
      }
}
```
***

> [!TIP]
> Localize properties in the "de" language before you run the application with the code above. Otherwise, the default (English) language will be used.

You can use the [IModelApplication.PreferredLanguage](xref:DevExpress.ExpressApp.Model.IModelApplication.PreferredLanguage) property of the Application Model's **Application** node to set a language, if you do not use any conditions to determine the language the application should use.