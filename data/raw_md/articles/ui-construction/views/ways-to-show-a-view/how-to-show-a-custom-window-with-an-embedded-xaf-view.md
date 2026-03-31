---
uid: "118165"
seealso:
- linkId: "118222"
- linkId: "114159"
- linkId: "118240"
title: 'How to: Show a Custom Window with an Embedded XAF View'
---
# How to: Show a Custom Window with an Embedded XAF View

The most recommended way to show a non-XAF window in a WinForms application is to embed custom controls in an XAF form (e.g. [](xref:DevExpress.ExpressApp.DashboardView)) using custom view items. However, if it is not appropriate for your case, you can embed XAF views in a custom window by creating views and adding their controls to the form. In the simplest case, it is sufficient to create a [](xref:DevExpress.ExpressApp.View) instance, configure it as required, call its [View.CreateControls](xref:DevExpress.ExpressApp.View.CreateControls) method, and add its Control to the form.

![CustomWindowWithXAFView](~/images/customwindowwithxafview127386.png)

[!include[CustomWindowWithAnEmbeddedXAFView](~/templates/customwindowwithanembeddedxafview13158.md)]

If it is necessary to show a toolbar with Actions and manage the View's behavior using the Controllers, create a nested [](xref:DevExpress.ExpressApp.Frame)'s instance, place a View in it, and add the Frame's Template to the form.

# [C#](#tab/tabid-csharp)

```csharp
void showWindowAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
    NonXAFForm form = new NonXAFForm();
    //...
    Frame frame = Application.CreateFrame(TemplateContext.NestedFrame);
    frame.CreateTemplate();
    frame.SetView(listView);
    LayoutControlItem item2 = new LayoutControlItem();
    item2.Parent = layoutControl.Root;
    item2.Text = "Persons";
    item2.Control = (Control)frame.Template;
    form.ShowDialog();        
}
```
***

![CustomWindowWithXAFView_NestedFrame](~/images/customwindowwithxafview_nestedframe127388.png)