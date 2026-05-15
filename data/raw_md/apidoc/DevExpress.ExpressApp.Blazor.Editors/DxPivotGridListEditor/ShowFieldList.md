---
uid: DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.ShowFieldList
name: ShowFieldList()
type: Method
summary: Shows the [Field List](xref:405459#field-list) popup window.
syntax:
  content: public void ShowFieldList()
seealso: []
---
`DxPivotGridListEditor` includes a **Field List** that allows users to manage component structure:
* Reorder fields within each area.
* Move fields across different areas.
* Display or hide fields. The Hidden Fields list shows hidden fields.
* Change field sort order.
* Apply field filters.
* Defer layout update.

Users can invoke the **Field List** via the [context menu](xref:DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.EnableContextMenu#remarks).

You can call the `ShowFieldList` method to display the **Field List** from code.

# [SolutionName.Blazor.Server\Controllers\AddFieldListAction.cs](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.Persistent.Base;
using MainDemo.Module.BusinessObjects;
public partial class AddFieldListAction : ObjectViewController<ListView, Paycheck> {
    public AddFieldListAction() {
            SimpleAction showFieldListAction = new SimpleAction(this, "Show Field List", PredefinedCategory.View);
            showFieldListAction.Execute += (s, e) => {
                ((DxPivotGridListEditor)View.Editor).ShowFieldList();
            };
    }
}
```
 
***

![Show Field List Action](~/images/pivot-grid/xaf-blazor-pivot-grid-show-field-list.png)