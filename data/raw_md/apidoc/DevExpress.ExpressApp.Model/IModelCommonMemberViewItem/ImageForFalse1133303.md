---
uid: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.ImageForFalse
name: ImageForFalse
type: Property
summary: Specifies the name of the image that is displayed for the property's False value.
syntax:
  content: |-
    [ModelBrowsable(typeof(BooleanPropertyOnlyCalculator))]
    string ImageForFalse { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the name of the image that is displayed for the property's False value.
seealso:
- linkId: DevExpress.Persistent.Base.ImagesForBoolValuesAttribute
---
This property is considered for Boolean type properties. The **ImageForFalse** property is available in the [Model Editor](xref:112582) in the following nodes: 

* **BOModel** | **_\<Class\>_** | **OwnMembers** | **Property** 
* [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] 
* **Views** | **\<ListView\>** | **Columns** | **\<BooleanColumn\>**

You can also specify the default value in code using the [](xref:DevExpress.Persistent.Base.ImagesForBoolValuesAttribute).
