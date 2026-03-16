---
uid: DevExpress.ExpressApp.Editors.ListEditor.ProtectedContentText
name: ProtectedContentText
type: Property
summary: Specifies the text that is used by a [List Editor](xref:113189) to display a property which is prohibited for viewing by the current user.
syntax:
  content: public string ProtectedContentText { get; set; }
  parameters: []
  return:
    type: System.String
    description: A `string` value that represents text to be displayed by a List Editor if a user does not have permission to view an object's property. The default value is specified by the `ProtectedContentText` property of the Application Model's **Application** node.
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelApplication.ProtectedContentText
example:
- '[!include[](~/templates/listeditor.protectedcontenttext11912.md)]'
---
Use this property to set the text that will be displayed instead of an actual value of a property that is prohibited for viewing by the current user by the [Security System](xref:113366). This text is not available at the data source level. Protected properties return default type values instead of actual values. The `null` value is returned for reference properties, zero - for integer properties, `DateTime.MinValue` - for `DateTime` properties.