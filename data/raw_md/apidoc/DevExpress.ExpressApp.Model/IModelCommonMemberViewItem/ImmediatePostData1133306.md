---
uid: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.ImmediatePostData
name: ImmediatePostData
type: Property
summary: Specifies whether the property editor's control value should be passed to the property of a bound object as soon as possible when the value is changed by user. For instance, it allows you to enforce updating other displayed values that are calculated based on the current property.
syntax:
  content: |-
    [ModelBrowsable(typeof(TagBoxListPropertyEditorCalculator))]
    bool ImmediatePostData { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true** if the property editor's control value should be passed as soon as possible; otherwise, **false**."
seealso:
- linkId: DevExpress.Persistent.Base.ImmediatePostDataAttribute
---
This property derives its default value from the **ImmediatePostData** attribute and can be accessed from the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node. The property sets the default value for [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] | **ImmediatePostData** and [!include[Node_Views_ListView_Columns_Column](~/templates/node_views_listview_columns_column111388.md)] | **ImmediatePostData**.

Refer to the [](xref:DevExpress.Persistent.Base.ImmediatePostDataAttribute) topic for details.