---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.ReadValue
name: ReadValue()
type: Method
summary: Reads a value to the current Property Editor's control.
syntax:
  content: public void ReadValue()
seealso: []
---
This method calls the **ReadValueCore** method that does nothing in this class. To implement reading the property's value to the Property Editor's control, override the **ReadValueCore** method in your descendant of the [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) class. In addition, you can override the **CanReadValue** method to indicate whether the property's value can now be read to the control. In the **PropertyEditor** class, this method checks whether the [ViewItem.Control](xref:DevExpress.ExpressApp.Editors.ViewItem.Control) property is not set to **null** (**Nothing**).

After the property value is read to the Property Editor's control, the [PropertyEditor.ValueRead](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ValueRead) event is raised.