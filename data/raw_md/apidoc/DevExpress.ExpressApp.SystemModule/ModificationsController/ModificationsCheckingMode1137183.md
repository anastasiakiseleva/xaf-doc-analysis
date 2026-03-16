---
uid: DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsCheckingMode
name: ModificationsCheckingMode
type: Property
summary: Applicable to List Views. Specifies when the modifications made in an editable List View are committed.
syntax:
  content: |-
    [DefaultValue(ModificationsCheckingMode.Always)]
    public ModificationsCheckingMode ModificationsCheckingMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SystemModule.ModificationsCheckingMode
    description: A [](xref:DevExpress.ExpressApp.SystemModule.ModificationsCheckingMode) enumeration value that specifies when the modifications made in an editable List View are committed.
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode
---
This property is set to **Always** in all XAF projects. 

In WinForms applications, the value is overridden and set to **OnCloseOnly** for [List Views](xref:112611#list-view). This means, data modifications are committed when a List View is closed. Set the **ModificationsCheckingMode** property to [ModificationsCheckingMode.Always](xref:DevExpress.ExpressApp.SystemModule.ModificationsCheckingMode.Always) to commit modifications each time a record is modified. Changes will be committed and confirmation will be displayed when a user proceeds to the next record in the editable List View.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.SystemModule;
using DevExpress.ExpressApp.Win.SystemModule;
// ...
public class MyWinModificationsController : WinModificationsController {
    protected override void OnActivated() {
        base.OnActivated();
        this.ModificationsCheckingMode = ModificationsCheckingMode.Always;
    }
}
```
***