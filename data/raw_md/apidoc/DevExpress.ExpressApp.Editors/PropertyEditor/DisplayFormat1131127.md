---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.DisplayFormat
name: DisplayFormat
type: Property
summary: Specifies the display format string for the Property Editor's value.
syntax:
  content: public string DisplayFormat { get; set; }
  parameters: []
  return:
    type: System.String
    description: The format string for the Property Editor's value.
seealso:
- linkId: "113015"
- linkId: "402141"
---
The `DisplayFormat` property uses a syntax similar to that in [String.Format()](xref:System.String.Format*) method calls. If a Property Editor displays date-time values, you can apply the following format string: `Due Date: {0:MMM/d/yyyy hh:mm tt}`:

 ![|Display Format](~/images/display-format.png)

The `DisplayFormat` property value can contain literal characters (displayed as is) and a value placeholder. In the format string example above, the `Due Date: ` text is displayed as is. The value placeholder is `{0:MMM/d/yyyy hh:mm tt}`.

The placeholder syntax is `{0[:formatString]}`. Since a Property Editor contains a single value, the index is always 0. The `formatString` portion is optional. It sets [Format Specifiers](xref:2141) that determine how the editor converts its value into display text.

You can set the `DisplayFormat` property in the [Application Model](xref:112580). Locate the View Item node that corresponds to the Property Editor. In that node, set the [DisplayFormat](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.DisplayFormat) property value. The following topic gives an example of how you can do this in the [Model Editor](xref:112582): [Apply the Display Format to an Integer Property Value](xref:402141).

You can also set the `DisplayFormat` property in Controller code:

# [C#](#tab/tabid-csharp)
 
```csharp{9}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

namespace MySolution.Blazor.Server.Controllers {
    public class ZipPostalDisplayFormatController : ViewController<DetailView> {
        protected override void OnActivated() {
            base.OnActivated();
            if (View.FindItem("ZipPostal") is BlazorPropertyEditorBase editor) {
                editor.DisplayFormat = "Zip Code: {0}";
            }
        }
    }
}
```
*** 

### Change Display Format Dynamically

The controller sets the `DisplayFormat` property in the `OnActivated` method, before the Property Editor control is created. If you change the `DisplayFormat` property after the control is created, the new value does not appear in the UI. Use the following solution to change formatting settings in this case: 

[!example[How to dynamically change mask settings based on the current object.](https://github.com/DevExpress-Examples/xaf-how-to-dynamically-change-mask-settings-based-on-the-current-object)] 


For more information on how to access editors in code, see the following topics: [](xref:112612#access-and-customize-view-items-in-code) and [](xref:402153).

If you create a custom Property Editor that should support the `DisplayFormat` property, implement your logic to apply the `DisplayFormat` property value to the custom editor.