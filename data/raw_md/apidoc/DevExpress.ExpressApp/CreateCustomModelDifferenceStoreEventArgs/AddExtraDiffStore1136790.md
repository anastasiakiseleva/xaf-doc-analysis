---
uid: DevExpress.ExpressApp.CreateCustomModelDifferenceStoreEventArgs.AddExtraDiffStore(System.String,DevExpress.ExpressApp.ModelStoreBase)
name: AddExtraDiffStore(String, ModelStoreBase)
type: Method
summary: Adds extra model differences storage.
syntax:
  content: public void AddExtraDiffStore(string id, ModelStoreBase store)
  parameters:
  - id: id
    type: System.String
    description: A string identifier of extra model differences storage.
  - id: store
    type: DevExpress.ExpressApp.ModelStoreBase
    description: A [](xref:DevExpress.ExpressApp.ModelStoreBase) extra model differences storage.
seealso: []
---

**File:** _SolutionName.Blazor.Server\BlazorModule.cs_

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.BaseImpl.EF;
using SolutionName.Blazor.Server.Controllers;

namespace SolutionName.Blazor.Server;

public sealed class SolutionNameBlazorModule : ModuleBase {
    public SolutionNameBlazorModule() {
        Description = "XAF Blazor Demo module";    }
    // ...
    private void Application_CreateCustomUserModelDifferenceStore(object sender, CreateCustomModelDifferenceStoreEventArgs e) {
        var application = (XafApplication)sender;        
        // Main store: Database-based user model differences
        e.Store = new ModelDifferenceDbStore(application, typeof(ModelDifference), false, "Blazor");        
        // Add extra file-based store for shared customizations
        string extraDiffFile = Path.Combine(
            Path.GetDirectoryName(Application.ExecutablePath),
            "SharedCustomizations.xafml"
        );        
        if (File.Exists(extraDiffFile)) {
            e.AddExtraDiffStore("SharedCustomizations", new FileModelStore(extraDiffFile));
        }        
        e.Handled = true;
    }
    // ...
}
```