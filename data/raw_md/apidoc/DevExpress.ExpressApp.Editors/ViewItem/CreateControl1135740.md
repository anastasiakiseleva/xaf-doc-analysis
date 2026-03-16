---
uid: DevExpress.ExpressApp.Editors.ViewItem.CreateControl
name: CreateControl()
type: Method
summary: Creates a control that represents the current View Item in a UI.
syntax:
  content: public void CreateControl()
seealso: []
---
The Detail View (see [ViewItem.View](xref:DevExpress.ExpressApp.Editors.ViewItem.View)) automatically calls this method when the detail form is created. You do not have to call it manually.

When implementing a descendant of the [](xref:DevExpress.ExpressApp.Editors.ViewItem) class, override the `CreateControlCore` method to create the required control. This method is called by the **CreateControl** method.

# [C#](#tab/tabid-csharp)

```csharp
public class MyViewItem : ViewItem {
   protected override object CreateControlCore() {
      DevExpress.XtraEditors.LabelControl result = new DevExpress.XtraEditors.LabelControl();
      result.Dock = DockStyle.Fill;
      result.Text = Info.GetAttributeValue("Text");
      result.AutoSizeMode = LabelAutoSizeMode.Vertical;
      return result;
   }
}
```
***

To access the control returned by the `Control` property, use the [ViewItem.Control](xref:DevExpress.ExpressApp.Editors.ViewItem.Control) property. If you need to execute a custom action when this control is created, use the @DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl* extension method.