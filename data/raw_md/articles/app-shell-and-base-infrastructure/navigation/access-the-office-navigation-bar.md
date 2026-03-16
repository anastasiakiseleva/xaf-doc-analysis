---
uid: "116417"
seealso: []
title: Access the Office Navigation Bar
---
# Access the Office Navigation Bar

This topic demonstrates how to access the **Office Navigation Bar** used to show the navigation root groups when the **OutlookStyleMainRibbonForm** [Template](xref:112609) is used in a WinForms application.

Perform the following steps to access the [](xref:DevExpress.XtraBars.Navigation.OfficeNavigationBar) object and customize its settings.

1. Create a new [](xref:DevExpress.ExpressApp.WindowController) in your WinForms module.
2. The **OfficeNavigationBar** control is located on the **OutlookStyleMainRibbonForm** [Template](xref:112609) (see [IModelRootGroupsStyle.RootGroupsStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelRootGroupsStyle.RootGroupsStyle)). To access this Template after it has been created or changed, override the Controller's **OnActivated** method and subscribe to the [Frame.TemplateChanged](xref:DevExpress.ExpressApp.Frame.TemplateChanged) event of the main Window.
3. In the **TemplateChanged** event handler, cast the [Frame.Template](xref:DevExpress.ExpressApp.Frame.Template) property to the [Form](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.form) type and handle the [Form.Load](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.form.load) event.
4. In the **Form.Load** event handler, cast the sender to the **IOfficeNavigationBarHolder** type.
5. To access the **OfficeNavigationBar** object, use the **IOfficeNavigationBarHolder.OfficeNavigationBar** property. For instance, you can set the [OfficeNavigationBar.MaxItemCount](xref:DevExpress.XtraBars.Navigation.OfficeNavigationBar.MaxItemCount) property to _4_ to change the maximum number of items simultaneously displayed within the **OfficeNavigationBar** control.
6. Unsubscribe from the **TemplateChanged** event in the overridden **OnDeactivated** method when the Controller is deactivated.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Win.Templates;
using DevExpress.XtraBars.Ribbon;
//...
public class OfficeNavigationBarCustomizationController : WindowController {
    private void Frame_TemplateChanged(object sender, EventArgs e) {
        Form form = Frame.Template as Form;
        if(form != null) {
            form.Load += Form_Load;
        }
    }
    private void Form_Load(object sender, EventArgs e) {
        IOfficeNavigationBarHolder officeNavigationBarHolder = sender as IOfficeNavigationBarHolder;
        if(officeNavigationBarHolder != null) {
            officeNavigationBarHolder.OfficeNavigationBar.MaxItemCount = 4;
        }
    }
    protected override void OnActivated() {
        base.OnActivated();
        Frame.TemplateChanged += Frame_TemplateChanged;
    }
    protected override void OnDeactivated() {
        Frame.TemplateChanged -= Frame_TemplateChanged;
        base.OnDeactivated();
    }

    public OfficeNavigationBarCustomizationController() {
        TargetWindowType = WindowType.Main;
    }
}
```
***

Run the application to ensure that the maximum number of visible **OfficeNavigationBar** items is 4.
