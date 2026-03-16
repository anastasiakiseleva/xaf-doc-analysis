---
uid: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.NullText
name: NullText
type: Property
summary: Specifies the text that a [Property Editor](xref:113097) displays when its value is *null* or [String.Empty](xref:System.String.Empty). WinForms Property Editors also show this text if their value is [DBNull.Value](xref:System.DBNull.Value)
syntax:
  content: |-
    [ModelBrowsable(typeof(NullTextVisibilityCalculator))]
    string NullText { get; set; }
  parameters: []
  return:
    type: System.String
    description: A text that a Property Editor displays when its value is *null*, [String.Empty](xref:System.String.Empty), or [DBNull.Value](xref:System.DBNull.Value) (WinForms only).
seealso: []
---
The following Model Editor nodes allow you to specify this property:

* [!include[Template Title](~/templates/node_views_detailview_items111383.md)]&nbsp;|&nbsp;**\<*ViewItem*>**  
    ![Null text in Model Editor](~/images/ViewItem_NullText.png)
* **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_**  
    ![Null text in Model Editor](~/images/OwnMembers_NullText.png)

The following image illustrates the result.

![Null text in Editor](~/images/NullText_UI_Anniversary.png)

> [!Note]
> You can also set the [PropertyEditor.NullText](xref:DevExpress.ExpressApp.Editors.PropertyEditor.NullText) property in code. Refer to its description to see an example.
