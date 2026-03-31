---
uid: DevExpress.ExpressApp.Editors.ColumnsListEditor
name: ColumnsListEditor
type: Class
summary: Represents the base class for built-in grid-like [List Editors](xref:113189).
syntax:
  content: 'public abstract class ColumnsListEditor : ListEditor, ISupportToolTip'
seealso:
- linkId: DevExpress.ExpressApp.Editors.ColumnsListEditor._members
  altText: ColumnsListEditor Members
---
The **ColumnsListEditor** serves as the base class for List Editors that represent object collections in the form of a grid. In such grids, a row represents a particular object and columns represent the object properties.

Compared to the [](xref:DevExpress.ExpressApp.Editors.ListEditor) class, the **ColumnsListEditor** class introduces members dealing with columns such as the [ColumnsListEditor.AddColumn](xref:DevExpress.ExpressApp.Editors.ColumnsListEditor.AddColumn(DevExpress.ExpressApp.Model.IModelColumn)) and `DevExpress.ExpressApp.Editors.ColumnsListEditor.RemoveColumn` methods. Note that the **ColumnsListEditor**'s members are not intended to be used in your code and are used internally by **XAF**. To customize the columns displayed by a List Editor for a particular [List View](xref:112611), use the [Application Model](xref:112580)'s corresponding Views | ListView | Columns node. To learn how to customize the Application Model in code, refer to the [Access the Application Model in Code](xref:112810).