---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.NullText
name: NullText
type: Property
summary: Specifies the text that a [Property Editor](xref:113097) displays when its value is *null* or [String.Empty](xref:System.String.Empty). WinForms Property Editors also show this text if their value is [DBNull.Value](xref:System.DBNull.Value).
syntax:
  content: public virtual string NullText { get; set; }
  parameters: []
  return:
    type: System.String
    description: A text that a Property Editor displays when its value is *null*, [String.Empty](xref:System.String.Empty), or [DBNull.Value](xref:System.DBNull.Value) (WinForms only).
seealso: []
---
The following [View Controller](xref:112621) created in the _MySolution\Module\Controllers_ folder shows how to specify this property for the "Address1" Property Editor in the **Contact** Detail View.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
// ...
public class CustomizeNullTextValueController : ObjectViewController<DetailView, Contact> {
    protected override void OnActivated() {
        base.OnActivated();
        PropertyEditor propertyEditor = View.FindItem("Address1") as PropertyEditor;
        if (propertyEditor != null) {
            propertyEditor.NullText = "Type your text here…";
        }
    }
}
```
***

The following image illustrates the result.

![Null text in an editor](~/images/NullText_UI_Address.png)

> [!Note]
> You can also set the @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.NullText property in the [Model Editor](xref:112582).