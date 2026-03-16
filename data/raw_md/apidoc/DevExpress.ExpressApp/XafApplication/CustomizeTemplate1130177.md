---
uid: DevExpress.ExpressApp.XafApplication.CustomizeTemplate
name: CustomizeTemplate
type: Event
summary: Occurs after a [Template](xref:112609) has been created.
syntax:
  content: public event EventHandler<CustomizeTemplateEventArgs> CustomizeTemplate
seealso:
- linkId: "112696"
- linkId: "112618"
---
Handle this event to customize a particular template. Use the handler's [CustomizeTemplateEventArgs.Context](xref:DevExpress.ExpressApp.CustomizeTemplateEventArgs.Context) or [CustomizeTemplateEventArgs.Template](xref:DevExpress.ExpressApp.CustomizeTemplateEventArgs.Template) parameter. For more information, refer to the following topics:
* [Template Customization](xref:112696)
* [How to: Access the Navigation Control](xref:112617).

The following code snippet demonstrates how to handle the `CustomizeTemplate` event to hide toolbars that accompany a nested [List View](xref:112611) in ASP.NET Core Blazor and Windows Forms XAF applications:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Templates;
//...
public class MyHideToolbarController : Controller {
    protected override void OnActivated() {
        base.OnActivated();
        Application.CustomizeTemplate += Application_CustomizeTemplate;
    }
    void Application_CustomizeTemplate(object sender, CustomizeTemplateEventArgs e) {
        if (e.Context == TemplateContext.NestedFrame) {
            ISupportActionsToolbarVisibility template = 
                e.Template as ISupportActionsToolbarVisibility;
            if (template != null) template.SetVisible(false);
        }
    }
    protected override void OnDeactivated() {
        Application.CustomizeTemplate -= Application_CustomizeTemplate;
        base.OnDeactivated();
    }
}
```
***

In Windows Forms applications, this event is raised after XAF creates a [Template](xref:112609) and before the template is assigned to a [Window](xref:112608).