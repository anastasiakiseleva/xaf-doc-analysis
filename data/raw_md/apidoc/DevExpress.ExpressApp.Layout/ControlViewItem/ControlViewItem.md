---
uid: DevExpress.ExpressApp.Layout.ControlViewItem
name: ControlViewItem
type: Class
summary: A [View Item](xref:112612) that displays a specific unbound control in a UI.
syntax:
  content: 'public class ControlViewItem : ViewItem, IComplexViewItem'
seealso:
- linkId: DevExpress.ExpressApp.Layout.ControlViewItem._members
  altText: ControlViewItem Members
- linkId: DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem
- linkId: DevExpress.ExpressApp.Editors.ViewItemAttribute
---
In certain scenarios, you may need to add an unbound control to a [Detail View](xref:112611). To do this, add a [](xref:DevExpress.ExpressApp.Model.IModelControlDetailItem) child node to the required [!include[Node_Views_DetailView_Items](~/templates/node_views_detailview_items111383.md)] node.

![HT_Add_Button2_1](~/images/ht_add_button2_1117523.png)

Set the child node's [IModelControlDetailItem.ControlTypeName](xref:DevExpress.ExpressApp.Model.IModelControlDetailItem.ControlTypeName) property to the required control's type. To handle the control's events, implement a custom [Controller](xref:112621) that is activated for the View containing the **ControlViewItem**.

For an example of using the **ControlViewItem**, refer to [How to: Create a Custom Control Detail Item](xref:113652) topic.