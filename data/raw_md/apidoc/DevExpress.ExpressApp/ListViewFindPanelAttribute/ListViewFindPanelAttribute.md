---
uid: DevExpress.ExpressApp.ListViewFindPanelAttribute
name: ListViewFindPanelAttribute
type: Class
summary: Applied to business classes. Specifies whether a [List View](xref:112611#list-view)'s @DevExpress.ExpressApp.Win.Editors.GridListEditor shows the [Find Panel](xref:8869) at runtime.
syntax:
  content: 'public class ListViewFindPanelAttribute : Attribute'
seealso:
- linkId: DevExpress.ExpressApp.ListViewFindPanelAttribute._members
  altText: ListViewFindPanelAttribute Members
---
Apply this attribute to a business class as shown below if you need to enable the Find Panel and Search Panel in the @DevExpress.ExpressApp.Win.Editors.GridListEditor's [List Views](xref:112611#list-view). :

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
[DefaultClassOptions, ListViewFindPanel]
  public class Contact : Person, IMapsMarker {
    // ...
}
```
***

When a business class has the **ListViewFindPanelAttribute** and [Find Panel](xref:8869) (WinForms), the List View's GridListEditor displays the panels at runtime. Alternatively, you can use the @DevExpress.ExpressApp.SystemModule.IModelClassShowFindPanel.DefaultListViewShowFindPanel or @DevExpress.ExpressApp.SystemModule.IModelListViewShowFindPanel.ShowFindPanel properties to activate the panels.

The Find Panel and the Search Panel allow the end-user to search and filter List Views.

**WinForms**

![WinForms-ListViewFindPanelAttribute](~/images/WinForms-ListViewFindPanelAttribute.png)
