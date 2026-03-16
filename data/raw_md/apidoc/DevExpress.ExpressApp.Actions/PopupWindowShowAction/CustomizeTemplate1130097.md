---
uid: DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizeTemplate
name: CustomizeTemplate
type: Event
summary: Occurs when setting a [Template](xref:112609) for a Pop-up Window Show Action's pop-up Window.
syntax:
  content: public event EventHandler<CustomizeTemplateEventArgs> CustomizeTemplate
seealso:
- linkId: "112696"
- linkId: "112618"
---
A Pop-up Window Show Action displays a pop-up [Window](xref:112608) with a specified [View](xref:112611). In a Windows Forms application, the `PopupForm` or `LookupForm` Template is used, depending on whether a Detail or List View is included. ASP.NET Core Blazor uses `PopupWindowTemplate`. To customize the pop-up Window's Template, handle the `CustomizeTemplate` event that occurs after assigning the Template to the Window. Use the handler's [CustomizeTemplateEventArgs.Template](xref:DevExpress.ExpressApp.CustomizeTemplateEventArgs.Template) parameter to access the Template.

The following code snipped demonstrates a sample `CustomizeTemplate` event handler implementation. The code displays Actions from the `PopupActions` category at the top of the pop-up window, in Windows Forms applications.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Templates;
using DevExpress.ExpressApp.Win.Templates.ActionContainers;
using DevExpress.XtraLayout;
//...
private void MyPopupAction_CustomizeTemplate(object sender, CustomizeTemplateEventArgs e) {
    foreach (IActionContainer container in e.Template.GetContainers()) {
        if (container.ContainerId == "PopupActions" && container is ButtonsContainer) {
            LayoutControl layoutControl = (LayoutControl)((ButtonsContainer)container).Parent;
            layoutControl.Dock = System.Windows.Forms.DockStyle.Top;
            break;
        }
    }
}
```

See more examples in the following articles:
[How to: Adjust Window Size and Style (WinForms)](xref:117231)
[How to: Adjust the Size and Style of Pop-up Dialogs (Blazor)](xref:404014)
***