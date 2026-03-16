---
uid: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.CaptionForTrue
name: CaptionForTrue
type: Property
summary: Specifies the caption for the **true** value of the current Property Editor, if this Property Editor displays a property of the Boolean type.
syntax:
  content: |-
    [ModelBrowsable(typeof(BooleanPropertyOnlyCalculator))]
    string CaptionForTrue { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the caption for the **true** value of the current Property Editor, if this Property Editor displays a property of the Boolean type.
seealso:
- linkId: DevExpress.Persistent.Base.CaptionsForBoolValuesAttribute
---
The **CaptionForTrue** property is available in the [Model Editor](xref:112582) in the following nodes: 

* **BOModel** | **_\<Class\>_** | **OwnMembers** | **Property** 
* [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] 
* **Views** | **\<ListView\>** | **Columns** | **\<BooleanColumn\>**

You can also specify the default value in code using the [](xref:DevExpress.Persistent.Base.CaptionsForBoolValuesAttribute).
