---
uid: DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute
name: ListViewFilterAttribute
type: Class
summary: Specifies the filters that an end-user will be able to apply to the List View that displays the target class'objects.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Struct | AttributeTargets.Interface, AllowMultiple = true)]
    public class ListViewFilterAttribute : Attribute
seealso:
- linkId: "112809"
- linkId: DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute._members
  altText: ListViewFilterAttribute Members
---
The following example demonstrates how to apply the **ListViewFilter** attribute: 

[!include[ListViewFilterAttribute_example](~/templates/ListViewFilterAttribute_example.md)]

The **XAF** is shipped with the **SetFilter** Action (see [FilterController.SetFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.SetFilterAction)). This Action is displayed as a combo box, whose items represent filter captions. When an end-user selects an item, the current List View is filtered.

![Read-OnlyParameters for List Views_Result](~/images/read-onlyparameters-for-list-views_result115588.png)

To add items to this Action, apply the **ListViewFilter** attribute to the business class whose List Views are to be filtered. Pass the required [ListViewFilterAttribute.Caption](xref:DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute.Caption), [ListViewFilterAttribute.Criteria](xref:DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute.Criteria), [ListViewFilterAttribute.Description](xref:DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute.Description) and other filter details via the attribute's parameters.

You can add as many **ListViewFilter** attributes as you wish to the target business class. The filters specified by these attributes will be loaded to the [Application Model](xref:112580). The **Filter** child nodes will be added to the corresponding [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] | **Filters** node. You can modify these filters via the [Model Editor](xref:112582). In addition, you can add new filters via the [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] | **Filters** node's context menu. For details, refer to the [Filters Application Model Node](xref:112992) topic.

[!example[XAF - How to show filter dialog before a List View](https://github.com/DevExpress-Examples/XAF_how-to-show-filter-dialog-before-listview)]
