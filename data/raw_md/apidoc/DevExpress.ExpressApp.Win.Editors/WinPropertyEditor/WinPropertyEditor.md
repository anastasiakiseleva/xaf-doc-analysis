---
uid: DevExpress.ExpressApp.Win.Editors.WinPropertyEditor
name: WinPropertyEditor
type: Class
summary: Represents a base class for Windows Forms Property Editors.
syntax:
  content: 'public abstract class WinPropertyEditor : PropertyEditor, ISupportToolTip'
seealso:
- linkId: DevExpress.ExpressApp.Win.Editors.WinPropertyEditor._members
  altText: WinPropertyEditor Members
- linkId: DevExpress.ExpressApp.Editors.PropertyEditor
- linkId: "113097"
- linkId: "112679"
- linkId: DevExpress.ExpressApp.Editors.PropertyEditorAttribute
---
Inherit from this class, to implement a custom Windows Forms Property Editor using a standard control that supports binding. If the control does not support binding, inherit from the [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) class. To implement a custom Property Editor based on a control derived from [](xref:DevExpress.XtraEditors.BaseEdit), inherit from the [](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor) class.

Compared to the [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) class, the **WinPropertyEditor** class introduces additional members:

| Member | Description |
|---|---|
| [WinPropertyEditor.Control](xref:DevExpress.ExpressApp.Win.Editors.WinPropertyEditor.Control) | Provides access to the control that represents the current Property Editor in a UI. |
| [WinPropertyEditor.ControlBindingProperty](xref:DevExpress.ExpressApp.Win.Editors.WinPropertyEditor.ControlBindingProperty) | Specifies the control's property that is used for data binding. |
| [WinPropertyEditor.TextControlHeight](xref:DevExpress.ExpressApp.Win.Editors.WinPropertyEditor.TextControlHeight) | Returns the default control height in pixels. Used by the XAF [built-in Property Editors](xref:113014). |

The simplest implementation of the **WinPropertyEditor** class' descendant requires the following:

* Override the **CreateControlCore** method. Create and return an instance of the required control in this method.
* Determine which event of the control occurs when the editing value is changed by a user (refer to the control's documentation to find the appropriate event). Subscribe to this event and call the **OnControlValueChanged** method from the event handler.
* Specify the [WinPropertyEditor.ControlBindingProperty](xref:DevExpress.ExpressApp.Win.Editors.WinPropertyEditor.ControlBindingProperty) value in the constructor or in the **CreateControlCore** method.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Editors;
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.Win.Editors;
// ...
[PropertyEditor(typeof(int), false)]
public class MyPropertyEditor : WinPropertyEditor {
    public MyPropertyEditor(Type objectType, IModelMemberViewItem model) : base(objectType, model) { }
    protected override object CreateControlCore() {
        System.Windows.Forms.TrackBar trackbarControl = new System.Windows.Forms.TrackBar();
        trackbarControl.Minimum = 0;
        trackbarControl.Maximum = 100;
        trackbarControl.Scroll += trackbarControl_Scroll;
        this.ControlBindingProperty = "Value";
        return trackbarControl;
    }
    void trackbarControl_Scroll(object sender, EventArgs e) {
        this.OnControlValueChanged();
    }
}
```
***

> [!TIP]
> [!include[CanUpdateControlEnabled_Note](~/templates/canupdatecontrolenabled_note111203.md)]