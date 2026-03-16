---
uid: DevExpress.ExpressApp.DefaultListViewOptionsAttribute
name: DefaultListViewOptionsAttribute
type: Class
summary: Applied to business classes. Sets a number of default options for the [List Views](xref:112611) that display objects of the target type.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Interface, Inherited = true, AllowMultiple = false)]
    public class DefaultListViewOptionsAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.DefaultListViewOptionsAttribute._members
  altText: DefaultListViewOptionsAttribute Members
---
The `DefaultListViewOptions` attribute allows you to specify the following parameters:

1. A List View's master-detail mode. The default mode is `ListViewOnly`. WinForms and ASP.NET Core Blazor applications support this option.
2. A List View's [AllowEdit](xref:DevExpress.ExpressApp.View.AllowEdit) state. The default List View does not allow users to edit data.
3. The position of the new item row in a List View's [List Editor](xref:113189). The default List View does not add this row (`NewItemRowPosition.None`). The remaining `NewItemRowPosition.Top` and `NewItemRowPosition.Bottom` values are available when the List View's `AllowEdit` option is enabled.

As an alternative to `DefaultListViewOptionsAttribute`, you can set the `MasterDetailMode`, `AllowEdit`, and `NewItemRowPosition` properties of the corresponding [](xref:DevExpress.ExpressApp.Model.IModelListView) node.