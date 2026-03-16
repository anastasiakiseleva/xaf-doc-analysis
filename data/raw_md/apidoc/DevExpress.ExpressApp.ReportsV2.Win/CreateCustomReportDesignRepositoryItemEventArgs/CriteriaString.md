---
uid: DevExpress.ExpressApp.ReportsV2.Win.CreateCustomReportDesignRepositoryItemEventArgs.CriteriaString
name: CriteriaString
type: Property
summary: Specifies the criteria that filters the collection of report parameter objects.
syntax:
  content: public string CriteriaString { get; set; }
  parameters: []
  return:
    type: System.String
    description: The criteria that filters the collection of report parameter objects.
seealso: []
---
The following example demonstrates how to set this property:

[!include[<MySolution.Win\WinModule.cs>](~/templates/platform_specific_file_path.md)]

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ReportsV2.Win;
using DevExpress.Persistent.Base.ReportsV2;
// ...
public sealed partial class MySolutionWindowsFormsModule : ModuleBase {
    // ...
    public MySolutionWindowsFormsModule() {
        InitializeComponent();
        ReportsWindowsFormsModuleV2.CreateCustomReportDesignRepositoryItem += 
        ReportsWindowsFormsModuleV2_CreateCustomReportDesignRepositoryItem;
    }
    private void ReportsWindowsFormsModuleV2_CreateCustomReportDesignRepositoryItem(object sender, 
    CreateCustomReportDesignRepositoryItemEventArgs e) {
        e.CriteriaString = "[MyProperty] = True";
    }
}
```
***

The image below demonstrates the result:

![The filtered list of report parameter objects](~/images/CreateCustomReportDesignRepositoryItemEventArgs_CriteriaString.png)
