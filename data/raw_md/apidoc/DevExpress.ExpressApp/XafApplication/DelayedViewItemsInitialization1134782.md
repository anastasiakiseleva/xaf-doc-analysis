---
uid: DevExpress.ExpressApp.XafApplication.DelayedViewItemsInitialization
name: DelayedViewItemsInitialization
type: Property
summary: Indicates whether [View Items](xref:112612) controls are initialized immediately when a [View](xref:112611) is created.
syntax:
  content: |-
    [Browsable(false)]
    [DefaultValue(true)]
    public bool DelayedViewItemsInitialization { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, if View Item controls are initialized once they are visible to end-users; `false`, if View Item controls are initialized once a View is created. The default value is `true`.'
seealso:
- linkId: DevExpress.ExpressApp.View.ControlsCreated
- linkId: DevExpress.ExpressApp.ViewController.ViewControlsCreated
---
When this property is set to true, controls corresponding to View Items will not be created immediately after the root control of the View is created. Instead, they will be created only once they are visible to end-users. Complex Property Editors will also create their [Frame](xref:112608) and View only when their respective controls are created. Since their Frame, View and Control properties are null before the editors are visible, that leads to a potential problem in your code. So, instead of handling the [View.ControlsCreated](xref:DevExpress.ExpressApp.View.ControlsCreated) and [ViewController.ViewControlsCreated](xref:DevExpress.ExpressApp.ViewController.ViewControlsCreated) events to access a View Item's control, you should ensure that you are not accessing the properties mentioned above before the controls are created.  In order to bypass any possible problems, you should handle the [ViewItem.ControlCreated](xref:DevExpress.ExpressApp.Editors.ViewItem.ControlCreated) event of the required View Item or test whether the properties accessed are null.

You can change the default value of the `DelayedViewItemsInitialization` property in the [](xref:DevExpress.ExpressApp.XafApplication) descendant's constructor implemented in the default WinForms and ASP.NET Core Blazor application project. For instance, here is the code for the Windows Forms application.

# [C#](#tab/tabid-csharp)

```csharp
public partial class MySolutionWindowsFormsApplication : WinApplication {
    public MySolutionWindowsFormsApplication() {
        //...
        DelayedViewItemsInitialization = false;
    }
    // ...
}
```
***

To change this behavior for an individual View, use the [CompositeView.DelayedItemsInitialization](xref:DevExpress.ExpressApp.CompositeView.DelayedItemsInitialization) property.