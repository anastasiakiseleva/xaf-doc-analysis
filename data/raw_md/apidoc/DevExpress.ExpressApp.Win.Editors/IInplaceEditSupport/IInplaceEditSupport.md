---
uid: DevExpress.ExpressApp.Win.Editors.IInplaceEditSupport
name: IInplaceEditSupport
type: Interface
summary: Implemented by WinForms [Property Editors](xref:112612) that can be used by [List Editors](xref:113189) for in-place editing.
syntax:
  content: public interface IInplaceEditSupport
seealso:
- linkId: DevExpress.ExpressApp.Win.Editors.IInplaceEditSupport._members
  altText: IInplaceEditSupport Members
---
List Editors that support in-place editing can visualize cell values using various controls. For instance, a DateTime value can be displayed using a drop-down date picker. If a Property Editor corresponding to the type of a cell value does not implement the **IInplaceEditSupport** interface, the cell will be rendered as a simple label. Note that in this case, your Property Editor should be a [](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor) class inheritor.

The **IInplaceEditSupport** interface exposes a single [IInplaceEditSupport.CreateRepositoryItem](xref:DevExpress.ExpressApp.Win.Editors.IInplaceEditSupport.CreateRepositoryItem) method. This method is called when an editable column of cells is created. The method must return a [](xref:DevExpress.XtraEditors.Repository.RepositoryItem) corresponding to the editor control used by the Property Editor.