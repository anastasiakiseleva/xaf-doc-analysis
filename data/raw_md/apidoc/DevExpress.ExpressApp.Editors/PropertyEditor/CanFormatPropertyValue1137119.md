---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.CanFormatPropertyValue
name: CanFormatPropertyValue
type: Property
summary: Gets whether or not the [](xref:DevExpress.ExpressApp.Editors.PropertyEditor)'s value can be formatted.
syntax:
  content: public virtual bool CanFormatPropertyValue { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the value can be formatted; otherwise - **false**. The default is **false**.'
seealso: []
---
The **CanFormatPropertyValue** always returns **false**. This behavior should be overridden in descendants that use the [PropertyEditor.DisplayFormat](xref:DevExpress.ExpressApp.Editors.PropertyEditor.DisplayFormat) and/or [PropertyEditor.EditMask](xref:DevExpress.ExpressApp.Editors.PropertyEditor.EditMask) properties to format a property value.

A custom PropertyEditor class will use the default formatting from the Application Model only if it overrides the **CanFormatPropertyValue** property in order to return **true** there.