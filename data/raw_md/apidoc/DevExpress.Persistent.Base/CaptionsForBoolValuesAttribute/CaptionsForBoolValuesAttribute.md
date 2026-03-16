---
uid: DevExpress.Persistent.Base.CaptionsForBoolValuesAttribute
name: CaptionsForBoolValuesAttribute
type: Class
summary: Applied to Boolean business class properties. Specifies captions used to display the target property's values.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field, Inherited = true, AllowMultiple = false)]
    public class CaptionsForBoolValuesAttribute : ModelExportedValuesAttribute
seealso:
- linkId: DevExpress.Persistent.Base.CaptionsForBoolValuesAttribute._members
  altText: CaptionsForBoolValuesAttribute Members
---
By default, Boolean properties are represented in a UI via a check box:

![BooleanPropertyEditor_1](~/images/booleanpropertyeditor_1116337.png)

When the **CaptionsForBoolValuesAttribute** is applied to a property, it is displayed via a combo box containing the specified captions:

![BooleanPropertyEditor_2](~/images/booleanpropertyeditor_2116338.png)

The attribute's parameter values are assigned to the [IModelCommonMemberViewItem.CaptionForFalse](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.CaptionForFalse) and [IModelCommonMemberViewItem.CaptionForTrue](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.CaptionForTrue) properties of the Application Model's **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node. Additionally, these attribute values are set for the same properties of the [!include[Node_Views_ListView_Columns_Column](~/templates/node_views_listview_columns_column111388.md)] and [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] nodes. You can can set other values to these properties, in the appropriate node.

To add images to the combo box, you can apply the [](xref:DevExpress.Persistent.Base.ImagesForBoolValuesAttribute):

![BooleanPropertyEditor_3](~/images/booleanpropertyeditor_3116339.png)