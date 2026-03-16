---
uid: DevExpress.ExpressApp.Validation.ValidationModule.InitializeRuleSet
name: InitializeRuleSet()
type: Method
summary: Initializes the [](xref:DevExpress.Persistent.Validation.RuleSet) object assigned to the `DevExpress.Persistent.Validation.Validator.RuleSet` property.
syntax:
  content: public void InitializeRuleSet()
seealso: []
---

> [!NOTE]
>
> In v23.1 and higher, you do not need to use the `InitializeRuleSet` method in .NET Core-based applications (both Blazor and WinForms). All required initialization is done automatically.

The [Validation Module](xref:113684) calls this method on logon and when a user closes the [Model Editor at runtime](xref:113326). To initialize validation rules before the main window is displayed and a user logs into the application, follow the steps below:
1. Override the [ModuleBase.Setup](xref:DevExpress.ExpressApp.ModuleBase.Setup*) method in a platform-specific (_MySolution.Blazor.Server_, _MySolution.Win_, _MySolution.Web_) or platform-agnostic (_MySolution.Module_)project.
2. In this overridden method, handle the [XafApplication.SetupComplete](xref:DevExpress.ExpressApp.XafApplication.SetupComplete) event.
3. In the event handler, access the Validation Module and call the `InitializeRuleSet` method.

**File**: _MySolution.Module\Module.cs_.

# [C#](#tab/tabid-csharp)
```csharp{12}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Validation;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    public override void Setup(XafApplication application) {
        base.Setup(application);
        application.SetupComplete += Application_SetupComplete;
    }
    private void Application_SetupComplete(object sender, EventArgs e) {
        ValidationModule module = (ValidationModule)Application.Modules.FindModule(typeof(ValidationModule));
        if(module != null) {
            module.InitializeRuleSet();
        }
    }
    // ...
}
```
***