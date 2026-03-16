---
uid: DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode
name: ModificationsHandlingMode
type: Property
summary: Specifies the WinForms application behavior when a user modifies data and then changes the current object or closes the View.
syntax:
  content: |-
    [DefaultValue(ModificationsHandlingMode.Confirmation)]
    public ModificationsHandlingMode ModificationsHandlingMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SystemModule.ModificationsHandlingMode
    description: A [](xref:DevExpress.ExpressApp.SystemModule.ModificationsHandlingMode) enumeration value that specifies the WinForms application behavior when a user modifies data and then changes the current object or closes the View.
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsCheckingMode
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/bc5122/winforms-the-save-confirmation-dialog-is-not-shown-when-closing-detailview-for-a-new
  altText: The save confirmation dialog is not shown when closing DetailView for a new unmodified object
---
To specify the **ModificationsHandlingMode** in your code, inherit the [](xref:DevExpress.ExpressApp.Win.SystemModule.WinModificationsController) and override the **OnActivated** method.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.SystemModule;
using DevExpress.ExpressApp.Win.SystemModule;
// ...
public class MyWinModificationsController : WinModificationsController {
    protected override void OnActivated() {
        base.OnActivated();
        if (View is ListView)
            this.ModificationsHandlingMode = ModificationsHandlingMode.AutoCommit;
    }
}
```
***

Note that a custom value should be assigned after the base class' **OnActivated** method is called, as the default value is calculated by this method. Avoid changing the **ModificationsHandlingMode** by accessing the [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController) from a custom controller via the [Frame.GetController\<ControllerType>](xref:DevExpress.ExpressApp.Frame.GetController``1) method. Your custom controller may be activated before the **ModificationsController** activation, and your customization will be ignored.
