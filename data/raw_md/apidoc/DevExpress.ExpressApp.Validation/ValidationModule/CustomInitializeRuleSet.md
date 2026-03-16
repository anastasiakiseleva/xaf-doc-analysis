---
uid: DevExpress.ExpressApp.Validation.ValidationModule.CustomInitializeRuleSet
name: CustomInitializeRuleSet
type: Event
summary: Replaces the default @DevExpress.ExpressApp.Validation.ValidationModule.InitializeRuleSet implementation with custom logic.
syntax:
  content: public event EventHandler<HandledEventArgs> CustomInitializeRuleSet
seealso: []
---
To replace the `ValidationModule.InitializeRuleSet` method's default logic, handle the `ValidationModule.CustomInitializeRuleSet` event and set its `Handled` argument to `true` in your Module. The following example demonstrates how to handle this event in the _MySolution.Module_ project:

**File**: _MySolution.Module\Module.cs_.

# [C#](#tab/tabid-cs)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Validation;
using System;
using System.ComponentModel;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    // ...
    public override void Setup(XafApplication application) {
        base.Setup(application);
        application.SetupComplete += Application_SetupComplete;
    }
    private void Application_SetupComplete(object sender, EventArgs e) {
        ValidationModule vModule = (ValidationModule)Application.Modules.FindModule(typeof(ValidationModule));
        if(vModule != null) {
            vModule.CustomInitializeRuleSet += ValidationModule_CustomInitializeRuleSet;
        }
    }
    private void ValidationModule_CustomInitializeRuleSet(object sender, HandledEventArgs e) {
        // custom logic
        e.Handled = true;
    }
}
```
***