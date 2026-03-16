---
uid: DevExpress.Persistent.Base.ImagesForBoolValuesAttribute
name: ImagesForBoolValuesAttribute
type: Class
summary: Applied to Boolean business class properties. Specifies the names of the images used to display the target property's values.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field, Inherited = true, AllowMultiple = false)]
    public class ImagesForBoolValuesAttribute : ModelExportedValuesAttribute
seealso:
- linkId: DevExpress.Persistent.Base.ImagesForBoolValuesAttribute._members
  altText: ImagesForBoolValuesAttribute Members
---
By default, Boolean properties are represented in a UI via a check box:

![BooleanPropertyEditor_1](~/images/booleanpropertyeditor_1116337.png)

When the **ImagesForBoolValuesAttribute** is applied to a property, it is displayed via a combo box containing the specified images:

![BooleanPropertyEditor_4](~/images/booleanpropertyeditor_4116340.png)

The attribute's parameter values are assigned to the [IModelCommonMemberViewItem.ImageForFalse](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.ImageForFalse) and [IModelCommonMemberViewItem.ImageForTrue](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.ImageForTrue) properties of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node. Additionally, these property values are set for the same properties of the **Views** | **ListView** | **Columns** | **Column** and [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] nodes. You can set other values to these properties, in the appropriate node.

To add captions to the combo box, you can apply the [](xref:DevExpress.Persistent.Base.CaptionsForBoolValuesAttribute):

![BooleanPropertyEditor_3](~/images/booleanpropertyeditor_3116339.png)

For information on how to add and override images in **XAF** applications, refer to the following topics:

* [](xref:404201)
* [](xref:404209)
* [](xref:112792)